import pytest

from backup_coverage import solve_backup_coverage


def test_two_independent_facilities_must_reach_demand():
    costs = [
        [1, 2, 9, 9],
        [1, 9, 2, 9],
        [9, 1, 2, 9],
    ]
    sites, value, covered, counts = solve_backup_coverage(
        costs, p=2, service_threshold=2, demand_weights=[10, 4, 3]
    )
    assert sites == (0, 1)
    assert value == 10
    assert covered == (True, False, False)
    assert counts == (2, 1, 1)


def test_one_facility_cannot_satisfy_two_cover_requirement():
    with pytest.raises(ValueError, match="cannot exceed"):
        solve_backup_coverage([[1, 2]], p=1, service_threshold=2)


def test_demand_needs_distinct_selected_candidates():
    sites, value, covered, counts = solve_backup_coverage(
        [[1, 1, 9], [1, 9, 1]], p=2, service_threshold=1,
        required_cover_count=2, demand_weights=[5, 7]
    )
    assert sites == (0, 1)
    assert value == 5
    assert covered == (True, False)
    assert counts == (2, 1)


def test_at_most_budget_and_deterministic_tie_breaking():
    sites, value, covered, counts = solve_backup_coverage(
        [[1, 1, 1], [9, 9, 9]], p=3, service_threshold=1,
        required_cover_count=2, demand_weights=[4, 0]
    )
    assert sites == (0, 1)
    assert value == 4
    assert covered == (True, False)
    assert counts == (2, 0)


def test_zero_weights_choose_empty_solution():
    assert solve_backup_coverage(
        [[1, 2, 3]], p=3, service_threshold=3,
        required_cover_count=2, demand_weights=[0]
    ) == ((), 0.0, (False,), (0,))


def test_one_cover_requirement_matches_threshold_coverage():
    sites, value, covered, counts = solve_backup_coverage(
        [[1, 8], [8, 1]], p=1, service_threshold=2,
        required_cover_count=1
    )
    assert sites == (0,)
    assert value == 1
    assert covered == (True, False)
    assert counts == (1, 0)


@pytest.mark.parametrize("p", [-1, 4, 1.5, True])
def test_invalid_budget(p):
    with pytest.raises(ValueError, match="p must"):
        solve_backup_coverage([[1, 2, 3]], p, 2)


@pytest.mark.parametrize("r", [0, -1, 1.5, True])
def test_invalid_redundancy_requirement(r):
    with pytest.raises(ValueError, match="required_cover_count"):
        solve_backup_coverage([[1, 2, 3]], 3, 2, required_cover_count=r)


@pytest.mark.parametrize("threshold", [-1, float("inf"), float("nan")])
def test_invalid_threshold(threshold):
    with pytest.raises(ValueError, match="service_threshold"):
        solve_backup_coverage([[1, 2, 3]], 3, threshold)


@pytest.mark.parametrize("costs", [[], [[1, float("nan")]], [[1, -1]], [[float("inf")]]])
def test_invalid_cost_matrix(costs):
    with pytest.raises(ValueError, match="costs"):
        solve_backup_coverage(costs, 2, 2)


def test_invalid_weights():
    with pytest.raises(ValueError, match="demand_weights"):
        solve_backup_coverage([[1, 2], [2, 1]], 2, 2, demand_weights=[1])
    with pytest.raises(ValueError, match="demand_weights"):
        solve_backup_coverage([[1, 2], [2, 1]], 2, 2, demand_weights=[1, -1])
