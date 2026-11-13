import pytest

from proximity_graphs import (
    euclidean_mst,
    gabriel_graph,
    relative_neighborhood_graph,
)


SQUARE = [(0, 0), (1, 0), (1, 1), (0, 1)]


def test_gabriel_graph_keeps_square_sides_not_diagonals():
    edges = gabriel_graph(SQUARE)
    assert len(edges) == 4
    assert (0, 1) in edges and (0, 3) in edges
    assert (0, 2) not in edges


def test_rng_is_subset_of_gabriel_graph_for_fixture():
    gabriel = set(gabriel_graph(SQUARE))
    rng = set(relative_neighborhood_graph(SQUARE))
    assert rng <= gabriel


def test_rng_blocks_long_edge_with_intermediate_point():
    points = [(0, 0), (2, 0), (1, 0.1)]
    assert (0, 1) not in relative_neighborhood_graph(points)


def test_mst_has_n_minus_one_edges_and_connects_points():
    points = [(0, 0), (2, 0), (2, 2), (0, 2)]
    edges = euclidean_mst(points)
    assert len(edges) == len(points) - 1
    assert sum(edge[2] for edge in edges) == pytest.approx(6.0)


def test_mst_empty_and_singleton():
    assert euclidean_mst([]) == []
    assert euclidean_mst([(1, 2)]) == []


@pytest.mark.parametrize("function", [
    gabriel_graph, relative_neighborhood_graph, euclidean_mst
])
def test_duplicate_points_rejected(function):
    with pytest.raises(ValueError):
        function([(0, 0), (0, 0)])


@pytest.mark.parametrize("function", [
    gabriel_graph, relative_neighborhood_graph, euclidean_mst
])
def test_non_finite_points_rejected(function):
    with pytest.raises(ValueError):
        function([(0, 0), (1, float("inf"))])
