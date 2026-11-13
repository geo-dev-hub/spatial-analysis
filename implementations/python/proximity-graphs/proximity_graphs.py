"""Small-input Euclidean proximity graph baselines."""
from __future__ import annotations

from math import hypot, isfinite
from typing import Sequence


def _normalise(points: Sequence[Sequence[float]]) -> list[tuple[float, float]]:
    result = []
    for point in points:
        if len(point) != 2:
            raise ValueError("Each point must have two coordinates")
        x, y = float(point[0]), float(point[1])
        if not isfinite(x) or not isfinite(y):
            raise ValueError("Coordinates must be finite")
        result.append((x, y))
    if len(set(result)) != len(result):
        raise ValueError("Points must be distinct")
    return result


def _distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    return hypot(a[0] - b[0], a[1] - b[1])


def gabriel_graph(points: Sequence[Sequence[float]]) -> list[tuple[int, int]]:
    """Return edges whose open diameter disk contains no other input point."""
    pts = _normalise(points)
    edges = []
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            u, v = pts[i], pts[j]
            blocked = False
            for k, w in enumerate(pts):
                if k in (i, j):
                    continue
                # Strictly negative means w is strictly inside the diameter disk.
                dot = (w[0] - u[0]) * (w[0] - v[0]) + (w[1] - u[1]) * (w[1] - v[1])
                if dot < 0:
                    blocked = True
                    break
            if not blocked:
                edges.append((i, j))
    return edges


def relative_neighborhood_graph(points: Sequence[Sequence[float]]) -> list[tuple[int, int]]:
    """Return edges whose open lune contains no third point."""
    pts = _normalise(points)
    edges = []
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            uv = _distance(pts[i], pts[j])
            blocked = any(
                k not in (i, j)
                and max(_distance(pts[i], w), _distance(pts[j], w)) < uv
                for k, w in enumerate(pts)
            )
            if not blocked:
                edges.append((i, j))
    return edges


def euclidean_mst(points: Sequence[Sequence[float]]) -> list[tuple[int, int, float]]:
    """Kruskal MST over the complete Euclidean graph; O(n^2 log n)."""
    pts = _normalise(points)
    n = len(pts)
    if n <= 1:
        return []
    candidates = sorted(
        (_distance(pts[i], pts[j]), i, j)
        for i in range(n) for j in range(i + 1, n)
    )
    parent = list(range(n))
    rank = [0] * n

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    result = []
    for weight, i, j in candidates:
        ri, rj = find(i), find(j)
        if ri == rj:
            continue
        if rank[ri] < rank[rj]:
            ri, rj = rj, ri
        parent[rj] = ri
        if rank[ri] == rank[rj]:
            rank[ri] += 1
        result.append((i, j, weight))
        if len(result) == n - 1:
            break
    return result


def beta_skeleton(points: Sequence[Sequence[float]], beta: float = 2.0
                  ) -> list[tuple[int, int]]:
    """Lune-based beta-skeleton for 1 <= beta <= 2.

    beta=1 is the open-disk Gabriel definition; beta=2 is the open-lune
    relative-neighbourhood definition. Points strictly inside both defining
    disks block an edge; boundary ties do not.
    """
    if not isfinite(beta) or not 1.0 <= beta <= 2.0:
        raise ValueError("this lune-based implementation requires beta in [1, 2]")
    pts = _normalise(points)
    if beta == 1.0:
        return gabriel_graph(pts)
    if beta == 2.0:
        return relative_neighborhood_graph(pts)
    edges = []
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            u, v = pts[i], pts[j]
            dx, dy = v[0] - u[0], v[1] - u[1]
            distance = hypot(dx, dy)
            radius = beta * distance / 2.0
            c1 = (u[0] + beta * dx / 2.0, u[1] + beta * dy / 2.0)
            c2 = (v[0] - beta * dx / 2.0, v[1] - beta * dy / 2.0)
            radius2 = radius * radius
            boundary_epsilon = 1e-12 * max(1.0, radius2)
            blocked = False
            for k, w in enumerate(pts):
                if k in (i, j):
                    continue
                d1 = (w[0] - c1[0]) ** 2 + (w[1] - c1[1]) ** 2
                d2 = (w[0] - c2[0]) ** 2 + (w[1] - c2[1]) ** 2
                if d1 < radius2 - boundary_epsilon and d2 < radius2 - boundary_epsilon:
                    blocked = True
                    break
            if not blocked:
                edges.append((i, j))
    return edges


def yao_graph(points: Sequence[Sequence[float]], cones: int = 8,
              orientation: float = 0.0) -> list[tuple[int, int]]:
    """Return the undirected union of each point's nearest-neighbour cone choices.

    Each vertex selects at most one nearest point in each equal-angle cone.
    Ties are broken by input index. The output is the undirected union of
    directed selections, not the mutual-choice intersection.
    """
    from math import atan2, pi

    if not isinstance(cones, int) or cones < 3:
        raise ValueError("cones must be an integer of at least 3")
    if not isfinite(orientation):
        raise ValueError("orientation must be finite")
    pts = _normalise(points)
    width = 2.0 * pi / cones
    selected = set()
    for i, origin in enumerate(pts):
        best: dict[int, tuple[float, int]] = {}
        for j, target in enumerate(pts):
            if i == j:
                continue
            dx, dy = target[0] - origin[0], target[1] - origin[1]
            angle = (atan2(dy, dx) - orientation) % (2.0 * pi)
            cone = min(cones - 1, int(angle / width))
            distance2 = dx * dx + dy * dy
            candidate = (distance2, j)
            if cone not in best or candidate < best[cone]:
                best[cone] = candidate
        for _distance2, j in best.values():
            selected.add((min(i, j), max(i, j)))
    return sorted(selected)
