import numpy as np
import pytest

from watershed_delineation import delineate_watershed


def test_single_outlet_includes_all_upstream_contributors():
    directions = [
        [-1, 4, -1],
        [-1, 1, -1],
        [-1, 64, -1],
    ]
    expected = np.array([
        [False, True, False],
        [False, True, False],
        [False, True, False],
    ])
    np.testing.assert_array_equal(
        delineate_watershed(directions, outlet=(1, 1)), expected
    )


def test_cells_draining_to_another_sink_are_not_in_basin():
    directions = [[1, 0, 1, 0]]
    result = delineate_watershed(directions, outlet=(0, 1))
    np.testing.assert_array_equal(result, [[True, True, False, False]])


def test_invalid_cells_and_flow_exiting_grid_do_not_enter_basin():
    directions = [[1, -1], [0, 0]]
    result = delineate_watershed(directions, outlet=(0, 0))
    np.testing.assert_array_equal(result, [[True, False], [False, False]])


def test_cycle_is_rejected_even_when_outside_requested_basin():
    directions = [[0, -1, 1, 16]]
    with pytest.raises(ValueError, match="cycle"):
        delineate_watershed(directions, outlet=(0, 0))


def test_outlet_must_be_valid_and_inside_raster():
    with pytest.raises(ValueError, match="outside"):
        delineate_watershed([[0]], outlet=(1, 0))
    with pytest.raises(ValueError, match="valid"):
        delineate_watershed([[-1]], outlet=(0, 0))


def test_invalid_codes_and_non_integer_arrays_are_rejected():
    with pytest.raises(ValueError, match="unsupported"):
        delineate_watershed([[3]], outlet=(0, 0))
    with pytest.raises(ValueError, match="integer"):
        delineate_watershed([[0.0]], outlet=(0, 0))
