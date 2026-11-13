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


def bellman_ford(graph: Graph, start: Node, goal: Node) -> tuple[list[Node] | None, float]:
    """Shortest path with negative edges; rejects a reachable negative cycle."""
    edges = []
    nodes = set(graph)
    for node, outgoing in graph.items():
        for neighbor, weight in outgoing:
            if not isfinite(weight):
                raise ValueError("edge weights must be finite")
            nodes.add(neighbor)
            edges.append((node, neighbor, float(weight)))
    distance = {node: float("inf") for node in nodes}
    previous: dict[Node, Node] = {}
    distance[start] = 0.0

    for _ in range(max(0, len(nodes) - 1)):
        changed = False
        for u, v, weight in edges:
            if distance[u] != float("inf") and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                previous[v] = u
                changed = True
        if not changed:
            break

    for u, v, weight in edges:
        if distance[u] != float("inf") and distance[u] + weight < distance[v]:
            raise ValueError("reachable negative-weight cycle")

    if distance.get(goal, float("inf")) == float("inf"):
        return None, float("inf")
    path = [goal]
    while path[-1] != start:
        path.append(previous[path[-1]])
    path.reverse()
    return path, distance[goal]


def floyd_warshall(graph: Graph) -> dict[tuple[Node, Node], float]:
    """Return all-pairs shortest distances; supports negative edges, not cycles."""
    nodes = list(dict.fromkeys(
        list(graph) + [neighbor for outgoing in graph.values() for neighbor, _ in outgoing]
    ))
    distance = {(u, v): (0.0 if u == v else float("inf"))
                for u in nodes for v in nodes}
    for u, outgoing in graph.items():
        for v, weight in outgoing:
            if not isfinite(weight):
                raise ValueError("edge weights must be finite")
            distance[(u, v)] = min(distance[(u, v)], float(weight))

    for k in nodes:
        for i in nodes:
            dik = distance[(i, k)]
            if dik == float("inf"):
                continue
            for j in nodes:
                candidate = dik + distance[(k, j)]
                if candidate < distance[(i, j)]:
                    distance[(i, j)] = candidate

    if any(distance[(node, node)] < 0 for node in nodes):
        raise ValueError("negative-weight cycle detected")
    return distance
