"""Empirical omnidirectional Matheron semivariogram for Euclidean coordinates."""
from math import isfinite, sqrt
from typing import Sequence


def experimental_semivariogram(points: Sequence[Sequence[float]],
                               values: Sequence[float],
                               bin_edges: Sequence[float]) -> list[dict]:
    """Calculate binned Matheron semivariances.

    Bins are [left, right), except the final bin includes its right edge.
    The returned lag is each bin midpoint. Empty bins have semivariance=None.
    """
    if len(points) < 2:
        raise ValueError("at least two observations are required")
    if len(points) != len(values):
        raise ValueError("points and values must have the same length")
    dimension = len(points[0])
    if dimension == 0:
        raise ValueError("points must have at least one coordinate")

    clean_points = []
    for point in points:
        if len(point) != dimension:
            raise ValueError("all points must have the same dimension")
        coords = tuple(float(v) for v in point)
        if not all(isfinite(v) for v in coords):
            raise ValueError("coordinates must be finite")
        clean_points.append(coords)

    clean_values = [float(v) for v in values]
    if not all(isfinite(v) for v in clean_values):
        raise ValueError("values must be finite")

    edges = [float(v) for v in bin_edges]
    if len(edges) < 2 or not all(isfinite(v) for v in edges):
        raise ValueError("at least two finite bin edges are required")
    if any(right <= left for left, right in zip(edges, edges[1:])):
        raise ValueError("bin edges must be strictly increasing")
    if edges[0] < 0:
        raise ValueError("distance bin edges cannot be negative")

    sums = [0.0] * (len(edges) - 1)
    counts = [0] * (len(edges) - 1)

    for i in range(len(clean_points) - 1):
        for j in range(i + 1, len(clean_points)):
            distance = sqrt(sum((a - b) ** 2 for a, b in zip(clean_points[i], clean_points[j])))
            if not isfinite(distance):
                raise ValueError("computed distances must be finite")
            if distance < edges[0] or distance > edges[-1]:
                continue
            if distance == edges[-1]:
                index = len(edges) - 2
            else:
                index = next(k for k in range(len(edges) - 1)
                             if edges[k] <= distance < edges[k + 1])
            difference = clean_values[i] - clean_values[j]
            sums[index] += difference * difference
            counts[index] += 1

    result = []
    for index, count in enumerate(counts):
        midpoint = (edges[index] + edges[index + 1]) / 2
        result.append({
            "lag": midpoint,
            "semivariance": sums[index] / (2 * count) if count else None,
            "pairs": count,
        })
    return result
