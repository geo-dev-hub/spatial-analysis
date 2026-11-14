"""Exact-predicate ear clipping for simple polygons (teaching implementation)."""
from __future__ import annotations

from fractions import Fraction
from math import isfinite
from typing import Iterable, Sequence

Point = tuple[Fraction, Fraction]
Triangle = tuple[Point, Point, Point]


def _point(value: Sequence[float | int]) -> Point:
    if len(value) != 2:
        raise ValueError("Each vertex must contain exactly x and y.")
    out = []
    for coordinate in value:
        if isinstance(coordinate, float) and not isfinite(coordinate):
            raise ValueError("Coordinates must be finite.")
        out.append(Fraction(str(coordinate)))
    return out[0], out[1]


def orient(a: Point, b: Point, c: Point) -> Fraction:
    """Twice the signed area of triangle abc."""
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def _on_segment(a: Point, b: Point, p: Point) -> bool:
    return (orient(a, b, p) == 0 and
            min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and
            min(a[1], b[1]) <= p[1] <= max(a[1], b[1]))


def _segments_intersect(a: Point, b: Point, c: Point, d: Point) -> bool:
    o1, o2, o3, o4 = orient(a, b, c), orient(a, b, d), orient(c, d, a), orient(c, d, b)
    if ((o1 > 0 and o2 < 0) or (o1 < 0 and o2 > 0)) and ((o3 > 0 and o4 < 0) or (o3 < 0 and o4 > 0)):
        return True
    return ((o1 == 0 and _on_segment(a, b, c)) or
            (o2 == 0 and _on_segment(a, b, d)) or
            (o3 == 0 and _on_segment(c, d, a)) or
            (o4 == 0 and _on_segment(c, d, b)))


def _signed_area2(ring: Sequence[Point]) -> Fraction:
    return sum((ring[i][0] * ring[(i + 1) % len(ring)][1] -
                ring[(i + 1) % len(ring)][0] * ring[i][1])
               for i in range(len(ring)))


def _clean_ring(vertices: Iterable[Sequence[float | int]]) -> list[Point]:
    ring = [_point(v) for v in vertices]
    if len(ring) > 1 and ring[0] == ring[-1]:
        ring.pop()
    compact: list[Point] = []
    for p in ring:
        if not compact or p != compact[-1]:
            compact.append(p)
    if len(compact) > 1 and compact[0] == compact[-1]:
        compact.pop()
    # Remove a middle point only when it is exactly collinear and lies between its neighbours.
    changed = True
    while changed and len(compact) >= 3:
        changed = False
        for i, p in enumerate(compact):
            a, c = compact[i - 1], compact[(i + 1) % len(compact)]
            if orient(a, p, c) == 0 and _on_segment(a, c, p):
                compact.pop(i)
                changed = True
                break
    if len(compact) < 3:
        raise ValueError("A polygon needs at least three distinct non-collinear vertices.")
    if _signed_area2(compact) == 0:
        raise ValueError("Polygon area must be non-zero.")
    return compact


def _validate_simple(ring: Sequence[Point]) -> None:
    n = len(ring)
    for i in range(n):
        previous, current, following = ring[i - 1], ring[i], ring[(i + 1) % n]
        if orient(previous, current, following) == 0:
            u = (previous[0] - current[0], previous[1] - current[1])
            v = (following[0] - current[0], following[1] - current[1])
            if u[0] * v[0] + u[1] * v[1] >= 0:
                raise ValueError("Input ring contains overlapping adjacent edges.")
        a, b = ring[i], ring[(i + 1) % n]
        for j in range(i + 1, n):
            # Adjacent boundary edges share their common endpoint by definition.
            if j == i or j == (i + 1) % n or i == (j + 1) % n:
                continue
            c, d = ring[j], ring[(j + 1) % n]
            if _segments_intersect(a, b, c, d):
                raise ValueError("Input ring is not a simple polygon (non-adjacent edges intersect).")


def _inside_or_on_triangle(p: Point, a: Point, b: Point, c: Point) -> bool:
    return orient(a, b, p) >= 0 and orient(b, c, p) >= 0 and orient(c, a, p) >= 0


def _is_ear(ring: Sequence[Point], i: int) -> bool:
    n = len(ring)
    a, b, c = ring[i - 1], ring[i], ring[(i + 1) % n]
    if orient(a, b, c) <= 0:
        return False
    # A reflex or boundary vertex inside/on the candidate triangle blocks the ear.
    for j, p in enumerate(ring):
        if j in (i - 1, i, (i + 1) % n):
            continue
        if _inside_or_on_triangle(p, a, b, c):
            return False
    return True


def triangulate(vertices: Iterable[Sequence[float | int]]) -> list[Triangle]:
    """Triangulate one simple polygon ring into n-2 CCW triangles.

    Coordinates are converted to exact decimal fractions for predicates. Holes,
    self-intersections, and repair of invalid rings are intentionally unsupported.
    """
    ring = _clean_ring(vertices)
    _validate_simple(ring)
    if _signed_area2(ring) < 0:
        ring.reverse()

    active = list(range(len(ring)))
    triangles: list[Triangle] = []
    while len(active) > 3:
        clipped = False
        current = [ring[k] for k in active]
        for local_i, original_i in enumerate(active):
            if _is_ear(current, local_i):
                a = current[local_i - 1]
                b = current[local_i]
                c = current[(local_i + 1) % len(current)]
                triangles.append((a, b, c))
                active.pop(local_i)
                clipped = True
                break
        if not clipped:
            raise ValueError("No valid ear found; check for degeneracy or invalid topology.")

    final = tuple(ring[k] for k in active)
    if orient(*final) <= 0:
        raise ValueError("Final triangle is degenerate or incorrectly oriented.")
    triangles.append(final)  # type: ignore[arg-type]
    return triangles


def triangle_area(triangle: Triangle) -> Fraction:
    return abs(orient(*triangle)) / 2


def polygon_area(vertices: Iterable[Sequence[float | int]]) -> Fraction:
    ring = _clean_ring(vertices)
    return abs(_signed_area2(ring)) / 2
