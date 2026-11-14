"""A deterministic, quadratic DBSCAN teaching implementation."""
from __future__ import annotations

from math import isfinite
from typing import Sequence

import numpy as np


def dbscan(
    points: Sequence[Sequence[float]] | np.ndarray,
    *,
    eps: float,
    min_samples: int,
) -> list[int]:
    """Return cluster IDs, using -1 for noise.

    min_samples counts the point itself. Border-point ties are resolved by
    the first cluster expanded, which makes this implementation deterministic
    but can make labels depend on input ordering in ambiguous cases.
    """
    coordinates = np.asarray(points, dtype=float)
    if coordinates.ndim != 2 or coordinates.shape[1] != 2 or coordinates.shape[0] == 0:
        raise ValueError("points must be a non-empty array of 2D coordinates")
    if not np.isfinite(coordinates).all():
        raise ValueError("point coordinates must be finite")
    if not isfinite(eps) or eps <= 0:
        raise ValueError("eps must be finite and greater than zero")
    if not isinstance(min_samples, int) or isinstance(min_samples, bool) or min_samples < 1:
        raise ValueError("min_samples must be a positive integer")

    differences = coordinates[:, None, :] - coordinates[None, :, :]
    distances = np.sqrt(np.sum(differences * differences, axis=2))
    neighbours = [np.flatnonzero(row <= eps).tolist() for row in distances]

    unvisited = None
    noise = -1
    labels: list[int | None] = [unvisited] * len(coordinates)
    cluster_id = 0

    for point_index in range(len(coordinates)):
        if labels[point_index] is not unvisited:
            continue
        if len(neighbours[point_index]) < min_samples:
            labels[point_index] = noise
            continue

        labels[point_index] = cluster_id
        queue = list(neighbours[point_index])
        queued = set(queue)
        cursor = 0
        while cursor < len(queue):
            candidate = queue[cursor]
            cursor += 1
            if labels[candidate] == noise:
                labels[candidate] = cluster_id
            if labels[candidate] is not unvisited:
                continue
            labels[candidate] = cluster_id
            if len(neighbours[candidate]) >= min_samples:
                for neighbour in neighbours[candidate]:
                    if neighbour not in queued:
                        queue.append(neighbour)
                        queued.add(neighbour)
        cluster_id += 1

    return [noise if label is None else label for label in labels]
