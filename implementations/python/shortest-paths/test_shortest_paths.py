import math
import pytest

from shortest_paths import astar, bellman_ford, dijkstra, floyd_warshall


GRAPH = {
    "A": [("B", 2), ("C", 1)],
    "B": [("D", 2)],
    "C": [("B", 0.5), ("D", 8)],
    "D": [],
}


def test_dijkstra_returns_lowest_cost_path():
    path, cost = dijkstra(GRAPH, "A", "D")
    assert path == ["A", "C", "B", "D"]
    assert cost == pytest.approx(3.5)


def test_astar_with_zero_heuristic_matches_dijkstra():
    zero = lambda _node, _goal: 0
    assert astar(GRAPH, "A", "D", zero) == dijkstra(GRAPH, "A", "D")


def test_astar_with_admissible_heuristic_returns_optimum():
    coordinates = {"A": (0, 0), "B": (2, 0), "C": (1, 0), "D": (3, 0)}
    heuristic = lambda node, goal: abs(coordinates[node][0] - coordinates[goal][0])
    path, cost = astar(GRAPH, "A", "D", heuristic)
    assert path == ["A", "C", "B", "D"]
    assert cost == pytest.approx(3.5)


def test_unreachable_goal_returns_none_and_infinity():
    path, cost = dijkstra({"A": [("B", 1)], "B": []}, "A", "Z")
    assert path is None and math.isinf(cost)


def test_start_equals_goal():
    assert dijkstra(GRAPH, "A", "A") == (["A"], 0.0)


@pytest.mark.parametrize("weight", [-1, float("nan"), float("inf")])
def test_invalid_edge_weights_rejected(weight):
    with pytest.raises(ValueError):
        dijkstra({"A": [("B", weight)]}, "A", "B")


def test_invalid_heuristic_rejected_when_node_is_expanded():
    with pytest.raises(ValueError):
        astar({"A": [("B", 1)], "B": []}, "A", "B",
              lambda node, _goal: -1 if node == "B" else 0)


def test_invalid_start_heuristic_rejected_even_when_start_is_goal():
    with pytest.raises(ValueError):
        astar({"A": []}, "A", "A", lambda _node, _goal: float("nan"))


def test_bellman_ford_supports_negative_edges_without_negative_cycles():
    graph = {
        "A": [("B", 4), ("C", 5)],
        "B": [("D", 2)],
        "C": [("B", -3)],
        "D": [],
    }
    path, cost = bellman_ford(graph, "A", "D")
    assert path == ["A", "C", "B", "D"]
    assert cost == pytest.approx(4.0)


def test_bellman_ford_detects_reachable_negative_cycle():
    graph = {"A": [("B", 1)], "B": [("A", -2)]}
    with pytest.raises(ValueError, match="negative-weight cycle"):
        bellman_ford(graph, "A", "B")


def test_floyd_warshall_computes_all_pairs_distances():
    graph = {"A": [("B", 3), ("C", 10)], "B": [("C", 2)], "C": []}
    distance = floyd_warshall(graph)
    assert distance[("A", "C")] == pytest.approx(5)
    assert distance[("C", "A")] == float("inf")
    assert distance[("B", "B")] == 0


def test_floyd_warshall_detects_negative_cycle():
    graph = {"A": [("B", 1)], "B": [("A", -2)]}
    with pytest.raises(ValueError, match="negative-weight cycle"):
        floyd_warshall(graph)


def test_bellman_ford_handles_missing_source_and_target_keys():
    assert bellman_ford({}, "source", "target") == (None, float("inf"))
