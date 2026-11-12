"""Bentley–Ottmann using an implicit treap for the status sequence.

Input restrictions match the list-based reference implementation. The treap
has expected O(log n) rank, insertion, removal and adjacent-swap operations.
"""
from fractions import Fraction
import heapq

from bentley_ottmann import Segment, _intersection
from status_treap import ImplicitTreap, Node


def bentley_ottmann_treap(segments: list[Segment]) -> list[tuple[int, int, tuple[Fraction, Fraction]]]:
    by_id = {s.id: s for s in segments}
    if len(by_id) != len(segments):
        raise ValueError("Segment IDs must be unique")
    endpoints = [p for s in segments for p in (s.a, s.b)]
    if len(set(endpoints)) != len(endpoints):
        raise ValueError("Shared endpoints are outside this implementation's contract")

    queue = []
    for s in segments:
        heapq.heappush(queue, (Fraction(s.a[0]), Fraction(s.a[1]), 0, s.id, -1))
        heapq.heappush(queue, (Fraction(s.b[0]), Fraction(s.b[1]), 2, s.id, -1))

    status = ImplicitTreap()
    nodes: dict[int, Node] = {}
    active: set[int] = set()
    scheduled: set[tuple[int, int]] = set()
    output = []

    def key(sid: int, x: Fraction):
        segment = by_id[sid]
        return segment.y_at(x), segment.slope, sid

    def schedule(first: int | None, second: int | None, x: Fraction) -> None:
        if first is None or second is None or first == second:
            return
        pair = tuple(sorted((first, second)))
        if pair in scheduled:
            return
        point = _intersection(by_id[pair[0]], by_id[pair[1]])
        if point is not None and point[0] > x:
            scheduled.add(pair)
            heapq.heappush(queue, (point[0], point[1], 1, pair[0], pair[1]))

    while queue:
        x, y, kind, first, second = heapq.heappop(queue)
        point = (x, y)
        if kind == 0:
            target = key(first, x)
            index = status.lower_bound(lambda node: key(node.value, x), target)
            node = status.new_node(first)
            status.insert_at(index, node)
            nodes[first] = node
            active.add(first)
            below = status.at(index - 1).value if index else None
            above = status.at(index + 1).value if index + 1 < len(status) else None
            schedule(below, first, x)
            schedule(first, above, x)
        elif kind == 2:
            if first not in active:
                raise RuntimeError("Status invariant failed: ending segment is not active")
            index = status.rank(nodes[first])
            below = status.at(index - 1).value if index else None
            above = status.at(index + 1).value if index + 1 < len(status) else None
            status.remove_at(index)
            active.remove(first)
            schedule(below, above, x)
        else:
            if first not in active or second not in active:
                continue
            i = status.rank(nodes[first])
            j = status.rank(nodes[second])
            if abs(i - j) != 1:
                continue
            lower = min(i, j)
            output.append((min(first, second), max(first, second), point))
            status.swap_adjacent(lower)
            below = status.at(lower - 1).value if lower else None
            above = status.at(lower + 2).value if lower + 2 < len(status) else None
            schedule(below, status.at(lower).value, x)
            schedule(status.at(lower + 1).value, above, x)

    return sorted(output, key=lambda item: (item[2][0], item[2][1], item[0], item[1]))
