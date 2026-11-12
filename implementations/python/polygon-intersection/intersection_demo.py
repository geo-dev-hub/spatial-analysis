"""Small, reproducible polygon-intersection example using Shapely 2.1+.

This demonstrates the geometry operation; it does not reimplement GEOS overlay.
"""

from __future__ import annotations

import shapely
from shapely import Polygon


def polygon_intersection(
    first: Polygon,
    second: Polygon,
    *,
    grid_size: float | None = None,
):
    """Return the point-set intersection of two planar geometries.

    Invalid inputs are rejected rather than silently repaired. This function
    does not choose a CRS or a precision policy for the caller.
    """
    if first is None or second is None:
        raise TypeError("Both inputs must be Shapely geometries, not None.")
    if not first.is_valid or not second.is_valid:
        raise ValueError("Both input geometries must be valid.")
    return shapely.intersection(first, second, grid_size=grid_size)


def example() -> tuple[Polygon, Polygon, object]:
    """Return the two teaching polygons and their intersection."""
    first = shapely.box(0, 0, 4, 4)
    second = shapely.box(2, 1, 5, 3)
    shared = polygon_intersection(first, second)
    return first, second, shared


if __name__ == "__main__":
    a, b, result = example()
    print(f"Shapely: {shapely.__version__}")
    print(f"A: {a.wkt}")
    print(f"B: {b.wkt}")
    print(f"Intersection: {result.wkt}")
    print(f"Result type: {result.geom_type}")
    print(f"Area: {result.area}")
