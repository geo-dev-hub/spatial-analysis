import math

import pytest

from dijkstra import dijkstra


def test_finds_least_cost_path_not_fewest_edges():
    graph = {
        "S": [("A", 4), ("B", 2)],
        "B": [("A", 1), ("C", 5), ("T", 9)],
        "A": [("C", 3), ("T", 7)],
        "C": [("T", 1)],
        "T": [],
    }
    result = dijkstra(graph, "S")
    assert result.distances["T"] == 7
    assert result.path_to("T") == ["S", "B", "A", "C", "T"]


def test_returns_distances_to_all_reachable_nodes():
    result = dijkstra({"s": [("a", 2), ("b", 5)], "a": [("b", 1)], "b": []}, "s")
    assert result.distances == {"s": 0.0, "a": 2.0, "b": 3.0}


def test_unreachable_node_has_infinite_distance_and_no_path():
    result = dijkstra({"s": [("a", 1)], "a": [], "isolated": []}, "s")
    assert math.isinf(result.distances["isolated"])
    assert result.path_to("isolated") is None


def test_zero_weight_edges_are_supported():
    result = dijkstra({"s": [("a", 0)], "a": [("b", 0)], "b": []}, "s")
    assert result.distances["b"] == 0
    assert result.path_to("b") == ["s", "a", "b"]


def test_directed_edges_are_followed_only_in_the_given_direction():
    result = dijkstra({"a": [("b", 2)], "b": []}, "b")
    assert result.path_to("a") is None


def test_undirected_graph_requires_both_adjacency_entries():
    graph = {"a": [("b", 3)], "b": [("a", 3)]}
    assert dijkstra(graph, "a").path_to("b") == ["a", "b"]
    assert dijkstra(graph, "b").path_to("a") == ["b", "a"]


def test_duplicate_edges_keep_the_lowest_cost_route():
    result = dijkstra({"s": [("a", 9), ("a", 2)], "a": []}, "s")
    assert result.distances["a"] == 2
    assert result.path_to("a") == ["s", "a"]


def test_non_orderable_nodes_are_supported():
    a, b, c = object(), object(), object()
    result = dijkstra({a: [(b, 1), (c, 1)], b: [], c: []}, a)
    assert result.distances[b] == 1
    assert result.distances[c] == 1


def test_path_to_source_is_source_only():
    result = dijkstra({"s": [("a", 2)], "a": []}, "s")
    assert result.path_to("s") == ["s"]


def test_unknown_source_is_rejected():
    with pytest.raises(KeyError, match="not in the graph"):
        dijkstra({"a": []}, "missing")


@pytest.mark.parametrize("weight", [-1, float("nan"), float("inf"), -float("inf")])
def test_negative_or_non_finite_weights_are_rejected(weight):
    with pytest.raises(ValueError, match="finite and non-negative"):
        dijkstra({"s": [("a", weight)], "a": []}, "s")


def test_float_weights_are_accumulated():
    result = dijkstra({"s": [("a", 0.25)], "a": [("b", 0.5)], "b": []}, "s")
    assert result.distances["b"] == 0.75


def test_equal_cost_alternatives_keep_first_discovered_predecessor():
    graph = {"s": [("a", 1), ("b", 1)], "a": [("t", 1)], "b": [("t", 1)], "t": []}
    result = dijkstra(graph, "s")
    assert result.distances["t"] == 2
    assert result.path_to("t") == ["s", "a", "t"]
