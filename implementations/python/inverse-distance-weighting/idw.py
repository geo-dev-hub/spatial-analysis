"""Small, dependency-free inverse-distance weighting reference implementation.

Distances are Euclidean in the coordinate units supplied by the caller.
This module calculates estimates; it does not choose a CRS, fit parameters,
or assess predictive uncertainty.
"""
from math import isfinite, sqrt
from typing import Sequence

Point = Sequence[float]


def _validated_points(points: Sequence[Point], values: Sequence[float]):
    if len(points) == 0:
        raise ValueError("at least one observation is required")
    if len(points) != len(values):
        raise ValueError("points and values must have the same length")
    dimension = len(points[0])
    if dimension == 0:
        raise ValueError("points must have at least one coordinate")
    clean_points = []
    for point in points:
        if len(point) != dimension:
            raise ValueError("all points must have the same dimension")
        coords = tuple(float(value) for value in point)
        if not all(isfinite(value) for value in coords):
            raise ValueError("coordinates must contain only finite numbers")
        clean_points.append(coords)
    clean_values = [float(value) for value in values]
    if not all(isfinite(value) for value in clean_values):
        raise ValueError("observed values must contain only finite numbers")
    return clean_points, clean_values


def predict(points: Sequence[Point], values: Sequence[float], target: Point, *,
            power: float = 2.0, max_neighbors: int | None = None,
            radius: float | None = None) -> float:
    """Estimate a value at target using inverse-distance weighting.

    Coincident observations are averaged and returned directly. Otherwise,
    weights are proportional to distance**(-power) and normalized.
    """
    clean_points, clean_values = _validated_points(points, values)
    dimension = len(clean_points[0])
    target_coords = tuple(float(value) for value in target)
    if len(target_coords) != dimension:
        raise ValueError("target dimension must match observation dimension")
    if not all(isfinite(value) for value in target_coords):
        raise ValueError("target coordinates must contain only finite numbers")

    exponent = float(power)
    if not isfinite(exponent) or exponent <= 0:
        raise ValueError("power must be a finite positive number")
    if max_neighbors is not None and (
        not isinstance(max_neighbors, int) or isinstance(max_neighbors, bool) or max_neighbors < 1
    ):
        raise ValueError("max_neighbors must be a positive integer")
    if radius is not None:
        radius = float(radius)
        if not isfinite(radius) or radius <= 0:
            raise ValueError("radius must be a finite positive number")

    distances = []
    exact_values = []
    for point, value in zip(clean_points, clean_values):
        distance = sqrt(sum((a - b) ** 2 for a, b in zip(point, target_coords)))
        if not isfinite(distance):
            raise ValueError("computed distances must be finite")
        if distance == 0:
            exact_values.append(value)
        elif radius is None or distance <= radius:
            distances.append((distance, value))
    if exact_values:
        return sum(exact_values) / len(exact_values)
    if not distances:
        raise ValueError("no observations fall within the selected search neighbourhood")

    distances.sort(key=lambda item: item[0])
    if max_neighbors is not None:
        distances = distances[:max_neighbors]
    nearest_distance = distances[0][0]
    # Scaling every raw weight equally preserves the normalized result.
    raw_weights = [(nearest_distance / distance) ** exponent for distance, _ in distances]
    total_weight = sum(raw_weights)
    return sum(weight * value for weight, (_, value) in zip(raw_weights, distances)) / total_weight
