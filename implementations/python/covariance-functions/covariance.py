"""Small Euclidean stationary covariance models for teaching and diagnostics."""
from __future__ import annotations

from typing import Literal

import numpy as np
from numpy.typing import ArrayLike, NDArray

Model = Literal["exponential", "gaussian", "matern32", "spherical", "wendland_c2"]


def covariance_from_distance(
    distances: ArrayLike,
    *,
    model: Model = "exponential",
    variance: float = 1.0,
    range_scale: float = 1.0,
) -> NDArray[np.float64]:
    """Evaluate a normalised stationary covariance model at nonnegative distances.

    Distances and range_scale must use the same Euclidean coordinate units.
    The spherical and Wendland C2 forms are restricted here to dimensions <= 3;
    use them only with coordinates in those dimensions.
    """
    h = np.asarray(distances, dtype=np.float64)
    if not np.all(np.isfinite(h)) or np.any(h < 0):
        raise ValueError("distances must be finite and non-negative")
    if not np.isfinite(variance) or variance <= 0:
        raise ValueError("variance must be finite and positive")
    if not np.isfinite(range_scale) or range_scale <= 0:
        raise ValueError("range_scale must be finite and positive")

    r = h / float(range_scale)
    if model == "exponential":
        corr = np.exp(-r)
    elif model == "gaussian":
        corr = np.exp(-(r**2))
    elif model == "matern32":
        q = np.sqrt(3.0) * r
        corr = (1.0 + q) * np.exp(-q)
    elif model == "spherical":
        corr = np.where(r < 1.0, 1.0 - 1.5 * r + 0.5 * r**3, 0.0)
    elif model == "wendland_c2":
        corr = np.where(r < 1.0, (1.0 - r) ** 4 * (1.0 + 4.0 * r), 0.0)
    else:
        raise ValueError(f"unsupported covariance model: {model}")
    return np.asarray(float(variance) * corr, dtype=np.float64)


def covariance_matrix(
    locations: ArrayLike,
    *,
    model: Model = "exponential",
    variance: float = 1.0,
    range_scale: float = 1.0,
) -> NDArray[np.float64]:
    """Build a dense covariance matrix from finite Euclidean coordinates."""
    xy = np.asarray(locations, dtype=np.float64)
    if xy.ndim != 2 or xy.shape[0] == 0 or xy.shape[1] == 0:
        raise ValueError("locations must be a non-empty (n, dimensions) array")
    if not np.all(np.isfinite(xy)):
        raise ValueError("locations must be finite")
    if model in ("spherical", "wendland_c2") and xy.shape[1] > 3:
        raise ValueError(f"{model} is only enabled for Euclidean dimensions <= 3")
    delta = xy[:, None, :] - xy[None, :, :]
    distances = np.sqrt(np.sum(delta * delta, axis=2))
    return covariance_from_distance(
        distances, model=model, variance=variance, range_scale=range_scale
    )


def semivariogram_from_distance(
    distances: ArrayLike,
    *,
    model: Model = "exponential",
    variance: float = 1.0,
    range_scale: float = 1.0,
) -> NDArray[np.float64]:
    """Return gamma(h) = C(0) - C(h) for the selected covariance model."""
    return variance - covariance_from_distance(
        distances, model=model, variance=variance, range_scale=range_scale
    )


def covariance_matrix_diagnostics(matrix: ArrayLike, *, tolerance: float = 1e-10) -> dict[str, float | bool]:
    """Report symmetry and eigenvalue diagnostics; this is not a proof of validity."""
    cov = np.asarray(matrix, dtype=np.float64)
    if cov.ndim != 2 or cov.shape[0] == 0 or cov.shape[0] != cov.shape[1]:
        raise ValueError("matrix must be a non-empty square array")
    if not np.all(np.isfinite(cov)):
        raise ValueError("matrix must be finite")
    if not np.isfinite(tolerance) or tolerance < 0:
        raise ValueError("tolerance must be finite and non-negative")
    symmetric = bool(np.allclose(cov, cov.T, rtol=0.0, atol=tolerance))
    eigenvalues = np.linalg.eigvalsh((cov + cov.T) / 2.0)
    minimum = float(eigenvalues[0])
    maximum = float(eigenvalues[-1])
    return {
        "symmetric": symmetric,
        "minimum_eigenvalue": minimum,
        "maximum_eigenvalue": maximum,
        "positive_semidefinite_within_tolerance": bool(symmetric and minimum >= -tolerance),
    }
