import numpy as np
import pytest

from d8_flow_accumulation import d8_flow_accumulation


def test_linear_eastward_flow_counts_upstream_cells_including_self():
    result = d8_flow_accumulation([[1, 1, 0]])
    np.testing.assert_allclose(result, [[1, 2, 3]])


def test_confluence_accumulates_all_upstream_branches():
    # Top and bottom flow into the centre, which then flows east.
    directions = np.array([
        [-1, 4, -1],
        [-1, 1, -1],
        [-1, 64, -1],
    ])
    result = d8_flow_accumulation(directions)
    assert result[0, 1] == 2
    assert result[2, 1] == 2
    assert result[1, 1] == 3


def test_weighted_accumulation_sums_source_contributions():
    directions = [[1, 1, 0]]
    weights = [[2.5, 3.0, 4.5]]
    np.testing.assert_allclose(
        d8_flow_accumulation(directions, weights=weights),
        [[2.5, 5.5, 10.0]],
    )


def test_flow_exiting_grid_or_entering_nodata_leaves_valid_domain():
    directions = np.array([[16, -1], [0, 0]])
    result = d8_flow_accumulation(directions)
    assert result[0, 0] == 1
    assert np.isnan(result[0, 1])
    assert result[1, 0] == 1


def test_cycle_is_detected_instead_of_returning_partial_result():
    with pytest.raises(ValueError, match="cycle"):
        d8_flow_accumulation([[1, 16]])


def test_invalid_codes_and_non_integer_grids_are_rejected():
    with pytest.raises(ValueError, match="unsupported"):
        d8_flow_accumulation([[3]])
    with pytest.raises(ValueError, match="integer"):
        d8_flow_accumulation([[1.0, 0.0]])


def test_invalid_weights_are_rejected_but_nodata_weight_is_ignored():
    with pytest.raises(ValueError, match="weights"):
        d8_flow_accumulation([[1, 0]], weights=[[1]])
    with pytest.raises(ValueError, match="finite and non-negative"):
        d8_flow_accumulation([[1, 0]], weights=[[1, -1]])
    result = d8_flow_accumulation([[-1, 0]], weights=[[float("nan"), 2]])
    assert np.isnan(result[0, 0])
    assert result[0, 1] == 2
