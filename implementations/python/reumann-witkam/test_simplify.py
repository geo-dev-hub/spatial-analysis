import math
import pytest
from simplify import reumann_witkam

def test_straight_line_reduces_to_endpoints():
    pts = [(0, 0), (1, 0.1), (2, -0.1), (3, 0)]
    assert reumann_witkam(pts, 0.2) == [(0.0, 0.0), (3.0, 0.0)]

def test_deviation_retains_vertex_before_strip_exit():
    pts = [(0, 0), (1, 0), (2, 1), (3, 1)]
    result = reumann_witkam(pts, 0.25)
    assert result[0] == (0.0, 0.0) and result[-1] == (3.0, 1.0)
    assert (1.0, 0.0) in result

def test_two_points_are_unchanged():
    assert reumann_witkam([(0, 0), (1, 1)], 0.5) == [(0.0, 0.0), (1.0, 1.0)]

def test_zero_tolerance_preserves_all_vertices():
    pts = [(0, 0), (1, 0), (2, 1)]
    assert reumann_witkam(pts, 0) == [(0.0, 0.0), (1.0, 0.0), (2.0, 1.0)]

def test_duplicate_vertices_do_not_crash():
    result = reumann_witkam([(0, 0), (0, 0), (1, 0), (2, 0)], 0.1)
    assert result[0] == (0.0, 0.0) and result[-1] == (2.0, 0.0)

@pytest.mark.parametrize("tolerance", [-1, math.inf, math.nan])
def test_invalid_tolerance_rejected(tolerance):
    with pytest.raises(ValueError):
        reumann_witkam([(0, 0), (1, 1)], tolerance)

@pytest.mark.parametrize("coordinates", [[(0, 0), (math.inf, 1)], [(0, 0), (math.nan, 1)], [(0, 0, 0), (1, 1, 1)]])
def test_invalid_coordinates_rejected(coordinates):
    with pytest.raises(ValueError):
        reumann_witkam(coordinates, 0.1)

def test_boolean_tolerance_rejected():
    with pytest.raises(TypeError):
        reumann_witkam([(0, 0), (1, 1)], True)
