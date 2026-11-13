"""Polygon validity inspection and explicit repair using Shapely.

This is a library-backed workflow example, not a new validity algorithm.
"""
from __future__ import annotations

from dataclasses import dataclass

import shapely
from shapely.geometry import MultiPolygon, Polygon


@dataclass(frozen=True)
class ValidityReport:
    geometry_type: str
    is_valid: bool
    reason: str
    area: float
    component_count: int


def inspect_polygon(geometry: Polygon | MultiPolygon) -> ValidityReport:
    """Report validity without modifying or repairing the input geometry."""
    if not isinstance(geometry, (Polygon, MultiPolygon)):
        raise TypeError("geometry must be a Polygon or MultiPolygon")
    if geometry.is_empty:
        component_count = 0
    elif isinstance(geometry, MultiPolygon):
        component_count = len(geometry.geoms)
    else:
        component_count = 1

    return ValidityReport(
        geometry_type=geometry.geom_type,
        is_valid=bool(shapely.is_valid(geometry)),
        reason=str(shapely.is_valid_reason(geometry)),
        area=float(geometry.area),
        component_count=component_count,
    )


def repair_polygon_explicitly(geometry: Polygon | MultiPolygon) -> Polygon | MultiPolygon | shapely.GeometryCollection:
    """Return Shapely's make_valid result; never replace or mutate the input.

    The linework method is Shapely's default. Its output may be a different
    geometry type or dimension, so callers must inspect it before use.
    """
    if not isinstance(geometry, (Polygon, MultiPolygon)):
        raise TypeError("geometry must be a Polygon or MultiPolygon")
    return shapely.make_valid(geometry)
