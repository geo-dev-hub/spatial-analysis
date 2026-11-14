import math
import pytest
from forecast_verification import (
    ContingencyTable, contingency_table, categorical_scores, brier_score,
    brier_skill_score, reliability_bins, roc_auc,
)

def test_contingency_counts_and_scores():
    table = contingency_table([1, 1, 0, 0], [1, 0, 1, 0])
    assert table == ContingencyTable(1, 1, 1, 1)
    scores = categorical_scores(table)
    assert scores["pod"] == 0.5
    assert scores["far"] == 0.5
    assert scores["false_positive_rate"] == 0.5
    assert scores["csi"] == pytest.approx(1/3)
    assert scores["ets"] == 0.0

def test_perfect_forecast_and_undefined_ratios():
    table = contingency_table([1, 0, 1], [1, 0, 1])
    scores = categorical_scores(table)
    assert scores["pod"] == 1.0
    assert scores["far"] == 0.0
    assert scores["csi"] == 1.0
    assert scores["ets"] == 1.0
    all_nonevent = categorical_scores(contingency_table([0, 0], [0, 0]))
    assert all_nonevent["pod"] is None
    assert all_nonevent["far"] is None
    assert all_nonevent["csi"] is None

def test_ets_random_hits_denominator_can_be_zero():
    scores = categorical_scores(ContingencyTable(0, 0, 0, 5))
    assert scores["ets"] is None

def test_invalid_counts_and_inputs():
    with pytest.raises(ValueError): contingency_table([1, 0], [1])
    with pytest.raises(ValueError): contingency_table([2], [1])
    with pytest.raises(ValueError): categorical_scores(ContingencyTable(-1, 0, 0, 1))
    with pytest.raises(ValueError): categorical_scores(ContingencyTable(0, 0, 0, 0))

def test_brier_score_hand_calculation():
    assert brier_score([1, 0, 1, 0], [0.8, 0.2, 0.6, 0.4]) == pytest.approx(0.1)

def test_brier_skill_against_climatology_reference():
    obs = [1, 0, 1, 0]
    forecast = [0.8, 0.2, 0.8, 0.2]
    reference = [0.5] * 4
    assert brier_skill_score(obs, forecast, reference) == pytest.approx(0.84)
    assert brier_skill_score([1, 0], [1, 0], [1, 0]) is None

def test_reliability_bins_keep_empty_bins_and_close_last_edge():
    bins = reliability_bins([0, 1, 1], [0.1, 0.5, 1.0], [0, 0.25, 0.75, 1])
    assert [b["count"] for b in bins] == [1, 1, 1]
    assert bins[0]["observed_frequency"] == 0
    assert bins[-1]["mean_probability"] == 1.0
    empty = reliability_bins([0], [0.2], [0, 0.1, 1])
    assert empty[0]["count"] == 0
    assert empty[0]["mean_probability"] is None

def test_reliability_edges_validation():
    with pytest.raises(ValueError): reliability_bins([0], [0.2], [0.1, 1])
    with pytest.raises(ValueError): reliability_bins([0], [0.2], [0, 0.7, 0.6, 1])

def test_roc_auc_perfect_and_reversed_ranking():
    obs = [0, 0, 1, 1]
    assert roc_auc(obs, [0.1, 0.2, 0.8, 0.9]) == 1.0
    assert roc_auc(obs, [0.9, 0.8, 0.2, 0.1]) == 0.0

def test_roc_auc_ties_use_average_ranks():
    assert roc_auc([0, 1], [0.5, 0.5]) == 0.5
    assert roc_auc([0, 0, 1, 1], [0.1, 0.5, 0.5, 0.9]) == pytest.approx(0.875)

def test_roc_auc_requires_both_classes_but_accepts_nonprobability_scores():
    assert roc_auc([1, 1], [3, 9]) is None
    assert roc_auc([0, 1], [-2, 4]) == 1.0

def test_probability_and_score_validation():
    with pytest.raises(ValueError): brier_score([0], [1.1])
    with pytest.raises(ValueError): brier_score([0], [math.nan])
    with pytest.raises(ValueError): brier_score([0, 1], [0.5])
    with pytest.raises(ValueError): roc_auc([0, 1], [0, math.inf])
