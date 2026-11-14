"""Schoenberg-series covariance models for isotropic fields on the 2-sphere."""
from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray


def _weights(coefficients: ArrayLike) -> NDArray[np.float64]:
    values = np.asarray(coefficients, dtype=np.float64)
    if values.ndim != 1 or values.size == 0:
        raise ValueError("coefficients must be a non-empty one-dimensional array")
    if not np.all(np.isfinite(values)) or np.any(values < 0):
        raise ValueError("Schoenberg coefficients must be finite and non-negative")
    if not np.sum(values) > 0:
        raise ValueError("at least one Schoenberg coefficient must be positive")
    return values


def latlon_to_unit_vectors(
    latitude_degrees: ArrayLike, longitude_degrees: ArrayLike
) -> NDArray[np.float64]:
    """Convert matching latitude/longitude arrays in degrees to unit-sphere XYZ."""
    lat, lon = np.broadcast_arrays(
        np.asarray(latitude_degrees, dtype=np.float64),
        np.asarray(longitude_degrees, dtype=np.float64),
    )
    if not np.all(np.isfinite(lat)) or not np.all(np.isfinite(lon)):
        raise ValueError("latitude and longitude must be finite")
    if np.any((lat < -90.0) | (lat > 90.0)):
        raise ValueError("latitude must be within [-90, 90] degrees")
    if np.any((lon < -180.0) | (lon > 180.0)):
        raise ValueError("longitude must be within [-180, 180] degrees")
    phi = np.deg2rad(lat)
    lam = np.deg2rad(lon)
    cos_phi = np.cos(phi)
    return np.stack(
        (cos_phi * np.cos(lam), cos_phi * np.sin(lam), np.sin(phi)), axis=-1
    )


def _unit_vectors(locations: ArrayLike) -> NDArray[np.float64]:
    xyz = np.asarray(locations, dtype=np.float64)
    if xyz.ndim != 2 or xyz.shape[0] == 0 or xyz.shape[1] != 3:
        raise ValueError("locations must be a non-empty (n, 3) array of unit vectors")
    if not np.all(np.isfinite(xyz)):
        raise ValueError("locations must be finite")
    norms = np.linalg.norm(xyz, axis=1)
    if not np.allclose(norms, 1.0, rtol=0.0, atol=1e-10):
        raise ValueError("each location must be a unit vector within 1e-10")
    return xyz


def legendre_series_covariance(
    angular_distance_radians: ArrayLike,
    coefficients: ArrayLike,
    *,
    normalise: bool = False,
) -> NDArray[np.float64]:
    """Evaluate sum_l b_l P_l(cos(theta)) for non-negative coefficients.

    Coefficients are indexed by degree l=0,...,L. Their sum is the marginal
    variance unless normalise=True, in which case the returned variance is 1.
    The finite non-negative series is positive definite on S2 by construction.
    """
    b = _weights(coefficients)
    theta = np.asarray(angular_distance_radians, dtype=np.float64)
    if not np.all(np.isfinite(theta)) or np.any((theta < 0) | (theta > np.pi)):
        raise ValueError("angular distances must be finite and within [0, pi]")
    if normalise:
        b = b / np.sum(b)
    x = np.cos(theta)
    # Three-term recurrence avoids a SciPy dependency and works on arrays.
    p0 = np.ones_like(x)
    result = b[0] * p0
    if b.size == 1:
        return np.asarray(result, dtype=np.float64)
    p1 = x
    result = result + b[1] * p1
    for degree in range(2, b.size):
        p2 = ((2 * degree - 1) * x * p1 - (degree - 1) * p0) / degree
        result = result + b[degree] * p2
        p0, p1 = p1, p2
    return np.asarray(result, dtype=np.float64)


def spherical_covariance_matrix(
    unit_vectors: ArrayLike,
    coefficients: ArrayLike,
    *,
    normalise: bool = False,
) -> NDArray[np.float64]:
    """Build a dense isotropic covariance matrix on S2 from unit XYZ vectors."""
    xyz = _unit_vectors(unit_vectors)
    dots = np.clip(xyz @ xyz.T, -1.0, 1.0)
    theta = np.arccos(dots)
    return legendre_series_covariance(theta, coefficients, normalise=normalise)


def spherical_covariance_diagnostics(
    matrix: ArrayLike, *, tolerance: float = 1e-10
) -> dict[str, float | bool]:
    """Inspect one finite covariance matrix; numerical checks do not prove the theorem."""
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
