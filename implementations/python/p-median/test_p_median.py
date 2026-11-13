import numpy as np
import pytest

from p_median import solve_p_median


def test_exact_p_median_finds_best_two_facilities():
    costs = np.array([[2, 8, 5, 9], [7, 3, 4, 8], [6, 7, 2, 4]])
    facilities, objective, assignment = solve_p_median(costs, 2)
    assert facilities == (0, 2)
    assert objective == pytest.approx(7)
    assert assignment == (0, 2, 2)


def test_demand_weights_change_the_selected_facilities():
    costs = [[0, 5, 9], [5, 0, 9], [9, 9, 0]]
    unweighted = solve_p_median(costs, 1)
    weighted = solve_p_median(costs, 1, demand_weights=[10, 1, 1])
    assert unweighted[0] == (0,)
    assert weighted[0] == (0,)


def test_assignment_ties_are_deterministic():
    facilities, objective, assignment = solve_p_median([[1, 1, 5]], 1)
    assert facilities == (0,)
    assert objective == pytest.approx(1)
    assert assignment == (0,)


def test_p_equal_to_all_candidates_opens_all():
    facilities, objective, assignment = solve_p_median([[1, 4], [3, 2]], 2)
    assert facilities == (0, 1)
    assert objective == pytest.approx(3)
    assert assignment == (0, 1)


@pytest.mark.parametrize("p", [0, -1, 3, 1.5, True])
def test_invalid_p_rejected(p):
    with pytest.raises(ValueError, match="p must"):
        solve_p_median([[1, 2]], p)


@pytest.mark.parametrize("costs", [[], [[1, float("nan")]], [[1, -1]], [[float("inf")]]])
def test_invalid_cost_matrix_rejected(costs):
    with pytest.raises(ValueError, match="costs"):
        solve_p_median(costs, 1)


def test_invalid_demand_weights_rejected():
    with pytest.raises(ValueError, match="demand_weights"):
        solve_p_median([[1, 2], [2, 1]], 1, demand_weights=[1])
    with pytest.raises(ValueError, match="demand_weights"):
        solve_p_median([[1, 2], [2, 1]], 1, demand_weights=[0, 0])
