import numpy as np
import pytest

from ahp_weights import ahp_weights


def test_consistent_matrix_recovers_known_ratio_weights():
    expected = np.array([0.6, 0.3, 0.1])
    matrix = expected[:, None] / expected[None, :]
    result = ahp_weights(matrix, ["access", "terrain", "flood"])
    np.testing.assert_allclose(result.weights, expected, atol=1e-10)
    assert result.lambda_max == pytest.approx(3.0)
    assert result.consistency_index == pytest.approx(0.0, abs=1e-10)
    assert result.consistency_ratio == pytest.approx(0.0, abs=1e-10)
    assert result.criteria == ("access", "terrain", "flood")


def test_inconsistent_example_returns_normalised_priorities():
    matrix = np.array([[1, 3, 5], [1/3, 1, 2], [1/5, 1/2, 1]], dtype=float)
    result = ahp_weights(matrix)
    assert result.weights.sum() == pytest.approx(1.0)
    assert np.all(result.weights > 0)
    assert result.consistency_ratio is not None
    assert result.consistency_ratio >= 0


def test_single_and_two_criteria_have_no_reference_ratio():
    assert ahp_weights([[1]]).consistency_ratio is None
    assert ahp_weights([[1, 4], [0.25, 1]]).consistency_ratio is None


@pytest.mark.parametrize("matrix", [
    [], [1, 2], [[1, 0], [0, 1]], [[1, np.nan], [np.nan, 1]],
    [[1, 2], [0.4, 1]], [[2, 2], [0.5, 1]],
])
def test_invalid_matrices_are_rejected(matrix):
    with pytest.raises(ValueError):
        ahp_weights(matrix)


def test_criteria_names_must_be_unique_and_complete():
    with pytest.raises(ValueError, match="one non-empty name"):
        ahp_weights(np.eye(2), ["only_one"])
    with pytest.raises(ValueError, match="unique"):
        ahp_weights(np.eye(2), ["same", "same"])
