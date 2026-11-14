"""Small spectral-index calculations with explicit validity handling."""
from __future__ import annotations

import numpy as np


def ndvi(
    nir: np.ndarray,
    red: np.ndarray,
    *,
    nodata: float | None = None,
    valid_mask: np.ndarray | None = None,
) -> np.ndarray:
    """Calculate NDVI; invalid or undefined pixels are returned as NaN."""
    near_infrared = np.asarray(nir, dtype=np.float64)
    red_band = np.asarray(red, dtype=np.float64)
    if near_infrared.shape != red_band.shape:
        raise ValueError("NIR and red arrays must have the same shape")
    valid = np.isfinite(near_infrared) & np.isfinite(red_band)
    if valid_mask is not None:
        mask = np.asarray(valid_mask, dtype=bool)
        if mask.shape != near_infrared.shape:
            raise ValueError("valid_mask must have the same shape as the bands")
        valid &= mask
    if nodata is not None:
        valid &= (near_infrared != nodata) & (red_band != nodata)
    denominator = near_infrared + red_band
    valid &= denominator != 0.0
    result = np.full(near_infrared.shape, np.nan, dtype=np.float64)
    np.divide(
        near_infrared - red_band,
        denominator,
        out=result,
        where=valid,
    )
    return result
