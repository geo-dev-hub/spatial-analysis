"""Exact-arithmetic teaching baseline for hot-pixel snap rounding."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isfinite
from typing import Sequence, TypeAlias

Number: TypeAlias = int | float | Fraction | str
Point: TypeAlias = tuple[Fraction, Fraction]
GridPoint: TypeAlias = tuple[int, int]
InputSegment: TypeAlias = tuple[tuple[Number, Number], tuple[Number, Number]]


@dataclass(frozen=True)
class NodedEdge:
    source_segment: int
    start: GridPoint
    end: GridPoint


@dataclass(frozen=True)
class SnapRoundingResult:
    grid_size: Fraction
    hot_pixels: tuple[GridPoint, ...]
    polylines: tuple[tuple[GridPoint, ...], ...]
    edges: tuple[NodedEdge, ...]


def _as_fraction(value: Number) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("coordinates and grid_size must be finite numbers")
    try:
        if isinstance(value, float) and not isfinite(value):
            raise ValueError("coordinates and grid_size must be finite numbers")
        result = Fraction(str(value)) if isinstance(value, float) else Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise ValueError("coordinates and grid_size must be finite numbers") from exc
    return result


def _point(value: Sequence[Number]) -> Point:
    if len(value) != 2:
        raise ValueError("each point must contain exactly two coordinates")
    return (_as_fraction(value[0]), _as_fraction(value[1]))


def _cross(a: Point, b: Point) -> Fraction:
    return a[0] * b[1] - a[1] * b[0]


def _subtract(a: Point, b: Point) -> Point:
    return (a[0] - b[0], a[1] - b[1])


def _on_segment(point: Point, start: Point, end: Point) -> bool:
    direction = _subtract(end, start)
    offset = _subtract(point, start)
    return (
        _cross(direction, offset) == 0
        and min(start[0], end[0]) <= point[0] <= max(start[0], end[0])
        and min(start[1], end[1]) <= point[1] <= max(start[1], end[1])
    )


def _pair_intersections(a: Point, b: Point, c: Point, d: Point) -> set[Point]:
    if a == b:
        return {a} if _on_segment(a, c, d) else set()
    if c == d:
        return {c} if _on_segment(c, a, b) else set()
    r = _subtract(b, a)
    s = _subtract(d, c)
    q_minus_p = _subtract(c, a)
    denominator = _cross(r, s)
    if denominator != 0:
        t = _cross(q_minus_p, s) / denominator
        u = _cross(q_minus_p, r) / denominator
        if 0 <= t <= 1 and 0 <= u <= 1:
            return {(a[0] + t * r[0], a[1] + t * r[1])}
        return set()
    if _cross(q_minus_p, r) != 0:
        return set()
    candidates = {a, b, c, d}
    return {p for p in candidates if _on_segment(p, a, b) and _on_segment(p, c, d)}


def _round_half_toward_positive(value: Fraction) -> int:
    return (2 * value.numerator + value.denominator) // (2 * value.denominator)


def _hot_pixel(point: Point) -> GridPoint:
    return (_round_half_toward_positive(point[0]),
            _round_half_toward_positive(point[1]))


def _segment_intersects_pixel(start: Point, end: Point, pixel: GridPoint) -> bool:
    lower = (Fraction(pixel[0]) - Fraction(1, 2),
             Fraction(pixel[1]) - Fraction(1, 2))
    upper = (Fraction(pixel[0]) + Fraction(1, 2),
             Fraction(pixel[1]) + Fraction(1, 2))
    direction = _subtract(end, start)
    t_min, t_max = Fraction(0), Fraction(1)
    for axis in (0, 1):
        if direction[axis] == 0:
            if start[axis] < lower[axis] or start[axis] > upper[axis]:
                return False
            continue
        t1 = (lower[axis] - start[axis]) / direction[axis]
        t2 = (upper[axis] - start[axis]) / direction[axis]
        t_min = max(t_min, min(t1, t2))
        t_max = min(t_max, max(t1, t2))
        if t_min > t_max:
            return False
    return True


def _projection_parameter(start: Point, end: Point, pixel: GridPoint) -> Fraction:
    direction = _subtract(end, start)
    denominator = direction[0] ** 2 + direction[1] ** 2
    if denominator == 0:
        return Fraction(0)
    centre = (Fraction(pixel[0]), Fraction(pixel[1]))
    offset = _subtract(centre, start)
    parameter = (offset[0] * direction[0] + offset[1] * direction[1]) / denominator
    return min(Fraction(1), max(Fraction(0), parameter))


def snap_round(segments: Sequence[InputSegment], *, grid_size: Number = 1) -> SnapRoundingResult:
    """Node segments onto a fixed grid using hot pixels.

    Exact arrangement vertices are found pairwise. Each is mapped to its
    nearest grid centre. Every input segment is rerouted through every
    closed hot-pixel square it intersects. Half-grid ties round toward
    positive infinity; equal projection parameters use lexicographic order.

    This O(n² + nH) teaching baseline does not provide production-scale
    indexing or claim every topological guarantee of production noders.
    """
    size = _as_fraction(grid_size)
    if size <= 0:
        raise ValueError("grid_size must be positive")
    if not segments:
        return SnapRoundingResult(size, (), (), ())
    normalised: list[tuple[Point, Point]] = []
    for segment in segments:
        if len(segment) != 2:
            raise ValueError("each segment must contain exactly two endpoints")
        start, end = _point(segment[0]), _point(segment[1])
        normalised.append((
            (start[0] / size, start[1] / size),
            (end[0] / size, end[1] / size),
        ))

    vertices: set[Point] = set()
    for start, end in normalised:
        vertices.update((start, end))
    for i, (a, b) in enumerate(normalised):
        for c, d in normalised[i + 1:]:
            vertices.update(_pair_intersections(a, b, c, d))

    hot_pixels = tuple(sorted({_hot_pixel(vertex) for vertex in vertices}))
    polylines: list[tuple[GridPoint, ...]] = []
    edges: list[NodedEdge] = []
    for source_index, (start, end) in enumerate(normalised):
        hits = [pixel for pixel in hot_pixels
                if _segment_intersects_pixel(start, end, pixel)]
        hits.sort(key=lambda pixel: (
            _projection_parameter(start, end, pixel), pixel[0], pixel[1]
        ))
        ordered: list[GridPoint] = []
        for pixel in hits:
            if not ordered or ordered[-1] != pixel:
                ordered.append(pixel)
        if not ordered:
            ordered = [_hot_pixel(start)]
            if _hot_pixel(end) != ordered[0]:
                ordered.append(_hot_pixel(end))
        polyline = tuple(ordered)
        polylines.append(polyline)
        edges.extend(
            NodedEdge(source_index, left, right)
            for left, right in zip(polyline, polyline[1:])
            if left != right
        )
    return SnapRoundingResult(size, hot_pixels, tuple(polylines), tuple(edges))
