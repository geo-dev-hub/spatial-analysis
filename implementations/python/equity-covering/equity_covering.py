"""Exact small-instance equity-constrained maximal covering baseline."""
from __future__ import annotations
import math
from itertools import combinations


def equity_maximal_covering(
    travel_costs, groups, group_minimum_coverage, max_facilities, max_cost,
    demand_weights=None, objective_weights=None,
):
    """Maximise covered objective weight subject to group population coverage floors.

    Rows are demand units; columns are candidate facilities. Positive infinity
    denotes an unreachable pair. Each demand row belongs to exactly one group.
    """
    matrix = [[float(v) for v in row] for row in travel_costs]
    if not matrix or not matrix[0]:
        raise ValueError("travel_costs must be a non-empty rectangular matrix")
    n, m = len(matrix), len(matrix[0])
    if any(len(row) != m for row in matrix):
        raise ValueError("travel_costs must be rectangular")
    if any(math.isnan(v) or v < 0 or v == -math.inf for row in matrix for v in row):
        raise ValueError("travel costs must be non-negative; positive infinity may mark unreachable pairs")
    if isinstance(max_facilities, bool) or not isinstance(max_facilities, int) or not 0 <= max_facilities <= m:
        raise ValueError("max_facilities must be an integer between zero and the candidate count")
    threshold = float(max_cost)
    if not math.isfinite(threshold) or threshold < 0:
        raise ValueError("max_cost must be finite and non-negative")
    if len(groups) != n or any(not str(g).strip() for g in groups):
        raise ValueError("groups must provide one non-empty label per demand row")
    labels = [str(g) for g in groups]
    unique_groups = sorted(set(labels))
    if set(group_minimum_coverage) != set(unique_groups):
        raise ValueError("group_minimum_coverage must define exactly the observed groups")
    floors = {g: float(group_minimum_coverage[g]) for g in unique_groups}
    if any(not math.isfinite(v) or not 0 <= v <= 1 for v in floors.values()):
        raise ValueError("group coverage floors must lie between zero and one")
    demand = [1.0] * n if demand_weights is None else [float(v) for v in demand_weights]
    objective = demand[:] if objective_weights is None else [float(v) for v in objective_weights]
    for name, weights in (("demand_weights", demand), ("objective_weights", objective)):
        if len(weights) != n or any(not math.isfinite(v) or v < 0 for v in weights):
            raise ValueError(f"{name} must be finite, non-negative and match demand rows")
    group_totals = {g: math.fsum(demand[i] for i in range(n) if labels[i] == g) for g in unique_groups}
    if any(total <= 0 for total in group_totals.values()):
        raise ValueError("each group must have positive total demand weight")
    if math.fsum(objective) <= 0:
        raise ValueError("objective_weights must have a positive total")

    best = None
    best_value = -math.inf
    for size in range(max_facilities + 1):
        for selected in combinations(range(m), size):
            covered = tuple(
                i for i, row in enumerate(matrix)
                if any(row[j] <= threshold for j in selected)
            )
            covered_set = set(covered)
            shares = {
                g: math.fsum(demand[i] for i in covered if labels[i] == g) / group_totals[g]
                for g in unique_groups
            }
            if any(shares[g] + 1e-12 < floors[g] for g in unique_groups):
                continue
            value = math.fsum(objective[i] for i in covered)
            if (value > best_value or
                (value == best_value and best is not None and
                 (len(selected), selected) < (len(best[0]), best[0]))):
                best_value = value
                best = (selected, covered, shares)
    if best is None:
        raise ValueError("no facility set satisfies all group coverage floors")
    return {
        "selected_facilities": best[0],
        "covered_demand": best[1],
        "objective": best_value,
        "group_coverage": best[2],
        "max_facilities": max_facilities,
        "max_cost": threshold,
    }
