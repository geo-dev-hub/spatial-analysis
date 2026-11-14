import pytest
from maximal_covering import solve_maximal_covering


def test_selects_sites_maximising_weighted_coverage():
    costs = [[1, 8, 9, 5], [2, 7, 8, 4], [8, 1, 7, 5],
             [9, 2, 6, 4], [5, 5, 1, 8]]
    sites, value, covered = solve_maximal_covering(
        costs, 2, 2, demand_weights=[10, 5, 8, 4, 3])
    assert sites == (0, 1)
    assert value == pytest.approx(27)
    assert covered == (True, True, True, True, False)


def test_threshold_is_inclusive():
    sites, value, covered = solve_maximal_covering([[5, 8], [6, 2]], 1, 5)
    assert sites == (0,)
    assert value == 1
    assert covered == (True, False)


def test_at_most_p_may_open_fewer_sites():
    sites, value, covered = solve_maximal_covering(
        [[1, 1, 1], [9, 9, 9]], 3, 2, demand_weights=[4, 7])
    assert sites == (0,)
    assert value == 4
    assert covered == (True, False)


def test_zero_budget_returns_empty_solution():
    assert solve_maximal_covering([[1, 2], [2, 1]], 0, 2) == ((), 0.0, (False, False))


def test_ties_prefer_fewer_then_lexicographic_sites():
    sites, value, covered = solve_maximal_covering([[1, 1, 1]], 2, 1)
    assert sites == (0,)
    assert value == 1
    assert covered == (True,)


def test_zero_weight_rows_do_not_force_open_sites():
    assert solve_maximal_covering([[1, 9], [9, 1]], 1, 1,
                                  demand_weights=[0, 0]) == ((), 0.0, (False, False))


@pytest.mark.parametrize("p", [-1, 3, 1.5, True])
def test_invalid_p(p):
    with pytest.raises(ValueError, match="p must"):
        solve_maximal_covering([[1, 2]], p, 1)


@pytest.mark.parametrize("threshold", [-1, float("inf"), float("nan")])
def test_invalid_threshold(threshold):
    with pytest.raises(ValueError, match="service_threshold"):
        solve_maximal_covering([[1, 2]], 1, threshold)


@pytest.mark.parametrize("costs", [[], [[1, float("nan")]], [[1, -1]], [[float("inf")]]])
def test_invalid_costs(costs):
    with pytest.raises(ValueError, match="costs"):
        solve_maximal_covering(costs, 1, 2)


def test_invalid_weights():
    with pytest.raises(ValueError, match="demand_weights"):
        solve_maximal_covering([[1, 2], [2, 1]], 1, 2, demand_weights=[1])
    with pytest.raises(ValueError, match="demand_weights"):
        solve_maximal_covering([[1, 2], [2, 1]], 1, 2, demand_weights=[1, -1])
