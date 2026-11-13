import math
import random

import pytest

from kd_tree import KDTree2D


def brute_force(points, query):
    if not points:
        return None
    ranked = []
    for index, (x, y) in enumerate(points):
        distance_sq = (x - query[0]) ** 2 + (y - query[1]) ** 2
        ranked.append((distance_sq, index))
    distance_sq, index = min(ranked)
    return index, distance_sq


def test_empty_tree_returns_none():
    assert KDTree2D([]).nearest((0, 0)) is None


def test_single_point():
    tree = KDTree2D([(3, 4)])
    assert tree.nearest((0, 0)) == (0, 25.0)


def test_query_outside_data_extent():
    points = [(0, 0), (2, 0), (4, 0)]
    assert KDTree2D(points).nearest((100, 0)) == (2, 96**2)


def test_duplicate_points_use_lowest_original_index():
    tree = KDTree2D([(1, 1), (1, 1), (2, 2)])
    assert tree.nearest((1, 1)) == (0, 0.0)


def test_equidistant_points_use_lowest_original_index():
    tree = KDTree2D([(-1, 0), (1, 0), (0, 3)])
    assert tree.nearest((0, 0)) == (0, 1.0)


def test_split_plane_query_is_exact():
    points = [(0, 0), (2, 0), (1, 1), (1, -1)]
    assert KDTree2D(points).nearest((1, 0)) == (0, 1.0)


def test_rejects_wrong_dimension_and_non_finite_values():
    with pytest.raises(ValueError):
        KDTree2D([(1, 2, 3)])
    with pytest.raises(ValueError):
        KDTree2D([(math.inf, 0)])
    with pytest.raises(ValueError):
        KDTree2D([(0, 0)]).nearest((math.nan, 1))


def test_random_queries_match_brute_force():
    rng = random.Random(20261113)
    for size in (1, 2, 3, 10, 50, 200):
        points = [
            (rng.uniform(-100, 100), rng.uniform(-100, 100))
            for _ in range(size)
        ]
        # Include repeated coordinates to exercise deterministic tie handling.
        if size >= 3:
            points[1] = points[0]
        tree = KDTree2D(points)
        for _ in range(100):
            query = (rng.uniform(-120, 120), rng.uniform(-120, 120))
            assert tree.nearest(query) == brute_force(points, query)


def test_clustered_and_anisotropic_data_match_brute_force():
    points = [(i / 1000, i * 0.001) for i in range(-500, 501)]
    tree = KDTree2D(points)
    for query in [(-2, 0), (0, 0), (0.2, 0.2), (5, 4)]:
        assert tree.nearest(query) == brute_force(points, query)
