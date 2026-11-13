"""Small, explicit IDW and ordinary-kriging teaching implementations."""
from __future__ import annotations

from math import exp, hypot, isfinite
from typing import Sequence

import numpy as np

Sample = tuple[float, float, float]
Point = tuple[float, float]


def _validated_samples(samples: Sequence[Sample]) -> list[Sample]:
    if not samples:
        raise ValueError("at least one sample is required")
    result: list[Sample] = []
    seen: set[Point] = set()
    for sample in samples:
        if len(sample) != 3:
            raise ValueError("each sample must be an (x, y, value) triple")
        x, y, value = map(float, sample)
        if not all(isfinite(v) for v in (x, y, value)):
            raise ValueError("sample coordinates and values must be finite")
        point = (x, y)
        if point in seen:
            raise ValueError("sample coordinates must be unique")
        seen.add(point)
        result.append((x, y, value))
    return result


def _validated_targets(targets: Sequence[Point]) -> list[Point]:
    result = []
    for target in targets:
        if len(target) != 2:
            raise ValueError("each target must be an (x, y) pair")
        x, y = map(float, target)
        if not isfinite(x) or not isfinite(y):
            raise ValueError("target coordinates must be finite")
        result.append((x, y))
    return result


def idw_predict(
    samples: Sequence[Sample],
    targets: Sequence[Point],
    *,
    power: float = 2.0,
    radius: float | None = None,
    max_neighbors: int | None = None,
) -> list[float | None]:
    """Predict by inverse distance weighting; None means no eligible neighbour."""
    data = _validated_samples(samples)
    query_points = _validated_targets(targets)
    if not isfinite(power) or power <= 0:
        raise ValueError("power must be finite and greater than zero")
    if radius is not None and (not isfinite(radius) or radius <= 0):
        raise ValueError("radius must be finite and greater than zero")
    if max_neighbors is not None and (
        not isinstance(max_neighbors, int) or isinstance(max_neighbors, bool) or max_neighbors < 1
    ):
        raise ValueError("max_neighbors must be a positive integer")

    predictions: list[float | None] = []
    for qx, qy in query_points:
        distances = [
            (hypot(sx - qx, sy - qy), index, value)
            for index, (sx, sy, value) in enumerate(data)
        ]
        exact = [value for distance, _index, value in distances if distance == 0.0]
        if exact:
            predictions.append(exact[0])
            continue
        eligible = [
            item for item in distances
            if radius is None or item[0] <= radius
        ]
        eligible.sort(key=lambda item: (item[0], item[1]))
        if max_neighbors is not None:
            eligible = eligible[:max_neighbors]
        if not eligible:
            predictions.append(None)
            continue
        weights = [distance ** (-power) for distance, _index, _value in eligible]
        denominator = sum(weights)
        predictions.append(
            sum(weight * item[2] for weight, item in zip(weights, eligible)) / denominator
        )
    return predictions


def exponential_semivariogram(distance: float, *, partial_sill: float, range_scale: float) -> float:
    """Exponential semivariogram with zero nugget and gamma(0) = 0."""
    if not isfinite(distance) or distance < 0:
        raise ValueError("distance must be finite and non-negative")
    if not isfinite(partial_sill) or partial_sill <= 0:
        raise ValueError("partial_sill must be finite and greater than zero")
    if not isfinite(range_scale) or range_scale <= 0:
        raise ValueError("range_scale must be finite and greater than zero")
    if distance == 0:
        return 0.0
    return partial_sill * (1.0 - exp(-distance / range_scale))


def ordinary_kriging_predict(
    samples: Sequence[Sample],
    targets: Sequence[Point],
    *,
    partial_sill: float,
    range_scale: float,
) -> list[tuple[float, float]]:
    """Return (estimate, kriging variance) for each target point.

    Uses a dense ordinary-kriging semivariogram system and a zero-nugget
    isotropic exponential model. A singular system raises ValueError.
    """
    data = _validated_samples(samples)
    query_points = _validated_targets(targets)
    if len(data) < 2:
        raise ValueError("ordinary kriging requires at least two samples")
    # Validate model parameters even when targets is empty.
    exponential_semivariogram(0.0, partial_sill=partial_sill, range_scale=range_scale)

    count = len(data)
    matrix = np.zeros((count + 1, count + 1), dtype=float)
    for i, (xi, yi, _zi) in enumerate(data):
        for j in range(i + 1, count):
            xj, yj, _zj = data[j]
            gamma = exponential_semivariogram(
                hypot(xi - xj, yi - yj),
                partial_sill=partial_sill,
                range_scale=range_scale,
            )
            matrix[i, j] = gamma
            matrix[j, i] = gamma
    matrix[:count, count] = 1.0
    matrix[count, :count] = 1.0

    values = np.asarray([sample[2] for sample in data], dtype=float)
    results: list[tuple[float, float]] = []
    for qx, qy in query_points:
        rhs = np.zeros(count + 1, dtype=float)
        for i, (sx, sy, _value) in enumerate(data):
            rhs[i] = exponential_semivariogram(
                hypot(sx - qx, sy - qy),
                partial_sill=partial_sill,
                range_scale=range_scale,
            )
        rhs[count] = 1.0
        try:
            solution = np.linalg.solve(matrix, rhs)
        except np.linalg.LinAlgError as exc:
            raise ValueError("kriging system is singular; inspect sample geometry and model") from exc
        weights = solution[:count]
        multiplier = solution[count]
        estimate = float(weights @ values)
        variance = float(weights @ rhs[:count] + multiplier)
        # Numerical round-off can create tiny negative values at exact samples.
        if variance < 0 and variance > -1e-10 * max(1.0, partial_sill):
            variance = 0.0
        if variance < 0:
            raise ArithmeticError("computed kriging variance is negative; inspect model and inputs")
        results.append((estimate, variance))
    return results


def empirical_variogram(
    samples: Sequence[Sample],
    bin_edges: Sequence[float],
) -> list[tuple[float, float | None, int]]:
    """Return (mean pair distance, semivariance, pair count) for distance bins.

    Bins are left-closed and right-open, except that the final bin includes
    its right edge. Empty bins retain their midpoint with semivariance None.
    This is an exploratory classical method-of-moments estimate, not a fitted
    variogram model and not a directional/robust estimator.
    """
    from itertools import combinations

    data = _validated_samples(samples)
    edges = [float(edge) for edge in bin_edges]
    if len(edges) < 2 or any(not isfinite(edge) for edge in edges):
        raise ValueError("bin_edges must contain at least two finite values")
    if edges[0] < 0 or any(right <= left for left, right in zip(edges, edges[1:])):
        raise ValueError("bin_edges must be non-negative and strictly increasing")

    distances: list[list[float]] = [[] for _ in range(len(edges) - 1)]
    squared_differences: list[list[float]] = [[] for _ in range(len(edges) - 1)]
    for first, second in combinations(data, 2):
        distance = hypot(first[0] - second[0], first[1] - second[1])
        if distance < edges[0] or distance > edges[-1]:
            continue
        bin_index = None
        for index, (lower, upper) in enumerate(zip(edges, edges[1:])):
            is_last = index == len(edges) - 2
            if lower <= distance and (distance < upper or (is_last and distance <= upper)):
                bin_index = index
                break
        if bin_index is not None:
            distances[bin_index].append(distance)
            squared_differences[bin_index].append((first[2] - second[2]) ** 2)

    result = []
    for index, pair_distances in enumerate(distances):
        if not pair_distances:
            midpoint = (edges[index] + edges[index + 1]) / 2.0
            result.append((midpoint, None, 0))
            continue
        semivariance = sum(squared_differences[index]) / (2.0 * len(pair_distances))
        result.append((sum(pair_distances) / len(pair_distances), semivariance, len(pair_distances)))
    return result
