import pytest

from proximity_graphs import (
    beta_skeleton,
    delaunay_filtered_gabriel_graph,
    delaunay_filtered_rng,
    euclidean_mst,
    gabriel_graph,
    relative_neighborhood_graph,
    yao_graph,
)


SQUARE = [(0, 0), (1, 0), (1, 1), (0, 1)]


def test_gabriel_graph_open_disk_convention_keeps_square_diagonal_ties():
    edges = gabriel_graph(SQUARE)
    # The other square corners lie on the diameter-circle boundary, not inside it.
    assert len(edges) == 6
    assert (0, 1) in edges and (0, 3) in edges
    assert (0, 2) in edges


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


def test_beta_skeleton_endpoints_match_gabriel_and_rng_definitions():
    assert beta_skeleton(SQUARE, 1.0) == gabriel_graph(SQUARE)
    assert beta_skeleton(SQUARE, 2.0) == relative_neighborhood_graph(SQUARE)


def test_beta_skeleton_rejects_out_of_scope_beta():
    with pytest.raises(ValueError):
        beta_skeleton(SQUARE, 2.5)


def test_yao_graph_returns_valid_undirected_edges():
    points = [(0, 0), (2, 0), (2, 2), (0, 2), (1, 1)]
    edges = yao_graph(points, cones=4)
    assert edges
    assert all(i < j and 0 <= i < len(points) and 0 <= j < len(points)
               for i, j in edges)
    assert edges == sorted(set(edges))


def test_yao_graph_rejects_invalid_cone_count():
    with pytest.raises(ValueError):
        yao_graph(SQUARE, cones=2)


GENERAL_POSITION = [(0, 0), (4, 0), (5, 3), (2, 5), (-1, 3), (1, 2)]


def test_delaunay_filtered_gabriel_matches_all_pairs_on_general_position_fixture():
    assert delaunay_filtered_gabriel_graph(GENERAL_POSITION) == gabriel_graph(GENERAL_POSITION)


def test_delaunay_filtered_rng_matches_all_pairs_on_general_position_fixture():
    assert delaunay_filtered_rng(GENERAL_POSITION) == relative_neighborhood_graph(GENERAL_POSITION)


@pytest.mark.parametrize("function", [delaunay_filtered_gabriel_graph, delaunay_filtered_rng])
def test_delaunay_filtered_variants_reject_collinear_sites(function):
    with pytest.raises(ValueError, match="collinear"):
        function([(0, 0), (1, 1), (2, 2), (3, 3)])


@pytest.mark.parametrize("function", [delaunay_filtered_gabriel_graph, delaunay_filtered_rng])
def test_delaunay_filtered_variants_require_three_sites(function):
    with pytest.raises(ValueError, match="three points"):
        function([(0, 0), (1, 0)])
