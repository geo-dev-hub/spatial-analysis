"""Educational ray-crossing point-in-ring test.

Boundary is reported separately. This is for one simple planar ring and uses
exact floating-point comparisons; it is not a robust geometry engine.
"""

from enum import Enum
from typing import Sequence

Coordinate = tuple[float, float]


class PointLocation(str, Enum):
    INSIDE = "inside"
    OUTSIDE = "outside"
    BOUNDARY = "boundary"


def _on_segment(point: Coordinate, start: Coordinate, end: Coordinate) -> bool:
    px, py = point
    ax, ay = start
    bx, by = end
    cross = (px - ax) * (by - ay) - (py - ay) * (bx - ax)
    if cross != 0:
        return False
    return (
        min(ax, bx) <= px <= max(ax, bx)
        and min(ay, by) <= py <= max(ay, by)
    )


def locate_point(point: Coordinate, ring: Sequence[Coordinate]) -> PointLocation:
    """Classify a point relative to a closed or implicitly closed simple ring.

    The ring must contain at least three distinct vertices. The first vertex
    may, but need not, be repeated at the end.
    """
    vertices = list(ring)
    if len(vertices) > 1 and vertices[0] == vertices[-1]:
        vertices.pop()
    if len(vertices) < 3 or len(set(vertices)) < 3:
        raise ValueError("A ring must contain at least three distinct vertices.")

    x, y = point
    inside = False
    previous = vertices[-1]

    for current in vertices:
        if _on_segment(point, previous, current):
            return PointLocation.BOUNDARY

        x1, y1 = previous
        x2, y2 = current
        # Half-open vertical interval prevents counting a shared vertex twice.
        crosses_scanline = (y1 > y) != (y2 > y)
        if crosses_scanline:
            crossing_x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < crossing_x:
                inside = not inside
        previous = current

    return PointLocation.INSIDE if inside else PointLocation.OUTSIDE


if __name__ == "__main__":
    square = [(0, 0), (4, 0), (4, 4), (0, 4)]
    for candidate in [(2, 2), (5, 2), (4, 2)]:
        print(candidate, locate_point(candidate, square).value)
