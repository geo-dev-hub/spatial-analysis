"""Bucket point-region quadtree for exact 2D rectangular window queries.

The root extent is closed. Midline ties go east and north, assigning each
point to exactly one child. Queries use inclusive rectangular boundaries.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from math import isfinite
from typing import Iterable, TypeAlias

Point: TypeAlias = tuple[float, float]
Bounds: TypeAlias = tuple[float, float, float, float]
Entry: TypeAlias = tuple[int, Point]


def _pair(value: Iterable[float], label: str) -> Point:
    coords = tuple(float(v) for v in value)
    if len(coords) != 2:
        raise ValueError(f"{label} must contain exactly two coordinates")
    if not all(isfinite(v) for v in coords):
        raise ValueError(f"{label} coordinates must be finite")
    return coords[0], coords[1]


def _rectangle(value: Iterable[float], label: str) -> Bounds:
    coords = tuple(float(v) for v in value)
    if len(coords) != 4:
        raise ValueError(f"{label} must be (min_x, min_y, max_x, max_y)")
    if not all(isfinite(v) for v in coords):
        raise ValueError(f"{label} coordinates must be finite")
    min_x, min_y, max_x, max_y = coords
    if min_x > max_x or min_y > max_y:
        raise ValueError(f"{label} minimums must not exceed maximums")
    return min_x, min_y, max_x, max_y


@dataclass
class _Node:
    bounds: Bounds
    depth: int
    entries: list[Entry] = field(default_factory=list)
    children: tuple["_Node", "_Node", "_Node", "_Node"] | None = None


class PointRegionQuadtree:
    """Static-root bucket PR quadtree for 2D points and window queries.

    Root bounds are closed. Points outside them are rejected. A midpoint tie
    goes east and/or north. Queries are inclusive and return stable point IDs.
    Coincident points may remain in an over-capacity leaf at max_depth.
    """

    def __init__(self, extent: Iterable[float], points: Iterable[Iterable[float]] = (),
                 *, capacity: int = 8, max_depth: int = 16) -> None:
        self.extent = _rectangle(extent, "extent")
        if self.extent[0] == self.extent[2] or self.extent[1] == self.extent[3]:
            raise ValueError("extent must have positive width and height")
        if not isinstance(capacity, int) or isinstance(capacity, bool) or capacity < 1:
            raise ValueError("capacity must be a positive integer")
        if not isinstance(max_depth, int) or isinstance(max_depth, bool) or max_depth < 0:
            raise ValueError("max_depth must be a non-negative integer")
        self.capacity, self.max_depth = capacity, max_depth
        self._root = _Node(self.extent, 0)
        self._points: list[Point] = []
        for point in points:
            self.insert(point)

    def __len__(self) -> int:
        return len(self._points)

    def insert(self, value: Iterable[float]) -> int:
        point = _pair(value, "point")
        if not self._contains(self.extent, point):
            raise ValueError("point lies outside the root extent")
        point_id = len(self._points)
        self._points.append(point)
        self._insert(self._root, (point_id, point))
        return point_id

    def query(self, window: Iterable[float]) -> list[int]:
        """Return matching original point IDs in input/insertion order."""
        bounds = _rectangle(window, "window")
        matches: list[int] = []
        self._query(self._root, bounds, matches)
        matches.sort()
        return matches

    def query_points(self, window: Iterable[float]) -> list[Point]:
        return [self._points[i] for i in self.query(window)]

    @property
    def node_count(self) -> int:
        def count(node: _Node) -> int:
            return 1 if node.children is None else 1 + sum(count(c) for c in node.children)
        return count(self._root)

    @property
    def depth(self) -> int:
        def deepest(node: _Node) -> int:
            return node.depth if node.children is None else max(deepest(c) for c in node.children)
        return deepest(self._root)

    @staticmethod
    def _contains(b: Bounds, p: Point) -> bool:
        return b[0] <= p[0] <= b[2] and b[1] <= p[1] <= b[3]

    @staticmethod
    def _intersects(a: Bounds, b: Bounds) -> bool:
        return not (a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1])

    @staticmethod
    def _midpoints(b: Bounds) -> tuple[float, float] | None:
        mx = b[0] + (b[2] - b[0]) / 2
        my = b[1] + (b[3] - b[1]) / 2
        if mx in (b[0], b[2]) or my in (b[1], b[3]):
            return None
        return mx, my

    @classmethod
    def _quadrant(cls, b: Bounds, p: Point) -> int:
        mid = cls._midpoints(b)
        if mid is None:
            raise RuntimeError("cannot subdivide a cell without distinct midpoints")
        east, north = p[0] >= mid[0], p[1] >= mid[1]
        return (2 if north else 0) + (1 if east else 0)

    @classmethod
    def _make_children(cls, b: Bounds, depth: int):
        mid = cls._midpoints(b)
        if mid is None:
            return None
        mx, my = mid
        # SW, SE, NW, NE. Closed child bounds overlap on split lines for safe pruning.
        return (
            _Node((b[0], b[1], mx, my), depth),
            _Node((mx, b[1], b[2], my), depth),
            _Node((b[0], my, mx, b[3]), depth),
            _Node((mx, my, b[2], b[3]), depth),
        )

    def _insert(self, node: _Node, entry: Entry) -> None:
        if node.children is not None:
            self._insert(node.children[self._quadrant(node.bounds, entry[1])], entry)
            return
        node.entries.append(entry)
        if len(node.entries) <= self.capacity or node.depth >= self.max_depth:
            return
        children = self._make_children(node.bounds, node.depth + 1)
        if children is None:
            return
        old_entries, node.entries, node.children = node.entries, [], children
        for old in old_entries:
            self._insert(node.children[self._quadrant(node.bounds, old[1])], old)

    def _query(self, node: _Node, window: Bounds, matches: list[int]) -> None:
        if not self._intersects(node.bounds, window):
            return
        if node.children is None:
            matches.extend(i for i, p in node.entries if self._contains(window, p))
            return
        for child in node.children:
            self._query(child, window, matches)
