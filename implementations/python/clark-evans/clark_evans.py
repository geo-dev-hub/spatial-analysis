"""Clark–Evans nearest-neighbour index for planar point patterns."""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, sqrt
from typing import Sequence

import numpy as np


@dataclass(frozen=True)
class ClarkEvansResult:
    observed_mean_distance: float
    expected_mean_distance: float
    ratio: float
    nearest_neighbour_distances: np.ndarray


def clark_evans_index(
    points: Sequence[Sequence[float]] | np.ndarray,
    *,
    bounds: Sequence[float],
    chunk_size: int = 512,
) -> ClarkEvansResult:
    """Calculate the descriptive Clark–Evans R index.

    Expected mean nearest-neighbour distance is 1/(2*sqrt(lambda)) under
    homogeneous Poisson CSR on the infinite plane, with lambda=n/window area.
    No edge correction or significance test is performed.
    """
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
    if isinstance(chunk_size, (bool, np.bool_)) or not isinstance(chunk_size, (int, np.integer)) or chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")

    n = events.shape[0]
    nearest = np.empty(n, dtype=float)
    for start in range(0, n, int(chunk_size)):
        stop = min(start + int(chunk_size), n)
        delta = events[start:stop, None, :] - events[None, :, :]
        squared = np.einsum("ijk,ijk->ij", delta, delta)
        row_indices = np.arange(start, stop)
        squared[np.arange(stop - start), row_indices] = np.inf
        nearest[start:stop] = np.sqrt(np.min(squared, axis=1))

    observed = float(np.mean(nearest))
    area = (xmax - xmin) * (ymax - ymin)
    intensity = n / area
    expected = 1.0 / (2.0 * sqrt(intensity))
    ratio = observed / expected
    return ClarkEvansResult(observed, expected, ratio, nearest)
