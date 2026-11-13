"""Boolean and fuzzy overlay operators for aligned 2D arrays."""
from __future__ import annotations

from collections.abc import Sequence

import numpy as np
from numpy.typing import ArrayLike, NDArray


def _stack_layers(layers: Sequence[ArrayLike], *, boolean: bool = False) -> tuple[NDArray, NDArray]:
    if not layers:
        raise ValueError("at least one layer is required")
    arrays = [np.asarray(layer) for layer in layers]
    shape = arrays[0].shape
    if len(shape) != 2 or 0 in shape or any(a.ndim != 2 or a.shape != shape for a in arrays):
        raise ValueError("all layers must be non-empty, aligned 2D arrays")
    if boolean:
        if any(a.dtype != np.bool_ for a in arrays):
            raise ValueError("Boolean overlay layers must have Boolean dtype")
        valid = np.ones(shape, dtype=bool)
    else:
        arrays = [a.astype(np.float64) for a in arrays]
        valid = np.ones(shape, dtype=bool)
        for a in arrays:
            finite = np.isfinite(a)
            if np.any(finite & ((a < 0) | (a > 1))):
                raise ValueError("finite fuzzy memberships must lie in [0, 1]")
            valid &= finite
    return np.stack(arrays), valid


def boolean_overlay(layers: Sequence[ArrayLike], operation: str = "and") -> NDArray[np.bool_]:
    """Combine aligned Boolean masks with logical AND or OR."""
    stack, _ = _stack_layers(layers, boolean=True)
    if operation == "and":
        return np.all(stack, axis=0)
    if operation == "or":
        return np.any(stack, axis=0)
    raise ValueError("operation must be 'and' or 'or'")


def fuzzy_overlay(
    layers: Sequence[ArrayLike],
    operator: str = "gamma",
    *,
    gamma: float = 0.9,
) -> NDArray[np.float64]:
    """Combine [0,1] memberships; any non-finite input makes the cell NoData.

    Operators: min, product, max, probabilistic_sum, gamma.
    Gamma uses probabilistic_sum**gamma * product**(1-gamma).
    """
    stack, valid = _stack_layers(layers)
    if operator == "min":
        combined = np.min(stack, axis=0)
    elif operator == "product":
        combined = np.prod(stack, axis=0)
    elif operator == "max":
        combined = np.max(stack, axis=0)
    elif operator in {"probabilistic_sum", "gamma"}:
        summed = 1.0 - np.prod(1.0 - stack, axis=0)
        if operator == "probabilistic_sum":
            combined = summed
        else:
            if not np.isfinite(gamma) or not 0.0 <= gamma <= 1.0:
                raise ValueError("gamma must be finite and in [0, 1]")
            product = np.prod(stack, axis=0)
            combined = np.power(summed, gamma) * np.power(product, 1.0 - gamma)
    else:
        raise ValueError("unknown fuzzy overlay operator")
    result = np.full(stack.shape[1:], np.nan, dtype=np.float64)
    result[valid] = combined[valid]
    return result
