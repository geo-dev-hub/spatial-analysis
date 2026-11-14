"""Greedy triangle merging for convex decomposition of a simple polygon.

This is a transparent teaching baseline inspired by triangulate-and-merge
approaches. It is not presented as an optimized Hertel-Mehlhorn implementation.
"""
from __future__ import annotations

from fractions import Fraction
from typing import Iterable, Sequence

from ear_clipping import polygon_area, triangulate

Point = tuple[Fraction, Fraction]
RawPoint = Sequence[int | float | str | Fraction]


def _cross(a: Point, b: Point, c: Point) -> Fraction:
    return ((b[0] - a[0]) * (c[1] - b[1])
            - (b[1] - a[1]) * (c[0] - b[0]))


def _dot(a: Point, b: Point) -> Fraction:
    return a[0] * b[0] + a[1] * b[1]


def _sub(a: Point, b: Point) -> Point:
    return (a[0] - b[0], a[1] - b[1])


def _area2(ring: Sequence[Point]) -> Fraction:
    return sum(ring[i][0] * ring[(i + 1) % len(ring)][1]
               - ring[(i + 1) % len(ring)][0] * ring[i][1]
               for i in range(len(ring)))


def _clean(ring: list[Point]) -> list[Point]:
    result: list[Point] = []
    for p in ring:
        if not result or result[-1] != p:
            result.append(p)
    if len(result) > 1 and result[0] == result[-1]:
        result.pop()
    changed = True
    while changed and len(result) >= 3:
        changed = False
        for i, p in enumerate(result):
            prev, nxt = result[i - 1], result[(i + 1) % len(result)]
            incoming, outgoing = _sub(p, prev), _sub(nxt, p)
            if _cross(prev, p, nxt) == 0 and _dot(incoming, outgoing) > 0:
                result.pop(i)
                changed = True
                break
    return result


def _merge_if_convex(a: Sequence[Point], b: Sequence[Point]) -> list[Point] | None:
    """Remove one oppositely directed shared edge if the union stays convex."""
    shared: list[tuple[int, int]] = []
    for i, u in enumerate(a):
        v = a[(i + 1) % len(a)]
        for j, x in enumerate(b):
            y = b[(j + 1) % len(b)]
            if u == y and v == x:
                shared.append((i, j))
    if len(shared) != 1:
        return None

    i, j = shared[0]
    # Walk around A from the shared edge's end back to its start, then around
    # B along its non-shared boundary. The common edge disappears.
    path_a = [a[(i + 1 + k) % len(a)] for k in range(len(a))]
    path_b = [b[(j + 1 + k) % len(b)] for k in range(len(b))]
    candidate = _clean(list(path_a) + list(path_b[1:-1]))
    if len(candidate) < 3 or _area2(candidate) <= 0:
        return None
    if any(_cross(candidate[k - 1], candidate[k],
                  candidate[(k + 1) % len(candidate)]) < 0
           for k in range(len(candidate))):
        return None
    return candidate


def convex_decompose(vertices: Iterable[RawPoint]) -> list[list[Point]]:
    """Partition one simple polygon ring into convex pieces.

    Ear clipping creates an initial triangulation. Adjacent pieces are then
    greedily merged whenever their shared edge can be removed without creating
    a reflex corner. Coordinates and predicates use exact rational arithmetic.
    The result is a valid convex partition, not necessarily a minimum-cardinality
    partition. Holes and self-intersecting inputs are unsupported.
    """
    triangles = triangulate(vertices)
    pieces: list[list[Point]] = [list(t) for t in triangles]

    changed = True
    while changed:
        changed = False
        for i in range(len(pieces)):
            if changed:
                break
            for j in range(i + 1, len(pieces)):
                merged = _merge_if_convex(pieces[i], pieces[j])
                if merged is not None:
                    pieces[i] = merged
                    pieces.pop(j)
                    changed = True
                    break

    expected_area = polygon_area(vertices)
    actual_area = sum((abs(_area2(piece)) / 2 for piece in pieces), Fraction(0))
    if actual_area != expected_area:
        raise RuntimeError("convex partition failed area conservation")
    return pieces
