import numpy as np
import pytest

from topsis import topsis


def test_benefit_and_cost_criteria_rank_expected_alternative_first():
    matrix = np.array([
        [80, 20],
        [60, 10],
        [90, 40],
    ], dtype=float)
    result = topsis(matrix, [0.5, 0.5], [True, False])
    assert result.ranking[0] == 1
    assert result.scores[1] > result.scores[0] > result.scores[2]
    assert np.all((result.scores >= 0) & (result.scores <= 1))


def test_weights_are_normalised_and_ranking_is_stable():
    matrix = np.array([[1, 4], [2, 3], [3, 2]], dtype=float)
    a = topsis(matrix, [1, 1], [True, True])
    b = topsis(matrix, [10, 10], [True, True])
    np.testing.assert_allclose(a.scores, b.scores)
    np.testing.assert_array_equal(a.ranking, b.ranking)


def test_identical_alternatives_have_neutral_undefined_closeness():
    result = topsis([[5, 2], [5, 2]], [0.5, 0.5], [True, False])
    np.testing.assert_allclose(result.scores, [0.5, 0.5])
    np.testing.assert_allclose(result.distance_to_ideal, [0, 0])
    np.testing.assert_allclose(result.distance_to_anti_ideal, [0, 0])


@pytest.mark.parametrize("matrix", [[], [1, 2], [[-1, 2]], [[1, np.nan]], [[0, 0], [0, 0]]])
def test_invalid_decision_matrices_are_rejected(matrix):
    with pytest.raises(ValueError):
        topsis(matrix, [1, 1], [True, True])


def test_invalid_weights_and_benefit_mask_are_rejected():
    with pytest.raises(ValueError):
        topsis([[1, 2]], [0, 0], [True, True])
    with pytest.raises(ValueError):
        topsis([[1, 2]], [1, 1], [1, 0])
