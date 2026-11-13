"""Euclidean raster distance transform using SciPy."""
from __future__ import annotations

from math import isfinite
from typing import Sequence

import numpy as np
from scipy.ndimage import distance_transform_edt


def distance_to_targets(
    target_mask: np.ndarray,
    *,
    cell_size: Sequence[float] = (1.0, 1.0),
) -> np.ndarray:
    """Return centre-to-centre Euclidean distance to the nearest True cell.

    cell_size is ordered (row_spacing, column_spacing), in map units.
    """
    mask = np.asarray(target_mask, dtype=bool)
    if mask.ndim != 2 or mask.size == 0:
        raise ValueError("target_mask must be a non-empty 2D array")
    if len(cell_size) != 2:
        raise ValueError("cell_size must contain row and column spacing")
    row_spacing, column_spacing = map(float, cell_size)
    if not all(isfinite(value) and value > 0 for value in (row_spacing, column_spacing)):
        raise ValueError("cell_size values must be finite and greater than zero")
    if not mask.any():
        raise ValueError("target_mask must contain at least one target cell")
    return distance_transform_edt(~mask, sampling=(row_spacing, column_spacing))
