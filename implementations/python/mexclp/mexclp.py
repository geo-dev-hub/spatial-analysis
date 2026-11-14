"""Exact small-instance MEXCLP solver under equal independent busy fractions."""
from __future__ import annotations

from itertools import combinations_with_replacement
from math import isfinite
from numbers import Real
from typing import Sequence


def solve_mexclp(
    costs: Sequence[Sequence[float]],
    p: int,
    service_threshold: float,
    busy_fraction: float,
    *,
    demand_weights: Sequence[float] | None = None,
) -> tuple[tuple[int, ...], float, tuple[float, ...]]:
    """Choose exactly p unit placements to maximise expected covered demand.

    Candidate indices may repeat: more than one unit may be placed at a site.
    Returns (unit site indices, expected covered demand, per-demand contributions).
    Ties are resolved by lexicographically earlier sorted placement tuples.
    """
    try:
        matrix = [[float(value) for value in row] for row in costs]
    except (TypeError, ValueError) as exc:
        raise ValueError("costs must be a rectangular numeric matrix") from exc
    if not matrix or not matrix[0] or any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("costs must be a non-empty rectangular matrix")
    if any(not isfinite(value) or value < 0 for row in matrix for value in row):
        raise ValueError("costs must be finite and non-negative")
    if not isinstance(p, int) or isinstance(p, bool) or p < 0:
        raise ValueError("p must be a non-negative integer")
    if not isinstance(service_threshold, Real) or isinstance(service_threshold, bool):
        raise ValueError("service_threshold must be a real numeric value")
    try:
        threshold = float(service_threshold)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError("service_threshold must be finite and non-negative") from exc
    if not isfinite(threshold) or threshold < 0:
        raise ValueError("service_threshold must be finite and non-negative")
    if not isinstance(busy_fraction, Real) or isinstance(busy_fraction, bool):
        raise ValueError("busy_fraction must be a real numeric value")
    try:
        q = float(busy_fraction)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError("busy_fraction must be in [0, 1)") from exc
    if not isfinite(q) or not 0 <= q < 1:
        raise ValueError("busy_fraction must be in [0, 1)")
    n, m = len(matrix), len(matrix[0])
    if demand_weights is None:
        weights = [1.0] * n
    else:
        try:
            weights = [float(value) for value in demand_weights]
        except (TypeError, ValueError) as exc:
            raise ValueError("demand_weights must be numeric") from exc
        if len(weights) != n or any(not isfinite(value) or value < 0 for value in weights):
            raise ValueError("demand_weights must be finite, non-negative and match demand rows")

    eligible = [[value <= threshold for value in row] for row in matrix]
    best_sites: tuple[int, ...] | None = None
    best_contributions: tuple[float, ...] = ()
    best_value = float("-inf")
    for sites in combinations_with_replacement(range(m), p):
        counts = [sum(1 for site in sites if eligible[i][site]) for i in range(n)]
        contributions = tuple(
            weights[i] * (1.0 - q ** counts[i]) for i in range(n)
        )
        value = sum(contributions)
        if value > best_value or (value == best_value and (best_sites is None or sites < best_sites)):
            best_sites, best_value, best_contributions = sites, value, contributions

    # combinations_with_replacement yields one empty placement when p == 0.
    assert best_sites is not None
    return best_sites, best_value, best_contributions
