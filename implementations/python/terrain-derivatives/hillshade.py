"""Local analytical hillshade from slope and downslope aspect."""
from __future__ import annotations
import numpy as np

def hillshade_from_slope_aspect(slope_degrees, aspect_degrees, *, sun_azimuth_degrees: float=315.0, sun_altitude_degrees: float=45.0) -> np.ndarray:
    """Return normalized local illumination in [0, 1].

    Azimuth is clockwise from north. Flat cells (zero slope) have no defined
    aspect and are assigned illumination equal to sin(sun altitude). This
    computes local illumination only; it does not cast terrain shadows.
    """
    slope=np.asarray(slope_degrees,dtype=float)
    aspect=np.asarray(aspect_degrees,dtype=float)
    if slope.shape!=aspect.shape:
        raise ValueError("slope and aspect arrays must have the same shape")
    if not np.isfinite([sun_azimuth_degrees,sun_altitude_degrees]).all():
        raise ValueError("sun angles must be finite")
    if not 0<=sun_altitude_degrees<=90:
        raise ValueError("sun altitude must be between 0 and 90 degrees")
    if ((slope[np.isfinite(slope)]<0)|(slope[np.isfinite(slope)]>90)).any():
        raise ValueError("finite slope values must be between 0 and 90 degrees")
    valid=np.isfinite(slope)
    flat=valid&(slope==0)
    angled=valid&np.isfinite(aspect)
    result=np.full(slope.shape,np.nan,dtype=float)
    altitude=np.radians(sun_altitude_degrees)
    azimuth=np.radians(sun_azimuth_degrees%360)
    sl=np.radians(slope[angled])
    asp=np.radians(aspect[angled]%360)
    illumination=np.sin(altitude)*np.cos(sl)+np.cos(altitude)*np.sin(sl)*np.cos(azimuth-asp)
    result[angled]=np.clip(illumination,0.0,1.0)
    result[flat]=np.sin(altitude)
    return result
