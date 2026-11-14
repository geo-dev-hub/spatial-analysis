import pytest

from mexclp import solve_mexclp


def test_single_cover_uses_one_minus_busy_fraction():
    sites, value, contributions = solve_mexclp([[1]], 1, 5, 0.3, demand_weights=[100])
    assert sites == (0,)
    assert value == pytest.approx(70)
    assert contributions == pytest.approx((70,))


def test_second_cover_adds_diminishing_expected_coverage():
    sites, value, contributions = solve_mexclp([[1, 2]], 2, 5, 0.3, demand_weights=[100])
    assert sites == (0, 0)
    assert value == pytest.approx(91)
    assert contributions == pytest.approx((91,))


def test_solver_can_choose_different_sites_to_cover_more_demand():
    costs = [[1, 9], [9, 1]]
    sites, value, contributions = solve_mexclp(costs, 2, 2, 0.25, demand_weights=[100, 80])
    assert sites == (0, 1)
    assert value == pytest.approx(135)
    assert contributions == pytest.approx((75, 60))


def test_zero_units_produce_zero_expected_coverage():
    sites, value, contributions = solve_mexclp([[1, 2], [3, 4]], 0, 5, 0.2)
    assert sites == ()
    assert value == 0
    assert contributions == (0, 0)


def test_zero_busy_fraction_reduces_to_deterministic_coverage():
    sites, value, contributions = solve_mexclp([[1, 9], [9, 1]], 1, 2, 0, demand_weights=[5, 7])
    assert sites == (1,)
    assert value == 7
    assert contributions == (0, 7)


def test_ties_are_deterministic():
    assert solve_mexclp([[1, 1]], 1, 2, 0.2)[0] == (0,)


@pytest.mark.parametrize("busy", [-0.1, 1, float("inf"), float("nan")])
def test_invalid_busy_fraction_is_rejected(busy):
    with pytest.raises(ValueError, match="busy_fraction"):
        solve_mexclp([[1]], 1, 2, busy)


@pytest.mark.parametrize("p", [-1, 1.5, True])
def test_invalid_unit_count_is_rejected(p):
    with pytest.raises(ValueError, match="p"):
        solve_mexclp([[1]], p, 2, 0.2)


def test_invalid_costs_are_rejected():
    with pytest.raises(ValueError, match="costs"):
        solve_mexclp([[1, -1]], 1, 2, 0.2)
    with pytest.raises(ValueError, match="rectangular"):
        solve_mexclp([[1, 2], [3]], 1, 2, 0.2)


def test_invalid_demand_weights_are_rejected():
    with pytest.raises(ValueError, match="demand_weights"):
        solve_mexclp([[1], [2]], 1, 2, 0.2, demand_weights=[1])


@pytest.mark.parametrize("busy", ["0.2", None])
def test_non_numeric_busy_fraction_raises_value_error(busy):
    with pytest.raises(ValueError, match="busy_fraction"):
        solve_mexclp([[1]], 1, 2, busy)


@pytest.mark.parametrize("threshold", ["5", None])
def test_non_numeric_threshold_raises_value_error(threshold):
    with pytest.raises(ValueError, match="service_threshold"):
        solve_mexclp([[1]], 1, threshold, 0.2)
