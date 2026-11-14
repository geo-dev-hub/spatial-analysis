"""Horn 3x3 finite-difference terrain slope and downslope aspect."""
from __future__ import annotations
from typing import Sequence
import numpy as np

def horn_slope_aspect(elevation: Sequence[Sequence[float]] | np.ndarray, *, cell_size_x: float = 1.0, cell_size_y: float = 1.0, z_factor: float = 1.0) -> dict[str, np.ndarray]:
    """Return slope degrees, slope percent and downslope aspect clockwise from north.

    Borders and any 3x3 window containing non-finite elevation return NaN.
    Flat cells have NaN aspect.
    """
    dem = np.asarray(elevation, dtype=float)
    if dem.ndim != 2 or dem.size == 0:
        raise ValueError("elevation must be a non-empty 2D array")
    if not np.isfinite([cell_size_x, cell_size_y, z_factor]).all():
        raise ValueError("cell sizes and z_factor must be finite")
    if cell_size_x <= 0 or cell_size_y <= 0 or z_factor <= 0:
        raise ValueError("cell sizes and z_factor must be positive")
    rows, cols = dem.shape
    slope_deg = np.full(dem.shape, np.nan)
    slope_pct = np.full(dem.shape, np.nan)
    aspect_deg = np.full(dem.shape, np.nan)
    if rows < 3 or cols < 3:
        return {"slope_degrees": slope_deg, "slope_percent": slope_pct, "aspect_degrees": aspect_deg}
    a,b,c = dem[:-2,:-2],dem[:-2,1:-1],dem[:-2,2:]
    d,e,f = dem[1:-1,:-2],dem[1:-1,1:-1],dem[1:-1,2:]
    g,h,i = dem[2:,:-2],dem[2:,1:-1],dem[2:,2:]
    valid = np.isfinite(a)&np.isfinite(b)&np.isfinite(c)&np.isfinite(d)&np.isfinite(e)&np.isfinite(f)&np.isfinite(g)&np.isfinite(h)&np.isfinite(i)
    dz_dx = ((c+2*f+i)-(a+2*d+g))/(8*cell_size_x)*z_factor
    # Array rows increase southward; this derivative is north-positive.
    dz_dy = ((a+2*b+c)-(g+2*h+i))/(8*cell_size_y)*z_factor
    gradient = np.hypot(dz_dx,dz_dy)
    slope = np.degrees(np.arctan(gradient))
    percent = gradient*100.0
    aspect = np.degrees(np.arctan2(-dz_dx,-dz_dy))%360.0
    aspect = np.where(gradient==0,np.nan,aspect)
    target=(slice(1,-1),slice(1,-1))
    slope_deg[target]=np.where(valid,slope,np.nan)
    slope_pct[target]=np.where(valid,percent,np.nan)
    aspect_deg[target]=np.where(valid,aspect,np.nan)
    return {"slope_degrees":slope_deg,"slope_percent":slope_pct,"aspect_degrees":aspect_deg}
