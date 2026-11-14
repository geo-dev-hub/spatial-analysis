"""Geodetic, ECEF and local East-North-Up coordinate conversions.

Angles are in degrees at the public API. Coordinates and heights are in
metres. Heights are ellipsoidal, not orthometric/geoid-referenced.
"""
from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np
from numpy.typing import ArrayLike, NDArray


@dataclass(frozen=True)
class Ellipsoid:
    semi_major_axis_m: float = 6378137.0
    inverse_flattening: float = 298.257223563

    def __post_init__(self):
        if not math.isfinite(self.semi_major_axis_m) or self.semi_major_axis_m <= 0:
            raise ValueError("semi_major_axis_m must be finite and positive")
        if not math.isfinite(self.inverse_flattening) or self.inverse_flattening <= 1:
            raise ValueError("inverse_flattening must be finite and greater than one")

    @property
    def flattening(self) -> float:
        return 1.0 / self.inverse_flattening

    @property
    def eccentricity_squared(self) -> float:
        f = self.flattening
        return f * (2.0 - f)


WGS84 = Ellipsoid()


def _finite(value: ArrayLike, name: str) -> NDArray[np.float64]:
    array = np.asarray(value, dtype=np.float64)
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must contain only finite values")
    return array


def geodetic_to_ecef(
    longitude_deg: ArrayLike,
    latitude_deg: ArrayLike,
    ellipsoidal_height_m: ArrayLike = 0.0,
    *,
    ellipsoid: Ellipsoid = WGS84,
) -> NDArray[np.float64]:
    """Convert geodetic longitude, latitude and ellipsoidal height to XYZ."""
    lon = _finite(longitude_deg, "longitude_deg")
    lat = _finite(latitude_deg, "latitude_deg")
    height = _finite(ellipsoidal_height_m, "ellipsoidal_height_m")
    lon, lat, height = np.broadcast_arrays(lon, lat, height)
    if np.any((lat < -90.0) | (lat > 90.0)):
        raise ValueError("latitude_deg must lie in [-90, 90]")

    lam = np.deg2rad(lon)
    phi = np.deg2rad(lat)
    sin_phi = np.sin(phi)
    cos_phi = np.cos(phi)
    e2 = ellipsoid.eccentricity_squared
    prime_vertical = ellipsoid.semi_major_axis_m / np.sqrt(1.0 - e2 * sin_phi**2)

    x = (prime_vertical + height) * cos_phi * np.cos(lam)
    y = (prime_vertical + height) * cos_phi * np.sin(lam)
    z = (prime_vertical * (1.0 - e2) + height) * sin_phi
    return np.stack((x, y, z), axis=-1)


def _origin_parameters(longitude_deg: float, latitude_deg: float,
                       ellipsoidal_height_m: float, ellipsoid: Ellipsoid):
    lon = float(_finite(longitude_deg, "origin_longitude_deg"))
    lat = float(_finite(latitude_deg, "origin_latitude_deg"))
    height = float(_finite(ellipsoidal_height_m, "origin_ellipsoidal_height_m"))
    if not -90.0 <= lat <= 90.0:
        raise ValueError("origin_latitude_deg must lie in [-90, 90]")
    origin = geodetic_to_ecef(lon, lat, height, ellipsoid=ellipsoid)
    lam, phi = math.radians(lon), math.radians(lat)
    return origin, math.sin(lam), math.cos(lam), math.sin(phi), math.cos(phi)


def ecef_to_enu(
    ecef_xyz_m: ArrayLike,
    *,
    origin_longitude_deg: float,
    origin_latitude_deg: float,
    origin_ellipsoidal_height_m: float = 0.0,
    ellipsoid: Ellipsoid = WGS84,
) -> NDArray[np.float64]:
    """Rotate ECEF XYZ coordinates into a local East, North, Up frame."""
    xyz = _finite(ecef_xyz_m, "ecef_xyz_m")
    if xyz.ndim < 1 or xyz.shape[-1] != 3:
        raise ValueError("ecef_xyz_m must have final dimension of length three")
    origin, sin_lam, cos_lam, sin_phi, cos_phi = _origin_parameters(
        origin_longitude_deg, origin_latitude_deg,
        origin_ellipsoidal_height_m, ellipsoid,
    )
    dx, dy, dz = np.moveaxis(xyz - origin, -1, 0)
    east = -sin_lam * dx + cos_lam * dy
    north = -sin_phi * cos_lam * dx - sin_phi * sin_lam * dy + cos_phi * dz
    up = cos_phi * cos_lam * dx + cos_phi * sin_lam * dy + sin_phi * dz
    return np.stack((east, north, up), axis=-1)


def enu_to_ecef(
    enu_xyz_m: ArrayLike,
    *,
    origin_longitude_deg: float,
    origin_latitude_deg: float,
    origin_ellipsoidal_height_m: float = 0.0,
    ellipsoid: Ellipsoid = WGS84,
) -> NDArray[np.float64]:
    """Rotate local East, North, Up coordinates back into ECEF XYZ."""
    enu = _finite(enu_xyz_m, "enu_xyz_m")
    if enu.ndim < 1 or enu.shape[-1] != 3:
        raise ValueError("enu_xyz_m must have final dimension of length three")
    origin, sin_lam, cos_lam, sin_phi, cos_phi = _origin_parameters(
        origin_longitude_deg, origin_latitude_deg,
        origin_ellipsoidal_height_m, ellipsoid,
    )
    east, north, up = np.moveaxis(enu, -1, 0)
    dx = -sin_lam * east - sin_phi * cos_lam * north + cos_phi * cos_lam * up
    dy = cos_lam * east - sin_phi * sin_lam * north + cos_phi * sin_lam * up
    dz = cos_phi * north + sin_phi * up
    return origin + np.stack((dx, dy, dz), axis=-1)


def geodetic_to_enu(
    longitude_deg: ArrayLike,
    latitude_deg: ArrayLike,
    ellipsoidal_height_m: ArrayLike,
    *,
    origin_longitude_deg: float,
    origin_latitude_deg: float,
    origin_ellipsoidal_height_m: float = 0.0,
    ellipsoid: Ellipsoid = WGS84,
) -> NDArray[np.float64]:
    """Convert geodetic coordinates directly to a local ENU frame."""
    xyz = geodetic_to_ecef(
        longitude_deg, latitude_deg, ellipsoidal_height_m, ellipsoid=ellipsoid
    )
    return ecef_to_enu(
        xyz,
        origin_longitude_deg=origin_longitude_deg,
        origin_latitude_deg=origin_latitude_deg,
        origin_ellipsoidal_height_m=origin_ellipsoidal_height_m,
        ellipsoid=ellipsoid,
    )
