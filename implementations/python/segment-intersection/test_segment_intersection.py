from fractions import Fraction

import pytest

from segment_intersection import Intersection, orientation, segment_intersection


def test_orientation_signs():
    assert orientation((0, 0), (2, 0), (1, 1)) == 1
    assert orientation((0, 0), (2, 0), (1, -1)) == -1
    assert orientation((0, 0), (2, 0), (1, 0)) == 0


def test_proper_crossing():
    result = segment_intersection((0, 0), (4, 4), (0, 4), (4, 0))
    assert result == Intersection("point", (Fraction(2), Fraction(2)))


def test_rational_intersection_is_exact():
    result = segment_intersection((0, 0), (3, 3), (0, 2), (3, 0))
    assert result == Intersection("point", (Fraction(6, 5), Fraction(6, 5)))


def test_endpoint_touch():
    result = segment_intersection((0, 0), (4, 0), (4, 0), (4, 3))
    assert result == Intersection("point", (Fraction(4), Fraction(0)))


def test_collinear_overlap():
    result = segment_intersection((0, 0), (6, 0), (2, 0), (4, 0))
    assert result == Intersection("overlap", ((2, 0), (4, 0)))


def test_collinear_touch():
    result = segment_intersection((0, 0), (2, 0), (2, 0), (5, 0))
    assert result == Intersection("point", (Fraction(2), Fraction(0)))


def test_collinear_disjoint():
    assert segment_intersection((0, 0), (1, 0), (2, 0), (3, 0)).kind == "none"


def test_parallel_disjoint():
    assert segment_intersection((0, 0), (4, 0), (0, 1), (4, 1)).kind == "none"


def test_vertical_crossing():
    result = segment_intersection((2, -2), (2, 2), (0, 0), (4, 0))
    assert result == Intersection("point", (Fraction(2), Fraction(0)))


def test_reversed_endpoint_order_does_not_change_result():
    forward = segment_intersection((0, 0), (4, 4), (0, 4), (4, 0))
    reversed_result = segment_intersection((4, 4), (0, 0), (4, 0), (0, 4))
    assert forward == reversed_result


def test_zero_length_segment_is_rejected():
    with pytest.raises(ValueError, match="distinct endpoints"):
        segment_intersection((1, 1), (1, 1), (0, 0), (2, 2))
