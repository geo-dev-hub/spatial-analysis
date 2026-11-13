import pytest

from point_in_polygon import PointLocation, locate_point


SQUARE = [(0, 0), (4, 0), (4, 4), (0, 4)]


def test_point_inside_square():
    assert locate_point((2, 2), SQUARE) is PointLocation.INSIDE


def test_point_outside_square():
    assert locate_point((5, 2), SQUARE) is PointLocation.OUTSIDE


@pytest.mark.parametrize("point", [(0, 2), (4, 2), (2, 0), (2, 4), (0, 0)])
def test_point_on_boundary_is_reported_separately(point):
    assert locate_point(point, SQUARE) is PointLocation.BOUNDARY


def test_implicitly_closed_ring():
    assert locate_point((1, 1), SQUARE) is PointLocation.INSIDE


def test_explicitly_closed_ring():
    closed = SQUARE + [SQUARE[0]]
    assert locate_point((1, 1), closed) is PointLocation.INSIDE


def test_concave_polygon():
    concave = [(0, 0), (4, 0), (4, 1), (1, 1), (1, 4), (0, 4)]
    assert locate_point((0.5, 3), concave) is PointLocation.INSIDE
    assert locate_point((3, 3), concave) is PointLocation.OUTSIDE


def test_ray_through_concave_vertex_uses_half_open_crossing_rule():
    concave = [(0, 0), (4, 0), (4, 4), (2, 2), (0, 4)]
    # The horizontal ray from (1, 2) passes through the concave vertex (2, 2).
    assert locate_point((1, 2), concave) is PointLocation.INSIDE
    assert locate_point((5, 2), concave) is PointLocation.OUTSIDE


def test_ring_requires_three_distinct_vertices():
    with pytest.raises(ValueError, match="three distinct"):
        locate_point((0, 0), [(0, 0), (1, 1), (0, 0)])
