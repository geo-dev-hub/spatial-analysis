"""NoData-aware focal mean using summed-area tables."""
from __future__ import annotations

from typing import Sequence

import numpy as np


def _integral_image(array: np.ndarray) -> np.ndarray:
    """Build a summed-area table with a zero-padded top row and left column."""
    summed = np.cumsum(np.cumsum(array, axis=0), axis=1)
    result = np.zeros((array.shape[0] + 1, array.shape[1] + 1), dtype=summed.dtype)
    result[1:, 1:] = summed
    return result


def _rectangle_sum(integral: np.ndarray, r0: int, c0: int, r1: int, c1: int):
    """Sum half-open rectangle [r0:r1, c0:c1] in O(1)."""
    return (
        integral[r1, c1]
        - integral[r0, c1]
        - integral[r1, c0]
        + integral[r0, c0]
    )


def focal_mean(
    values: Sequence[Sequence[float]] | np.ndarray,
    *,
    window_size: int = 3,
    valid_mask: np.ndarray | None = None,
    nodata: float | None = None,
    min_count: int = 1,
) -> tuple[np.ndarray, np.ndarray]:
    """Return (focal mean, valid observation count) for each cell.

    The odd-sized square window is truncated at raster edges. Invalid values
    are ignored; means with fewer than min_count valid cells are NaN.
    """
    data = np.asarray(values, dtype=float)
    if data.ndim != 2 or data.size == 0:
        raise ValueError("values must be a non-empty 2D array")
    if isinstance(window_size, (bool, np.bool_)) or not isinstance(window_size, (int, np.integer)):
        raise ValueError("window_size must be a positive odd integer")
    if window_size <= 0 or window_size % 2 == 0:
        raise ValueError("window_size must be a positive odd integer")
    if isinstance(min_count, (bool, np.bool_)) or not isinstance(min_count, (int, np.integer)) or min_count <= 0:
        raise ValueError("min_count must be a positive integer")

    valid = np.isfinite(data)
    if nodata is not None:
        valid &= data != nodata
    if valid_mask is not None:
        mask = np.asarray(valid_mask, dtype=bool)
        if mask.shape != data.shape:
            raise ValueError("valid_mask must have the same shape as values")
        valid &= mask

    sums = _integral_image(np.where(valid, data, 0.0))
    counts = _integral_image(valid.astype(np.int64))
    rows, cols = data.shape
    radius = window_size // 2
    means = np.full(data.shape, np.nan, dtype=float)
    observed = np.zeros(data.shape, dtype=np.int64)

    for r in range(rows):
        r0, r1 = max(0, r - radius), min(rows, r + radius + 1)
        for c in range(cols):
            c0, c1 = max(0, c - radius), min(cols, c + radius + 1)
            count = int(_rectangle_sum(counts, r0, c0, r1, c1))
            observed[r, c] = count
            if count >= min_count:
                total = float(_rectangle_sum(sums, r0, c0, r1, c1))
                means[r, c] = total / count
    return means, observed
