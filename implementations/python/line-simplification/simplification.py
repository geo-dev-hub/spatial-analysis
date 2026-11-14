"""Teaching implementations of open-polyline simplification.

Coordinates are planar (x, y) pairs. Tolerances use coordinate units for
Douglas-Peucker and squared coordinate units for Visvalingam-Whyatt.
"""
from __future__ import annotations

from heapq import heappop, heappush
from math import hypot, isfinite
from typing import Sequence

Point = tuple[float, float]


def _points(values: Sequence[Sequence[float]]) -> list[Point]:
    if any(len(p) != 2 for p in values):
        raise ValueError("Each point must contain exactly two coordinates")
    result = [(float(p[0]), float(p[1])) for p in values]
    if any(not isfinite(x) or not isfinite(y) for x, y in result):
        raise ValueError("Coordinates must be finite")
    return result


def _distance_to_segment(p: Point, a: Point, b: Point) -> float:
    dx, dy = b[0] - a[0], b[1] - a[1]
    length2 = dx * dx + dy * dy
    if length2 == 0:
        return hypot(p[0] - a[0], p[1] - a[1])
    t = ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / length2
    t = min(1.0, max(0.0, t))
    q = (a[0] + t * dx, a[1] + t * dy)
    return hypot(p[0] - q[0], p[1] - q[1])


def douglas_peucker(points: Sequence[Sequence[float]], tolerance: float) -> list[Point]:
    """Simplify an open polyline, retaining its first and last vertices."""
    pts = _points(points)
    if not isfinite(tolerance) or tolerance < 0:
        raise ValueError("tolerance must be finite and non-negative")
    if len(pts) <= 2:
        return pts[:]

    keep = {0, len(pts) - 1}
    stack = [(0, len(pts) - 1)]
    while stack:
        start, end = stack.pop()
        a, b = pts[start], pts[end]
        best_distance, best_index = -1.0, None
        for i in range(start + 1, end):
            distance = _distance_to_segment(pts[i], a, b)
            if distance > best_distance:
                best_distance, best_index = distance, i
        if best_index is not None and best_distance > tolerance:
            keep.add(best_index)
            stack.append((start, best_index))
            stack.append((best_index, end))
    return [pts[i] for i in sorted(keep)]


def _triangle_area(a: Point, b: Point, c: Point) -> float:
    return abs((b[0] - a[0]) * (c[1] - a[1]) -
               (b[1] - a[1]) * (c[0] - a[0])) / 2.0


def visvalingam_whyatt(points: Sequence[Sequence[float]], area_threshold: float) -> list[Point]:
    """Remove least-effective vertices from an open polyline.

    Endpoints are never removed. The threshold uses squared coordinate units.
    The monotonic effective-area rule prevents later removals receiving a
    lower importance value than an earlier removal.
    """
    pts = _points(points)
    if not isfinite(area_threshold) or area_threshold < 0:
        raise ValueError("area_threshold must be finite and non-negative")
    n = len(pts)
    if n <= 2:
        return pts[:]

    previous = [i - 1 for i in range(n)]
    following = [i + 1 for i in range(n)]
    following[-1] = -1
    alive = [True] * n
    version = [0] * n
    heap: list[tuple[float, int, int]] = []

    def push(i: int, floor: float) -> None:
        if i <= 0 or i >= n - 1 or not alive[i]:
            return
        area = max(floor, _triangle_area(pts[previous[i]], pts[i], pts[following[i]]))
        version[i] += 1
        heappush(heap, (area, i, version[i]))

    for i in range(1, n - 1):
        push(i, 0.0)

    last_area = 0.0
    while heap:
        area, i, stamp = heappop(heap)
        if not alive[i] or stamp != version[i]:
            continue
        if area > area_threshold:
            break
        last_area = max(last_area, area)
        alive[i] = False
        left, right = previous[i], following[i]
        following[left] = right
        previous[right] = left
        push(left, last_area)
        push(right, last_area)

    return [point for i, point in enumerate(pts) if alive[i]]
