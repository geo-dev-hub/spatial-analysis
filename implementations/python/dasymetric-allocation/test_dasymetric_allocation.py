import numpy as np
import pytest
from dasymetric_allocation import dasymetric_allocate


def test_weighted_allocation_conserves_each_source_total():
    result = dasymetric_allocate(
        [100, 60],
        [[1, 3, 0], [0, 2, 2]],
    )
    np.testing.assert_allclose(result["allocations"], [[25, 75, 0], [0, 30, 30]])
    np.testing.assert_allclose(result["source_totals_reconstructed"], [100, 60])
    np.testing.assert_allclose(result["target_totals"], [25, 105, 30])


def test_eligibility_mask_allows_uniform_zero_weight_fallback():
    result = dasymetric_allocate(
        [40],
        [[0, 0, 0]],
        eligible_mask=[[True, False, True]],
        zero_weight="uniform",
    )
    np.testing.assert_allclose(result["allocations"], [[20, 0, 20]])
    assert result["uniform_fallback_rows"] == (0,)


def test_zero_population_row_needs_no_eligible_targets():
    result = dasymetric_allocate([0], [[0, 0]])
    np.testing.assert_allclose(result["allocations"], [[0, 0]])


def test_positive_population_without_eligible_targets_is_rejected():
    with pytest.raises(ValueError, match="no eligible"):
        dasymetric_allocate([10], [[0, 0]])


def test_zero_weight_eligible_row_errors_by_default():
    with pytest.raises(ValueError, match="zero ancillary"):
        dasymetric_allocate([10], [[0, 0]], eligible_mask=[[True, True]])


@pytest.mark.parametrize("totals,weights", [
    ([], []), ([1], [[1], [2]]), ([1], [[-1]]),
    ([1], [[float("nan")]]), ([-1], [[1]]), ([float("inf")], [[1]]),
])
def test_invalid_inputs_are_rejected(totals, weights):
    with pytest.raises(ValueError):
        dasymetric_allocate(totals, weights)


def test_positive_weight_outside_eligibility_is_rejected():
    with pytest.raises(ValueError, match="outside"):
        dasymetric_allocate([10], [[1, 0]], eligible_mask=[[False, True]])


def test_invalid_zero_weight_policy_is_rejected():
    with pytest.raises(ValueError):
        dasymetric_allocate([10], [[1]], zero_weight="ignore")
