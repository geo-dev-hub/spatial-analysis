"""Dijkstra and A* teaching implementations for weighted directed graphs."""
from __future__ import annotations

from heapq import heappop, heappush
from itertools import count
from math import isfinite
from typing import Callable, Hashable, Mapping, Sequence

Node = Hashable
Graph = Mapping[Node, Sequence[tuple[Node, float]]]


def _validate_graph(graph: Graph) -> None:
    for edges in graph.values():
        for _neighbor, weight in edges:
            if not isfinite(weight) or weight < 0:
                raise ValueError("Dijkstra and this A* implementation require finite non-negative edge weights")


def shortest_path(graph: Graph, start: Node, goal: Node,
                  heuristic: Callable[[Node, Node], float] | None = None
                  ) -> tuple[list[Node] | None, float]:
    """Return an optimal path and cost, or (None, infinity) if unreachable.

    For A* optimality, heuristic(node, goal) must be admissible (never
    overestimate remaining cost). A consistent heuristic is recommended.
    """
    _validate_graph(graph)
    h = heuristic or (lambda _node, _goal: 0.0)
    serial = count()
    initial_estimate = float(h(start, goal))
    if not isfinite(initial_estimate) or initial_estimate < 0:
        raise ValueError("heuristic values must be finite and non-negative")
    best = {start: 0.0}
    previous: dict[Node, Node] = {}
    queue = [(initial_estimate, next(serial), 0.0, start)]

    while queue:
        _priority, _order, cost, node = heappop(queue)
        if cost != best.get(node):
            continue
        if node == goal:
            path = [goal]
            while path[-1] != start:
                path.append(previous[path[-1]])
            path.reverse()
            return path, cost

        for neighbor, weight in graph.get(node, ()):
            candidate = cost + weight
            if candidate < best.get(neighbor, float("inf")):
                estimate = float(h(neighbor, goal))
                if not isfinite(estimate) or estimate < 0:
                    raise ValueError("heuristic values must be finite and non-negative")
                best[neighbor] = candidate
                previous[neighbor] = node
                heappush(queue, (candidate + estimate, next(serial), candidate, neighbor))

    return None, float("inf")


def dijkstra(graph: Graph, start: Node, goal: Node) -> tuple[list[Node] | None, float]:
    """Dijkstra is A* with a zero heuristic."""
    return shortest_path(graph, start, goal)


def astar(graph: Graph, start: Node, goal: Node,
          heuristic: Callable[[Node, Node], float]
          ) -> tuple[list[Node] | None, float]:
    return shortest_path(graph, start, goal, heuristic)
