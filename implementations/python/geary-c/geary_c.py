"""Small, dependency-free reference implementation of global Geary's C.

This module computes the statistic only. It does not calculate analytical
or permutation-based significance tests.
"""

from math import isfinite
from typing import Sequence


def _validated_weights(weights: Sequence[Sequence[float]], n: int) -> list[list[float]]:
    """Validate and copy a dense spatial weights matrix."""
    if len(weights) != n:
        raise ValueError("weights must have one row per observation")

    matrix: list[list[float]] = []
    for i, row in enumerate(weights):
        if len(row) != n:
            raise ValueError("weights must be a square n-by-n matrix")
        clean_row: list[float] = []
        for j, raw_weight in enumerate(row):
            weight = float(raw_weight)
            if not isfinite(weight):
                raise ValueError("weights must contain only finite values")
            if weight < 0:
                raise ValueError("weights must be non-negative")
            if i == j and weight != 0:
                raise ValueError("self-weights must be zero")
            clean_row.append(weight)
        matrix.append(clean_row)
    return matrix


def gearys_c(values: Sequence[float], weights: Sequence[Sequence[float]]) -> float:
    """Calculate global Geary's C for values and a dense spatial weights matrix.

    Args:
        values: One continuous numeric value per spatial unit.
        weights: Dense n-by-n matrix with finite non-negative weights and
            a zero diagonal. The matrix need not be symmetric.

    Returns:
        The global Geary's C statistic.

    Raises:
        ValueError: If inputs are misaligned, invalid, constant, or contain
            no positive spatial weights.
    """
    n = len(values)
    if n < 2:
        raise ValueError("at least two observations are required")

    x = [float(value) for value in values]
    if not all(isfinite(value) for value in x):
        raise ValueError("values must contain only finite numbers")

    w = _validated_weights(weights, n)
    s0 = sum(sum(row) for row in w)
    if s0 <= 0:
        raise ValueError("the spatial weights matrix must contain a positive weight")

    mean = sum(x) / n
    denominator = sum((value - mean) ** 2 for value in x)
    if denominator == 0:
        raise ValueError("Geary's C is undefined for a constant variable")

    numerator = sum(
        w[i][j] * (x[i] - x[j]) ** 2
        for i in range(n)
        for j in range(n)
    )
    return ((n - 1) / (2 * s0)) * (numerator / denominator)
