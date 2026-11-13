"""Ordered Weighted Averaging for aligned 2D criterion arrays."""
from __future__ import annotations

from collections.abc import Sequence

import numpy as np
from numpy.typing import ArrayLike, NDArray


def orness(order_weights: ArrayLike) -> float:
    """Return Yager ORness for weights applied to descending sorted values."""
    weights = np.asarray(order_weights, dtype=np.float64)
    if weights.ndim != 1 or weights.size == 0:
        raise ValueError("order_weights must be a non-empty 1D array")
    if not np.all(np.isfinite(weights)) or np.any(weights < 0):
        raise ValueError("order_weights must be finite and non-negative")
    if not np.isclose(weights.sum(), 1.0):
        raise ValueError("order_weights must sum to one")
    if weights.size == 1:
        return 0.5
    positions = np.arange(weights.size, 0, -1, dtype=np.float64)
    return float(np.dot(positions - 1.0, weights) / (weights.size - 1))


def ordered_weighted_averaging(
    layers: Sequence[ArrayLike],
    order_weights: ArrayLike,
    criterion_weights: ArrayLike | None = None,
) -> NDArray[np.float64]:
    """Aggregate memberships/scores by descending rank at each grid cell.

    When criterion_weights are supplied, their identities follow the criterion
    values as those values are sorted (GIS weighted OWA). Without them, this
    is standard OWA. Finite inputs must lie in [0,1]. Any non-finite input
    makes that output cell NoData.
    """
    if not layers:
        raise ValueError("at least one criterion layer is required")
    arrays = [np.asarray(layer, dtype=np.float64) for layer in layers]
    shape = arrays[0].shape
    if len(shape) != 2 or 0 in shape or any(a.ndim != 2 or a.shape != shape for a in arrays):
        raise ValueError("all layers must be non-empty, aligned 2D arrays")
    stack = np.stack(arrays)
    finite = np.isfinite(stack)
    if np.any(finite & ((stack < 0.0) | (stack > 1.0))):
        raise ValueError("finite criterion scores must lie in [0, 1]")
    valid = np.all(finite, axis=0)

    n = len(arrays)
    order = np.asarray(order_weights, dtype=np.float64)
    if order.shape != (n,) or not np.all(np.isfinite(order)) or np.any(order < 0):
        raise ValueError("order_weights must be a finite non-negative vector matching layer count")
    if not np.isclose(order.sum(), 1.0):
        raise ValueError("order_weights must sum to one")

    if criterion_weights is None:
        importance = np.full(n, 1.0 / n)
    else:
        importance = np.asarray(criterion_weights, dtype=np.float64)
        if importance.shape != (n,) or not np.all(np.isfinite(importance)) or np.any(importance < 0):
            raise ValueError("criterion_weights must be a finite non-negative vector matching layer count")
        total = float(importance.sum())
        if total <= 0:
            raise ValueError("criterion_weights must have a positive sum")
        importance = importance / total

    # argsort is along the criterion axis, independently for every cell.
    order_index = np.argsort(-stack, axis=0, kind="stable")
    sorted_values = np.take_along_axis(stack, order_index, axis=0)
    sorted_importance = importance[order_index]
    numerator = np.sum(order[:, None, None] * sorted_importance * sorted_values, axis=0)
    denominator = np.sum(order[:, None, None] * sorted_importance, axis=0)
    result = np.full(shape, np.nan, dtype=np.float64)
    usable = valid & (denominator > 0)
    result[usable] = numerator[usable] / denominator[usable]
    return result
