import pytest
from shapely import box
from shapely.geometry import Point, Polygon

from spatial_join import spatial_join


def test_point_within_polygon():
    left = [Point(1, 1)]
    right = [box(0, 0, 2, 2)]
    assert spatial_join(left, right, predicate="within") == [(0, 0)]


def test_boundary_point_intersects_but_is_not_within():
    left = [Point(0, 1)]
    right = [box(0, 0, 2, 2)]
    assert spatial_join(left, right, predicate="intersects") == [(0, 0)]
    assert spatial_join(left, right, predicate="within") == []


def test_one_left_geometry_can_match_multiple_right_geometries():
    left = [Point(1, 1)]
    right = [box(0, 0, 2, 2), box(0.5, 0.5, 1.5, 1.5)]
    assert spatial_join(left, right, predicate="within") == [(0, 0), (0, 1)]


def test_multiple_left_and_right_geometries_preserve_original_indices():
    left = [Point(0.5, 0.5), Point(3, 3), Point(1.5, 1.5)]
    right = [box(0, 0, 1, 1), box(1, 1, 2, 2)]
    assert spatial_join(left, right, predicate="within") == [(0, 0), (2, 1)]


def test_empty_left_or_right_returns_no_pairs():
    assert spatial_join([], [box(0, 0, 1, 1)]) == []
    assert spatial_join([Point(0, 0)], []) == []


def test_empty_geometry_does_not_match():
    left = [Point()]
    right = [box(0, 0, 1, 1)]
    assert spatial_join(left, right, predicate="intersects") == []


def test_predicate_direction_is_left_to_right():
    left = [box(0, 0, 2, 2)]
    right = [Point(1, 1)]
    assert spatial_join(left, right, predicate="contains") == [(0, 0)]
    assert spatial_join(left, right, predicate="within") == []


def test_invalid_predicate_is_rejected():
    with pytest.raises(ValueError):
        spatial_join([Point(0, 0)], [box(0, 0, 1, 1)], predicate="not-a-predicate")


def test_indexed_join_matches_brute_force():
    left = [Point(0.5, 0.5), Point(1.5, 1.5), Point(2.5, 2.5), Point(10, 10)]
    right = [box(0, 0, 2, 2), box(1, 1, 3, 3), box(3, 3, 4, 4)]
    expected = [
        (i, j)
        for i, a in enumerate(left)
        for j, b in enumerate(right)
        if a.within(b)
    ]
    assert spatial_join(left, right, predicate="within") == expected


def test_polygon_with_hole_uses_exact_predicate_after_index_filtering():
    polygon = Polygon(
        [(0, 0), (4, 0), (4, 4), (0, 4), (0, 0)],
        holes=[[(1, 1), (3, 1), (3, 3), (1, 3), (1, 1)]],
    )
    point_in_hole = Point(2, 2)
    point_in_shell = Point(0.5, 0.5)
    assert spatial_join([point_in_hole, point_in_shell], [polygon], predicate="within") == [(1, 0)]
