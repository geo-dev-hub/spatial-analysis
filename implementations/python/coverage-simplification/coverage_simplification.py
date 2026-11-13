"""Coverage-aware polygon simplification using Shapely/GEOS.

This wrapper preserves shared coverage edges. It is not a replacement for
validating source data, choosing a meaningful CRS, or reviewing boundaries.
"""
from __future__ import annotations

from math import isfinite
from typing import Iterable

from shapely import coverage_is_valid, coverage_simplify
from shapely.geometry.base import BaseGeometry


def simplify_coverage(
    polygons: Iterable[BaseGeometry],
    tolerance: float,
    *,
    simplify_boundary: bool = True,
) -> list[BaseGeometry]:
    """Simplify a polygon coverage while retaining shared-edge consistency.

    Input must be a valid polygonal coverage: polygon interiors do not overlap
    and shared boundaries are exactly edge-matched. The tolerance is in the
    coordinate units of the input. GEOS coverage simplification requires
    GEOS 3.12 or newer (provided by supported Shapely wheels).
    """
    if not isfinite(tolerance) or tolerance < 0:
        raise ValueError("tolerance must be finite and non-negative")
    source = list(polygons)
    if not source:
        return []
    if not all(g is not None and not g.is_empty for g in source):
        raise ValueError("coverage members must be non-empty geometries")
    if not coverage_is_valid(source):
        raise ValueError("input must be a valid, edge-matched polygon coverage")

    result = list(coverage_simplify(
        source, tolerance, simplify_boundary=simplify_boundary
    ))
    if not coverage_is_valid(result):
        raise RuntimeError("GEOS returned an invalid coverage after simplification")
    return result
