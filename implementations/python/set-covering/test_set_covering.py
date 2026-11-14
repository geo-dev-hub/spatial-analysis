import pytest
from set_covering import solve_set_cover


def test_finds_minimum_cardinality_cover():
    costs = [[1, 9, 9], [1, 1, 9], [9, 1, 1], [9, 9, 1]]
    sites, count, assignments = solve_set_cover(costs, 2)
    assert sites == (0, 2)
    assert count == 2
    assert assignments == (0, 0, 2, 2)


def test_threshold_is_inclusive():
    sites, count, assignments = solve_set_cover([[5, 9], [9, 5]], 5)
    assert sites == (0, 1)
    assert count == 2
    assert assignments == (0, 1)


def test_lexicographic_tie_break_is_deterministic():
    sites, count, assignments = solve_set_cover([[1, 1, 9], [9, 1, 1]], 1)
    assert sites == (0, 1)
    assert count == 2
    assert assignments == (0, 1)


def test_reports_uncoverable_demand_rows():
    with pytest.raises(ValueError, match="demand rows"):
        solve_set_cover([[1, 9], [9, 9], [9, 1]], 2)


@pytest.mark.parametrize("threshold", [-1, float("inf"), float("nan")])
def test_invalid_threshold_rejected(threshold):
    with pytest.raises(ValueError, match="service_threshold"):
        solve_set_cover([[1, 2]], threshold)


@pytest.mark.parametrize("costs", [[], [[1, float("nan")]], [[1, -1]], [[float("inf")]]])
def test_invalid_cost_matrix_rejected(costs):
    with pytest.raises(ValueError, match="costs"):
        solve_set_cover(costs, 2)
