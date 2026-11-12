"""Indexed filter-and-refine spatial join using Shapely 2.x STRtree."""

from collections.abc import Iterable

from shapely import STRtree
from shapely.geometry.base import BaseGeometry


def spatial_join(
    left_geometries: Iterable[BaseGeometry],
    right_geometries: Iterable[BaseGeometry],
    predicate: str = "intersects",
) -> list[tuple[int, int]]:
    """Return (left_index, right_index) pairs satisfying a Shapely predicate.

    The STRtree is built over the right-hand geometries. Shapely first uses
    bounding boxes to find candidates, then applies the exact predicate as
    predicate(left_geometry, right_geometry).

    Returned indices refer to the original input sequences. The pairs are
    sorted for stable output; no spatial ordering is implied.
    """
    left = tuple(left_geometries)
    right = tuple(right_geometries)

    if not left or not right:
        return []

    tree = STRtree(right)
    pair_indices = tree.query(left, predicate=predicate)

    if pair_indices.size == 0:
        return []

    return sorted(
        (int(left_index), int(right_index))
        for left_index, right_index in zip(pair_indices[0], pair_indices[1])
    )
