"""Uncorrected Ripley's K and L estimators for planar point patterns."""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, pi
from typing import Sequence

import numpy as np


@dataclass(frozen=True)
class RipleyKResult:
    radii: np.ndarray
    k_values: np.ndarray
    l_values: np.ndarray


def ripley_k(
    points: Sequence[Sequence[float]] | np.ndarray,
    *,
    bounds: Sequence[float],
    radii: Sequence[float] | np.ndarray,
) -> RipleyKResult:
    """Return uncorrected K(r) and L(r) values for each supplied radius."""
    events = np.asarray(points, dtype=float)
    if events.ndim != 2 or events.shape[1] != 2 or events.shape[0] < 2:
        raise ValueError("points must contain at least two coordinate pairs")
    if not np.isfinite(events).all():
        raise ValueError("point coordinates must be finite")
    if len(bounds) != 4:
        raise ValueError("bounds must be (xmin, xmax, ymin, ymax)")
    xmin, xmax, ymin, ymax = map(float, bounds)
    if not all(isfinite(v) for v in (xmin, xmax, ymin, ymax)):
        raise ValueError("bounds must be finite")
    if not (xmin < xmax and ymin < ymax):
        raise ValueError("bounds must have positive width and height")
    if (
        (events[:, 0] < xmin).any()
        or (events[:, 0] > xmax).any()
        or (events[:, 1] < ymin).any()
        or (events[:, 1] > ymax).any()
    ):
        raise ValueError("all point coordinates must lie inside bounds")

    distance_radii = np.asarray(radii, dtype=float)
    if distance_radii.ndim != 1 or distance_radii.size == 0:
        raise ValueError("radii must be a non-empty one-dimensional sequence")
    if not np.isfinite(distance_radii).all() or (distance_radii < 0).any():
        raise ValueError("radii must be finite and non-negative")

    n = events.shape[0]
    delta = events[:, None, :] - events[None, :, :]
    distances = np.sqrt(np.einsum("ijk,ijk->ij", delta, delta))
    pair_distances = np.sort(distances[np.triu_indices(n, k=1)])
    ordered_pair_counts = 2 * np.searchsorted(pair_distances, distance_radii, side="right")
    area = (xmax - xmin) * (ymax - ymin)
    k_values = (area / (n * n)) * ordered_pair_counts
    l_values = np.sqrt(k_values / pi)
    return RipleyKResult(distance_radii.copy(), k_values, l_values)
