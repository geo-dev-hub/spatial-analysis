"""Explicit-axis-order coordinate transformation using pyproj."""
from __future__ import annotations
from typing import Sequence
import numpy as np
from pyproj import CRS, Transformer
from pyproj.exceptions import ProjError

def transform_points(points: Sequence[Sequence[float]]|np.ndarray, source_crs, target_crs) -> np.ndarray:
    """Transform an N×2 coordinate array, enforcing traditional x/y order.

    For geographic coordinates x is longitude and y is latitude. For projected
    coordinates x is easting and y is northing. CRS units and datum operations
    are delegated to PROJ through pyproj.
    """
    coordinates=np.asarray(points,dtype=float)
    if coordinates.ndim!=2 or coordinates.shape[1]!=2 or coordinates.shape[0]==0:
        raise ValueError("points must be a non-empty N×2 coordinate array")
    if not np.isfinite(coordinates).all():
        raise ValueError("coordinates must be finite")
    try:
        source=CRS.from_user_input(source_crs)
        target=CRS.from_user_input(target_crs)
        transformer=Transformer.from_crs(source,target,always_xy=True)
        x,y=transformer.transform(coordinates[:,0],coordinates[:,1],errcheck=True)
    except (ProjError,ValueError,TypeError) as error:
        raise ValueError(f"coordinate transformation failed: {error}") from error
    result=np.column_stack([x,y]).astype(float)
    if not np.isfinite(result).all():
        raise ValueError("coordinate transformation produced non-finite output")
    return result
