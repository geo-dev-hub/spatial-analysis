"""Single-outlet watershed delineation from an existing D8 direction grid."""
from __future__ import annotations

from collections import deque
from typing import Sequence

import numpy as np

_DIRECTIONS = {
    1: (0, 1), 2: (1, 1), 4: (1, 0), 8: (1, -1),
    16: (0, -1), 32: (-1, -1), 64: (-1, 0), 128: (-1, 1),
}
_ALLOWED = {-1, 0, *_DIRECTIONS}


def delineate_watershed(
    directions: Sequence[Sequence[int]] | np.ndarray,
    *,
    outlet: tuple[int, int],
) -> np.ndarray:
    """Return cells whose D8 path reaches outlet; reject cyclic direction grids."""
    flow = np.asarray(directions)
    if flow.ndim != 2 or flow.size == 0:
        raise ValueError("directions must be a non-empty 2D array")
    if not np.issubdtype(flow.dtype, np.integer):
        raise ValueError("directions must contain integer direction codes")
    if not np.isin(flow, list(_ALLOWED)).all():
        raise ValueError("directions contain an unsupported D8 code")
    if len(outlet) != 2 or any(not isinstance(v, (int, np.integer)) for v in outlet):
        raise ValueError("outlet must be a (row, column) integer pair")

    rows, cols = flow.shape
    orow, ocol = map(int, outlet)
    if not (0 <= orow < rows and 0 <= ocol < cols):
        raise ValueError("outlet is outside the raster")
    if flow[orow, ocol] == -1:
        raise ValueError("outlet must be a valid cell")

    valid = flow != -1
    reverse: list[list[list[tuple[int, int]]]] = [
        [[] for _ in range(cols)] for _ in range(rows)
    ]
    indegree = np.zeros(flow.shape, dtype=np.int8)

    for r in range(rows):
        for c in range(cols):
            code = int(flow[r, c])
            if not valid[r, c] or code == 0:
                continue
            dr, dc = _DIRECTIONS[code]
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and valid[nr, nc]:
                reverse[nr][nc].append((r, c))
                indegree[nr, nc] += 1

    # Validate the entire valid flow graph, not only the outlet's upstream subset.
    queue = deque((int(r), int(c)) for r, c in zip(*np.where(valid & (indegree == 0))))
    processed = 0
    while queue:
        r, c = queue.popleft()
        processed += 1
        code = int(flow[r, c])
        if code == 0:
            continue
        dr, dc = _DIRECTIONS[code]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and valid[nr, nc]:
            indegree[nr, nc] -= 1
            if indegree[nr, nc] == 0:
                queue.append((nr, nc))
    if processed != int(valid.sum()):
        raise ValueError("flow-direction graph contains a cycle")

    basin = np.zeros(flow.shape, dtype=bool)
    basin[orow, ocol] = True
    stack = [(orow, ocol)]
    while stack:
        r, c = stack.pop()
        for ur, uc in reverse[r][c]:
            if not basin[ur, uc]:
                basin[ur, uc] = True
                stack.append((ur, uc))
    return basin
