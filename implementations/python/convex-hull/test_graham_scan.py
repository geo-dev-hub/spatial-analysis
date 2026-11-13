import pytest
from graham_scan import convex_hull


def test_square_returns_counter_clockwise_extreme_vertices():
    points = [(0, 0), (2, 0), (2, 2), (0, 2), (1, 1)]
    assert convex_hull(points) == [(0.0, 0.0), (2.0, 0.0), (2.0, 2.0), (0.0, 2.0)]


def test_interior_points_are_excluded():
    points = [(0, 0), (4, 0), (4, 4), (0, 4), (1, 1), (2, 2), (3, 1)]
    assert len(convex_hull(points)) == 4


def test_collinear_points_on_edges_are_omitted():
    points = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2),
              (1, 2), (0, 2), (0, 1), (1, 1)]
    assert convex_hull(points) == [(0.0, 0.0), (2.0, 0.0), (2.0, 2.0), (0.0, 2.0)]


def test_all_collinear_returns_only_two_extremes():
    points = [(3, 3), (0, 0), (1, 1), (2, 2), (4, 4)]
    assert convex_hull(points) == [(0.0, 0.0), (4.0, 4.0)]


def test_duplicate_points_are_removed():
    assert convex_hull([(0, 0), (1, 0), (0, 1), (0, 0), (1, 0)]) == [
        (0.0, 0.0), (1.0, 0.0), (0.0, 1.0)
    ]


def test_empty_input_returns_empty_list():
    assert convex_hull([]) == []


def test_one_point_returns_that_point():
    assert convex_hull([(3, 7)]) == [(3.0, 7.0)]


def test_two_points_return_both_points():
    assert convex_hull([(2, 2), (0, 0)]) == [(0.0, 0.0), (2.0, 2.0)]


def test_triangle_orientation_is_counter_clockwise():
    result = convex_hull([(0, 0), (2, 0), (1, 3)])
    area2 = sum(result[i][0] * result[(i + 1) % len(result)][1]
                - result[(i + 1) % len(result)][0] * result[i][1]
                for i in range(len(result)))
    assert area2 > 0


@pytest.mark.parametrize("bad", [(float("nan"), 0), (0, float("inf")), (float("-inf"), 1)])
def test_non_finite_coordinates_are_rejected(bad):
    with pytest.raises(ValueError, match="finite"):
        convex_hull([(0, 0), (1, 0), (0, 1), bad])


def test_pivot_uses_lowest_y_then_lowest_x():
    points = [(2, 0), (0, 0), (1, 2), (2, 2)]
    assert convex_hull(points)[0] == (0.0, 0.0)
