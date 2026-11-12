import random

import pytest

from str_packed_rtree import STRPackedRTree, _intersects


def test_empty_tree_returns_no_matches():
    tree = STRPackedRTree([])
    assert len(tree) == 0
    assert tree.query((0, 0, 1, 1)) == []


def test_single_box_is_returned_when_intersecting():
    tree = STRPackedRTree([(0, 0, 2, 2)])
    assert tree.query((1, 1, 3, 3)) == [0]


def test_non_intersecting_query_returns_empty():
    tree = STRPackedRTree([(0, 0, 1, 1), (3, 3, 4, 4)])
    assert tree.query((1.1, 1.1, 2, 2)) == []


def test_boundary_touch_counts_as_intersection():
    tree = STRPackedRTree([(0, 0, 1, 1)])
    assert tree.query((1, 0.25, 2, 0.75)) == [0]


def test_query_returns_original_input_indices_in_sorted_order():
    bounds = [(5, 5, 6, 6), (0, 0, 2, 2), (1, 1, 3, 3)]
    tree = STRPackedRTree(bounds, node_capacity=2)
    assert tree.query((0.5, 0.5, 2.5, 2.5)) == [1, 2]


def test_overlapping_boxes_all_returned():
    bounds = [(0, 0, 2, 2), (1, 1, 3, 3), (2, 2, 4, 4)]
    tree = STRPackedRTree(bounds, node_capacity=2)
    assert tree.query((1.5, 1.5, 2.5, 2.5)) == [0, 1, 2]


def test_results_match_brute_force_for_random_boxes():
    rng = random.Random(20261113)
    bounds = []
    for _ in range(300):
        x, y = rng.uniform(-100, 100), rng.uniform(-100, 100)
        width, height = rng.uniform(0, 15), rng.uniform(0, 15)
        bounds.append((x, y, x + width, y + height))

    queries = []
    for _ in range(60):
        x, y = rng.uniform(-100, 100), rng.uniform(-100, 100)
        width, height = rng.uniform(0, 25), rng.uniform(0, 25)
        queries.append((x, y, x + width, y + height))

    for capacity in (2, 3, 4, 8, 10):
        tree = STRPackedRTree(bounds, node_capacity=capacity)
        for query in queries:
            expected = [i for i, item in enumerate(bounds) if _intersects(item, query)]
            assert tree.query(query) == expected


def test_invalid_node_capacity_is_rejected():
    with pytest.raises(ValueError, match="at least 2"):
        STRPackedRTree([(0, 0, 1, 1)], node_capacity=1)


@pytest.mark.parametrize(
    "bounds",
    [
        (0, 0, 1),
        (0, 2, 1, 1),
        (0, 0, float("inf"), 1),
        (0, 0, float("nan"), 1),
    ],
)
def test_invalid_stored_bounds_are_rejected(bounds):
    with pytest.raises(ValueError):
        STRPackedRTree([bounds])


def test_invalid_query_bounds_are_rejected():
    tree = STRPackedRTree([(0, 0, 1, 1)])
    with pytest.raises(ValueError):
        tree.query((2, 2, 1, 1))


def test_tree_keeps_all_input_items():
    bounds = [(i, i, i + 0.5, i + 0.5) for i in range(25)]
    tree = STRPackedRTree(bounds, node_capacity=3)
    assert len(tree) == len(bounds)
    assert tree.query((-1, -1, 30, 30)) == list(range(25))
