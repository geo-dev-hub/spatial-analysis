"""Fixed-bandwidth planar Gaussian kernel density estimation."""
from __future__ import annotations

from math import isfinite, pi
from typing import Sequence

import numpy as np


def gaussian_kde(
    points: Sequence[Sequence[float]] | np.ndarray,
    *,
    bounds: Sequence[float],
    grid_shape: Sequence[int] = (100, 100),
    bandwidth: float,
    weights: Sequence[float] | np.ndarray | None = None,
    chunk_size: int = 2048,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return (intensity grid, x cell centres, y cell centres).

    Density is evaluated as sum_i w_i K_h(x - x_i), where K_h is the
    isotropic 2D Gaussian kernel. No edge correction is applied.
    """
    events = np.asarray(points, dtype=float)
    if events.ndim != 2 or events.shape[1] != 2 or events.shape[0] == 0:
        raise ValueError("points must be a non-empty array with shape (n, 2)")
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

    if len(grid_shape) != 2:
        raise ValueError("grid_shape must be (rows, columns)")
    rows, cols = grid_shape
    for value in (rows, cols):
        if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)) or value <= 0:
            raise ValueError("grid_shape values must be positive integers")
    if not isfinite(bandwidth) or bandwidth <= 0:
        raise ValueError("bandwidth must be finite and greater than zero")
    if isinstance(chunk_size, (bool, np.bool_)) or not isinstance(chunk_size, (int, np.integer)) or chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")

    if weights is None:
        event_weights = np.ones(events.shape[0], dtype=float)
    else:
        event_weights = np.asarray(weights, dtype=float)
        if event_weights.shape != (events.shape[0],):
            raise ValueError("weights must contain one value per point")
        if not np.isfinite(event_weights).all() or (event_weights < 0).any():
            raise ValueError("weights must be finite and non-negative")

    x_centres = xmin + (np.arange(cols) + 0.5) * ((xmax - xmin) / cols)
    y_centres = ymin + (np.arange(rows) + 0.5) * ((ymax - ymin) / rows)
    xx, yy = np.meshgrid(x_centres, y_centres)
    grid = np.column_stack((xx.ravel(), yy.ravel()))
    density = np.empty(grid.shape[0], dtype=float)
    normaliser = 1.0 / (2.0 * pi * bandwidth * bandwidth)
    denominator = 2.0 * bandwidth * bandwidth

    for start in range(0, grid.shape[0], int(chunk_size)):
        stop = min(start + int(chunk_size), grid.shape[0])
        delta = grid[start:stop, None, :] - events[None, :, :]
        squared_distance = np.einsum("ijk,ijk->ij", delta, delta)
        kernel = np.exp(-squared_distance / denominator)
        density[start:stop] = normaliser * (kernel @ event_weights)

    return density.reshape(rows, cols), x_centres, y_centres
