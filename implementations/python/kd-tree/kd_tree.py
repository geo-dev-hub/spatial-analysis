"""A small static 2D k-d tree for exact Euclidean nearest-neighbour search.

The implementation returns the original input index and squared distance.
It is a teaching implementation, not a dynamic or high-dimensional index.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Iterable, TypeAlias

Point: TypeAlias = tuple[float, float]


@dataclass(frozen=True)
class _Node:
    index: int
    point: Point
    axis: int
    left: _Node | None
    right: _Node | None


def _point(value: Iterable[float]) -> Point:
    coords = tuple(float(v) for v in value)
    if len(coords) != 2:
        raise ValueError("each point must contain exactly two coordinates")
    if not all(isfinite(v) for v in coords):
        raise ValueError("point coordinates must be finite")
    return coords[0], coords[1]


def _build(items: list[tuple[int, Point]]) -> _Node | None:
    if not items:
        return None

    min_x = min(point[0] for _, point in items)
    max_x = max(point[0] for _, point in items)
    min_y = min(point[1] for _, point in items)
    max_y = max(point[1] for _, point in items)
    axis = 0 if max_x - min_x >= max_y - min_y else 1

    items.sort(key=lambda item: (item[1][axis], item[0]))
    middle = len(items) // 2
    index, point = items[middle]

    return _Node(
        index=index,
        point=point,
        axis=axis,
        left=_build(items[:middle]),
        right=_build(items[middle + 1 :]),
    )


class KDTree2D:
    """Static 2D k-d tree with exact nearest-neighbour queries.

    Ties are resolved by the smallest original input index. The metric is
    planar Euclidean distance in the coordinate units supplied by the caller.
    """

    def __init__(self, points: Iterable[Iterable[float]]) -> None:
        self._points = tuple(_point(point) for point in points)
        items = list(enumerate(self._points))
        self._root = _build(items)

    def __len__(self) -> int:
        return len(self._points)

    def nearest(self, query: Iterable[float]) -> tuple[int, float] | None:
        """Return (original_index, squared_distance), or None for an empty tree."""
        qx, qy = _point(query)
        if self._root is None:
            return None

        best: tuple[float, int] | None = None

        def visit(node: _Node | None) -> None:
            nonlocal best
            if node is None:
                return

            dx = qx - node.point[0]
            dy = qy - node.point[1]
            distance_sq = dx * dx + dy * dy
            candidate = (distance_sq, node.index)
            if best is None or candidate < best:
                best = candidate

            delta = (qx - node.point[node.axis])
            near, far = (
                (node.left, node.right) if delta <= 0
                else (node.right, node.left)
            )
            visit(near)

            # The split plane is a lower bound for every point in the far
            # subtree. Equality is visited so a lower-index tie can be found.
            if best is None or delta * delta <= best[0]:
                visit(far)

        visit(self._root)
        assert best is not None
        return best[1], best[0]
