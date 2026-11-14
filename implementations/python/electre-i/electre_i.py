"""Crisp concordance/discordance outranking relation (ELECTRE I-style)."""
from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Sequence

import numpy as np
from numpy.typing import ArrayLike, NDArray


@dataclass(frozen=True)
class ElectreIRelation:
    alternative_names: tuple[str, ...]
    normalised_weights: NDArray[np.float64]
    concordance: NDArray[np.float64]
    discordance: NDArray[np.float64]
    outranks: NDArray[np.bool_]


def electre_i_relation(
    performance: ArrayLike,
    weights: ArrayLike,
    directions: Sequence[str],
    *,
    concordance_threshold: float = 0.6,
    discordance_threshold: float = 0.4,
    alternative_names: Sequence[str] | None = None,
) -> ElectreIRelation:
    """Build a crisp pairwise outranking relation.

    Rows are alternatives and columns are criteria. Directions are "benefit"
    (larger is better) or "cost" (smaller is better). Concordance is the sum
    of normalised criterion weights for which a is at least as good as b.
    Discordance is the maximum disadvantage of a relative to b, divided by
    the observed range of that criterion across all alternatives.

    This constructs the outranking relation only. It does not extract an
    ELECTRE I kernel, rank alternatives, elicit thresholds or validate the
    decision model.
    """
    values = np.asarray(performance, dtype=np.float64)
    if values.ndim != 2 or values.shape[0] < 2 or values.shape[1] < 1:
        raise ValueError("performance must be a 2D array with at least two alternatives and one criterion")
    if not np.all(np.isfinite(values)):
        raise ValueError("performance values must be finite")

    raw_weights = np.asarray(weights, dtype=np.float64)
    if raw_weights.ndim != 1 or raw_weights.size != values.shape[1]:
        raise ValueError("weights must be a 1D array with one value per criterion")
    if not np.all(np.isfinite(raw_weights)) or np.any(raw_weights < 0):
        raise ValueError("weights must be finite and non-negative")
    total = float(raw_weights.sum())
    if total <= 0:
        raise ValueError("at least one criterion weight must be positive")
    normalised = raw_weights / total

    if len(directions) != values.shape[1] or any(
        direction not in {"benefit", "cost"} for direction in directions
    ):
        raise ValueError("directions must contain one 'benefit' or 'cost' value per criterion")
    if not np.isfinite(concordance_threshold) or not 0 <= concordance_threshold <= 1:
        raise ValueError("concordance_threshold must lie in [0, 1]")
    if not np.isfinite(discordance_threshold) or not 0 <= discordance_threshold <= 1:
        raise ValueError("discordance_threshold must lie in [0, 1]")

    n_alternatives, n_criteria = values.shape
    if alternative_names is None:
        names = tuple(f"A{i + 1}" for i in range(n_alternatives))
    else:
        names = tuple(alternative_names)
        if len(names) != n_alternatives or any(not isinstance(name, str) or not name for name in names):
            raise ValueError("alternative_names must contain one non-empty string per alternative")
        if len(set(names)) != len(names):
            raise ValueError("alternative_names must be unique")

    oriented = values.copy()
    for j, direction in enumerate(directions):
        if direction == "cost":
            oriented[:, j] *= -1.0
    ranges = np.ptp(oriented, axis=0)

    concordance = np.zeros((n_alternatives, n_alternatives), dtype=np.float64)
    discordance = np.zeros_like(concordance)
    for a in range(n_alternatives):
        for b in range(n_alternatives):
            if a == b:
                concordance[a, b] = 1.0
                continue
            at_least_as_good = oriented[a] >= oriented[b]
            concordance[a, b] = float(normalised[at_least_as_good].sum())

            disadvantages = np.zeros(n_criteria, dtype=np.float64)
            worse = oriented[a] < oriented[b]
            scalable = worse & (ranges > 0)
            disadvantages[scalable] = (
                oriented[b, scalable] - oriented[a, scalable]
            ) / ranges[scalable]
            discordance[a, b] = float(disadvantages.max(initial=0.0))

    outranks = (
        (concordance >= concordance_threshold)
        & (discordance <= discordance_threshold)
    )
    np.fill_diagonal(outranks, True)

    return ElectreIRelation(
        alternative_names=names,
        normalised_weights=normalised,
        concordance=concordance,
        discordance=discordance,
        outranks=outranks,
    )
