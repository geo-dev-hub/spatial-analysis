"""Top-down dasymetric allocation from source zones to target units."""
from __future__ import annotations
import numpy as np


def dasymetric_allocate(source_totals, ancillary_weights, *, eligible_mask=None, zero_weight="error"):
    """Allocate each source-zone total to eligible target units by ancillary weight.

    ancillary_weights[i, j] is a non-negative proxy weight for allocating
    source zone i to target unit j (for example, building floor area or a
    built-up fraction). eligible_mask defines which target units intersect
    each source zone. If omitted, positive weights define eligibility.

    The method conserves each source total. If an eligible row has zero total
    weight, zero_weight='uniform' distributes equally over its eligible
    targets; 'error' rejects the row. It does not perform polygon overlays,
    estimate population, or infer the validity of the ancillary proxy.
    """
    totals = np.asarray(source_totals, dtype=float)
    weights = np.asarray(ancillary_weights, dtype=float)
    if totals.ndim != 1 or totals.size == 0:
        raise ValueError("source_totals must be a non-empty 1D array")
    if weights.ndim != 2 or weights.shape[0] != totals.size or weights.shape[1] == 0:
        raise ValueError("ancillary_weights must be a non-empty 2D matrix with one row per source")
    if not np.all(np.isfinite(totals)) or np.any(totals < 0):
        raise ValueError("source_totals must be finite and non-negative")
    if not np.all(np.isfinite(weights)) or np.any(weights < 0):
        raise ValueError("ancillary_weights must be finite and non-negative")
    if zero_weight not in {"error", "uniform"}:
        raise ValueError("zero_weight must be 'error' or 'uniform'")

    if eligible_mask is None:
        eligible = weights > 0
    else:
        eligible = np.asarray(eligible_mask, dtype=bool)
        if eligible.shape != weights.shape:
            raise ValueError("eligible_mask must have the same shape as ancillary_weights")
        if np.any((weights > 0) & ~eligible):
            raise ValueError("positive ancillary weights cannot be outside eligible_mask")

    allocations = np.zeros_like(weights, dtype=float)
    fallback_rows = []
    for row, total in enumerate(totals):
        if total == 0:
            continue
        active = eligible[row]
        count = int(np.count_nonzero(active))
        if count == 0:
            raise ValueError(f"source row {row} has positive total but no eligible targets")
        row_weights = weights[row, active]
        weight_sum = float(row_weights.sum())
        if weight_sum > 0:
            shares = row_weights / weight_sum
        elif zero_weight == "uniform":
            shares = np.full(count, 1.0 / count)
            fallback_rows.append(row)
        else:
            raise ValueError(f"source row {row} has eligible targets but zero ancillary weight")
        allocations[row, active] = total * shares

    return {
        "allocations": allocations,
        "target_totals": allocations.sum(axis=0),
        "source_totals_reconstructed": allocations.sum(axis=1),
        "uniform_fallback_rows": tuple(fallback_rows),
        "allocation_method": "within_source_normalized_ancillary_weights",
    }
