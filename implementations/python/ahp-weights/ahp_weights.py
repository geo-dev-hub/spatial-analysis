"""A small, explicit Analytic Hierarchy Process priority-weight baseline."""
from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray

_RANDOM_INDEX = {
    1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12,
    6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49,
}


@dataclass(frozen=True)
class AHPResult:
    """Normalised priorities and conventional consistency diagnostics."""
    criteria: tuple[str, ...]
    weights: NDArray[np.float64]
    lambda_max: float
    consistency_index: float
    consistency_ratio: float | None


def ahp_weights(matrix: ArrayLike, criteria: Sequence[str] | None = None) -> AHPResult:
    """Derive principal-eigenvector priorities from a positive reciprocal matrix.

    CR is None for n=1 or n=2 because the conventional random-index reference
    is zero for those orders.
    """
    a = np.asarray(matrix, dtype=np.float64)
    if a.ndim != 2 or a.shape[0] != a.shape[1] or a.shape[0] == 0:
        raise ValueError("matrix must be a non-empty square 2D array")
    n = a.shape[0]
    if not np.all(np.isfinite(a)) or np.any(a <= 0.0):
        raise ValueError("matrix entries must be finite and strictly positive")
    if not np.allclose(np.diag(a), 1.0, rtol=1e-9, atol=1e-9):
        raise ValueError("matrix diagonal must contain ones")
    if not np.allclose(a * a.T, 1.0, rtol=1e-7, atol=1e-9):
        raise ValueError("matrix must be reciprocal")

    if criteria is None:
        names = tuple(f"criterion_{i + 1}" for i in range(n))
    else:
        names = tuple(criteria)
        if len(names) != n or any(not isinstance(x, str) or not x for x in names):
            raise ValueError("criteria must contain one non-empty name per matrix row")
        if len(set(names)) != n:
            raise ValueError("criterion names must be unique")

    eigenvalues, eigenvectors = np.linalg.eig(a)
    index = int(np.argmax(eigenvalues.real))
    principal_value = eigenvalues[index]
    vector = eigenvectors[:, index].real
    if vector.sum() < 0:
        vector = -vector
    if np.any(vector <= 0.0) or not np.isfinite(vector).all():
        raise ArithmeticError("could not obtain a positive principal priority vector")
    weights = vector / vector.sum()
    lambda_max = float(principal_value.real)
    ci = 0.0 if n == 1 else max(0.0, (lambda_max - n) / (n - 1))
    ri = _RANDOM_INDEX.get(n)
    cr = None if ri is None or ri == 0.0 else ci / ri
    return AHPResult(names, weights.astype(np.float64), lambda_max, ci, cr)
