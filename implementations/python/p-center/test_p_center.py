import pytest
from p_center import solve_p_center


def test_minimizes_worst_case_assignment_cost():
    costs = [[1, 8, 5], [7, 3, 4], [6, 7, 2]]
    sites, radius, assignment = solve_p_center(costs, 2)
    assert sites == (0, 2)
    assert radius == pytest.approx(4)
    assert assignment == (0, 2, 2)


def test_single_facility_is_the_minimum_maximum_column():
    sites, radius, assignment = solve_p_center([[1, 8, 5], [7, 3, 4]], 1)
    assert sites == (2,)
    assert radius == pytest.approx(5)
    assert assignment == (2, 2)


def test_opening_every_candidate_assigns_each_row_to_nearest():
    sites, radius, assignment = solve_p_center([[1, 4], [3, 2]], 2)
    assert sites == (0, 1)
    assert radius == pytest.approx(2)
    assert assignment == (0, 1)


def test_ties_are_deterministic():
    sites, radius, assignment = solve_p_center([[1, 1, 5]], 1)
    assert sites == (0,)
    assert radius == pytest.approx(1)
    assert assignment == (0,)


@pytest.mark.parametrize("p", [0, -1, 3, 1.5, True])
def test_invalid_p_rejected(p):
    with pytest.raises(ValueError, match="p must"):
        solve_p_center([[1, 2]], p)


@pytest.mark.parametrize("costs", [[], [[1, float("nan")]], [[1, -1]], [[float("inf")]]])
def test_invalid_cost_matrix_rejected(costs):
    with pytest.raises(ValueError, match="costs"):
        solve_p_center(costs, 1)
