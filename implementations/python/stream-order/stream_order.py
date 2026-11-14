"""Strahler stream order and Shreve magnitude on a D8 stream network."""
from __future__ import annotations

from collections import deque
from typing import Sequence

import numpy as np

_DIRECTIONS = {
    1: (0, 1), 2: (1, 1), 4: (1, 0), 8: (1, -1),
    16: (0, -1), 32: (-1, -1), 64: (-1, 0), 128: (-1, 1),
}
_ALLOWED = {-1, 0, *_DIRECTIONS}


def stream_order(
    directions: Sequence[Sequence[int]] | np.ndarray,
    stream_mask: Sequence[Sequence[bool]] | np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Return (Strahler order, Shreve magnitude) for the stream cells.

    Non-stream cells are zero; invalid direction cells are -1. The supplied
    stream mask must be downstream-connected: a stream cell may not flow into
    a valid non-stream cell.
    """
    flow = np.asarray(directions)
    streams = np.asarray(stream_mask, dtype=bool)
    if flow.ndim != 2 or flow.size == 0:
        raise ValueError("directions must be a non-empty 2D array")
    if not np.issubdtype(flow.dtype, np.integer):
        raise ValueError("directions must contain integer direction codes")
    if not np.isin(flow, list(_ALLOWED)).all():
        raise ValueError("directions contain an unsupported D8 code")
    if streams.shape != flow.shape:
        raise ValueError("stream_mask must have the same shape as directions")

    valid = flow != -1
    if (streams & ~valid).any():
        raise ValueError("stream_mask cannot include invalid direction cells")
    rows, cols = flow.shape
    stream_cells = streams
    indegree = np.zeros(flow.shape, dtype=np.int8)
    downstream = np.full((rows, cols, 2), -1, dtype=np.int32)

    for r in range(rows):
        for c in range(cols):
            if not stream_cells[r, c] or flow[r, c] == 0:
                continue
            dr, dc = _DIRECTIONS[int(flow[r, c])]
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and valid[nr, nc]:
                if not stream_cells[nr, nc]:
                    raise ValueError("stream mask is not downstream-connected")
                downstream[r, c] = (nr, nc)
                indegree[nr, nc] += 1

    order = np.zeros(flow.shape, dtype=np.int32)
    magnitude = np.zeros(flow.shape, dtype=np.int64)
    order[~valid] = -1
    magnitude[~valid] = -1
    max_incoming_order = np.zeros(flow.shape, dtype=np.int32)
    max_order_count = np.zeros(flow.shape, dtype=np.int8)

    queue = deque((int(r), int(c)) for r, c in zip(*np.where(stream_cells & (indegree == 0))))
    processed = 0
    while queue:
        r, c = queue.popleft()
        processed += 1
        if order[r, c] == 0:
            order[r, c] = 1
            magnitude[r, c] = 1
        nr, nc = downstream[r, c]
        if nr >= 0:
            incoming = int(order[r, c])
            if incoming > max_incoming_order[nr, nc]:
                max_incoming_order[nr, nc] = incoming
                max_order_count[nr, nc] = 1
            elif incoming == max_incoming_order[nr, nc]:
                max_order_count[nr, nc] += 1
            magnitude[nr, nc] += magnitude[r, c]
            indegree[nr, nc] -= 1
            if indegree[nr, nc] == 0:
                order[nr, nc] = max_incoming_order[nr, nc] + int(max_order_count[nr, nc] >= 2)
                queue.append((int(nr), int(nc)))

    if processed != int(stream_cells.sum()):
        raise ValueError("stream network contains a cycle")
    return order, magnitude
