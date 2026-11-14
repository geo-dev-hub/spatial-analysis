"""Teaching implementation of Graham scan for planar points.

The result contains only extreme hull vertices in counter-clockwise order.
Coordinates are finite real numbers. Orientation is evaluated using ordinary
floating-point arithmetic; this is not a robust exact-predicate library.
"""
from __future__ import annotations

from math import atan2, isfinite
from typing import Iterable

Point = tuple[float, float]


def cross(origin: Point, a: Point, b: Point) -> float:
    """Return the signed cross product for vectors origin->a and origin->b."""
    return ((a[0] - origin[0]) * (b[1] - origin[1])
            - (a[1] - origin[1]) * (b[0] - origin[0]))


def _normalise_points(points: Iterable[tuple[float, float]]) -> list[Point]:
    unique: set[Point] = set()
    for point in points:
        if len(point) != 2:
            raise ValueError("each point must contain exactly two coordinates")
        x, y = float(point[0]), float(point[1])
        if not isfinite(x) or not isfinite(y):
            raise ValueError("point coordinates must be finite")
        unique.add((x, y))
    return list(unique)


def graham_scan(points: Iterable[tuple[float, float]]) -> list[Point]:
    """Return the extreme vertices of the planar convex hull.

    The hull is counter-clockwise and does not repeat its first vertex.
    Duplicate inputs are removed. Collinear points between hull endpoints are
    omitted; a fully collinear input returns its two extreme endpoints.
    Empty input returns an empty list.

    This teaching implementation uses atan2 for polar-angle sorting and
    ordinary floating-point orientation tests. It is not intended for
    numerically ill-conditioned or production-critical geometry.
    """
    pts = _normalise_points(points)
    if len(pts) <= 2:
        return sorted(pts)

    anchor = min(pts, key=lambda p: (p[1], p[0]))
    others = [p for p in pts if p != anchor]

    # atan2 sorts points by polar angle. Distance breaks same-ray ties so
    # nearer collinear points are considered before farther points.
    others.sort(
        key=lambda p: (
            atan2(p[1] - anchor[1], p[0] - anchor[0]),
            (p[0] - anchor[0]) ** 2 + (p[1] - anchor[1]) ** 2,
        )
    )

    hull: list[Point] = [anchor]
    for point in others:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)

    # For a fully collinear set, the scan above leaves the two endpoints.
    return hull
