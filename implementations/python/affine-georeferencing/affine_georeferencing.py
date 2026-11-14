"""Least-squares 2D affine fitting from source/target control points."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray


@dataclass(frozen=True)
class AffineFit:
    coefficients: NDArray[np.float64]
    residual_vectors: NDArray[np.float64]
    rmse: float
    rank: int


def fit_affine(
    source_points: ArrayLike,
    target_points: ArrayLike,
) -> AffineFit:
    """Fit x'=a0+a1*x+a2*y, y'=b0+b1*x+b2*y by least squares."""
    source = np.asarray(source_points, dtype=np.float64)
    target = np.asarray(target_points, dtype=np.float64)
    if source.ndim != 2 or source.shape[1] != 2 or source.shape[0] < 3:
        raise ValueError("source_points must have shape (n, 2), n >= 3")
    if target.shape != source.shape:
        raise ValueError("target_points must have the same shape as source_points")
    if not np.all(np.isfinite(source)) or not np.all(np.isfinite(target)):
        raise ValueError("control point coordinates must be finite")

    design = np.column_stack((np.ones(source.shape[0]), source))
    coefficients, _, rank, _ = np.linalg.lstsq(design, target, rcond=None)
    if rank < 3:
        raise ValueError("source control points are collinear or ill-conditioned")
    predicted = design @ coefficients
    residuals = target - predicted
    rmse = float(np.sqrt(np.mean(np.sum(residuals * residuals, axis=1))))
    return AffineFit(coefficients, residuals, rmse, int(rank))


def apply_affine(points: ArrayLike, coefficients: ArrayLike) -> NDArray[np.float64]:
    """Apply 3x2 affine coefficients to an (n, 2) array."""
    xy = np.asarray(points, dtype=np.float64)
    coeff = np.asarray(coefficients, dtype=np.float64)
    if xy.ndim != 2 or xy.shape[1] != 2 or xy.shape[0] == 0:
        raise ValueError("points must be a non-empty (n, 2) array")
    if coeff.shape != (3, 2) or not np.all(np.isfinite(coeff)):
        raise ValueError("coefficients must be a finite (3, 2) array")
    if not np.all(np.isfinite(xy)):
        raise ValueError("points must be finite")
    design = np.column_stack((np.ones(xy.shape[0]), xy))
    return design @ coeff
