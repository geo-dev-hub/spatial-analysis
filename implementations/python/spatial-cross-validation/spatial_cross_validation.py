"""Transparent grid-block and buffered spatial cross-validation for point data."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray


@dataclass(frozen=True)
class SpatialFold:
    """Indices for one fold; excluded points are neither train nor test."""
    train_indices: NDArray[np.int64]
    test_indices: NDArray[np.int64]
    excluded_indices: NDArray[np.int64]


def grid_block_ids(
    coordinates: ArrayLike,
    block_size: float | tuple[float, float],
    origin: tuple[float, float] = (0.0, 0.0),
) -> NDArray[np.int64]:
    """Assign points to unique grid blocks using projected planar coordinates."""
    xy = np.asarray(coordinates, dtype=np.float64)
    if xy.ndim != 2 or xy.shape[1] != 2 or xy.shape[0] == 0:
        raise ValueError("coordinates must be a non-empty (n, 2) array")
    if not np.all(np.isfinite(xy)):
        raise ValueError("coordinates must be finite")
    if np.isscalar(block_size):
        width = height = float(block_size)
    else:
        if len(block_size) != 2:
            raise ValueError("block_size tuple must contain width and height")
        width, height = map(float, block_size)
    if not np.isfinite(width) or not np.isfinite(height) or width <= 0 or height <= 0:
        raise ValueError("block dimensions must be finite and positive")
    ox, oy = map(float, origin)
    if not np.isfinite(ox) or not np.isfinite(oy):
        raise ValueError("origin must be finite")
    grid = np.column_stack((
        np.floor((xy[:, 0] - ox) / width).astype(np.int64),
        np.floor((xy[:, 1] - oy) / height).astype(np.int64),
    ))
    _, inverse = np.unique(grid, axis=0, return_inverse=True)
    return inverse.astype(np.int64)


def spatial_block_folds(
    coordinates: ArrayLike,
    n_splits: int,
    block_size: float | tuple[float, float],
    *,
    origin: tuple[float, float] = (0.0, 0.0),
    buffer_distance: float = 0.0,
    seed: int = 0,
) -> list[SpatialFold]:
    """Create deterministic group folds, optionally buffering training points.

    Whole grid blocks are assigned to folds. The buffer removes candidate
    training observations whose Euclidean distance to any test point is
    strictly less than buffer_distance. Coordinates must use a suitable
    projected planar CRS whose units match block_size and buffer_distance.

    The direct buffer search is O(n_train * n_test) per fold and is intended
    for small teaching datasets, not large-scale production splitting.
    """
    xy = np.asarray(coordinates, dtype=np.float64)
    block_ids = grid_block_ids(xy, block_size, origin)
    if not isinstance(n_splits, (int, np.integer)) or n_splits < 2:
        raise ValueError("n_splits must be an integer of at least 2")
    unique_blocks = np.unique(block_ids)
    if n_splits > unique_blocks.size:
        raise ValueError("n_splits cannot exceed the number of occupied blocks")
    if not np.isfinite(buffer_distance) or buffer_distance < 0:
        raise ValueError("buffer_distance must be finite and non-negative")
    if not isinstance(seed, (int, np.integer)):
        raise ValueError("seed must be an integer")

    rng = np.random.default_rng(int(seed))
    shuffled = rng.permutation(unique_blocks)
    held_out_groups = np.array_split(shuffled, n_splits)
    all_indices = np.arange(xy.shape[0], dtype=np.int64)
    folds: list[SpatialFold] = []

    for groups in held_out_groups:
        test_mask = np.isin(block_ids, groups)
        test = all_indices[test_mask]
        candidate_train = all_indices[~test_mask]
        if test.size == 0 or candidate_train.size == 0:
            raise ValueError("each fold must have non-empty train and test sets")

        if buffer_distance > 0:
            keep = np.ones(candidate_train.size, dtype=bool)
            chunk_size = max(1, min(2048, 2_000_000 // max(test.size, 1)))
            for start in range(0, candidate_train.size, chunk_size):
                stop = min(start + chunk_size, candidate_train.size)
                delta = xy[candidate_train[start:stop], None, :] - xy[None, test, :]
                nearest = np.sqrt(np.min(np.sum(delta * delta, axis=2), axis=1))
                keep[start:stop] = nearest >= buffer_distance
            train = candidate_train[keep]
            excluded = candidate_train[~keep]
        else:
            train = candidate_train
            excluded = np.empty(0, dtype=np.int64)

        if train.size == 0:
            raise ValueError(
                "buffer removed every training observation in a fold; reduce buffer or redesign blocks"
            )
        folds.append(SpatialFold(train, test, excluded))

    return folds
