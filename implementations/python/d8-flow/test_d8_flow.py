import numpy as np
import pytest

from d8_flow import d8_flow_direction


def test_d8_routes_simple_eastward_descent():
    dem = np.array([[3, 2, 1]], dtype=float)
    np.testing.assert_array_equal(d8_flow_direction(dem), [[1, 1, 0]])


def test_d8_uses_steepest_slope_not_largest_elevation_drop():
    dem = np.array([
        [10, 9.5],
        [9.7, 10],
    ])
    # From the upper-left, south drops 0.3 over 1; east drops 0.5 over 2.
    result = d8_flow_direction(dem, cell_size=(1, 2))
    assert result[0, 0] == 4


def test_d8_diagonal_distance_uses_both_cell_dimensions():
    dem = np.array([[10, 20], [20, 9]], dtype=float)
    result = d8_flow_direction(dem, cell_size=(3, 4))
    assert result[0, 0] == 2


def test_d8_invalid_and_nodata_cells_are_marked_and_ignored():
    dem = np.array([[5, -9999], [4, 3]], dtype=float)
    result = d8_flow_direction(dem, nodata=-9999)
    assert result[0, 1] == -1
    assert result[0, 0] == 4


def test_d8_valid_mask_excludes_cells_and_checks_shape():
    dem = np.array([[5, 4], [4, 3]], dtype=float)
    mask = np.array([[True, False], [True, True]])
    result = d8_flow_direction(dem, valid_mask=mask)
    assert result[0, 1] == -1
    with pytest.raises(ValueError, match="valid_mask"):
        d8_flow_direction(dem, valid_mask=np.ones((3, 3)))


def test_d8_flat_or_pit_cell_receives_zero():
    dem = np.array([[5, 5, 5], [5, 1, 5], [5, 5, 5]], dtype=float)
    result = d8_flow_direction(dem)
    assert result[1, 1] == 0


def test_d8_tie_breaking_follows_direction_order():
    dem = np.array([[5, 4], [4, 5]], dtype=float)
    result = d8_flow_direction(dem)
    assert result[0, 0] == 1


@pytest.mark.parametrize("cell_size", [(0, 1), (1, -1), (float("inf"), 1), (1,)])
def test_d8_rejects_invalid_cell_size(cell_size):
    with pytest.raises(ValueError, match="cell_size"):
        d8_flow_direction([[2, 1]], cell_size=cell_size)


def test_d8_rejects_non_2d_dem():
    with pytest.raises(ValueError, match="2D"):
        d8_flow_direction([1, 2, 3])
