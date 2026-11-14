"""Static x-slab point locator for non-overlapping polygon faces.

This is a teaching implementation for a restricted planar subdivision:
valid, pairwise interior-disjoint polygon faces with linear ring boundaries.
It is not a randomized trapezoidal map or a general arrangement locator.
"""
from __future__ import annotations

from bisect import bisect_left
from math import isfinite
from typing import Hashable, Mapping, Sequence

Point = tuple[float, float]
FaceId = Hashable
BOUNDARY = "BOUNDARY"


def _normalise_faces(faces: Mapping[FaceId, Sequence[Sequence[Sequence[float]]]]):
    result = {}
    for face_id, rings in faces.items():
        if not rings:
            raise ValueError("Each face needs an exterior ring")
        normalised = []
        for ring in rings:
            pts = []
            for point in ring:
                if len(point) != 2:
                    raise ValueError("Each coordinate must contain x and y")
                x, y = float(point[0]), float(point[1])
                if not isfinite(x) or not isfinite(y):
                    raise ValueError("Coordinates must be finite")
                pts.append((x, y))
            if len(pts) < 4 or pts[0] != pts[-1]:
                raise ValueError("Each ring must be closed and contain at least four coordinates")
            normalised.append(pts)
        result[face_id] = normalised
    return result


def _edge_y(edge, x: float) -> float:
    x1, y1, x2, y2 = edge
    return y1 + (x - x1) * (y2 - y1) / (x2 - x1)


def _on_segment(point: Point, a: Point, b: Point, eps: float) -> bool:
    px, py = point
    cross = (px - a[0]) * (b[1] - a[1]) - (py - a[1]) * (b[0] - a[0])
    scale = max(1.0, abs(b[0] - a[0]), abs(b[1] - a[1]))
    if abs(cross) > eps * scale:
        return False
    return (min(a[0], b[0]) - eps <= px <= max(a[0], b[0]) + eps and
            min(a[1], b[1]) - eps <= py <= max(a[1], b[1]) + eps)


def _inside_ring(point: Point, ring) -> bool:
    x, y = point
    inside = False
    for a, b in zip(ring, ring[1:]):
        if (a[1] > y) != (b[1] > y):
            crossing_x = a[0] + (y - a[1]) * (b[0] - a[0]) / (b[1] - a[1])
            if crossing_x > x:
                inside = not inside
    return inside


class SlabPointLocator:
    """Preprocess disjoint polygon faces for static point-location queries.

    Query returns a face identifier, None for the unbounded/outside face,
    or the string BOUNDARY when the query lies on any represented boundary.
    """

    def __init__(self, faces: Mapping[FaceId, Sequence[Sequence[Sequence[float]]]],
                 epsilon: float = 1e-9):
        if not isfinite(epsilon) or epsilon < 0:
            raise ValueError("epsilon must be finite and non-negative")
        self.faces = _normalise_faces(faces)
        self.epsilon = epsilon
        self.x_events = sorted({x for rings in self.faces.values()
                                for ring in rings for x, _ in ring})
        self.slabs = []

        for left, right in zip(self.x_events, self.x_events[1:]):
            mid = (left + right) / 2.0
            crossings = []
            for face_id, rings in self.faces.items():
                for ring in rings:
                    for a, b in zip(ring, ring[1:]):
                        if a[0] == b[0]:
                            continue
                        if min(a[0], b[0]) < mid < max(a[0], b[0]):
                            edge = (a[0], a[1], b[0], b[1])
                            crossings.append((_edge_y(edge, mid), edge, face_id))
            crossings.sort(key=lambda item: item[0])

            groups = []
            for y_mid, edge, face_id in crossings:
                if groups and y_mid == groups[-1]["y_mid"]:
                    groups[-1]["edges"].append((edge, face_id))
                else:
                    groups.append({"y_mid": y_mid, "edges": [(edge, face_id)]})

            active = set()
            for group in groups:
                toggles = {}
                for _edge, face_id in group["edges"]:
                    toggles[face_id] = not toggles.get(face_id, False)
                for face_id, toggle in toggles.items():
                    if toggle:
                        if face_id in active:
                            active.remove(face_id)
                        else:
                            active.add(face_id)
                if len(active) > 1:
                    raise ValueError("Polygon interiors overlap within a slab")
                group["face_after"] = next(iter(active), None)
            self.slabs.append(groups)

    def _locate_on_event_line(self, point: Point):
        found = []
        for face_id, rings in self.faces.items():
            inside = False
            for ring in rings:
                for a, b in zip(ring, ring[1:]):
                    if _on_segment(point, a, b, self.epsilon):
                        return BOUNDARY
                if _inside_ring(point, ring):
                    inside = not inside
            if inside:
                found.append(face_id)
        if len(found) > 1:
            raise ValueError("Query lies in overlapping polygon interiors")
        return found[0] if found else None

    def locate(self, x: float, y: float):
        if not isfinite(x) or not isfinite(y):
            raise ValueError("Query coordinates must be finite")
        point = (float(x), float(y))
        if not self.x_events or x < self.x_events[0] or x > self.x_events[-1]:
            return None
        event_index = bisect_left(self.x_events, x)
        if event_index < len(self.x_events) and self.x_events[event_index] == x:
            return self._locate_on_event_line(point)

        slab_index = bisect_left(self.x_events, x) - 1
        groups = self.slabs[slab_index]
        lo, hi = 0, len(groups)
        while lo < hi:
            mid = (lo + hi) // 2
            edge, _face_id = groups[mid]["edges"][0]
            edge_y = _edge_y(edge, x)
            if abs(edge_y - y) <= self.epsilon:
                return BOUNDARY
            if edge_y < y:
                lo = mid + 1
            else:
                hi = mid
        return None if lo == 0 else groups[lo - 1]["face_after"]
