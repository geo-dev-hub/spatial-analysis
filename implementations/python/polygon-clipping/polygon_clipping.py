"""Sutherland–Hodgman clipping for convex polygons.

Both inputs must be convex, simple, non-degenerate rings in one planar
coordinate system. This is a deliberately scoped teaching implementation.
"""
from collections.abc import Sequence

Point = tuple[float, float]


def signed_area(points: Sequence[Point]) -> float:
    """Signed shoelace area; positive means counter-clockwise."""
    return 0.5 * sum(
        points[i][0] * points[(i + 1) % len(points)][1]
        - points[(i + 1) % len(points)][0] * points[i][1]
        for i in range(len(points))
    )


def _cross(a: Point, b: Point, p: Point) -> float:
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])


def _validate(points: Sequence[Point], name: str, eps: float) -> list[Point]:
    ring = [(float(x), float(y)) for x, y in points]
    if len(ring) > 1 and ring[0] == ring[-1]:
        ring.pop()
    if len(ring) < 3:
        raise ValueError(f"{name} needs at least three vertices")
    if len(set(ring)) != len(ring):
        raise ValueError(f"{name} must not repeat vertices")
    area = signed_area(ring)
    if abs(area) <= eps:
        raise ValueError(f"{name} must have non-zero area")
    turns = [_cross(ring[i], ring[(i + 1) % len(ring)], ring[(i + 2) % len(ring)])
             for i in range(len(ring))]
    turns = [value for value in turns if abs(value) > eps]
    if not turns or not (all(v > 0 for v in turns) or all(v < 0 for v in turns)):
        raise ValueError(f"{name} must be a convex ring with consistent turns")
    return ring if area > 0 else list(reversed(ring))


def _intersection(start: Point, end: Point, d_start: float, d_end: float) -> Point:
    t = d_start / (d_start - d_end)
    return (start[0] + t * (end[0] - start[0]),
            start[1] + t * (end[1] - start[1]))


def _deduplicate(points: list[Point], eps: float) -> list[Point]:
    result: list[Point] = []
    for point in points:
        if not result or ((point[0] - result[-1][0]) ** 2
                          + (point[1] - result[-1][1]) ** 2 > eps ** 2):
            result.append(point)
    if len(result) > 1 and ((result[0][0] - result[-1][0]) ** 2
                            + (result[0][1] - result[-1][1]) ** 2 <= eps ** 2):
        result.pop()
    return result


def clip_convex_polygon(subject: Sequence[Point], clip_window: Sequence[Point],
                        *, epsilon: float = 1e-10) -> list[Point]:
    """Return the area intersection as one counter-clockwise vertex ring.

    Both inputs must be convex simple polygons. Point-only and edge-only
    contacts return [], because this API represents area polygons only.
    Epsilon is a scale-dependent numerical tolerance, not a CRS setting.
    """
    if epsilon < 0:
        raise ValueError("epsilon must be non-negative")
    output = _validate(subject, "subject", epsilon)
    clipper = _validate(clip_window, "clip_window", epsilon)

    for i, clip_start in enumerate(clipper):
        clip_end = clipper[(i + 1) % len(clipper)]
        incoming, output = output, []
        if not incoming:
            break
        start = incoming[-1]
        d_start = _cross(clip_start, clip_end, start)
        for end in incoming:
            d_end = _cross(clip_start, clip_end, end)
            start_inside, end_inside = d_start >= -epsilon, d_end >= -epsilon
            if end_inside:
                if not start_inside and abs(d_start - d_end) > epsilon:
                    output.append(_intersection(start, end, d_start, d_end))
                output.append(end)
            elif start_inside and abs(d_start - d_end) > epsilon:
                output.append(_intersection(start, end, d_start, d_end))
            start, d_start = end, d_end
        output = _deduplicate(output, epsilon)

    if len(output) < 3 or abs(signed_area(output)) <= epsilon:
        return []
    return output
