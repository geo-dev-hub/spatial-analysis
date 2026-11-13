"""Single-source Dijkstra shortest paths for non-negative weighted graphs."""
from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from itertools import count
from math import inf, isfinite
from typing import Hashable, Iterable, Mapping, TypeVar

Node = TypeVar("Node", bound=Hashable)


@dataclass(frozen=True)
class DijkstraResult:
    """Shortest distances and predecessor links from one source node."""

    distances: dict[Hashable, float]
    predecessors: dict[Hashable, Hashable | None]
    source: Hashable

    def path_to(self, target: Hashable) -> list[Hashable] | None:
        """Return a shortest path to target, or None if it is unreachable."""
        if target not in self.distances or self.distances[target] == inf:
            return None
        path = []
        current = target
        while current is not None:
            path.append(current)
            current = self.predecessors[current]
        path.reverse()
        return path


def dijkstra(
    graph: Mapping[Node, Iterable[tuple[Node, float]]],
    source: Node,
) -> DijkstraResult:
    """Compute shortest paths from source in a directed weighted graph.

    Each mapping value is an iterable of (neighbour, weight) pairs. To model
    an undirected graph, include each edge in both adjacency lists.

    All edge weights must be finite and non-negative. Neighbour nodes that do
    not have their own mapping entry are treated as sink nodes. The source
    must occur as a key or as a neighbour somewhere in the graph.

    A binary heap with lazy stale-entry removal is used. Equal-cost
    alternatives retain the predecessor discovered first.
    """
    adjacency: dict[Node, list[tuple[Node, float]]] = {}
    vertices: set[Node] = set(graph.keys())

    for node, edges in graph.items():
        adjacency[node] = []
        for neighbour, raw_weight in edges:
            weight = float(raw_weight)
            if not isfinite(weight) or weight < 0:
                raise ValueError("edge weights must be finite and non-negative")
            adjacency[node].append((neighbour, weight))
            vertices.add(neighbour)

    if source not in vertices:
        raise KeyError(f"source node {source!r} is not in the graph")

    for vertex in vertices:
        adjacency.setdefault(vertex, [])

    distances: dict[Node, float] = {vertex: inf for vertex in vertices}
    predecessors: dict[Node, Node | None] = {vertex: None for vertex in vertices}
    distances[source] = 0.0

    sequence = count()
    queue: list[tuple[float, int, Node]] = [(0.0, next(sequence), source)]

    while queue:
        current_distance, _, node = heappop(queue)
        if current_distance > distances[node]:
            continue

        for neighbour, weight in adjacency[node]:
            candidate = current_distance + weight
            if candidate < distances[neighbour]:
                distances[neighbour] = candidate
                predecessors[neighbour] = node
                heappush(queue, (candidate, next(sequence), neighbour))

    return DijkstraResult(distances, predecessors, source)
