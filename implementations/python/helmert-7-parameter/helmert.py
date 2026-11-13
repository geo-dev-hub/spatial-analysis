"""Seven-parameter geocentric Helmert transformation, Position Vector convention."""
from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray


def helmert_position_vector(
    coordinates: ArrayLike,
    translations: ArrayLike,
    rotations_arcsec: ArrayLike,
    scale_ppm: float,
    *,
    inverse: bool = False,
) -> NDArray[np.float64]:
    """Transform geocentric XYZ coordinates using the small-angle PV convention.

    Coordinates and translations use the same linear unit (normally metres).
    Rotations are arc-seconds; scale correction is parts per million.
    The input array has shape (n, 3). This is not a geographic lon/lat transform.
    """
    xyz = np.asarray(coordinates, dtype=np.float64)
    if xyz.ndim != 2 or xyz.shape[1] != 3 or xyz.shape[0] == 0:
        raise ValueError("coordinates must be a non-empty (n, 3) array")
    if not np.all(np.isfinite(xyz)):
        raise ValueError("coordinates must be finite")

    translation = np.asarray(translations, dtype=np.float64)
    rotations = np.asarray(rotations_arcsec, dtype=np.float64)
    if translation.shape != (3,) or not np.all(np.isfinite(translation)):
        raise ValueError("translations must be a finite length-3 vector")
    if rotations.shape != (3,) or not np.all(np.isfinite(rotations)):
        raise ValueError("rotations_arcsec must be a finite length-3 vector")
    if not np.isfinite(scale_ppm):
        raise ValueError("scale_ppm must be finite")

    radians = rotations * (np.pi / (180.0 * 3600.0))
    rx, ry, rz = radians
    scale = 1.0 + float(scale_ppm) * 1e-6
    if scale <= 0:
        raise ValueError("scale factor must be positive")

    rotation = np.array([
        [1.0, -rz, ry],
        [rz, 1.0, -rx],
        [-ry, rx, 1.0],
    ], dtype=np.float64)
    matrix = scale * rotation

    if inverse:
        return np.linalg.solve(matrix, (xyz - translation).T).T
    return xyz @ matrix.T + translation
