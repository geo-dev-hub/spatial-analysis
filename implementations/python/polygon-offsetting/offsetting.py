"""Explicit Shapely buffer wrapper for polygon offset demonstrations."""
from __future__ import annotations

from math import isfinite
from shapely.geometry.base import BaseGeometry


def offset_polygon(geometry: BaseGeometry, distance: float, join_style: str = "round",
                   mitre_limit: float = 5.0, quad_segs: int = 8) -> BaseGeometry:
    """Offset a valid planar polygonal geometry using GEOS buffer semantics."""
    if geometry.geom_type not in {"Polygon", "MultiPolygon"}:
        raise TypeError("geometry must be a Polygon or MultiPolygon")
    if not geometry.is_valid:
        raise ValueError("input geometry must be valid")
    if not isfinite(distance):
        raise ValueError("distance must be finite")
    if join_style not in {"round", "mitre", "bevel"}:
        raise ValueError("join_style must be round, mitre or bevel")
    if not isfinite(mitre_limit) or mitre_limit <= 0:
        raise ValueError("mitre_limit must be finite and positive")
    if not isinstance(quad_segs, int) or quad_segs < 1:
        raise ValueError("quad_segs must be a positive integer")
    return geometry.buffer(distance, quad_segs=quad_segs,
                           join_style=join_style, mitre_limit=mitre_limit)
