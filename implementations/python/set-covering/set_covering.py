"""Exact exhaustive location set-covering solver for small instances."""
from __future__ import annotations
from itertools import combinations
from math import isfinite
from typing import Sequence
import numpy as np


def solve_set_cover(costs: Sequence[Sequence[float]] | np.ndarray,
                    service_threshold: float
                    ) -> tuple[tuple[int, ...], int, tuple[int, ...]]:
    """Minimize the number of facilities needed to cover every demand row.

    A candidate covers demand i when costs[i, j] <= service_threshold.
    Returns (selected candidate indices, number opened, assigned candidate
    index per demand). Among minimum-cardinality solutions, the
    lexicographically first facility set is selected. Assignments go to the
    first selected site that covers each demand.
    """
    matrix = np.asarray(costs, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] == 0 or matrix.shape[1] == 0:
        raise ValueError("costs must be a non-empty 2D matrix")
    if not np.isfinite(matrix).all() or (matrix < 0).any():
        raise ValueError("costs must be finite and non-negative")
    if not isfinite(service_threshold) or service_threshold < 0:
        raise ValueError("service_threshold must be finite and non-negative")
    eligible = matrix <= float(service_threshold)
    unreachable = np.flatnonzero(~eligible.any(axis=1))
    if unreachable.size:
        raise ValueError(f"some demand rows have no eligible facility: {tuple(int(i) for i in unreachable)}")

    demand_count, facility_count = matrix.shape
    for size in range(1, facility_count + 1):
        for sites in combinations(range(facility_count), size):
            local = eligible[:, sites]
            if np.all(local.any(axis=1)):
                assignments = []
                for row in range(demand_count):
                    position = int(np.flatnonzero(local[row])[0])
                    assignments.append(sites[position])
                return sites, size, tuple(assignments)
    # Every demand row has at least one eligible site, so selecting all sites
    # must cover every row. Keep this guard for defensive completeness.
    raise RuntimeError("no covering facility set found despite eligible candidates")
