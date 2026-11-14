"""Transparent forecast verification metrics for binary events.

All observations and deterministic forecasts are encoded as 0/1.
Undefined scores return None rather than silently dividing by zero.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Iterable, Sequence


@dataclass(frozen=True)
class ContingencyTable:
    hits: int
    misses: int
    false_alarms: int
    correct_negatives: int

    @property
    def total(self) -> int:
        return self.hits + self.misses + self.false_alarms + self.correct_negatives


def _binary(values: Iterable[int], name: str) -> list[int]:
    result = []
    for value in values:
        if isinstance(value, bool):
            result.append(int(value))
        elif isinstance(value, int) and value in (0, 1):
            result.append(value)
        else:
            raise ValueError(f"{name} values must be boolean or integer 0/1")
    if not result:
        raise ValueError(f"{name} must not be empty")
    return result


def contingency_table(observed: Iterable[int], forecast: Iterable[int]) -> ContingencyTable:
    """Build H/M/F/C counts from paired binary observations and forecasts."""
    obs = _binary(observed, "observed")
    fcst = _binary(forecast, "forecast")
    if len(obs) != len(fcst):
        raise ValueError("observed and forecast must have equal length")
    h = m = f = c = 0
    for o, p in zip(obs, fcst):
        if p == 1 and o == 1: h += 1
        elif p == 0 and o == 1: m += 1
        elif p == 1 and o == 0: f += 1
        else: c += 1
    return ContingencyTable(h, m, f, c)


def categorical_scores(table: ContingencyTable) -> dict[str, float | None]:
    """Return POD, FAR, false-positive rate, CSI and ETS.

    None denotes a mathematically undefined ratio for the supplied sample.
    """
    h, m, f, c = table.hits, table.misses, table.false_alarms, table.correct_negatives
    if any(not isinstance(v, int) or isinstance(v, bool) or v < 0 for v in (h, m, f, c)):
        raise ValueError("contingency counts must be non-negative integers")
    if table.total == 0:
        raise ValueError("contingency table must contain at least one case")
    def ratio(num: float, den: float) -> float | None:
        return num / den if den != 0 else None
    random_hits = ((h + m) * (h + f)) / table.total
    return {
        "pod": ratio(h, h + m),
        "far": ratio(f, h + f),
        "false_positive_rate": ratio(f, f + c),
        "csi": ratio(h, h + m + f),
        "ets": ratio(h - random_hits, h + m + f - random_hits),
    }


def _probabilities(values: Iterable[float], name: str = "probabilities") -> list[float]:
    result = []
    for value in values:
        p = float(value)
        if not isfinite(p) or p < 0.0 or p > 1.0:
            raise ValueError(f"{name} must be finite and within [0, 1]")
        result.append(p)
    if not result:
        raise ValueError(f"{name} must not be empty")
    return result


def brier_score(observed: Iterable[int], probabilities: Iterable[float]) -> float:
    """Mean squared probability error for binary events; lower is better."""
    obs = _binary(observed, "observed")
    probs = _probabilities(probabilities)
    if len(obs) != len(probs):
        raise ValueError("observed and probabilities must have equal length")
    return sum((p - o) ** 2 for o, p in zip(obs, probs)) / len(obs)


def brier_skill_score(observed: Iterable[int], probabilities: Iterable[float],
                      reference_probabilities: Iterable[float]) -> float | None:
    """Brier skill relative to a supplied reference forecast.

    Returns None when the reference Brier score is zero; positive values
    indicate improvement over the reference.
    """
    obs = _binary(observed, "observed")
    probs = _probabilities(probabilities)
    ref = _probabilities(reference_probabilities, "reference probabilities")
    if len(obs) != len(probs) or len(obs) != len(ref):
        raise ValueError("observed, forecast and reference lengths must match")
    ref_score = sum((p - o) ** 2 for o, p in zip(obs, ref)) / len(obs)
    if ref_score == 0:
        return None
    score = sum((p - o) ** 2 for o, p in zip(obs, probs)) / len(obs)
    return 1.0 - score / ref_score


def reliability_bins(observed: Iterable[int], probabilities: Iterable[float],
                     edges: Sequence[float]) -> list[dict[str, float | int | None]]:
    """Summarise reliability in caller-defined bins [left, right), last closed.

    Empty bins are retained with count=0 and None means, making plots honest
    about unsupported probability ranges. Edges must strictly increase from
    exactly 0 to exactly 1.
    """
    obs = _binary(observed, "observed")
    probs = _probabilities(probabilities)
    if len(obs) != len(probs):
        raise ValueError("observed and probabilities must have equal length")
    bounds = [float(x) for x in edges]
    if len(bounds) < 2 or bounds[0] != 0.0 or bounds[-1] != 1.0:
        raise ValueError("edges must start at 0 and end at 1")
    if any(not isfinite(x) for x in bounds) or any(a >= b for a, b in zip(bounds, bounds[1:])):
        raise ValueError("edges must be finite and strictly increasing")
    result = []
    for i, (left, right) in enumerate(zip(bounds, bounds[1:])):
        pairs = [(o, p) for o, p in zip(obs, probs)
                 if left <= p and (p < right or (i == len(bounds)-2 and p <= right))]
        n = len(pairs)
        result.append({
            "lower": left, "upper": right, "count": n,
            "mean_probability": sum(p for _, p in pairs) / n if n else None,
            "observed_frequency": sum(o for o, _ in pairs) / n if n else None,
        })
    return result


def roc_auc(observed: Iterable[int], scores: Iterable[float]) -> float | None:
    """Area under the empirical ROC curve using average ranks for ties.

    Scores need not be calibrated probabilities. Returns None when either
    class is absent. The Mann–Whitney/rank formulation handles ties exactly.
    """
    obs = _binary(observed, "observed")
    values = [float(x) for x in scores]
    if len(obs) != len(values):
        raise ValueError("observed and scores must have equal length")
    if not values or any(not isfinite(x) for x in values):
        raise ValueError("scores must be non-empty and finite")
    positives = sum(obs)
    negatives = len(obs) - positives
    if positives == 0 or negatives == 0:
        return None
    order = sorted(range(len(values)), key=lambda i: values[i])
    rank_sum = 0.0
    i = 0
    while i < len(order):
        j = i + 1
        while j < len(order) and values[order[j]] == values[order[i]]:
            j += 1
        average_rank = ((i + 1) + j) / 2.0
        rank_sum += average_rank * sum(obs[order[k]] for k in range(i, j))
        i = j
    return (rank_sum - positives * (positives + 1) / 2) / (positives * negatives)
