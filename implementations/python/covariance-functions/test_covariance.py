import numpy as np
import pytest

from covariance import (
    covariance_from_distance,
    covariance_matrix,
    covariance_matrix_diagnostics,
    semivariogram_from_distance,
)


@pytest.mark.parametrize("model", ["exponential", "gaussian", "matern32", "spherical", "wendland_c2"])
def test_covariance_matrix_is_symmetric_with_correct_diagonal(model):
    points = np.array([[0, 0], [0.4, 0.2], [1.2, -0.1], [2.0, 0.8]])
    matrix = covariance_matrix(points, model=model, variance=2.5, range_scale=1.7)
    np.testing.assert_allclose(matrix, matrix.T, atol=1e-12)
    np.testing.assert_allclose(np.diag(matrix), 2.5)


@pytest.mark.parametrize("model", ["exponential", "gaussian", "matern32", "spherical", "wendland_c2"])
def test_covariance_matrices_are_positive_semidefinite_on_small_euclidean_fixture(model):
    points = np.array([[0, 0], [0.4, 0.2], [1.2, -0.1], [2.0, 0.8], [0.2, 1.4]])
    matrix = covariance_matrix(points, model=model, range_scale=0.8)
    result = covariance_matrix_diagnostics(matrix, tolerance=1e-9)
    assert result["symmetric"]
    assert result["positive_semidefinite_within_tolerance"]


def test_semivariogram_is_zero_at_origin_and_increases_for_exponential():
    gamma = semivariogram_from_distance([0, 0.5, 1, 2], model="exponential")
    assert gamma[0] == pytest.approx(0)
    assert np.all(np.diff(gamma) > 0)


def test_compact_support_models_are_zero_at_and_beyond_the_range():
    for model in ("spherical", "wendland_c2"):
        values = covariance_from_distance([1.0, 1.5, 4.0], model=model, range_scale=1.0)
        np.testing.assert_allclose(values, 0.0, atol=0.0)


def test_duplicate_locations_produce_a_valid_singular_covariance_matrix():
    matrix = covariance_matrix([[0, 0], [0, 0], [1, 0]], model="gaussian")
    result = covariance_matrix_diagnostics(matrix)
    assert result["positive_semidefinite_within_tolerance"]
    assert np.linalg.matrix_rank(matrix) < len(matrix)


@pytest.mark.parametrize("bad", [[-1], [float("nan")], [float("inf")]])
def test_invalid_distances_are_rejected(bad):
    with pytest.raises(ValueError):
        covariance_from_distance(bad)


def test_invalid_locations_and_parameters_are_rejected():
    with pytest.raises(ValueError):
        covariance_matrix([[0, float("nan")]])
    with pytest.raises(ValueError):
        covariance_matrix([[0, 0]], model="spherical")  # valid shape; no exception expected


def test_compact_support_models_reject_dimensions_above_three():
    with pytest.raises(ValueError):
        covariance_matrix(np.zeros((4, 4)), model="wendland_c2")
