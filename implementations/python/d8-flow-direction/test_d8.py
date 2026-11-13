import pytest
from d8 import flow_direction


def test_selects_steepest_orthogonal_direction():
    dem = [[10, 9, 10], [10, 10, 10], [10, 10, 10]]
    assert flow_direction(dem)[0][0] == 1


def test_diagonal_gradient_accounts_for_diagonal_distance():
    dem = [[10, 10, 10], [10, 10, 8], [10, 10, 10]]
    assert flow_direction(dem)[1][1] == 2


def test_no_lower_neighbour_is_a_sink_or_flat():
    assert flow_direction([[5, 5, 5], [5, 5, 5], [5, 5, 5]])[1][1] == 0
    assert flow_direction([[6, 6, 6], [6, 1, 6], [6, 6, 6]])[1][1] == 0


def test_nodata_cell_remains_nodata():
    result = flow_direction([[1, None], [2, 3]])
    assert result[0][1] is None


def test_nodata_neighbours_are_ignored():
    dem = [[None, 8, None], [None, 10, None], [None, None, None]]
    assert flow_direction(dem)[1][1] == 64


def test_equal_gradient_uses_documented_direction_order():
    dem = [[10, 10, 10], [9, 10, 9], [10, 10, 10]]
    assert flow_direction(dem)[1][1] == 1


def test_rectangular_cells_change_diagonal_distance():
    dem = [[10, 10, 10], [10, 10, 10], [10, 9, 8]]
    square = flow_direction(dem, cell_width=1, cell_height=1)
    short_cells = flow_direction(dem, cell_width=1, cell_height=0.5)
    assert square[1][1] == 2
    assert short_cells[1][1] == 4


def test_rectangular_grid_is_supported():
    assert len(flow_direction([[3, 2, 1], [4, 3, 2]])) == 2


def test_ragged_grid_is_rejected():
    with pytest.raises(ValueError, match="equal length"):
        flow_direction([[1, 2], [3]])


@pytest.mark.parametrize("width,height", [(0, 1), (-1, 1), (1, 0), (1, float("inf"))])
def test_invalid_cell_dimensions_are_rejected(width, height):
    with pytest.raises(ValueError):
        flow_direction([[1]], cell_width=width, cell_height=height)


def test_non_finite_elevation_is_rejected():
    with pytest.raises(ValueError, match="finite"):
        flow_direction([[1, float("nan")]])
