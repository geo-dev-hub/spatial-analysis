import numpy as np
import pytest

from two_step_fca import two_step_fca


def test_two_step_fca_calculates_provider_ratios_and_accessibility():
    costs = [[1, 4], [2, 1]]
    ratios, accessibility = two_step_fca(costs, [10, 20], [100, 100], max_cost=2)
    assert ratios == pytest.approx([0.05, 0.2])
    assert accessibility == pytest.approx([0.05, 0.25])


def test_two_step_fca_uses_inclusive_catchment_threshold():
    ratios, accessibility = two_step_fca([[2, 2.01]], [10, 20], [100], max_cost=2)
    assert ratios == pytest.approx([0.1, 0])
    assert accessibility == pytest.approx([0.1])


def test_two_step_fca_returns_zero_for_isolated_provider_and_population():
    ratios, accessibility = two_step_fca(
        [[1, 9], [9, 1]], [10, 20], [100, 100], max_cost=2
    )
    assert ratios == pytest.approx([0.1, 0.2])
    assert accessibility == pytest.approx([0.1, 0.2])


def test_two_step_fca_accepts_zero_supply_but_rejects_all_zero_demand():
    ratios, accessibility = two_step_fca([[1]], [0], [10], max_cost=2)
    assert ratios == [0]
    assert accessibility == [0]
    with pytest.raises(ValueError, match="positive"):
        two_step_fca([[1]], [10], [0], max_cost=2)


@pytest.mark.parametrize("max_cost", [0, -1, float("nan"), float("inf")])
def test_two_step_fca_rejects_invalid_threshold(max_cost):
    with pytest.raises(ValueError, match="max_cost"):
        two_step_fca([[1]], [1], [1], max_cost=max_cost)


def test_two_step_fca_rejects_shape_mismatch():
    with pytest.raises(ValueError, match="provider_supply"):
        two_step_fca([[1, 2]], [1], [10], max_cost=2)
    with pytest.raises(ValueError, match="population_demand"):
        two_step_fca([[1, 2]], [1, 2], [10, 20], max_cost=2)


def test_two_step_fca_rejects_invalid_cost_and_weights():
    with pytest.raises(ValueError, match="impedance"):
        two_step_fca([[1, -1]], [1, 2], [10], max_cost=2)
    with pytest.raises(ValueError, match="provider_supply"):
        two_step_fca([[1]], [-1], [10], max_cost=2)
    with pytest.raises(ValueError, match="population_demand"):
        two_step_fca([[1]], [1], [float("nan")], max_cost=2)
