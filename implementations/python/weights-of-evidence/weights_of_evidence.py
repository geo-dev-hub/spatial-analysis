"""Binary weights-of-evidence model for aligned 2D spatial arrays."""
from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Mapping

import numpy as np
from numpy.typing import ArrayLike, NDArray


@dataclass(frozen=True)
class EvidenceWeight:
    name: str
    positive: float
    negative: float
    contrast: float
    n_event_present: int
    n_event_absent: int
    n_non_event_present: int
    n_non_event_absent: int


@dataclass(frozen=True)
class WeightsOfEvidenceResult:
    prior_probability: float
    weights: tuple[EvidenceWeight, ...]
    log_odds: NDArray[np.float64]
    probability: NDArray[np.float64]
    valid_mask: NDArray[np.bool_]


def _binary_or_nan(value: ArrayLike, *, name: str) -> NDArray[np.float64]:
    array = np.asarray(value, dtype=np.float64)
    if array.ndim != 2 or 0 in array.shape:
        raise ValueError(f"{name} must be a non-empty 2D array")
    finite = np.isfinite(array)
    if np.any(finite & (array != 0.0) & (array != 1.0)):
        raise ValueError(f"{name} values must be binary (0 or 1) or non-finite NoData")
    return array


def weights_of_evidence(
    event: ArrayLike,
    evidence: Mapping[str, ArrayLike],
    *,
    study_area: ArrayLike | None = None,
    pseudocount: float = 0.5,
) -> WeightsOfEvidenceResult:
    """Estimate binary evidence weights and map posterior event probability.

    Event and evidence arrays contain 0, 1 or non-finite NoData. A cell is
    scored only when all layers are finite and the optional Boolean study
    area mask is True. The default additive pseudocount is 0.5.
    """
    if not isinstance(evidence, Mapping) or not evidence:
        raise ValueError("evidence must be a non-empty mapping")
    names = list(evidence)
    if any(not isinstance(name, str) or not name for name in names):
        raise ValueError("evidence names must be non-empty strings")
    if not np.isfinite(pseudocount) or pseudocount < 0:
        raise ValueError("pseudocount must be finite and non-negative")

    event_array = _binary_or_nan(event, name="event")
    shape = event_array.shape
    layers: list[NDArray[np.float64]] = []
    for name in names:
        layer = _binary_or_nan(evidence[name], name=f"evidence {name!r}")
        if layer.shape != shape:
            raise ValueError("all evidence layers must have the same shape as event")
        layers.append(layer)

    valid = np.isfinite(event_array)
    for layer in layers:
        valid &= np.isfinite(layer)
    if study_area is not None:
        area = np.asarray(study_area)
        if area.dtype != np.bool_:
            raise ValueError("study_area must be a Boolean array")
        if area.shape != shape:
            raise ValueError("study_area must have the same shape as event")
        valid &= area
    if not np.any(valid):
        raise ValueError("no valid cells remain inside the study area")

    event_cells = valid & (event_array == 1.0)
    non_event_cells = valid & (event_array == 0.0)
    n_event = int(np.count_nonzero(event_cells))
    n_non_event = int(np.count_nonzero(non_event_cells))
    if n_event == 0 or n_non_event == 0:
        raise ValueError("study area must contain both event and non-event cells")

    prior = n_event / (n_event + n_non_event)
    prior_log_odds = float(np.log(prior / (1.0 - prior)))
    estimated: list[EvidenceWeight] = []
    combined = np.full(int(np.count_nonzero(valid)), prior_log_odds, dtype=np.float64)

    for name, layer in zip(names, layers):
        present = layer == 1.0
        n11 = int(np.count_nonzero(event_cells & present))
        n10 = int(np.count_nonzero(event_cells & ~present))
        n01 = int(np.count_nonzero(non_event_cells & present))
        n00 = int(np.count_nonzero(non_event_cells & ~present))

        denominator_event = n_event + 2.0 * pseudocount
        denominator_non_event = n_non_event + 2.0 * pseudocount
        p_present_event = (n11 + pseudocount) / denominator_event
        p_present_non_event = (n01 + pseudocount) / denominator_non_event
        p_absent_event = (n10 + pseudocount) / denominator_event
        p_absent_non_event = (n00 + pseudocount) / denominator_non_event

        probabilities = (
            p_present_event, p_present_non_event,
            p_absent_event, p_absent_non_event,
        )
        if any(p <= 0.0 or p >= 1.0 for p in probabilities):
            raise ValueError(
                f"evidence {name!r} has a zero contingency count; "
                "use a positive pseudocount or review the evidence layer"
            )

        positive = float(np.log(p_present_event / p_present_non_event))
        negative = float(np.log(p_absent_event / p_absent_non_event))
        estimated.append(EvidenceWeight(
            name=name,
            positive=positive,
            negative=negative,
            contrast=positive - negative,
            n_event_present=n11,
            n_event_absent=n10,
            n_non_event_present=n01,
            n_non_event_absent=n00,
        ))
        combined += np.where(layer[valid] == 1.0, positive, negative)

    log_odds = np.full(shape, np.nan, dtype=np.float64)
    log_odds[valid] = combined
    probabilities = 1.0 / (1.0 + np.exp(-np.clip(combined, -700.0, 700.0)))
    probability = np.full(shape, np.nan, dtype=np.float64)
    probability[valid] = probabilities

    return WeightsOfEvidenceResult(
        prior_probability=prior,
        weights=tuple(estimated),
        log_odds=log_odds,
        probability=probability,
        valid_mask=valid,
    )
