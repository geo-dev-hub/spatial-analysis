"""Classical vector-normalised TOPSIS for a finite decision matrix."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray


@dataclass(frozen=True)
class TOPSISResult:
    scores: NDArray[np.float64]
    distance_to_ideal: NDArray[np.float64]
    distance_to_anti_ideal: NDArray[np.float64]
    ranking: NDArray[np.int64]


def topsis(
    decision_matrix: ArrayLike,
    weights: ArrayLike,
    benefit: ArrayLike,
) -> TOPSISResult:
    """Rank rows (alternatives) using vector normalisation and Euclidean distance.

    All matrix entries must be finite and non-negative. benefit[j] is True
    when larger values are preferred for criterion j, otherwise the criterion
    is treated as a cost. Weights are non-negative and normalised internally.
    """
    x = np.asarray(decision_matrix, dtype=np.float64)
    if x.ndim != 2 or 0 in x.shape:
        raise ValueError("decision_matrix must be a non-empty 2D array")
    m, n = x.shape
    if not np.all(np.isfinite(x)) or np.any(x < 0):
        raise ValueError("decision_matrix values must be finite and non-negative")
    w = np.asarray(weights, dtype=np.float64)
    if w.shape != (n,) or not np.all(np.isfinite(w)) or np.any(w < 0):
        raise ValueError("weights must be a finite non-negative vector matching criteria")
    total = float(w.sum())
    if total <= 0:
        raise ValueError("at least one criterion weight must be positive")
    w = w / total
    benefit_mask = np.asarray(benefit)
    if benefit_mask.dtype != np.bool_ or benefit_mask.shape != (n,):
        raise ValueError("benefit must be a Boolean vector matching criteria")

    norms = np.linalg.norm(x, axis=0)
    if np.any(norms == 0):
        raise ValueError("zero-norm criteria cannot be vector-normalised")
    weighted = (x / norms) * w
    positive = np.where(benefit_mask, np.max(weighted, axis=0), np.min(weighted, axis=0))
    negative = np.where(benefit_mask, np.min(weighted, axis=0), np.max(weighted, axis=0))
    d_positive = np.linalg.norm(weighted - positive, axis=1)
    d_negative = np.linalg.norm(weighted - negative, axis=1)
    denominator = d_positive + d_negative
    scores = np.full(m, 0.5, dtype=np.float64)
    np.divide(d_negative, denominator, out=scores, where=denominator > 0)
    ranking = np.argsort(-scores, kind="stable").astype(np.int64)
    return TOPSISResult(scores, d_positive, d_negative, ranking)
