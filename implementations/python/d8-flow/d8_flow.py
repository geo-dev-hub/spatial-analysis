"""D8 steepest-descent flow direction for a raster elevation grid."""
from __future__ import annotations

from math import hypot, isfinite
from typing import Sequence

import numpy as np

# Row increases southward; column increases eastward.
# Order also defines deterministic tie-breaking.
_DIRECTIONS = (
    (0, 1, 1),      # E
    (1, 1, 2),      # SE
    (1, 0, 4),      # S
    (1, -1, 8),     # SW
    (0, -1, 16),    # W
    (-1, -1, 32),   # NW
    (-1, 0, 64),    # N
    (-1, 1, 128),   # NE
)


def d8_flow_direction(
    elevation: Sequence[Sequence[float]] | np.ndarray,
    *,
    cell_size: Sequence[float] = (1.0, 1.0),
    valid_mask: np.ndarray | None = None,
    nodata: float | None = None,
) -> np.ndarray:
    """Return ESRI-style D8 codes; 0=sink/flat and -1=invalid/NoData."""
    dem = np.asarray(elevation, dtype=float)
    if dem.ndim != 2 or dem.size == 0:
        raise ValueError("elevation must be a non-empty 2D array")
    if len(cell_size) != 2:
        raise ValueError("cell_size must contain row and column spacing")
    row_spacing, column_spacing = map(float, cell_size)
    if not all(isfinite(v) and v > 0 for v in (row_spacing, column_spacing)):
        raise ValueError("cell_size values must be finite and greater than zero")

    valid = np.isfinite(dem)
    if nodata is not None:
        valid &= dem != nodata
    if valid_mask is not None:
        mask = np.asarray(valid_mask, dtype=bool)
        if mask.shape != dem.shape:
            raise ValueError("valid_mask must have the same shape as elevation")
        valid &= mask

    rows, columns = dem.shape
    result = np.full(dem.shape, -1, dtype=np.int16)
    for row in range(rows):
        for column in range(columns):
            if not valid[row, column]:
                continue
            best_slope = 0.0
            best_code = 0
            centre = dem[row, column]
            for dr, dc, code in _DIRECTIONS:
                nr, nc = row + dr, column + dc
                if not (0 <= nr < rows and 0 <= nc < columns and valid[nr, nc]):
                    continue
                drop = centre - dem[nr, nc]
                if drop <= 0:
                    continue
                distance = hypot(dr * row_spacing, dc * column_spacing)
                slope = drop / distance
                if slope > best_slope:
                    best_slope = slope
                    best_code = code
            result[row, column] = best_code
    return result
