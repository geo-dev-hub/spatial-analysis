"""Eight-neighbour Priority-Flood depression filling for a DEM."""
from __future__ import annotations

import heapq
from itertools import count
from typing import Sequence

import numpy as np

_NEIGHBOURS = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
)


def priority_flood(
    elevation: Sequence[Sequence[float]] | np.ndarray,
    *,
    valid_mask: np.ndarray | None = None,
    nodata: float | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Return (filled DEM, fill depth); invalid cells are NaN.

    Every valid raster-edge cell and every valid cell adjacent to an invalid
    cell is a seed/outlet. Depressions are filled to their lowest spill level.
    """
    dem = np.asarray(elevation, dtype=float)
    if dem.ndim != 2 or dem.size == 0:
        raise ValueError("elevation must be a non-empty 2D array")

    valid = np.isfinite(dem)
    if nodata is not None:
        valid &= dem != nodata
    if valid_mask is not None:
        mask = np.asarray(valid_mask, dtype=bool)
        if mask.shape != dem.shape:
            raise ValueError("valid_mask must have the same shape as elevation")
        valid &= mask
    if not valid.any():
        raise ValueError("elevation must contain at least one valid cell")

    rows, cols = dem.shape
    filled = np.full(dem.shape, np.nan, dtype=float)
    filled[valid] = dem[valid]
    visited = np.zeros(dem.shape, dtype=bool)
    heap: list[tuple[float, int, int, int]] = []
    sequence = count()

    # Seed all valid cells that touch the raster edge or a NoData boundary.
    for r in range(rows):
        for c in range(cols):
            if not valid[r, c]:
                continue
            boundary = r == 0 or c == 0 or r == rows - 1 or c == cols - 1
            if not boundary:
                boundary = any(
                    not valid[r + dr, c + dc]
                    for dr, dc in _NEIGHBOURS
                    if 0 <= r + dr < rows and 0 <= c + dc < cols
                )
            if boundary:
                visited[r, c] = True
                heapq.heappush(heap, (float(dem[r, c]), r, c, next(sequence)))

    while heap:
        level, r, c, _ = heapq.heappop(heap)
        for dr, dc in _NEIGHBOURS:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if not valid[nr, nc] or visited[nr, nc]:
                continue
            visited[nr, nc] = True
            filled[nr, nc] = max(float(dem[nr, nc]), level)
            heapq.heappush(
                heap, (float(filled[nr, nc]), nr, nc, next(sequence))
            )

    depth = np.full(dem.shape, np.nan, dtype=float)
    depth[valid] = filled[valid] - dem[valid]
    return filled, depth
