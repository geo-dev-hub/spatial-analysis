from fractions import Fraction
import pytest
from snap_rounding import snap_round


def test_crossing_segments_share_a_hot_pixel_node():
    result = snap_round([((0, 0), (2, 2)), ((0, 2), (2, 0))])
    assert (1, 1) in result.hot_pixels
    assert (1, 1) in result.polylines[0]
    assert (1, 1) in result.polylines[1]


def test_fractional_intersection_is_found_before_rounding():
    result = snap_round([((0, 0), (3, 3)), ((0, 2), (3, 0))])
    assert (1, 1) in result.hot_pixels
    assert all((1, 1) in line for line in result.polylines)


def test_endpoint_contact_creates_one_shared_hot_pixel():
    result = snap_round([((0, 0), (1, 0)), ((1, 0), (1, 1))])
    assert result.polylines[0][-1] == (1, 0)
    assert result.polylines[1][0] == (1, 0)


def test_collinear_overlap_endpoints_are_arrangement_vertices():
    result = snap_round([((0, 0), (4, 0)), ((1, 0), (3, 0))])
    assert (1, 0) in result.hot_pixels
    assert (3, 0) in result.hot_pixels
    assert (1, 0) in result.polylines[0]
    assert (3, 0) in result.polylines[0]


def test_zero_length_segment_is_treated_as_a_point():
    result = snap_round([((0.2, 0.2), (0.2, 0.2)), ((-1, 0), (1, 0))])
    assert result.polylines[0] == ((0, 0),)
    assert (0, 0) in result.polylines[1]


def test_negative_half_grid_tie_goes_toward_positive_infinity():
    result = snap_round([((-0.5, -0.5), (0.5, 0.5))])
    assert result.polylines[0][0] == (0, 0)
    assert result.polylines[0][-1] == (1, 1)


def test_grid_size_scales_coordinates_not_pixel_indices():
    result = snap_round([((0, 0), (4, 4)), ((0, 4), (4, 0))], grid_size=2)
    assert result.grid_size == Fraction(2)
    assert (1, 1) in result.hot_pixels


def test_noded_edges_keep_source_segment_index():
    result = snap_round([((0, 0), (2, 2)), ((0, 2), (2, 0))])
    assert result.edges
    assert {edge.source_segment for edge in result.edges} == {0, 1}
    assert all(edge.start != edge.end for edge in result.edges)


def test_empty_input_returns_empty_result():
    result = snap_round([])
    assert result.hot_pixels == ()
    assert result.polylines == ()
    assert result.edges == ()


@pytest.mark.parametrize("grid_size", [0, -1, float("nan"), float("inf")])
def test_invalid_grid_size_is_rejected(grid_size):
    with pytest.raises(ValueError, match="grid_size"):
        snap_round([((0, 0), (1, 1))], grid_size=grid_size)


def test_invalid_point_dimensions_are_rejected():
    with pytest.raises(ValueError, match="two coordinates"):
        snap_round([((0,), (1, 1))])


def test_non_finite_coordinate_is_rejected():
    with pytest.raises(ValueError, match="finite"):
        snap_round([((0, 0), (float("inf"), 1))])
