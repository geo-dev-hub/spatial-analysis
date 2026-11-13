import math

import pytest

from graham_scan import cross, graham_scan


def test_returns_expected_counter_clockwise_hull():
    points = [(0, 0), (2, 0), (3, 1), (2, 2), (0, 2), (1, 1)]
    assert graham_scan(points) == [
        (0.0, 0.0), (2.0, 0.0), (3.0, 1.0), (2.0, 2.0), (0.0, 2.0)
    ]


def test_ignores_interior_points():
    assert graham_scan([(0, 0), (4, 0), (4, 4), (0, 4), (2, 2)]) == [
        (0.0, 0.0), (4.0, 0.0), (4.0, 4.0), (0.0, 4.0)
    ]


def test_removes_duplicate_points():
    assert graham_scan([(0, 0), (1, 0), (1, 0), (0, 1), (0, 0)]) == [
        (0.0, 0.0), (1.0, 0.0), (0.0, 1.0)
    ]


def test_fully_collinear_points_return_extreme_endpoints():
    assert graham_scan([(0, 0), (1, 1), (2, 2), (3, 3)]) == [
        (0.0, 0.0), (3.0, 3.0)
    ]


def test_collinear_points_on_one_hull_edge_are_omitted():
    assert graham_scan([(0, 0), (1, 0), (2, 0), (2, 2), (0, 2)]) == [
        (0.0, 0.0), (2.0, 0.0), (2.0, 2.0), (0.0, 2.0)
    ]


def test_empty_and_small_inputs():
    assert graham_scan([]) == []
    assert graham_scan([(2, 3)]) == [(2.0, 3.0)]
    assert graham_scan([(2, 3), (1, 4)]) == [(1.0, 4.0), (2.0, 3.0)]


def test_anchor_tie_uses_leftmost_point():
    assert graham_scan([(1, 0), (0, 0), (2, 1), (0, 2)]) == [
        (0.0, 0.0), (1.0, 0.0), (2.0, 1.0), (0.0, 2.0)
    ]


def test_same_ray_keeps_farthest_point():
    assert graham_scan([(0, 0), (1, 1), (2, 2), (2, 0), (0, 2)]) == [
        (0.0, 0.0), (2.0, 0.0), (2.0, 2.0), (0.0, 2.0)
    ]


def test_hull_is_counter_clockwise():
    hull = graham_scan([(0, 0), (3, 0), (3, 2), (0, 2), (1, 1)])
    signed_area_twice = sum(
        hull[i][0] * hull[(i + 1) % len(hull)][1]
        - hull[(i + 1) % len(hull)][0] * hull[i][1]
        for i in range(len(hull))
    )
    assert signed_area_twice > 0


def test_cross_product_orientation():
    assert cross((0, 0), (1, 0), (1, 1)) == 1
    assert cross((0, 0), (1, 0), (1, -1)) == -1
    assert cross((0, 0), (1, 1), (2, 2)) == 0


@pytest.mark.parametrize("points", [
    [(0, 0), (math.inf, 1)],
    [(0, 0), (math.nan, 1)],
    [(0, 0), (1, -math.inf)],
])
def test_rejects_non_finite_coordinates(points):
    with pytest.raises(ValueError, match="finite"):
        graham_scan(points)


def test_rejects_points_with_wrong_coordinate_count():
    with pytest.raises((ValueError, TypeError)):
        graham_scan([(0, 0, 1)])
