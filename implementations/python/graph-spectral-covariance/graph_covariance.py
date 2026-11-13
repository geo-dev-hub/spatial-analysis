"""Positive-semidefinite covariance constructions from undirected graph spectra."""
from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray


def graph_laplacian(adjacency: ArrayLike) -> NDArray[np.float64]:
    """Return the combinatorial Laplacian D - A for a weighted undirected graph."""
    a = np.asarray(adjacency, dtype=np.float64)
    if a.ndim != 2 or a.shape[0] == 0 or a.shape[0] != a.shape[1]:
        raise ValueError("adjacency must be a non-empty square matrix")
    if not np.all(np.isfinite(a)):
        raise ValueError("adjacency must be finite")
    if np.any(a < 0):
        raise ValueError("edge weights must be non-negative")
    if not np.allclose(a, a.T, rtol=0.0, atol=1e-12):
        raise ValueError("adjacency must be symmetric for an undirected graph")
    if not np.allclose(np.diag(a), 0.0, rtol=0.0, atol=1e-12):
        raise ValueError("self-loops are not supported in this teaching implementation")
    degree = np.sum(a, axis=1)
    return np.diag(degree) - a


def graph_spectral_covariance(
    adjacency: ArrayLike, spectral_variances: ArrayLike
) -> NDArray[np.float64]:
    """Construct K = Q diag(gamma) Q.T with non-negative graph spectral variances.

    Eigenvectors are ordered by ascending combinatorial-Laplacian eigenvalue.
    The result is positive semidefinite by construction. It is generally not
    stationary or isotropic over graph vertices, and diagonal variances may differ.
    """
    laplacian = graph_laplacian(adjacency)
    gamma = np.asarray(spectral_variances, dtype=np.float64)
    n = laplacian.shape[0]
    if gamma.ndim != 1 or gamma.size != n:
        raise ValueError("spectral_variances must have one value per graph vertex mode")
    if not np.all(np.isfinite(gamma)) or np.any(gamma < 0):
        raise ValueError("spectral variances must be finite and non-negative")
    eigenvalues, eigenvectors = np.linalg.eigh(laplacian)
    # Clip tiny negative round-off in theoretically non-negative Laplacian eigenvalues.
    eigenvalues = np.maximum(eigenvalues, 0.0)
    covariance = (eigenvectors * gamma) @ eigenvectors.T
    return np.asarray((covariance + covariance.T) / 2.0, dtype=np.float64)


def graph_heat_covariance(
    adjacency: ArrayLike, *, diffusion_time: float, variance_scale: float = 1.0
) -> NDArray[np.float64]:
    """Use exp(-t lambda) spectral variances to obtain a graph heat covariance."""
    if not np.isfinite(diffusion_time) or diffusion_time < 0:
        raise ValueError("diffusion_time must be finite and non-negative")
    if not np.isfinite(variance_scale) or variance_scale <= 0:
        raise ValueError("variance_scale must be finite and positive")
    laplacian = graph_laplacian(adjacency)
    eigenvalues = np.linalg.eigvalsh(laplacian)
    eigenvalues = np.maximum(eigenvalues, 0.0)
    gamma = float(variance_scale) * np.exp(-float(diffusion_time) * eigenvalues)
    return graph_spectral_covariance(adjacency, gamma)


def covariance_diagnostics(
    matrix: ArrayLike, *, tolerance: float = 1e-10
) -> dict[str, float | bool]:
    """Inspect one finite covariance matrix; numerical checks do not prove model validity."""
    cov = np.asarray(matrix, dtype=np.float64)
    if cov.ndim != 2 or cov.shape[0] == 0 or cov.shape[0] != cov.shape[1]:
        raise ValueError("matrix must be a non-empty square array")
    if not np.all(np.isfinite(cov)):
        raise ValueError("matrix must be finite")
    if not np.isfinite(tolerance) or tolerance < 0:
        raise ValueError("tolerance must be finite and non-negative")
    symmetric = bool(np.allclose(cov, cov.T, rtol=0.0, atol=tolerance))
    eigenvalues = np.linalg.eigvalsh((cov + cov.T) / 2.0)
    minimum, maximum = float(eigenvalues[0]), float(eigenvalues[-1])
    return {
        "symmetric": symmetric,
        "minimum_eigenvalue": minimum,
        "maximum_eigenvalue": maximum,
        "positive_semidefinite_within_tolerance": bool(symmetric and minimum >= -tolerance),
    }
