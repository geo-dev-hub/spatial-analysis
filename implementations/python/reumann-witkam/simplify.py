"""Reumann-Witkam polyline simplification (pure Python teaching implementation)."""
from __future__ import annotations
from math import hypot, isfinite
from typing import Iterable, Sequence

Point = tuple[float, float]

def _point(value: Sequence[float]) -> Point:
    if len(value) != 2:
        raise ValueError("each point must contain exactly two coordinates")
    x, y = value
    if isinstance(x, bool) or isinstance(y, bool):
        raise TypeError("boolean coordinates are not supported")
    try:
        x, y = float(x), float(y)
    except (TypeError, ValueError) as exc:
        raise TypeError("coordinates must be real numbers") from exc
    if not isfinite(x) or not isfinite(y):
        raise ValueError("coordinates must be finite")
    return x, y

def _distance_to_line(point: Point, start: Point, end: Point) -> float:
    """Perpendicular distance to the infinite line through start and end."""
    dx, dy = end[0] - start[0], end[1] - start[1]
    length = hypot(dx, dy)
    if length == 0.0:
        return hypot(point[0] - start[0], point[1] - start[1])
    return abs(dx * (start[1] - point[1]) -
               (start[0] - point[0]) * dy) / length

def reumann_witkam(coordinates: Iterable[Sequence[float]], tolerance: float) -> list[Point]:
    """Simplify an ordered 2D polyline using a Reumann-Witkam strip.

    Coordinates must be planar Cartesian values; tolerance uses their units.
    This deterministic teaching variant measures distance to an infinite
    baseline line and preserves the first and last input vertices.
    """
    if isinstance(tolerance, bool):
        raise TypeError("tolerance must be a real number")
    try:
        tolerance = float(tolerance)
    except (TypeError, ValueError) as exc:
        raise TypeError("tolerance must be a real number") from exc
    if not isfinite(tolerance) or tolerance < 0:
        raise ValueError("tolerance must be finite and non-negative")
    points = [_point(p) for p in coordinates]
    if len(points) <= 2:
        return points
    if tolerance == 0:
        return points
    kept = [points[0]]
    anchor_index, baseline_index, i = 0, 1, 2
    while i < len(points):
        if _distance_to_line(points[i], points[anchor_index], points[baseline_index]) <= tolerance:
            i += 1
            continue
        retained_index = i - 1
        if retained_index > 0 and points[retained_index] != kept[-1]:
            kept.append(points[retained_index])
        anchor_index, baseline_index = retained_index, i
        i += 1
    if points[-1] != kept[-1]:
        kept.append(points[-1])
    return kept
