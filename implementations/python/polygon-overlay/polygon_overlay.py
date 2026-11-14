"""Explicit polygon Boolean operations using Shapely/GEOS."""
from __future__ import annotations
from math import isfinite
from typing import Literal
from shapely.geometry import MultiPolygon, Polygon
from shapely.geometry.base import BaseGeometry

OverlayOperation = Literal["intersection", "union", "difference", "symmetric_difference"]
_ALLOWED = {"intersection", "union", "difference", "symmetric_difference"}


def _validate_polygonal(geometry: BaseGeometry, name: str) -> Polygon | MultiPolygon:
    if not isinstance(geometry, (Polygon, MultiPolygon)):
        raise TypeError(f"{name} must be a Polygon or MultiPolygon")
    if geometry.is_empty:
        raise ValueError(f"{name} must not be empty")
    if not geometry.is_valid:
        raise ValueError(f"{name} is invalid: {geometry.is_valid}")
    return geometry


def overlay(a: BaseGeometry, b: BaseGeometry, operation: OverlayOperation,
            *, grid_size: float | None = None) -> BaseGeometry:
    """Apply one Boolean overlay to valid polygonal inputs.

    None uses floating precision. A non-negative grid_size requests GEOS
    precision reduction for this operation, in the input coordinate units.
    """
    left, right = _validate_polygonal(a, "a"), _validate_polygonal(b, "b")
    if operation not in _ALLOWED:
        raise ValueError(f"operation must be one of {sorted(_ALLOWED)}")
    if grid_size is not None and (not isfinite(grid_size) or grid_size < 0):
        raise ValueError("grid_size must be a finite non-negative number or None")
    method = getattr(left, operation)
    return method(right) if grid_size is None else method(right, grid_size=grid_size)


def describe_result(geometry: BaseGeometry) -> dict[str, object]:
    """Report actual output properties; do not infer them from input types."""
    return {
        "geometry_type": geometry.geom_type,
        "is_empty": geometry.is_empty,
        "is_valid": geometry.is_valid,
        "area": geometry.area,
        "length": geometry.length,
        "component_count": len(geometry.geoms) if hasattr(geometry, "geoms") else 1,
        "has_z": geometry.has_z,
    }
