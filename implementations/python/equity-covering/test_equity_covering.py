import math
import pytest
from equity_covering import equity_maximal_covering


def test_equity_floor_changes_selected_facilities():
    costs = [[1, 9, 8], [1, 8, 9], [9, 1, 8], [9, 1, 8]]
    groups = ["A", "A", "B", "B"]
    plain = equity_maximal_covering(costs, groups, {"A": 0, "B": 0}, 1, 2)
    fair = equity_maximal_covering(costs, groups, {"A": .5, "B": .5}, 1, 2)
    assert plain["selected_facilities"] == (0,)
    assert fair["selected_facilities"] == (0, 1)
    assert fair["group_coverage"] == {"A": 1.0, "B": 1.0}


def test_weighted_group_floor():
    result = equity_maximal_covering(
        [[1, 9], [9, 1], [9, 1]], ["A", "B", "B"], {"A": 1, "B": .5},
        1, 2, demand_weights=[10, 2, 2],
    )
    assert result["group_coverage"]["A"] == 1
    assert result["group_coverage"]["B"] == .5


def test_objective_weights_are_separate_from_population_floor():
    result = equity_maximal_covering(
        [[1, 9], [9, 1]], ["A", "B"], {"A": 1, "B": 1},
        2, 2, demand_weights=[10, 10], objective_weights=[1, 5],
    )
    assert result["objective"] == 6


def test_infeasible_floor_raises():
    with pytest.raises(ValueError, match="no facility set"):
        equity_maximal_covering([[1, 9], [9, 1]], ["A", "B"], {"A": 1, "B": 1}, 1, 2)


def test_positive_infinity_means_unreachable():
    result = equity_maximal_covering([[math.inf, 1]], ["A"], {"A": 1}, 1, 2)
    assert result["selected_facilities"] == (1,)


def test_at_most_p_and_deterministic_tie():
    result = equity_maximal_covering([[1, 1]], ["A"], {"A": 1}, 2, 2)
    assert result["selected_facilities"] == (0,)


def test_zero_facility_allowed_only_if_floors_allow():
    result = equity_maximal_covering([[1]], ["A"], {"A": 0}, 0, 2)
    assert result["selected_facilities"] == ()
    with pytest.raises(ValueError):
        equity_maximal_covering([[1]], ["A"], {"A": .1}, 0, 2)


def test_invalid_matrix_and_group_contracts():
    with pytest.raises(ValueError):
        equity_maximal_covering([], [], {}, 0, 1)
    with pytest.raises(ValueError):
        equity_maximal_covering([[1], [1, 2]], ["A", "A"], {"A": 1}, 1, 2)
    with pytest.raises(ValueError):
        equity_maximal_covering([[math.nan]], ["A"], {"A": 1}, 1, 2)
    with pytest.raises(ValueError):
        equity_maximal_covering([[1]], ["A"], {"B": 1}, 1, 2)


def test_invalid_parameters_and_weights():
    with pytest.raises(ValueError):
        equity_maximal_covering([[1]], ["A"], {"A": 1.1}, 1, 2)
    with pytest.raises(ValueError):
        equity_maximal_covering([[1]], ["A"], {"A": 1}, -1, 2)
    with pytest.raises(ValueError):
        equity_maximal_covering([[1]], ["A"], {"A": 1}, 1, -1)
    with pytest.raises(ValueError):
        equity_maximal_covering([[1]], ["A"], {"A": 1}, 1, 2, demand_weights=[0])
