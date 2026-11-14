import pytest
from capacitated_p_median import solve_capacitated_p_median

def test_capacity_changes_the_assignment_and_selected_sites():
    opened, objective, assignment = solve_capacitated_p_median(
        [[0, 5, 9], [1, 4, 8], [8, 1, 4], [9, 0, 3]], 2,
        capacities=[2, 2, 4], demand_quantities=[2, 1, 2, 1],
    )
    assert opened == (0, 2)
    assert objective == pytest.approx(15)
    assert assignment == (0, 2, 2, 2)

def test_capacity_can_force_a_higher_cost_assignment():
    opened, objective, assignment = solve_capacitated_p_median(
        [[0, 2], [0, 2], [1, 0]], 2,
        capacities=[1, 2], demand_quantities=[1, 1, 1],
    )
    assert opened == (0, 1)
    assert objective == pytest.approx(2)
    assert assignment == (0, 1, 1)

def test_demand_weights_change_assignment_cost_not_capacity_load():
    # Both demand rows prefer facility 0, but its capacity is one unit.
    # With equal weights, row 0 goes to facility 0 and row 1 to facility 1.
    # Prioritising row 1 makes it worth reversing those assignments.
    costs = [[0, 2], [0, 1]]
    unweighted = solve_capacitated_p_median(
        costs, 2, capacities=[1, 1], demand_quantities=[1, 1],
    )
    weighted = solve_capacitated_p_median(
        costs, 2, capacities=[1, 1], demand_quantities=[1, 1], demand_weights=[1, 10],
    )
    assert unweighted[1] == pytest.approx(1)
    assert unweighted[2] == (0, 1)
    assert weighted[0] == (0, 1)
    assert weighted[1] == pytest.approx(2)
    assert weighted[2] == (1, 0)

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


@pytest.mark.parametrize("costs", [
    [],
    [[1, float("nan")]],
    [[1, -1]],
    [[1, float("inf")]],
])
def test_invalid_cost_matrices_are_rejected(costs):
    with pytest.raises(ValueError, match="costs"):
        solve_capacitated_p_median(
            costs, 1, capacities=[1, 1], demand_quantities=[1]
        )


@pytest.mark.parametrize("weights", [
    [1, 2],
    [-1],
    [float("nan")],
    [0],
])
def test_invalid_demand_weights_are_rejected(weights):
    with pytest.raises(ValueError, match="demand_weights"):
        solve_capacitated_p_median(
            [[1, 2]], 1, capacities=[1, 1],
            demand_quantities=[1], demand_weights=weights,
        )


def test_priority_weights_can_change_selected_sites_without_changing_load_units():
    costs = [[3, 8, 6], [6, 1, 5], [5, 0, 2], [7, 7, 5]]
    quantities = [2, 1, 2, 1]
    capacities = [2, 2, 4]
    plain = solve_capacitated_p_median(
        costs, 2, capacities=capacities, demand_quantities=quantities,
    )
    weighted = solve_capacitated_p_median(
        costs, 2, capacities=capacities, demand_quantities=quantities,
        demand_weights=[1, 4, 1, 1],
    )
    assert plain[0] == (0, 2)
    assert weighted[0] == (1, 2)
    loads = [sum(quantities[i] for i, site in enumerate(weighted[2]) if site == j) for j in weighted[0]]
    assert loads == [2, 4]
