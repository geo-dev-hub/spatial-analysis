"""Classical three-product triple-collocation error-variance estimates."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class TripleCollocationResult:
    """Error variances, complete-case sample size and sample covariance matrix."""

    error_variances: tuple[float, float, float]
    covariance: np.ndarray
    n_observations: int


def triple_collocation(
    product_1: np.ndarray,
    product_2: np.ndarray,
    product_3: np.ndarray,
    *,
    denominator_tolerance: float = 1e-12,
) -> TripleCollocationResult:
    """Estimate classical TC error variances from three matched product arrays.

    Inputs must already refer to the same variable and collocated support.
    Rows containing a non-finite value in any product are removed jointly.
    Negative estimates are returned unchanged as diagnostics.
    """
    arrays = [np.asarray(values, dtype=float) for values in
              (product_1, product_2, product_3)]
    if any(values.ndim != 1 for values in arrays):
        raise ValueError("Each product must be a one-dimensional array.")
    if len({values.size for values in arrays}) != 1:
        raise ValueError("All products must have the same number of rows.")
    if not np.isfinite(denominator_tolerance) or denominator_tolerance <= 0:
        raise ValueError("denominator_tolerance must be finite and positive.")

    matched = np.column_stack(arrays)
    matched = matched[np.all(np.isfinite(matched), axis=1)]
    n = matched.shape[0]
    if n < 3:
        raise ValueError("At least three complete matched observations are required.")

    covariance = np.cov(matched, rowvar=False, ddof=1)
    c12, c13, c23 = covariance[0, 1], covariance[0, 2], covariance[1, 2]
    denominators = (c23, c13, c12)
    if any(abs(value) <= denominator_tolerance for value in denominators):
        raise ValueError(
            "A cross-covariance is too close to zero for a stable TC estimate."
        )

    variances = (
        covariance[0, 0] - c12 * c13 / c23,
        covariance[1, 1] - c12 * c23 / c13,
        covariance[2, 2] - c13 * c23 / c12,
    )
    return TripleCollocationResult(
        error_variances=tuple(float(value) for value in variances),
        covariance=covariance,
        n_observations=n,
    )
