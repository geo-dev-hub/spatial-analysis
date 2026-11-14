"""Exact maximal covering location solver for small instances."""
from __future__ import annotations
from itertools import combinations
from math import isfinite
from typing import Sequence
import numpy as np


def solve_maximal_covering(costs: Sequence[Sequence[float]] | np.ndarray,
                           p: int, service_threshold: float, *,
                           demand_weights: Sequence[float] | np.ndarray | None = None
                           ) -> tuple[tuple[int, ...], float, tuple[bool, ...]]:
    """Select at most p sites to maximize demand weight within the threshold.

    Returns (selected candidate indices, covered demand weight, covered flags).
    Ties prefer fewer sites, then lexicographically earlier candidate indices.
    """
    matrix = np.asarray(costs, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] == 0 or matrix.shape[1] == 0:
        raise ValueError("costs must be a non-empty 2D matrix")
    if not np.isfinite(matrix).all() or (matrix < 0).any():
        raise ValueError("costs must be finite and non-negative")
    if not isinstance(p, int) or isinstance(p, bool) or not 0 <= p <= matrix.shape[1]:
        raise ValueError("p must be an integer between zero and the number of candidate facilities")
    if not isfinite(service_threshold) or service_threshold < 0:
        raise ValueError("service_threshold must be finite and non-negative")
    n = matrix.shape[0]
    if demand_weights is None:
        weights = np.ones(n, dtype=float)
    else:
        weights = np.asarray(demand_weights, dtype=float)
        if weights.shape != (n,):
            raise ValueError("demand_weights must have one value per demand row")
        if not np.isfinite(weights).all() or (weights < 0).any():
            raise ValueError("demand_weights must be finite and non-negative")
    eligible = matrix <= float(service_threshold)
    best_sites: tuple[int, ...] = ()
    best_covered = np.zeros(n, dtype=bool)
    best_value = 0.0
    for size in range(p + 1):
        for sites in combinations(range(matrix.shape[1]), size):
            covered = np.any(eligible[:, sites], axis=1) if sites else np.zeros(n, dtype=bool)
            value = float(weights[covered].sum())
            if value > best_value or (value == best_value and (len(sites), sites) < (len(best_sites), best_sites)):
                best_sites, best_value, best_covered = sites, value, covered
    return best_sites, best_value, tuple(bool(v) for v in best_covered)
