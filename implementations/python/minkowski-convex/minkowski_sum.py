"""Exact-arithmetic Minkowski sum for two convex planar polygons.

Coordinates are converted through their decimal string representation, so
integers, decimal floats and Fraction values have predictable rational meaning.
The implementation is a teaching baseline, not a general polygon Boolean
engine. Inputs must be non-degenerate convex rings without holes.
"""
from __future__ import annotations

from fractions import Fraction
from typing import Iterable, Sequence

Point = tuple[Fraction, Fraction]
RawPoint = Sequence[int | float | str | Fraction]


def _point(value: RawPoint) -> Point:
    if len(value) != 2:
        raise ValueError("each point must have exactly two coordinates")
    return (Fraction(str(value[0])), Fraction(str(value[1])))


def _cross(a: Point, b: Point, c: Point | None = None) -> Fraction:
    """Cross product of vectors a->b and b->c, or vectors a and b."""
    if c is None:
        return a[0] * b[1] - a[1] * b[0]
    return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])


def _sub(a: Point, b: Point) -> Point:
    return (a[0] - b[0], a[1] - b[1])


def _add(a: Point, b: Point) -> Point:
    return (a[0] + b[0], a[1] + b[1])


def _dot(a: Point, b: Point) -> Fraction:
    return a[0] * b[0] + a[1] * b[1]


def _area2(ring: Sequence[Point]) -> Fraction:
    return sum(
        ring[i][0] * ring[(i + 1) % len(ring)][1]
        - ring[(i + 1) % len(ring)][0] * ring[i][1]
        for i in range(len(ring))
    )


def _clean_ring(vertices: Iterable[RawPoint]) -> list[Point]:
    ring = [_point(p) for p in vertices]
    if len(ring) > 1 and ring[0] == ring[-1]:
        ring.pop()
    compact: list[Point] = []
    for p in ring:
        if not compact or p != compact[-1]:
            compact.append(p)
    if len(compact) > 1 and compact[0] == compact[-1]:
        compact.pop()
    if len(compact) < 3:
        raise ValueError("a polygon needs at least three distinct vertices")

    # Remove redundant points on a straight boundary run. Backtracking is invalid.
    changed = True
    while changed and len(compact) >= 3:
        changed = False
        result: list[Point] = []
        n = len(compact)
        for i, current in enumerate(compact):
            prev, nxt = compact[i - 1], compact[(i + 1) % n]
            incoming, outgoing = _sub(current, prev), _sub(nxt, current)
            turn = _cross(incoming, outgoing)
            if turn == 0:
                if _dot(incoming, outgoing) < 0:
                    raise ValueError("polygon boundary backtracks along an edge")
                changed = True
                continue
            result.append(current)
        compact = result
    if len(compact) < 3 or _area2(compact) == 0:
        raise ValueError("polygon must have non-zero area")
    return compact


def _prepare(vertices: Iterable[RawPoint]) -> list[Point]:
    ring = _clean_ring(vertices)
    if _area2(ring) < 0:
        ring.reverse()

    turns = [
        _cross(ring[i], ring[(i + 1) % len(ring)], ring[(i + 2) % len(ring)])
        for i in range(len(ring))
    ]
    if any(turn < 0 for turn in turns):
        raise ValueError("input polygon must be convex and simple")
    if not any(turn > 0 for turn in turns):
        raise ValueError("input polygon must enclose a positive area")

    # Start at the lowest vertex (then leftmost), making the edge sequence
    # monotonically ordered by polar angle for a CCW convex polygon.
    start = min(range(len(ring)), key=lambda i: (ring[i][1], ring[i][0]))
    return ring[start:] + ring[:start]


def _half(v: Point) -> int:
    return 0 if (v[1] > 0 or (v[1] == 0 and v[0] >= 0)) else 1


def _angle_compare(a: Point, b: Point) -> int:
    """Compare polar angles in [0, 2π) without atan2 or floating point."""
    ha, hb = _half(a), _half(b)
    if ha != hb:
        return -1 if ha < hb else 1
    cross = _cross(a, b)
    if cross > 0:
        return -1
    if cross < 0:
        return 1
    return 0


def minkowski_sum(
    polygon_a: Iterable[RawPoint], polygon_b: Iterable[RawPoint]
) -> list[Point]:
    """Return the CCW boundary vertices of A ⊕ B in O(m+n) time.

    The result omits a repeated closing vertex. Coordinates are Fractions.
    Collinear same-direction edges are merged into one output edge.
    """
    a, b = _prepare(polygon_a), _prepare(polygon_b)
    edges_a = [_sub(a[(i + 1) % len(a)], a[i]) for i in range(len(a))]
    edges_b = [_sub(b[(i + 1) % len(b)], b[i]) for i in range(len(b))]

    current = _add(a[0], b[0])
    result = [current]
    i = j = 0
    while i < len(edges_a) or j < len(edges_b):
        if i == len(edges_a):
            step = edges_b[j]
            j += 1
        elif j == len(edges_b):
            step = edges_a[i]
            i += 1
        else:
            comparison = _angle_compare(edges_a[i], edges_b[j])
            if comparison < 0:
                step = edges_a[i]
                i += 1
            elif comparison > 0:
                step = edges_b[j]
                j += 1
            else:
                # Parallel, same-direction edges share one supporting direction.
                step = _add(edges_a[i], edges_b[j])
                i += 1
                j += 1
        current = _add(current, step)
        if i < len(edges_a) or j < len(edges_b):
            result.append(current)

    # Defensive canonical cleanup: remove any collinear middle vertices.
    cleaned: list[Point] = []
    for p in result:
        while len(cleaned) >= 2 and _cross(cleaned[-2], cleaned[-1], p) == 0:
            cleaned.pop()
        cleaned.append(p)
    while len(cleaned) >= 3 and _cross(cleaned[-2], cleaned[-1], cleaned[0]) == 0:
        cleaned.pop()
    while len(cleaned) >= 3 and _cross(cleaned[-1], cleaned[0], cleaned[1]) == 0:
        cleaned.pop(0)
    if _area2(cleaned) < 0:
        cleaned.reverse()
    return cleaned
