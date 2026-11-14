import math
import pytest

from road_routing import earliest_arrival, turn_aware_shortest_path


def test_turn_restriction_forces_alternative_route():
    edges = [
        ("ab", "A", "B", 1),
        ("bd", "B", "D", 1),
        ("bc", "B", "C", 2),
        ("cd", "C", "D", 1),
    ]
    path, cost = turn_aware_shortest_path(
        edges, "A", "D", prohibited_turns={("ab", "bd")}
    )
    assert path == ["ab", "bc", "cd"]
    assert cost == pytest.approx(4)


def test_turn_penalty_changes_best_route():
    edges = [
        ("ab", "A", "B", 1),
        ("bd", "B", "D", 1),
        ("bc", "B", "C", 1.5),
        ("cd", "C", "D", 1),
    ]
    path, cost = turn_aware_shortest_path(
        edges, "A", "D", turn_penalties={("ab", "bd"): 2}
    )
    assert path == ["ab", "bc", "cd"]
    assert cost == pytest.approx(3.5)


def test_no_turn_rules_matches_node_graph_shortest_path_cost():
    edges = [("ab", "A", "B", 2), ("bc", "B", "C", 3)]
    assert turn_aware_shortest_path(edges, "A", "C") == (["ab", "bc"], 5)


def test_unreachable_and_start_equals_goal():
    assert turn_aware_shortest_path([], "A", "B") == (None, math.inf)
    assert turn_aware_shortest_path([], "A", "A") == ([], 0.0)


def test_duplicate_edge_ids_rejected():
    with pytest.raises(ValueError, match="unique"):
        turn_aware_shortest_path([("e", "A", "B", 1), ("e", "B", "C", 1)], "A", "C")


def test_invalid_turn_penalty_rejected():
    with pytest.raises(ValueError, match="turn penalties"):
        turn_aware_shortest_path(
            [("ab", "A", "B", 1), ("bc", "B", "C", 1)],
            "A", "C", turn_penalties={("ab", "bc"): -1}
        )


def test_fifo_earliest_arrival_uses_departure_time_at_each_edge():
    graph = {"A": [("B", "ab")], "B": [("C", "bc")], "C": []}
    durations = {"ab": lambda t: 5.0, "bc": lambda t: 2.0 + 0.1 * t}
    path, arrival = earliest_arrival(
        graph, "A", "C", 0.0, lambda edge, t: durations[edge](t)
    )
    assert path == ["A", "B", "C"]
    assert arrival == pytest.approx(7.5)


def test_earliest_arrival_returns_absolute_time_not_elapsed_duration():
    graph = {"A": [("B", "ab")], "B": []}
    path, arrival = earliest_arrival(graph, "A", "B", 10.0, lambda _edge, _t: 3.0)
    assert path == ["A", "B"]
    assert arrival == pytest.approx(13.0)


def test_time_dependent_unreachable_goal():
    assert earliest_arrival({}, "A", "B", 0, lambda _edge, _t: 1) == (None, math.inf)


def test_invalid_time_or_travel_time_rejected():
    graph = {"A": [("B", "ab")], "B": []}
    with pytest.raises(ValueError, match="departure_time"):
        earliest_arrival(graph, "A", "B", math.inf, lambda _edge, _t: 1)
    with pytest.raises(ValueError, match="travel times"):
        earliest_arrival(graph, "A", "B", 0, lambda _edge, _t: -1)
