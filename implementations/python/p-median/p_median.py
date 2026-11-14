"""Exact exhaustive p-median solver for small cost matrices."""
from __future__ import annotations

from itertools import combinations
from math import isfinite
from typing import Sequence

import numpy as np


def solve_p_median(
    costs: Sequence[Sequence[float]] | np.ndarray,
    p: int,
    *,
    demand_weights: Sequence[float] | np.ndarray | None = None,
) -> tuple[tuple[int, ...], float, tuple[int, ...]]:
    """Return (open facility indices, objective, assigned facility per demand)."""
    matrix = np.asarray(costs, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] == 0 or matrix.shape[1] == 0:
        raise ValueError("costs must be a non-empty 2D matrix")
    if not np.isfinite(matrix).all() or (matrix < 0).any():
        raise ValueError("costs must be finite and non-negative")
    demand_count, facility_count = matrix.shape
    if not isinstance(p, int) or isinstance(p, bool) or not 1 <= p <= facility_count:
        raise ValueError("p must be an integer between 1 and the number of candidate facilities")

    if demand_weights is None:
        weights = np.ones(demand_count, dtype=float)
    else:
        weights = np.asarray(demand_weights, dtype=float)
        if weights.shape != (demand_count,):
            raise ValueError("demand_weights must have one value per demand row")
        if not np.isfinite(weights).all() or (weights < 0).any() or not (weights > 0).any():
            raise ValueError("demand_weights must be finite, non-negative and not all zero")

    best_facilities: tuple[int, ...] | None = None
    best_assignment: tuple[int, ...] | None = None
    best_objective = float("inf")
    for opened in combinations(range(facility_count), p):
        open_costs = matrix[:, opened]
        local_positions = np.argmin(open_costs, axis=1)
        assigned = tuple(opened[position] for position in local_positions)
        minimum_costs = open_costs[np.arange(demand_count), local_positions]
        objective = float(weights @ minimum_costs)
        # combinations are lexicographic, so strict improvement preserves the
        # lexicographically first solution when objective values tie.
        if objective < best_objective:
            best_objective = objective
            best_facilities = opened
            best_assignment = assigned

    assert best_facilities is not None and best_assignment is not None
    return best_facilities, best_objective, best_assignment
