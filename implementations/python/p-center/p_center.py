"""Exact exhaustive p-center solver for small cost matrices."""
from __future__ import annotations
from itertools import combinations
from typing import Sequence
import numpy as np


def solve_p_center(costs: Sequence[Sequence[float]] | np.ndarray,
                   p: int) -> tuple[tuple[int, ...], float, tuple[int, ...]]:
    """Return (open facility indices, worst assignment cost, assignments).

    Exactly p facilities are opened. Each demand is assigned to its nearest
    open candidate. Equal-radius solutions retain the lexicographically first
    facility set; assignment ties resolve to the earliest candidate index.
    """
    matrix = np.asarray(costs, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] == 0 or matrix.shape[1] == 0:
        raise ValueError("costs must be a non-empty 2D matrix")
    if not np.isfinite(matrix).all() or (matrix < 0).any():
        raise ValueError("costs must be finite and non-negative")
    m = matrix.shape[1]
    if not isinstance(p, int) or isinstance(p, bool) or not 1 <= p <= m:
        raise ValueError("p must be an integer between 1 and the number of candidate facilities")
    best_sites: tuple[int, ...] | None = None
    best_radius = float("inf")
    best_assignment: tuple[int, ...] | None = None
    for sites in combinations(range(m), p):
        local = matrix[:, sites]
        positions = np.argmin(local, axis=1)
        minimum = local[np.arange(matrix.shape[0]), positions]
        radius = float(minimum.max())
        if radius < best_radius:
            best_sites = sites
            best_radius = radius
            best_assignment = tuple(sites[int(k)] for k in positions)
    assert best_sites is not None and best_assignment is not None
    return best_sites, best_radius, best_assignment
