"""Edge-based turn-aware and FIFO time-dependent routing baselines."""
from __future__ import annotations

from heapq import heappop, heappush
from itertools import count
from math import isfinite
from typing import Callable, Hashable, Iterable, Mapping, Sequence

Node = Hashable
EdgeId = Hashable


def turn_aware_shortest_path(
    edges: Iterable[tuple[EdgeId, Node, Node, float]],
    start: Node,
    goal: Node,
    *,
    prohibited_turns: Iterable[tuple[EdgeId, EdgeId]] = (),
    turn_penalties: Mapping[tuple[EdgeId, EdgeId], float] | None = None,
) -> tuple[list[EdgeId] | None, float]:
    """Dijkstra over incoming-edge states.

    Each edge is (edge_id, tail, head, travel_cost). A transition from edge
    e1 to e2 can be prohibited or assigned an additional non-negative cost.
    """
    outgoing: dict[Node, list[tuple[EdgeId, Node, float]]] = {}
    edge_ids: set[EdgeId] = set()
    for edge_id, tail, head, cost in edges:
        if edge_id in edge_ids:
            raise ValueError("edge identifiers must be unique")
        if not isfinite(cost) or cost < 0:
            raise ValueError("edge costs must be finite and non-negative")
        edge_ids.add(edge_id)
        outgoing.setdefault(tail, []).append((edge_id, head, float(cost)))

    prohibited = set(prohibited_turns)
    penalties = dict(turn_penalties or {})
    for turn, penalty in penalties.items():
        if not isfinite(penalty) or penalty < 0:
            raise ValueError("turn penalties must be finite and non-negative")
    if any(a not in edge_ids or b not in edge_ids for a, b in prohibited):
        raise ValueError("prohibited turn references an unknown edge")
    if any(a not in edge_ids or b not in edge_ids for a, b in penalties):
        raise ValueError("turn penalty references an unknown edge")

    if start == goal:
        return [], 0.0

    serial = count()
    # State is the edge used to enter the current node. None is the start state.
    distance: dict[EdgeId | None, float] = {None: 0.0}
    previous: dict[EdgeId, EdgeId | None] = {}
    state_node: dict[EdgeId | None, Node] = {None: start}
    queue = [(0.0, next(serial), None)]

    while queue:
        cost_so_far, _order, incoming = heappop(queue)
        if cost_so_far != distance.get(incoming):
            continue
        node = state_node[incoming]
        if node == goal:
            path: list[EdgeId] = []
            state = incoming
            while state is not None:
                path.append(state)
                state = previous[state]
            path.reverse()
            return path, cost_so_far

        for edge_id, head, edge_cost in outgoing.get(node, ()):
            if incoming is not None and (incoming, edge_id) in prohibited:
                continue
            candidate = cost_so_far + edge_cost
            if incoming is not None:
                candidate += penalties.get((incoming, edge_id), 0.0)
            if candidate < distance.get(edge_id, float("inf")):
                distance[edge_id] = candidate
                previous[edge_id] = incoming
                state_node[edge_id] = head
                heappush(queue, (candidate, next(serial), edge_id))

    return None, float("inf")


def earliest_arrival(
    graph: Mapping[Node, Sequence[tuple[Node, EdgeId]]],
    start: Node,
    goal: Node,
    departure_time: float,
    travel_time: Callable[[EdgeId, float], float],
) -> tuple[list[Node] | None, float]:
    """FIFO time-dependent Dijkstra; returns path and absolute arrival time.

    The caller must supply a FIFO edge-arrival function: departing an edge
    later must never produce an earlier arrival on that same edge. The
    function validates finite non-negative travel times but cannot prove the
    FIFO property for an arbitrary callable.
    """
    if not isfinite(departure_time):
        raise ValueError("departure_time must be finite")
    if start == goal:
        return [start], float(departure_time)

    serial = count()
    arrival = {start: float(departure_time)}
    previous: dict[Node, Node] = {}
    queue = [(float(departure_time), next(serial), start)]

    while queue:
        current_arrival, _order, node = heappop(queue)
        if current_arrival != arrival.get(node):
            continue
        if node == goal:
            path = [goal]
            while path[-1] != start:
                path.append(previous[path[-1]])
            path.reverse()
            return path, current_arrival

        for neighbor, edge_id in graph.get(node, ()):
            duration = float(travel_time(edge_id, current_arrival))
            if not isfinite(duration) or duration < 0:
                raise ValueError("travel times must be finite and non-negative")
            candidate = current_arrival + duration
            if candidate < arrival.get(neighbor, float("inf")):
                arrival[neighbor] = candidate
                previous[neighbor] = node
                heappush(queue, (candidate, next(serial), neighbor))

    return None, float("inf")
