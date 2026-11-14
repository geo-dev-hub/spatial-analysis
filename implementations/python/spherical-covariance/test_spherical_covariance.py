import numpy as np
import pytest

from spherical_covariance import (
    latlon_to_unit_vectors,
    legendre_series_covariance,
    spherical_covariance_diagnostics,
    spherical_covariance_matrix,
)


def test_latlon_conversion_has_expected_equator_and_poles():
    xyz = latlon_to_unit_vectors([0, 0, 90, -90], [0, 90, 0, 0])
    np.testing.assert_allclose(xyz, [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, -1]], atol=1e-12)


def test_latlon_broadcasts_and_rejects_invalid_coordinates():
    assert latlon_to_unit_vectors([0, 10], [0]).shape == (2, 3)
    with pytest.raises(ValueError):
        latlon_to_unit_vectors([91], [0])
    with pytest.raises(ValueError):
        latlon_to_unit_vectors([0], [181])
    with pytest.raises(ValueError):
        latlon_to_unit_vectors([np.nan], [0])


def test_legendre_series_has_variance_equal_to_sum_of_coefficients():
    b = [2.0, 0.5, 0.25]
    values = legendre_series_covariance([0, np.pi], b)
    assert values[0] == pytest.approx(sum(b))
    assert values[1] == pytest.approx(2.0 - 0.5 + 0.25)


def test_normalised_series_has_unit_variance():
    assert legendre_series_covariance([0], [2, 1, 1], normalise=True)[0] == pytest.approx(1)


@pytest.mark.parametrize("bad", [[], [0, 0], [-1, 2], [1, np.nan], [1, np.inf], [[1, 2]]])
def test_invalid_schoenberg_coefficients_are_rejected(bad):
    with pytest.raises(ValueError):
        legendre_series_covariance([0], bad)


@pytest.mark.parametrize("bad", [[-0.1], [np.pi + 0.01], [np.nan], [np.inf]])
def test_invalid_angular_distances_are_rejected(bad):
    with pytest.raises(ValueError):
        legendre_series_covariance(bad, [1, 0.2])


def test_matrix_is_symmetric_and_has_expected_diagonal():
    xyz = latlon_to_unit_vectors([0, 0, 45], [0, 90, 45])
    matrix = spherical_covariance_matrix(xyz, [1.5, 0.4, 0.1])
    np.testing.assert_allclose(matrix, matrix.T, atol=1e-12)
    np.testing.assert_allclose(np.diag(matrix), 2.0)


def test_nonnegative_legendre_coefficients_generate_psd_matrices():
    xyz = latlon_to_unit_vectors(
        [-70, -30, 0, 25, 60, 80, 10],
        [-160, -40, 10, 80, 145, 20, -100],
    )
    for coefficients in ([1], [0.5, 0.5], [1, 0.3, 0.2, 0.1], [0, 0, 1, 0, 0.2]):
        matrix = spherical_covariance_matrix(xyz, coefficients)
        result = spherical_covariance_diagnostics(matrix, tolerance=1e-9)
        assert result["symmetric"]
        assert result["positive_semidefinite_within_tolerance"]


def test_antipodal_and_duplicate_points_are_handled():
    xyz = latlon_to_unit_vectors([0, 0, 0], [0, 0, 180])
    matrix = spherical_covariance_matrix(xyz, [1, 0.4, 0.1])
    assert matrix[0, 1] == pytest.approx(matrix[1, 0])
    assert matrix[0, 0] == pytest.approx(matrix[1, 1])
    assert spherical_covariance_diagnostics(matrix)["positive_semidefinite_within_tolerance"]


def test_matrix_requires_unit_vectors():
    with pytest.raises(ValueError):
        spherical_covariance_matrix([[2, 0, 0]], [1])
    with pytest.raises(ValueError):
        spherical_covariance_matrix([[1, 0]], [1])


def test_diagnostics_validate_input():
    with pytest.raises(ValueError):
        spherical_covariance_diagnostics([[1, np.nan]])
    with pytest.raises(ValueError):
        spherical_covariance_diagnostics([[1]], tolerance=-1)
