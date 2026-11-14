"""Explicit fixed-grid precision operations using Shapely/GEOS."""
from __future__ import annotations

from math import isfinite
from shapely import intersection, set_precision
from shapely.geometry.base import BaseGeometry

_VALID_MODES = {"valid_output", "pointwise", "keep_collapsed"}


def _check_grid(grid_size: float) -> None:
    if not isfinite(grid_size) or grid_size <= 0:
        raise ValueError("grid_size must be finite and greater than zero")


def reduce_precision(
    geometry: BaseGeometry,
    grid_size: float,
    *,
    mode: str = "valid_output",
) -> BaseGeometry:
    """Reduce coordinate precision to a fixed grid.

    This is coordinate precision reduction, not a full snap-rounding noder.
    """
    _check_grid(grid_size)
    if geometry is None:
        raise ValueError("geometry must not be None")
    if mode not in _VALID_MODES:
        raise ValueError(f"mode must be one of {sorted(_VALID_MODES)}")
    return set_precision(geometry, grid_size, mode=mode)


def fixed_precision_intersection(
    left: BaseGeometry,
    right: BaseGeometry,
    grid_size: float,
) -> BaseGeometry:
    """Compute intersection using GEOS fixed-grid overlay."""
    _check_grid(grid_size)
    if left is None or right is None:
        raise ValueError("input geometries must not be None")
    return intersection(left, right, grid_size=grid_size)
