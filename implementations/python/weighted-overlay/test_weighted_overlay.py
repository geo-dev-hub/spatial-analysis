import numpy as np
import pytest

from weighted_overlay import weighted_linear_combination


def test_weighted_sum_uses_relative_weights():
    criteria = {
        "access": np.array([[0.8, 0.2]]),
        "terrain": np.array([[0.6, 1.0]]),
    }
    result = weighted_linear_combination(criteria, {"access": 3, "terrain": 1})
    np.testing.assert_allclose(result, [[0.75, 0.4]])


def test_weights_are_normalised_even_if_they_do_not_sum_to_one():
    criteria = {"a": np.array([[1.0]]), "b": np.array([[0.0]])}
    result = weighted_linear_combination(criteria, {"a": 8, "b": 2})
    np.testing.assert_allclose(result, [[0.8]])


def test_zero_weight_criterion_does_not_affect_score():
    criteria = {"a": np.array([[0.25]]), "b": np.array([[1.0]])}
    result = weighted_linear_combination(criteria, {"a": 1, "b": 0})
    np.testing.assert_allclose(result, [[0.25]])


def test_eligibility_mask_excludes_cells():
    criteria = {"a": np.array([[0.2, 0.8], [0.4, 1.0]])}
    eligible = np.array([[True, False], [True, False]])
    result = weighted_linear_combination(criteria, {"a": 1}, eligible=eligible)
    assert result[0, 0] == pytest.approx(0.2)
    assert np.isnan(result[0, 1])
    assert result[1, 0] == pytest.approx(0.4)
    assert np.isnan(result[1, 1])


def test_any_missing_criterion_excludes_the_cell_under_strict_policy():
    criteria = {
        "a": np.array([[0.5, np.nan]]),
        "b": np.array([[0.5, 0.9]]),
    }
    result = weighted_linear_combination(criteria, {"a": 1, "b": 1})
    assert result[0, 0] == pytest.approx(0.5)
    assert np.isnan(result[0, 1])


def test_infinite_values_are_treated_as_nodata():
    criteria = {"a": np.array([[0.5, np.inf]])}
    result = weighted_linear_combination(criteria, {"a": 1})
    assert result[0, 0] == pytest.approx(0.5)
    assert np.isnan(result[0, 1])


def test_all_excluded_cells_return_all_nan():
    criteria = {"a": np.array([[0.1, 0.2]])}
    result = weighted_linear_combination(
        criteria, {"a": 1}, eligible=np.array([[False, False]])
    )
    assert np.isnan(result).all()


def test_criterion_names_and_weight_names_must_match():
    criteria = {"a": np.array([[0.5]]), "b": np.array([[0.6]])}
    with pytest.raises(ValueError, match="exactly one value"):
        weighted_linear_combination(criteria, {"a": 1, "c": 1})


@pytest.mark.parametrize("weights", [
    {"a": -1}, {"a": np.nan}, {"a": np.inf}, {"a": 0},
])
def test_invalid_or_zero_total_weights_are_rejected(weights):
    with pytest.raises(ValueError):
        weighted_linear_combination({"a": np.array([[0.5]])}, weights)


@pytest.mark.parametrize("value", [-0.01, 1.01])
def test_finite_scores_outside_unit_interval_are_rejected(value):
    with pytest.raises(ValueError, match=r"\[0, 1\]"):
        weighted_linear_combination({"a": np.array([[value]])}, {"a": 1})


def test_criterion_arrays_must_be_two_dimensional():
    with pytest.raises(ValueError, match="2D array"):
        weighted_linear_combination({"a": np.array([0.1, 0.2])}, {"a": 1})


def test_criterion_shapes_must_match():
    criteria = {"a": np.ones((2, 2)), "b": np.ones((1, 2))}
    with pytest.raises(ValueError, match="same shape"):
        weighted_linear_combination(criteria, {"a": 1, "b": 1})


def test_eligibility_mask_must_be_boolean_and_aligned():
    criteria = {"a": np.ones((2, 2))}
    with pytest.raises(ValueError, match="Boolean"):
        weighted_linear_combination(criteria, {"a": 1}, eligible=np.ones((2, 2)))
    with pytest.raises(ValueError, match="same shape"):
        weighted_linear_combination(criteria, {"a": 1}, eligible=np.ones((1, 2), dtype=bool))


def test_output_is_bounded_by_standardised_input_range():
    criteria = {"a": np.array([[0.0, 1.0]]), "b": np.array([[1.0, 0.0]])}
    result = weighted_linear_combination(criteria, {"a": 0.35, "b": 0.65})
    assert np.all((result >= 0.0) & (result <= 1.0))
