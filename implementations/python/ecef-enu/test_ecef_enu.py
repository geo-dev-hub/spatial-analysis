import numpy as np
import pytest

from ecef_enu import (
    Ellipsoid, ecef_to_enu, enu_to_ecef, geodetic_to_ecef, geodetic_to_enu,
)


def test_geodetic_origin_maps_to_zero_enu():
    origin = geodetic_to_ecef(5.0, 55.0, 200.0)
    enu = ecef_to_enu(
        origin, origin_longitude_deg=5.0, origin_latitude_deg=55.0,
        origin_ellipsoidal_height_m=200.0,
    )
    np.testing.assert_allclose(enu, [0.0, 0.0, 0.0], atol=1e-9)


def test_epsg_9836_published_topocentric_example():
    point = np.array([3771793.968, 140253.342, 5124304.349])
    actual = ecef_to_enu(
        point, origin_longitude_deg=5.0, origin_latitude_deg=55.0,
        origin_ellipsoidal_height_m=200.0,
    )
    np.testing.assert_allclose(
        actual, [-189013.869, -128642.040, -4220.171], atol=0.002
    )


def test_geodetic_to_ecef_equator_and_pole():
    a = 6378137.0
    np.testing.assert_allclose(geodetic_to_ecef(0, 0, 0), [a, 0, 0], atol=1e-8)
    pole = geodetic_to_ecef(0, 90, 0)
    assert abs(pole[0]) < 1e-8
    assert abs(pole[1]) < 1e-8
    assert pole[2] == pytest.approx(6356752.314245, abs=1e-5)


def test_enu_to_ecef_is_inverse_of_ecef_to_enu_for_batch():
    points = np.array([
        [3771793.968, 140253.342, 5124304.349],
        [3652755.3058, 319574.6799, 5201547.3536],
        [3652700.0, 319600.0, 5201500.0],
    ])
    local = ecef_to_enu(
        points, origin_longitude_deg=5, origin_latitude_deg=55,
        origin_ellipsoidal_height_m=200,
    )
    restored = enu_to_ecef(
        local, origin_longitude_deg=5, origin_latitude_deg=55,
        origin_ellipsoidal_height_m=200,
    )
    np.testing.assert_allclose(restored, points, atol=1e-8)


def test_geodetic_to_enu_supports_broadcast_arrays():
    east_north_up = geodetic_to_enu(
        [5.0, 5.001], 55.0, [200.0, 200.0],
        origin_longitude_deg=5.0, origin_latitude_deg=55.0,
        origin_ellipsoidal_height_m=200.0,
    )
    assert east_north_up.shape == (2, 3)
    np.testing.assert_allclose(east_north_up[0], [0, 0, 0], atol=1e-8)
    assert east_north_up[1, 0] > 0


def test_local_rotation_preserves_vector_length_and_is_orthonormal():
    vector = np.array([[120.0, -35.0, 8.0]])
    origin = np.array([0.0, 0.0, 0.0])
    xyz = enu_to_ecef(
        vector, origin_longitude_deg=-73.0, origin_latitude_deg=40.0,
    )
    local = ecef_to_enu(
        xyz, origin_longitude_deg=-73.0, origin_latitude_deg=40.0,
    )
    np.testing.assert_allclose(local, vector, atol=1e-8)
    np.testing.assert_allclose(np.linalg.norm(local, axis=1),
                               np.linalg.norm(vector, axis=1), atol=1e-8)


def test_invalid_coordinates_and_ellipsoids_are_rejected():
    with pytest.raises(ValueError, match="latitude"):
        geodetic_to_ecef(0, 91, 0)
    with pytest.raises(ValueError, match="finite"):
        geodetic_to_ecef(0, np.nan, 0)
    with pytest.raises(ValueError, match="final dimension"):
        ecef_to_enu([1, 2], origin_longitude_deg=0, origin_latitude_deg=0)
    with pytest.raises(ValueError, match="inverse_flattening"):
        Ellipsoid(6378137.0, 1.0)


def test_ellipsoid_parameter_changes_cartesian_result():
    wgs84 = geodetic_to_ecef(0, 45, 0)
    sphere = geodetic_to_ecef(0, 45, 0, ellipsoid=Ellipsoid(6371000, 1000000))
    assert not np.allclose(wgs84, sphere)
