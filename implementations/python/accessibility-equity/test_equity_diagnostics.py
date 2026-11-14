import math
import pytest
from equity_diagnostics import (weighted_gini, weighted_lorenz_curve, weighted_quantile,
    accessibility_summary, group_accessibility_summary, group_mean_gap)


def test_gini_equal_unequal_and_zero():
    assert weighted_gini([4, 4, 4]) == pytest.approx(0)
    assert weighted_gini([0, 10]) == pytest.approx(.5)
    assert weighted_gini([0, 0, 10]) == pytest.approx(2/3)
    assert weighted_gini([0, 0, 0]) == 0


def test_weights_equivalent_to_replication():
    assert weighted_gini([0, 10], [2, 1]) == pytest.approx(weighted_gini([0, 0, 10]))


def test_lorenz_endpoints_and_weighting():
    p, a = weighted_lorenz_curve([0, 10], [2, 1])
    assert p == pytest.approx([0, 2/3, 1])
    assert a == pytest.approx([0, 0, 1])


def test_quantiles():
    assert weighted_quantile([1, 9, 5], .5, [1, 1, 2]) == 5
    assert weighted_quantile([1, 9], 0) == 1
    assert weighted_quantile([1, 9], 1) == 9


def test_summary_and_shortfall():
    s = accessibility_summary([2, 8], [3, 1], minimum_threshold=5)
    assert s["weighted_mean"] == pytest.approx(3.5)
    assert s["population_share_below_threshold"] == pytest.approx(.75)


def test_groups_and_gap():
    g = group_accessibility_summary([2, 4, 8], ["A", "A", "B"], [1, 3, 2])
    gap = group_mean_gap(g)
    assert g["A"]["weighted_mean"] == pytest.approx(3.5)
    assert gap["absolute_gap"] == pytest.approx(4.5)
    assert gap["lowest_to_highest_ratio"] == pytest.approx(3.5/8)


@pytest.mark.parametrize("values", [[], [-1, 2], [1, math.inf], [1, math.nan]])
def test_invalid_values(values):
    with pytest.raises(ValueError):
        weighted_gini(values)


@pytest.mark.parametrize("weights", [[], [-1, 2], [1, math.inf], [0, 0]])
def test_invalid_weights(weights):
    with pytest.raises(ValueError):
        weighted_gini([1, 2], weights)


def test_mismatched_groups_and_invalid_quantile():
    with pytest.raises(ValueError):
        group_accessibility_summary([1, 2], ["A"])
    with pytest.raises(ValueError):
        weighted_quantile([1, 2], 1.1)


def test_zero_weight_group_omitted_and_zero_ratio():
    g = group_accessibility_summary([2, 8], ["A", "B"], [1, 0])
    assert list(g) == ["A"]
    assert group_mean_gap({"A": {"weighted_mean": 0}, "B": {"weighted_mean": 0}})["lowest_to_highest_ratio"] == 1


def test_empty_group_gap_rejected():
    with pytest.raises(ValueError):
        group_mean_gap({})
