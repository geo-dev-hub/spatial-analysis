"""Exact segment-pair intersection for integer-coordinate planar segments.

This educational implementation uses Python integers for orientation tests and
fractions.Fraction for exact intersection coordinates. It handles proper
crossings, endpoint contacts, collinear touches and collinear overlaps.
It does not implement Bentley-Ottmann or a many-segment sweep line.
"""

from dataclasses import dataclass
from fractions import Fraction
from typing import TypeAlias

Point: TypeAlias = tuple[int, int]
ExactPoint: TypeAlias = tuple[Fraction, Fraction]


@dataclass(frozen=True)
class Intersection:
    kind: str  # "none", "point", or "overlap"
    geometry: ExactPoint | tuple[Point, Point] | None


def orientation(a: Point, b: Point, c: Point) -> int:
    """Return 1 for counter-clockwise, -1 for clockwise, 0 for collinear."""
    determinant = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return (determinant > 0) - (determinant < 0)


def _on_segment(p: Point, a: Point, b: Point) -> bool:
    return (
        orientation(a, b, p) == 0
        and min(a[0], b[0]) <= p[0] <= max(a[0], b[0])
        and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
    )


def _line_intersection(a: Point, b: Point, c: Point, d: Point) -> ExactPoint:
    """Intersection of non-parallel supporting lines, computed exactly."""
    rx, ry = b[0] - a[0], b[1] - a[1]
    sx, sy = d[0] - c[0], d[1] - c[1]
    denominator = rx * sy - ry * sx
    numerator = (c[0] - a[0]) * sy - (c[1] - a[1]) * sx
    t = Fraction(numerator, denominator)
    return (Fraction(a[0]) + t * rx, Fraction(a[1]) + t * ry)


def _collinear_intersection(a: Point, b: Point, c: Point, d: Point) -> Intersection:
    # Lexicographic order is monotone along a non-degenerate line segment.
    first = sorted((a, b))
    second = sorted((c, d))
    lo = max(first[0], second[0])
    hi = min(first[1], second[1])
    if lo > hi:
        return Intersection("none", None)
    if lo == hi:
        return Intersection("point", (Fraction(lo[0]), Fraction(lo[1])))
    return Intersection("overlap", (lo, hi))


def segment_intersection(a: Point, b: Point, c: Point, d: Point) -> Intersection:
    """Find the intersection of two closed segments with integer endpoints.

    Returns none, one exact point, or the closed segment shared by both.
    Zero-length segments are rejected to keep the teaching contract explicit.
    """
    if a == b or c == d:
        raise ValueError("Segments must have two distinct endpoints.")

    o1 = orientation(a, b, c)
    o2 = orientation(a, b, d)
    o3 = orientation(c, d, a)
    o4 = orientation(c, d, b)

    if o1 == o2 == o3 == o4 == 0:
        return _collinear_intersection(a, b, c, d)

    # A collinear endpoint may touch a non-collinear segment.
    for point, start, end in ((c, a, b), (d, a, b), (a, c, d), (b, c, d)):
        if _on_segment(point, start, end):
            return Intersection("point", (Fraction(point[0]), Fraction(point[1])))

    if o1 * o2 < 0 and o3 * o4 < 0:
        return Intersection("point", _line_intersection(a, b, c, d))

    return Intersection("none", None)


if __name__ == "__main__":
    cases = [
        ((0, 0), (4, 4), (0, 4), (4, 0)),
        ((0, 0), (4, 0), (2, 0), (6, 0)),
        ((0, 0), (4, 0), (4, 0), (4, 3)),
    ]
    for case in cases:
        print(segment_intersection(*case))
