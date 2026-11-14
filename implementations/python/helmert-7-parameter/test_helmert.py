import numpy as np
import pytest

from helmert import helmert_position_vector


def test_published_wgs72_to_wgs84_geocentric_example():
    source = np.array([[3657660.66, 255768.55, 5201382.11]])
    target = helmert_position_vector(
        source,
        translations=[0, 0, 4.5],
        rotations_arcsec=[0, 0, 0.554],
        scale_ppm=0.219,
    )
    expected = np.array([[3657660.78, 255778.43, 5201387.75]])
    np.testing.assert_allclose(target, expected, atol=0.02)


def test_inverse_recovers_source_coordinates():
    source = np.array([
        [3657660.66, 255768.55, 5201382.11],
        [1111111.0, -2222222.0, 3333333.0],
    ])
    params = dict(
        translations=[0.2, -0.4, 4.5],
        rotations_arcsec=[-0.12, 0.08, 0.554],
        scale_ppm=0.219,
    )
    target = helmert_position_vector(source, **params)
    recovered = helmert_position_vector(target, **params, inverse=True)
    np.testing.assert_allclose(recovered, source, atol=1e-8)


def test_identity_parameters_leave_coordinates_unchanged():
    xyz = np.array([[1, 2, 3], [-10, 50, 100]], dtype=float)
    np.testing.assert_allclose(
        helmert_position_vector(xyz, [0, 0, 0], [0, 0, 0], 0), xyz
    )


@pytest.mark.parametrize("coords", [[], [1, 2, 3], [[1, 2]], [[1, 2, np.nan]]])
def test_invalid_coordinates_are_rejected(coords):
    with pytest.raises(ValueError):
        helmert_position_vector(coords, [0, 0, 0], [0, 0, 0], 0)


@pytest.mark.parametrize("translations,rotations,scale", [
    ([0, 0], [0, 0, 0], 0),
    ([0, 0, np.inf], [0, 0, 0], 0),
    ([0, 0, 0], [0, np.nan, 0], 0),
    ([0, 0, 0], [0, 0, 0], np.nan),
    ([0, 0, 0], [0, 0, 0], -1_000_000),
])
def test_invalid_parameters_are_rejected(translations, rotations, scale):
    with pytest.raises(ValueError):
        helmert_position_vector([[1, 2, 3]], translations, rotations, scale)
