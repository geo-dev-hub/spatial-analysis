"""Graham scan convex hull for finite 2D point sets.

The implementation is intended for learning. It uses floating-point
orientation predicates and does not provide exact/adaptive robust predicates.
"""
from __future__ import annotations
from collections.abc import Sequence
from functools import cmp_to_key
from math import isfinite

Point = tuple[float, float]


def _cross(origin: Point, a: Point, b: Point) -> float:
    return ((a[0] - origin[0]) * (b[1] - origin[1])
            - (a[1] - origin[1]) * (b[0] - origin[0]))


def _compare_polar(pivot: Point, a: Point, b: Point) -> int:
    """Order vectors counter-clockwise from the positive x direction."""
    cross = ((a[0] - pivot[0]) * (b[1] - pivot[1])
             - (a[1] - pivot[1]) * (b[0] - pivot[0]))
    if cross > 0:
        return -1
    if cross < 0:
        return 1
    da = (a[0] - pivot[0]) ** 2 + (a[1] - pivot[1]) ** 2
    db = (b[0] - pivot[0]) ** 2 + (b[1] - pivot[1]) ** 2
    return (da > db) - (da < db)


def convex_hull(points: Sequence[Point]) -> list[Point]:
    """Return the extreme vertices of the 2D convex hull, counter-clockwise.

    Duplicate coordinates are removed. Collinear points along hull edges are
    omitted except for the extreme endpoints. The returned ring is not closed:
    the first vertex is not repeated at the end. Empty input returns [].
    """
    unique = sorted({(float(x), float(y)) for x, y in points})
    if any(not isfinite(x) or not isfinite(y) for x, y in unique):
        raise ValueError("coordinates must be finite")
    if len(unique) <= 1:
        return unique

    pivot = min(unique, key=lambda point: (point[1], point[0]))
    candidates = sorted(
        (point for point in unique if point != pivot),
        key=cmp_to_key(lambda a, b: _compare_polar(pivot, a, b)),
    )

    # For a ray with multiple points, only the farthest can be a hull vertex.
    radial: list[Point] = []
    for point in candidates:
        if radial:
            previous = radial[-1]
            if _cross(pivot, previous, point) == 0:
                radial[-1] = point
                continue
        radial.append(point)

    stack: list[Point] = [pivot]
    for point in radial:
        while len(stack) >= 2 and _cross(stack[-2], stack[-1], point) <= 0:
            stack.pop()
        stack.append(point)
    return stack
