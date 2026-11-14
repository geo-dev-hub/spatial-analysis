import math
import random

import pytest

from quadtree import PointRegionQuadtree


def brute_force(points, window):
    min_x, min_y, max_x, max_y = window
    return [i for i, (x, y) in enumerate(points)
            if min_x <= x <= max_x and min_y <= y <= max_y]


def test_empty_tree_and_full_extent_query():
    tree = PointRegionQuadtree((0, 0, 10, 10), capacity=1)
    assert len(tree) == 0
    assert tree.query((0, 0, 10, 10)) == []


def test_midline_ties_and_inclusive_queries():
    points = [(5, 5), (5, 2), (2, 5), (5, 8), (8, 5)]
    tree = PointRegionQuadtree((0, 0, 10, 10), points, capacity=1)
    assert tree.query((5, 5, 5, 5)) == [0]
    assert tree.query((5, 0, 5, 10)) == [0, 1, 3]
    assert tree.query((0, 5, 10, 5)) == [0, 2, 4]


def test_outer_boundary_points_are_included():
    points = [(0, 0), (0, 10), (10, 0), (10, 10)]
    tree = PointRegionQuadtree((0, 0, 10, 10), points, capacity=1)
    assert tree.query((0, 0, 10, 10)) == [0, 1, 2, 3]
    assert tree.query((10, 10, 10, 10)) == [3]


def test_duplicate_points_stop_at_max_depth():
    points = [(4, 4)] * 20
    tree = PointRegionQuadtree((0, 0, 8, 8), points, capacity=2, max_depth=5)
    assert tree.query((4, 4, 4, 4)) == list(range(20))
    assert tree.depth <= 5
    assert tree.node_count > 1


def test_max_depth_zero_keeps_root_as_leaf():
    points = [(1, 1), (2, 2), (3, 3)]
    tree = PointRegionQuadtree((0, 0, 10, 10), points, capacity=1, max_depth=0)
    assert tree.node_count == 1
    assert tree.depth == 0
    assert tree.query((0, 0, 10, 10)) == [0, 1, 2]


def test_out_of_extent_insert_does_not_consume_id():
    tree = PointRegionQuadtree((0, 0, 10, 10))
    with pytest.raises(ValueError):
        tree.insert((11, 5))
    assert tree.insert((10, 10)) == 0


def test_invalid_inputs_are_rejected():
    with pytest.raises(ValueError):
        PointRegionQuadtree((0, 0, 0, 10))
    with pytest.raises(ValueError):
        PointRegionQuadtree((0, 0, 10, 10), capacity=0)
    with pytest.raises(ValueError):
        PointRegionQuadtree((0, 0, 10, 10), max_depth=-1)
    with pytest.raises(ValueError):
        PointRegionQuadtree((0, 0, 10, 10), [(math.nan, 1)])
    with pytest.raises(ValueError):
        PointRegionQuadtree((0, 0, 10, 10)).query((2, 2, 1, 3))


def test_query_outside_extent_returns_empty():
    tree = PointRegionQuadtree((0, 0, 10, 10), [(1, 1), (9, 9)])
    assert tree.query((20, 20, 30, 30)) == []


def test_random_queries_match_brute_force():
    rng = random.Random(20261113)
    for size in (1, 2, 10, 50, 250):
        points = [(rng.uniform(0, 100), rng.uniform(0, 100)) for _ in range(size)]
        if size >= 3:
            points[1] = points[0]
        tree = PointRegionQuadtree((0, 0, 100, 100), points, capacity=5, max_depth=12)
        for _ in range(80):
            x1, x2 = sorted((rng.uniform(-10, 110), rng.uniform(-10, 110)))
            y1, y2 = sorted((rng.uniform(-10, 110), rng.uniform(-10, 110)))
            window = (x1, y1, x2, y2)
            assert tree.query(window) == brute_force(points, window)


def test_clustered_points_and_thin_windows_match_brute_force():
    points = [(5 + i / 10000, 5 + i / 20000) for i in range(500)]
    points += [(i, 9.5) for i in range(11)]
    tree = PointRegionQuadtree((0, 0, 10, 10), points, capacity=3, max_depth=16)
    for window in [(5, 5, 5.01, 5.01), (0, 9.5, 10, 9.5),
                   (4.99, 4.99, 5.02, 5.02), (0, 0, 10, 10)]:
        assert tree.query(window) == brute_force(points, window)


def test_subdivision_stops_when_float_midpoint_collapses():
    hi = math.nextafter(1.0, math.inf)
    tree = PointRegionQuadtree((1.0, 1.0, hi, hi), [(1.0, 1.0), (hi, hi)],
                               capacity=1, max_depth=100)
    assert tree.query(tree.extent) == [0, 1]
    assert tree.depth == 0
