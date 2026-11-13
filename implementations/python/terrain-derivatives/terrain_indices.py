"""Topographic wetness index from specific catchment area and slope."""
from __future__ import annotations
import numpy as np

def topographic_wetness_index(specific_catchment_area, slope_degrees, *, slope_floor_degrees: float=0.1) -> np.ndarray:
    """Return ln(a / tan(beta)); a must be positive and expressed in metres.

    Non-finite inputs and non-positive catchment area return NaN. A declared
    positive slope floor avoids an infinite index on perfectly flat cells.
    """
    area=np.asarray(specific_catchment_area,dtype=float)
    slope=np.asarray(slope_degrees,dtype=float)
    if area.shape!=slope.shape:
        raise ValueError("area and slope arrays must have the same shape")
    try:
        slope_floor_degrees = float(slope_floor_degrees)
    except (TypeError, ValueError):
        raise ValueError("slope_floor_degrees must be finite and between 0 and 90") from None
    if not np.isfinite(slope_floor_degrees) or not 0 < slope_floor_degrees < 90:
        raise ValueError("slope_floor_degrees must be finite and between 0 and 90")
    finite_slope=slope[np.isfinite(slope)]
    if ((finite_slope<0)|(finite_slope>=90)).any():
        raise ValueError("finite slope values must be in [0, 90)")
    valid=np.isfinite(area)&(area>0)&np.isfinite(slope)
    result=np.full(area.shape,np.nan,dtype=float)
    beta=np.radians(np.maximum(slope[valid],slope_floor_degrees))
    result[valid]=np.log(area[valid]/np.tan(beta))
    return result
