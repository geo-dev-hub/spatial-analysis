"""Weighted linear combination for aligned, standardised raster criteria."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import numpy as np
from numpy.typing import ArrayLike, NDArray


def weighted_linear_combination(
    criteria: Mapping[str, ArrayLike],
    weights: Mapping[str, float],
    *,
    eligible: ArrayLike | None = None,
) -> NDArray[np.float64]:
    """Aggregate same-shaped 2D criterion arrays using a weighted sum.

    Criterion values must already be standardised to [0, 1], with larger
    values consistently representing greater preference. Non-finite values
    are treated as NoData. A cell is scored only if every criterion is finite
    and, when supplied, its Boolean eligibility mask is True.

    Weights are relative non-negative importance values and are normalised
    internally to sum to one. This function does not standardise raw criteria,
    derive weights, resample rasters, or decide whether WLC is an appropriate
    decision rule.
    """
    if not isinstance(criteria, Mapping) or not criteria:
        raise ValueError("criteria must be a non-empty mapping")

    criterion_names = list(criteria)
    if any(not isinstance(name, str) or not name for name in criterion_names):
        raise ValueError("criterion names must be non-empty strings")

    if not isinstance(weights, Mapping):
        raise ValueError("weights must be a mapping")
    if set(weights) != set(criterion_names):
        raise ValueError("weights must contain exactly one value for each criterion")

    arrays: list[NDArray[np.float64]] = []
    shape: tuple[int, ...] | None = None
    valid = None

    for name in criterion_names:
        array = np.asarray(criteria[name], dtype=np.float64)
        if array.ndim != 2 or 0 in array.shape:
            raise ValueError(f"criterion {name!r} must be a non-empty 2D array")
        if shape is None:
            shape = array.shape
            valid = np.ones(shape, dtype=bool)
        elif array.shape != shape:
            raise ValueError("all criterion arrays must have the same shape")

        finite = np.isfinite(array)
        if np.any(finite & ((array < 0.0) | (array > 1.0))):
            raise ValueError("finite criterion scores must lie in [0, 1]")
        valid &= finite
        arrays.append(array)

    weight_values = np.asarray([weights[name] for name in criterion_names], dtype=np.float64)
    if not np.all(np.isfinite(weight_values)) or np.any(weight_values < 0.0):
        raise ValueError("weights must be finite and non-negative")
    total = float(weight_values.sum())
    if total <= 0.0:
        raise ValueError("at least one weight must be positive")
    normalised_weights = weight_values / total

    if eligible is not None:
        mask = np.asarray(eligible)
        if mask.dtype != np.bool_:
            raise ValueError("eligible must be a Boolean array")
        if mask.shape != shape:
            raise ValueError("eligible mask must have the same shape as the criteria")
        valid &= mask

    result = np.full(shape, np.nan, dtype=np.float64)
    if np.any(valid):
        score = np.zeros(int(np.count_nonzero(valid)), dtype=np.float64)
        for weight, array in zip(normalised_weights, arrays):
            score += weight * array[valid]
        result[valid] = score
    return result
