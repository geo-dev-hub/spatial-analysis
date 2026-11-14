"""Exact backup-coverage solver for small facility-location instances.

A demand row is backup-covered when at least r distinct selected facilities
are within the service threshold. This is a deterministic redundancy proxy,
not a probability-of-service or capacity model.
"""
from __future__ import annotations

from itertools import combinations
from math import isfinite
from typing import Sequence

import numpy as np


def solve_backup_coverage(
    costs: Sequence[Sequence[float]] | np.ndarray,
    p: int,
    service_threshold: float,
    *,
    required_cover_count: int = 2,
    demand_weights: Sequence[float] | np.ndarray | None = None,
) -> tuple[tuple[int, ...], float, tuple[bool, ...], tuple[int, ...]]:
    """Maximize weighted demand reached by at least r selected facilities.

    Returns (selected candidate indices, covered weight, covered flags,
    number of selected facilities reaching each demand row).

    The solver chooses at most p facilities. Equal objective values prefer
    fewer facilities, then lexicographically earlier candidate indices.
    """
    matrix = np.asarray(costs, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] == 0 or matrix.shape[1] == 0:
        raise ValueError("costs must be a non-empty 2D matrix")
    if not np.isfinite(matrix).all() or (matrix < 0).any():
        raise ValueError("costs must be finite and non-negative")
    if not isinstance(p, int) or isinstance(p, bool) or not 0 <= p <= matrix.shape[1]:
        raise ValueError("p must be an integer between zero and the number of candidate facilities")
    if not isinstance(required_cover_count, int) or isinstance(required_cover_count, bool) or required_cover_count < 1:
        raise ValueError("required_cover_count must be a positive integer")
    if required_cover_count > p:
        raise ValueError("required_cover_count cannot exceed the facility budget p")
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
    best_counts = np.zeros(n, dtype=int)
    best_covered = np.zeros(n, dtype=bool)
    best_value = 0.0

    for size in range(required_cover_count, p + 1):
        for sites in combinations(range(matrix.shape[1]), size):
            counts = eligible[:, sites].sum(axis=1)
            covered = counts >= required_cover_count
            value = float(weights[covered].sum())
            if value > best_value or (
                value == best_value and (len(sites), sites) < (len(best_sites), best_sites)
            ):
                best_sites = sites
                best_value = value
                best_counts = counts
                best_covered = covered

    return (
        best_sites,
        best_value,
        tuple(bool(v) for v in best_covered),
        tuple(int(v) for v in best_counts),
    )
