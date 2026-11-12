"""Small, dependency-free reference implementation of global Moran's I.

This module computes the statistic only. It does not calculate analytical
or permutation-based significance tests.
"""

from math import isfinite
from typing import Sequence


def _validated_weights(
    weights: Sequence[Sequence[float]], n: int
) -> list[list[float]]:
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


def row_standardize(weights: Sequence[Sequence[float]]) -> list[list[float]]:
    """Return row-standardized weights.

    Each nonzero row sums to one. A row with no neighbours remains a row
    of zeros; this represents an island and should be reported by the user.
    """
    n = len(weights)
    if n == 0:
        raise ValueError("weights must contain at least one row")

    matrix = _validated_weights(weights, n)
    standardized: list[list[float]] = []

    for row in matrix:
        row_sum = sum(row)
        if row_sum == 0:
            standardized.append([0.0] * n)
        else:
            standardized.append([weight / row_sum for weight in row])

    return standardized


def morans_i(
    values: Sequence[float], weights: Sequence[Sequence[float]]
) -> float:
    """Calculate global Moran's I for values and a dense weights matrix.

    Args:
        values: One continuous numeric value per spatial unit.
        weights: Dense n-by-n spatial weights matrix. Self-weights must be
            zero and weights must be finite and non-negative.

    Returns:
        The global Moran's I statistic.

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
    z = [value - mean for value in x]
    denominator = sum(value * value for value in z)
    if denominator == 0:
        raise ValueError("Moran's I is undefined for a constant variable")

    numerator = sum(
        w[i][j] * z[i] * z[j]
        for i in range(n)
        for j in range(n)
    )

    return (n / s0) * (numerator / denominator)
