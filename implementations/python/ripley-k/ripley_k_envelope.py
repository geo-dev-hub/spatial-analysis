"""Conditional-CSR Monte Carlo inference for Ripley's L(r).

The global statistic is a studentised maximum absolute deviation over the
preselected radius vector. Pointwise quantile envelopes are also returned,
but they are not simultaneous global envelopes.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Sequence

import numpy as np
from numpy.typing import NDArray

from ripley_k import RipleyKResult, ripley_k


@dataclass(frozen=True)
class RipleyEnvelopeResult:
    observed: RipleyKResult
    simulated_l_values: NDArray[np.float64]
    pointwise_lower_l: NDArray[np.float64]
    pointwise_upper_l: NDArray[np.float64]
    global_statistic: float
    simulated_global_statistics: NDArray[np.float64]
    global_p_value: float
    alpha: float


def ripley_k_csr_envelope(
    points: Sequence[Sequence[float]] | np.ndarray,
    *,
    bounds: Sequence[float],
    radii: Sequence[float] | np.ndarray,
    n_simulations: int = 199,
    alpha: float = 0.05,
    seed: int | None = 0,
) -> RipleyEnvelopeResult:
    """Compare an observed pattern with conditional homogeneous CSR.

    The null model fixes the observed event count and study window, then
    places that many independent uniform points in the rectangular window.
    Every curve uses translation-corrected Ripley's K/L.

    The reported p-value uses a studentised maximum absolute deviation
    across the supplied radii. The observed and simulated curves are
    standardised symmetrically using their joint mean and standard
    deviation, preserving exchangeability for the Monte Carlo rank test.

    Pointwise quantile bands are included for visual inspection only.
    They do not control the probability of an excursion anywhere across
    the full radius interval.
    """
    if not isinstance(n_simulations, int) or n_simulations < 1:
        raise ValueError("n_simulations must be a positive integer")
    if not isfinite(alpha) or not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between zero and one")
    if len(bounds) != 4:
        raise ValueError("bounds must be (xmin, xmax, ymin, ymax)")
    xmin, xmax, ymin, ymax = map(float, bounds)
    if not all(isfinite(v) for v in (xmin, xmax, ymin, ymax)):
        raise ValueError("bounds must be finite")
    if not (xmin < xmax and ymin < ymax):
        raise ValueError("bounds must have positive width and height")

    observed = ripley_k(
        points, bounds=bounds, radii=radii, edge_correction="translation"
    )
    n = len(np.asarray(points))
    rng = np.random.default_rng(seed)
    simulations = np.empty((n_simulations, observed.radii.size), dtype=np.float64)

    for index in range(n_simulations):
        simulated_points = np.column_stack((
            rng.uniform(xmin, xmax, size=n),
            rng.uniform(ymin, ymax, size=n),
        ))
        simulations[index] = ripley_k(
            simulated_points,
            bounds=bounds,
            radii=observed.radii,
            edge_correction="translation",
        ).l_values

    pointwise_lower, pointwise_upper = np.quantile(
        simulations, [alpha / 2.0, 1.0 - alpha / 2.0], axis=0
    )

    # Include the observed curve and all simulations in the centring and
    # scaling step so every curve is treated symmetrically under the null.
    all_curves = np.vstack((observed.l_values, simulations))
    centre = all_curves.mean(axis=0)
    scale = all_curves.std(axis=0, ddof=1)
    active = scale > np.finfo(np.float64).eps
    if not np.any(active):
        raise ValueError("the selected radii contain no variable simulated L values")

    standardized = np.abs(all_curves[:, active] - centre[active]) / scale[active]
    statistics = standardized.max(axis=1)
    observed_statistic = float(statistics[0])
    simulated_statistics = statistics[1:]
    p_value = float(
        (1 + np.count_nonzero(simulated_statistics >= observed_statistic))
        / (n_simulations + 1)
    )

    return RipleyEnvelopeResult(
        observed=observed,
        simulated_l_values=simulations,
        pointwise_lower_l=pointwise_lower,
        pointwise_upper_l=pointwise_upper,
        global_statistic=observed_statistic,
        simulated_global_statistics=simulated_statistics,
        global_p_value=p_value,
        alpha=float(alpha),
    )
