"""Topological D8 flow accumulation for an existing direction raster."""
from __future__ import annotations

from collections import deque
from typing import Sequence

import numpy as np

# (row offset, column offset, ESRI code)
_DIRECTIONS = {
    1: (0, 1),
    2: (1, 1),
    4: (1, 0),
    8: (1, -1),
    16: (0, -1),
    32: (-1, -1),
    64: (-1, 0),
    128: (-1, 1),
}
_ALLOWED = {-1, 0, *_DIRECTIONS}


def d8_flow_accumulation(
    directions: Sequence[Sequence[int]] | np.ndarray,
    *,
    weights: Sequence[Sequence[float]] | np.ndarray | None = None,
) -> np.ndarray:
    """Return upstream accumulation including each cell's own weight.

    Out-of-grid flow and flow into invalid (-1) cells leave the valid domain.
    A directed cycle is rejected. Invalid cells are returned as NaN.
    """
    flow = np.asarray(directions)
    if flow.ndim != 2 or flow.size == 0:
        raise ValueError("directions must be a non-empty 2D array")
    if not np.issubdtype(flow.dtype, np.integer):
        raise ValueError("directions must contain integer direction codes")
    if not np.isin(flow, list(_ALLOWED)).all():
        raise ValueError("directions contain an unsupported D8 code")

    valid = flow != -1
    rows, cols = flow.shape
    if weights is None:
        contribution = np.ones(flow.shape, dtype=float)
    else:
        contribution = np.asarray(weights, dtype=float)
        if contribution.shape != flow.shape:
            raise ValueError("weights must have the same shape as directions")
        if not np.isfinite(contribution[valid]).all() or (contribution[valid] < 0).any():
            raise ValueError("valid-cell weights must be finite and non-negative")

    accumulation = np.full(flow.shape, np.nan, dtype=float)
    accumulation[valid] = contribution[valid]
    indegree = np.zeros(flow.shape, dtype=np.int8)
    downstream = np.full((rows, cols, 2), -1, dtype=np.int32)

    for r in range(rows):
        for c in range(cols):
            if not valid[r, c] or flow[r, c] == 0:
                continue
            dr, dc = _DIRECTIONS[int(flow[r, c])]
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and valid[nr, nc]:
                downstream[r, c] = (nr, nc)
                indegree[nr, nc] += 1

    queue = deque((int(r), int(c)) for r, c in zip(*np.where(valid & (indegree == 0))))
    processed = 0
    while queue:
        r, c = queue.popleft()
        processed += 1
        nr, nc = downstream[r, c]
        if nr >= 0:
            accumulation[nr, nc] += accumulation[r, c]
            indegree[nr, nc] -= 1
            if indegree[nr, nc] == 0:
                queue.append((int(nr), int(nc)))

    if processed != int(valid.sum()):
        raise ValueError("flow-direction graph contains a cycle")
    return accumulation
