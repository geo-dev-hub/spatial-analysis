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
    nodes.update((start, goal))
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



def _reverse_graph(graph: Graph) -> dict[Node, list[tuple[Node, float]]]:
    nodes = set(graph)
    for outgoing in graph.values():
        nodes.update(neighbor for neighbor, _weight in outgoing)
    reverse: dict[Node, list[tuple[Node, float]]] = {node: [] for node in nodes}
    for node, outgoing in graph.items():
        for neighbor, weight in outgoing:
            reverse[neighbor].append((node, weight))
    return reverse


def bidirectional_dijkstra(
    graph: Graph, start: Node, goal: Node
) -> tuple[list[Node] | None, float]:
    """Find a directed shortest path with forward and reverse Dijkstra.

    The reverse search traverses reversed arcs. The stopping condition uses
    the sum of the smallest unsettled labels and the best complete path found.
    """
    _validate_graph(graph)
    if start == goal:
        return [start], 0.0

    reverse = _reverse_graph(graph)
    serial = count()
    forward_dist = {start: 0.0}
    backward_dist = {goal: 0.0}
    forward_prev: dict[Node, Node] = {}
    backward_next: dict[Node, Node] = {}
    forward_done: set[Node] = set()
    backward_done: set[Node] = set()
    forward_heap = [(0.0, next(serial), start)]
    backward_heap = [(0.0, next(serial), goal)]
    best = float("inf")
    meeting: Node | None = None

    def clean(heap, distances, settled):
        while heap and (
            heap[0][2] in settled or heap[0][0] != distances.get(heap[0][2])
        ):
            heappop(heap)

    while forward_heap and backward_heap:
        clean(forward_heap, forward_dist, forward_done)
        clean(backward_heap, backward_dist, backward_done)
        if not forward_heap or not backward_heap:
            break
        if forward_heap[0][0] + backward_heap[0][0] >= best:
            break

        if forward_heap[0][0] <= backward_heap[0][0]:
            distance, _order, node = heappop(forward_heap)
            if node in forward_done:
                continue
            forward_done.add(node)
            if node in backward_dist and distance + backward_dist[node] < best:
                best, meeting = distance + backward_dist[node], node
            for neighbor, weight in graph.get(node, ()):
                candidate = distance + weight
                if candidate < forward_dist.get(neighbor, float("inf")):
                    forward_dist[neighbor] = candidate
                    forward_prev[neighbor] = node
                    heappush(forward_heap, (candidate, next(serial), neighbor))
                if neighbor in backward_dist:
                    total = candidate + backward_dist[neighbor]
                    if total < best:
                        best, meeting = total, neighbor
        else:
            distance, _order, node = heappop(backward_heap)
            if node in backward_done:
                continue
            backward_done.add(node)
            if node in forward_dist and distance + forward_dist[node] < best:
                best, meeting = distance + forward_dist[node], node
            for predecessor, weight in reverse.get(node, ()):
                candidate = distance + weight
                if candidate < backward_dist.get(predecessor, float("inf")):
                    backward_dist[predecessor] = candidate
                    backward_next[predecessor] = node
                    heappush(backward_heap, (candidate, next(serial), predecessor))
                if predecessor in forward_dist:
                    total = candidate + forward_dist[predecessor]
                    if total < best:
                        best, meeting = total, predecessor

    if meeting is None:
        return None, float("inf")

    left = [meeting]
    while left[-1] != start:
        left.append(forward_prev[left[-1]])
    left.reverse()
    right = []
    node = meeting
    while node != goal:
        node = backward_next[node]
        right.append(node)
    return left + right, best


class ALTHeuristic:
    """Directed ALT landmark lower bound for A* on a static weighted graph.

    Preprocessing stores distances from and to each selected landmark. The
    heuristic is admissible for non-negative directed edge weights.
    """

    def __init__(self, graph: Graph, landmarks: Sequence[Node]):
        _validate_graph(graph)
        self.reverse = _reverse_graph(graph)
        self.from_landmark: dict[Node, dict[Node, float]] = {}
        self.to_landmark: dict[Node, dict[Node, float]] = {}
        for landmark in landmarks:
            self.from_landmark[landmark] = _single_source_distances(graph, landmark)
            self.to_landmark[landmark] = _single_source_distances(self.reverse, landmark)

    def __call__(self, node: Node, goal: Node) -> float:
        lower_bound = 0.0
        for landmark, from_map in self.from_landmark.items():
            to_map = self.to_landmark[landmark]
            d_l_goal = from_map.get(goal, float("inf"))
            d_l_node = from_map.get(node, float("inf"))
            d_node_l = to_map.get(node, float("inf"))
            d_goal_l = to_map.get(goal, float("inf"))
            if isfinite(d_l_goal) and isfinite(d_l_node):
                lower_bound = max(lower_bound, d_l_goal - d_l_node)
            if isfinite(d_node_l) and isfinite(d_goal_l):
                lower_bound = max(lower_bound, d_node_l - d_goal_l)
        return max(0.0, lower_bound)


def _single_source_distances(graph: Graph, start: Node) -> dict[Node, float]:
    distances = {start: 0.0}
    serial = count()
    queue = [(0.0, next(serial), start)]
    while queue:
        distance, _order, node = heappop(queue)
        if distance != distances.get(node):
            continue
        for neighbor, weight in graph.get(node, ()):
            candidate = distance + weight
            if candidate < distances.get(neighbor, float("inf")):
                distances[neighbor] = candidate
                heappush(queue, (candidate, next(serial), neighbor))
    return distances


def k_shortest_paths(
    graph: Graph, start: Node, goal: Node, k: int
) -> list[tuple[list[Node], float]]:
    """Return up to k loopless shortest paths using Yen's algorithm.

    Paths are represented by node sequences. For parallel arcs between the
    same ordered node pair, the minimum edge weight is used in this model.
    """
    if not isinstance(k, int) or isinstance(k, bool) or k < 1:
        raise ValueError("k must be a positive integer")
    _validate_graph(graph)
    first_path, first_cost = dijkstra(graph, start, goal)
    if first_path is None:
        return []
    accepted: list[tuple[list[Node], float]] = [(first_path, first_cost)]
    accepted_keys = {tuple(first_path)}
    candidate_keys: set[tuple[Node, ...]] = set()
    candidates = []
    serial = count()

    def path_cost(path: list[Node]) -> float:
        total = 0.0
        for u, v in zip(path, path[1:]):
            weights = [weight for neighbor, weight in graph.get(u, ()) if neighbor == v]
            if not weights:
                raise ValueError("path contains an edge absent from the original graph")
            total += min(weights)
        return total

    while len(accepted) < k:
        previous_path = accepted[-1][0]
        for spur_index in range(len(previous_path) - 1):
            root = previous_path[: spur_index + 1]
            banned_edges: set[tuple[Node, Node]] = set()
            for known_path, _cost in accepted:
                if len(known_path) > spur_index and known_path[: spur_index + 1] == root:
                    banned_edges.add((known_path[spur_index], known_path[spur_index + 1]))

            banned_nodes = set(root[:-1])
            spur_node = root[-1]
            modified: dict[Node, list[tuple[Node, float]]] = {}
            for node, outgoing in graph.items():
                if node in banned_nodes:
                    continue
                modified[node] = [
                    (neighbor, weight)
                    for neighbor, weight in outgoing
                    if neighbor not in banned_nodes and (node, neighbor) not in banned_edges
                ]

            spur_path, spur_cost = dijkstra(modified, spur_node, goal)
            if spur_path is None:
                continue
            total_path = root[:-1] + spur_path
            key = tuple(total_path)
            if key in accepted_keys or key in candidate_keys:
                continue
            total_cost = path_cost(root) + spur_cost
            heappush(candidates, (total_cost, next(serial), total_path))
            candidate_keys.add(key)

        if not candidates:
            break
        cost, _order, path = heappop(candidates)
        key = tuple(path)
        candidate_keys.remove(key)
        accepted_keys.add(key)
        accepted.append((path, cost))

    return accepted
