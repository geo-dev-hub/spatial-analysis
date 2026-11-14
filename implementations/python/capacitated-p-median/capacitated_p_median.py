"""Exact exhaustive capacitated p-median solver for small instances."""
from __future__ import annotations
from itertools import combinations, product
from typing import Sequence
import numpy as np

def solve_capacitated_p_median(costs: Sequence[Sequence[float]] | np.ndarray, p: int, *, capacities: Sequence[float] | np.ndarray, demand_quantities: Sequence[float] | np.ndarray, demand_weights: Sequence[float] | np.ndarray | None = None) -> tuple[tuple[int, ...], float, tuple[int, ...]]:
    """Return opened candidates, weighted cost and assigned candidate per demand."""
    matrix = np.asarray(costs, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] == 0 or matrix.shape[1] == 0:
        raise ValueError("costs must be a non-empty 2D matrix")
    if not np.isfinite(matrix).all() or (matrix < 0).any():
        raise ValueError("costs must be finite and non-negative")
    n, m = matrix.shape
    if not isinstance(p, int) or isinstance(p, bool) or not 1 <= p <= m:
        raise ValueError("p must be an integer between 1 and the number of candidate facilities")
    cap = np.asarray(capacities, dtype=float)
    if cap.shape != (m,) or not np.isfinite(cap).all() or (cap < 0).any():
        raise ValueError("capacities must be finite, non-negative and have one value per candidate")
    quantities = np.asarray(demand_quantities, dtype=float)
    if quantities.shape != (n,) or not np.isfinite(quantities).all() or (quantities < 0).any():
        raise ValueError("demand_quantities must be finite, non-negative and have one value per demand row")
    if not (quantities > 0).any():
        raise ValueError("demand_quantities must contain at least one positive value")
    if demand_weights is None:
        weights = np.ones(n, dtype=float)
    else:
        weights = np.asarray(demand_weights, dtype=float)
        if weights.shape != (n,) or not np.isfinite(weights).all() or (weights < 0).any() or not (weights > 0).any():
            raise ValueError("demand_weights must be finite, non-negative and not all zero")
    best_key = None
    best_objective = float("inf")
    tolerance = 1e-10
    for opened in combinations(range(m), p):
        for positions in product(range(p), repeat=n):
            assignment = tuple(opened[k] for k in positions)
            loads = np.zeros(p, dtype=float)
            for i, k in enumerate(positions):
                loads[k] += quantities[i]
            if any(loads[k] > cap[site] + tolerance for k, site in enumerate(opened)):
                continue
            objective = float(weights @ matrix[np.arange(n), assignment])
            key = (opened, assignment)
            if objective < best_objective or (objective == best_objective and (best_key is None or key < best_key)):
                best_objective, best_key = objective, key
    if best_key is None:
        raise ValueError("no feasible assignment satisfies the selected facilities' capacities")
    return best_key[0], best_objective, best_key[1]
