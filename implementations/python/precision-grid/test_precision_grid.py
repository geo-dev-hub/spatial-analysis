import pytest
from shapely.geometry import LineString, Polygon

from precision_grid import fixed_precision_intersection, reduce_precision


def test_precision_reduction_snaps_coordinates_to_grid():
    line = LineString([(0.04, 0.04), (1.04, 1.04)])
    result = reduce_precision(line, 0.1)
    assert list(result.coords) == [(0.0, 0.0), (1.0, 1.0)]


def test_fixed_precision_intersection_nodes_near_crossing_lines():
    first = LineString([(0.04, 0.04), (1.04, 1.04)])
    second = LineString([(0.04, 1.04), (1.04, 0.04)])
    result = fixed_precision_intersection(first, second, 0.1)
    assert result.geom_type == "Point"
    assert result.x == pytest.approx(0.5)
    assert result.y == pytest.approx(0.5)


def test_valid_output_mode_can_collapse_narrow_polygon():
    narrow = Polygon([(0, 0), (0.04, 0), (0.04, 1), (0, 1)])
    result = reduce_precision(narrow, 0.1, mode="valid_output")
    assert result.is_empty


@pytest.mark.parametrize("grid", [0, -1, float("nan"), float("inf")])
def test_invalid_grid_size_rejected(grid):
    with pytest.raises(ValueError, match="grid_size"):
        reduce_precision(LineString([(0, 0), (1, 1)]), grid)


def test_invalid_mode_rejected():
    with pytest.raises(ValueError, match="mode"):
        reduce_precision(LineString([(0, 0), (1, 1)]), 0.1, mode="snap_rounding")


def test_none_geometry_rejected():
    with pytest.raises(ValueError, match="None"):
        fixed_precision_intersection(None, LineString([(0, 0), (1, 1)]), 0.1)
