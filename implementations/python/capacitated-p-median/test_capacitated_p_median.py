import pytest
from capacitated_p_median import solve_capacitated_p_median

def test_capacity_changes_the_assignment_and_selected_sites():
    opened, objective, assignment = solve_capacitated_p_median(
        [[0, 5, 9], [1, 4, 8], [8, 1, 4], [9, 0, 3]], 2,
        capacities=[2, 2, 4], demand_quantities=[2, 1, 2, 1],
    )
    assert opened == (0, 2)
    assert objective == pytest.approx(14)
    assert assignment == (0, 0, 2, 2)

def test_capacity_can_force_a_higher_cost_assignment():
    opened, objective, assignment = solve_capacitated_p_median(
        [[0, 2], [0, 2], [1, 0]], 2,
        capacities=[1, 2], demand_quantities=[1, 1, 1],
    )
    assert opened == (0, 1)
    assert objective == pytest.approx(3)
    assert assignment == (0, 1, 1)

def test_demand_weights_change_cost_not_capacity_load():
    opened, objective, assignment = solve_capacitated_p_median(
        [[0, 5], [1, 0]], 2,
        capacities=[1, 1], demand_quantities=[1, 1], demand_weights=[10, 1],
    )
    assert opened == (0, 1)
    assert objective == pytest.approx(0)
    assert assignment == (0, 1)

def test_infeasible_total_capacity_is_reported():
    with pytest.raises(ValueError, match="no feasible assignment"):
        solve_capacitated_p_median([[1, 2], [2, 1]], 1, capacities=[1, 1], demand_quantities=[1, 1])

def test_exactly_p_facilities_are_opened_and_ties_are_deterministic():
    opened, objective, assignment = solve_capacitated_p_median(
        [[1, 1, 1], [1, 1, 1]], 2, capacities=[1, 1, 2], demand_quantities=[1, 1],
    )
    assert opened == (0, 1)
    assert objective == pytest.approx(2)
    assert assignment == (0, 1)

@pytest.mark.parametrize("kwargs", [
    {"capacities": [1], "demand_quantities": [1]},
    {"capacities": [1, float("inf")], "demand_quantities": [1]},
    {"capacities": [-1, 1], "demand_quantities": [1]},
    {"capacities": [2, 2], "demand_quantities": [1, float("nan")]},
    {"capacities": [2, 2], "demand_quantities": [-1]},
    {"capacities": [2, 2], "demand_quantities": [0]},
])
def test_invalid_capacity_or_demand_inputs_are_rejected(kwargs):
    with pytest.raises(ValueError):
        solve_capacitated_p_median([[1, 2]], 1, **kwargs)

@pytest.mark.parametrize("p", [0, -1, 3, 1.5, True])
def test_invalid_p_is_rejected(p):
    with pytest.raises(ValueError, match="p must"):
        solve_capacitated_p_median([[1, 2]], p, capacities=[1, 1], demand_quantities=[1])
