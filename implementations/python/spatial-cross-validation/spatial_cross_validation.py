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


def buffered_leave_one_out_folds(coordinates: ArrayLike, buffer_distance: float = 0.0) -> list[SpatialFold]:
    """One-observation test folds with nearby candidate training points excluded."""
    xy = np.asarray(coordinates, dtype=np.float64)
    if xy.ndim != 2 or xy.shape[1] != 2 or xy.shape[0] < 2:
        raise ValueError("coordinates must be an (n, 2) array with n >= 2")
    if not np.all(np.isfinite(xy)):
        raise ValueError("coordinates must be finite")
    if not np.isfinite(buffer_distance) or buffer_distance < 0:
        raise ValueError("buffer_distance must be finite and non-negative")
    all_indices = np.arange(xy.shape[0], dtype=np.int64)
    folds = []
    for test_index in all_indices:
        test = np.array([test_index], dtype=np.int64)
        candidates = all_indices[all_indices != test_index]
        distances = np.linalg.norm(xy[candidates] - xy[test_index], axis=1)
        keep = distances >= buffer_distance
        train, excluded = candidates[keep], candidates[~keep]
        if train.size == 0:
            raise ValueError("buffer removed every training observation for a leave-one-out fold")
        folds.append(SpatialFold(train, test, excluded))
    return folds


def spatial_kfold_by_clustering(coordinates: ArrayLike, n_splits: int, *, max_iter: int = 100) -> list[SpatialFold]:
    """Deterministic farthest-first k-means on coordinates; each cluster is a test fold."""
    xy = np.asarray(coordinates, dtype=np.float64)
    if xy.ndim != 2 or xy.shape[1] != 2 or xy.shape[0] < 2:
        raise ValueError("coordinates must be an (n, 2) array with n >= 2")
    if not np.all(np.isfinite(xy)):
        raise ValueError("coordinates must be finite")
    if not isinstance(n_splits, (int, np.integer)) or isinstance(n_splits, bool) or not 2 <= n_splits <= len(xy):
        raise ValueError("n_splits must be an integer between 2 and n")
    if not isinstance(max_iter, int) or isinstance(max_iter, bool) or max_iter < 1:
        raise ValueError("max_iter must be a positive integer")
    if np.unique(xy, axis=0).shape[0] < n_splits:
        raise ValueError("need at least n_splits distinct coordinate locations")
    n = len(xy)
    first = min(range(n), key=lambda i: (xy[i, 0], xy[i, 1], i))
    centres = [xy[first].copy()]
    min_dist2 = np.sum((xy - centres[0]) ** 2, axis=1)
    for _ in range(1, n_splits):
        chosen = int(np.argmax(min_dist2))
        centres.append(xy[chosen].copy())
        min_dist2 = np.minimum(min_dist2, np.sum((xy - centres[-1]) ** 2, axis=1))
    centres = np.asarray(centres)
    labels = np.full(n, -1, dtype=np.int64)
    for _ in range(max_iter):
        distances = np.sum((xy[:, None, :] - centres[None, :, :]) ** 2, axis=2)
        new_labels = np.argmin(distances, axis=1)
        counts = np.bincount(new_labels, minlength=n_splits)
        for empty in np.flatnonzero(counts == 0):
            eligible = np.flatnonzero(counts[new_labels] > 1)
            if eligible.size == 0:
                raise RuntimeError("could not repair an empty spatial cluster")
            point = int(eligible[np.argmax(distances[eligible, new_labels[eligible]])])
            counts[new_labels[point]] -= 1
            new_labels[point] = int(empty)
            counts[empty] += 1
        new_centres = np.vstack([xy[new_labels == k].mean(axis=0) for k in range(n_splits)])
        converged = np.array_equal(new_labels, labels)
        labels, centres = new_labels, new_centres
        if converged:
            break
    all_indices = np.arange(n, dtype=np.int64)
    folds = []
    for cluster in range(n_splits):
        test = all_indices[labels == cluster]
        train = all_indices[labels != cluster]
        if test.size == 0 or train.size == 0:
            raise RuntimeError("clustering produced an empty fold")
        folds.append(SpatialFold(train, test, np.empty(0, dtype=np.int64)))
    return folds
