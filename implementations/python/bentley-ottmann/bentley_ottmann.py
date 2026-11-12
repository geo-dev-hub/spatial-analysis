"""Pedagogical Bentley–Ottmann sweep for restricted general-position inputs.

Exact Fraction event coordinates; heap event queue; list-based status.
The list is intentionally transparent but does not achieve the classical
O((n+k) log n) bound. See README.md for the full input contract.
"""
from dataclasses import dataclass
from fractions import Fraction
import heapq
from typing import TypeAlias
from segment_intersection import segment_intersection

Point: TypeAlias = tuple[int, int]
ExactPoint: TypeAlias = tuple[Fraction, Fraction]

@dataclass(frozen=True)
class Segment:
    id: int
    a: Point
    b: Point

    def __post_init__(self):
        if self.a == self.b:
            raise ValueError("Segments must have distinct endpoints")
        if self.a[0] == self.b[0]:
            raise ValueError("Vertical segments are outside this implementation's contract")
        if self.a[0] > self.b[0]:
            a, b = self.a, self.b
            object.__setattr__(self, "a", b)
            object.__setattr__(self, "b", a)

    def y_at(self, x: Fraction) -> Fraction:
        x1, y1 = self.a
        x2, y2 = self.b
        return Fraction(y1) + Fraction(y2-y1, x2-x1) * (x-x1)

    @property
    def slope(self) -> Fraction:
        return Fraction(self.b[1]-self.a[1], self.b[0]-self.a[0])


def _intersection(a: Segment, b: Segment) -> ExactPoint | None:
    r = segment_intersection(a.a, a.b, b.a, b.b)
    if r.kind == "none":
        return None
    if r.kind == "overlap":
        raise ValueError("Collinear overlaps are outside this implementation's contract")
    return r.geometry


def bentley_ottmann(segments: list[Segment]) -> list[tuple[int, int, ExactPoint]]:
    """Return crossing pairs; see README for preconditions and unsupported cases."""
    by_id = {s.id: s for s in segments}
    if len(by_id) != len(segments):
        raise ValueError("Segment IDs must be unique")
    endpoints = [p for s in segments for p in (s.a, s.b)]
    if len(set(endpoints)) != len(endpoints):
        raise ValueError("Shared endpoints are outside this implementation's contract")

    # Event tuple: x, y, kind priority (left=0, crossing=1, right=2), IDs.
    queue = []
    for s in segments:
        heapq.heappush(queue, (Fraction(s.a[0]), Fraction(s.a[1]), 0, s.id, -1))
        heapq.heappush(queue, (Fraction(s.b[0]), Fraction(s.b[1]), 2, s.id, -1))
    status: list[int] = []
    scheduled: set[tuple[int, int]] = set()
    output = []

    def key(sid: int, x: Fraction):
        s = by_id[sid]
        return s.y_at(x), s.slope, sid

    def schedule(a: int | None, b: int | None, x: Fraction):
        if a is None or b is None or a == b:
            return
        pair = tuple(sorted((a, b)))
        if pair in scheduled:
            return
        p = _intersection(by_id[pair[0]], by_id[pair[1]])
        if p is not None and p[0] > x:
            scheduled.add(pair)
            heapq.heappush(queue, (p[0], p[1], 1, pair[0], pair[1]))

    while queue:
        x, y, kind, a, b = heapq.heappop(queue)
        point = (x, y)
        if kind == 0:
            k = key(a, x)
            pos = 0
            while pos < len(status) and key(status[pos], x) < k:
                pos += 1
            status.insert(pos, a)
            schedule(status[pos-1] if pos else None, a, x)
            schedule(a, status[pos+1] if pos+1 < len(status) else None, x)
        elif kind == 2:
            if a not in status:
                raise RuntimeError("Status invariant failed: ending segment is not active")
            pos = status.index(a)
            below = status[pos-1] if pos else None
            above = status[pos+1] if pos+1 < len(status) else None
            status.pop(pos)
            schedule(below, above, x)
        else:
            if a not in status or b not in status:
                continue
            i, j = status.index(a), status.index(b)
            if abs(i-j) != 1:
                continue  # stale event
            lo, hi = sorted((i, j))
            output.append((min(a,b), max(a,b), point))
            status[lo:hi+1] = sorted((a,b), key=lambda sid: key(sid, x))
            below = status[lo-1] if lo else None
            above = status[hi+1] if hi+1 < len(status) else None
            schedule(below, status[lo], x)
            schedule(status[hi], above, x)

    return sorted(output, key=lambda item: (item[2][0], item[2][1], item[0], item[1]))


if __name__ == "__main__":
    demo = [Segment(1,(1,1),(9,7)), Segment(2,(1,7),(9,1)), Segment(3,(2,10),(8,2))]
    for crossing in bentley_ottmann(demo):
        print(crossing)
