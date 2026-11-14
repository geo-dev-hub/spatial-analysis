import numpy as np
import pytest

from weights_of_evidence import weights_of_evidence


def test_single_evidence_matches_hand_calculated_weights_and_probability():
    event = np.array([[1, 1, 1, 1, 1, 0, 0, 0, 0, 0]])
    evidence = {"fault_buffer": np.array([[1, 1, 1, 0, 0, 1, 1, 0, 0, 0]])}
    result = weights_of_evidence(event, evidence, pseudocount=0)
    weight = result.weights[0]
    assert result.prior_probability == pytest.approx(0.5)
    assert (weight.n_event_present, weight.n_event_absent) == (3, 2)
    assert (weight.n_non_event_present, weight.n_non_event_absent) == (2, 3)
    assert weight.positive == pytest.approx(np.log(1.5))
    assert weight.negative == pytest.approx(np.log(2 / 3))
    assert weight.contrast == pytest.approx(np.log(2.25))
    assert result.probability[0, 0] == pytest.approx(0.6)
    assert result.probability[0, 3] == pytest.approx(0.4)


def test_pseudocount_stabilises_zero_counts():
    event = np.array([[1, 1, 0, 0]])
    evidence = {"rare": np.array([[1, 1, 0, 0]])}
    result = weights_of_evidence(event, evidence, pseudocount=0.5)
    assert np.isfinite(result.weights[0].positive)
    assert np.isfinite(result.weights[0].negative)
    assert np.all((result.probability[result.valid_mask] > 0) &
                  (result.probability[result.valid_mask] < 1))


def test_zero_counts_without_smoothing_are_rejected():
    event = np.array([[1, 1, 0, 0]])
    evidence = {"rare": np.array([[1, 1, 0, 0]])}
    with pytest.raises(ValueError, match="zero contingency count"):
        weights_of_evidence(event, evidence, pseudocount=0)


def test_multiple_evidence_layers_add_log_odds_contributions():
    event = np.array([[1, 1, 0, 0], [1, 0, 1, 0]])
    evidence = {
        "a": np.array([[1, 1, 0, 0], [1, 0, 1, 0]]),
        "b": np.array([[0, 1, 0, 1], [1, 0, 0, 1]]),
    }
    result = weights_of_evidence(event, evidence)
    assert len(result.weights) == 2
    assert np.all(np.isfinite(result.log_odds[result.valid_mask]))


def test_non_finite_cells_are_excluded_using_complete_case_policy():
    event = np.array([[1, 0], [1, 0]], dtype=float)
    evidence = {"a": np.array([[1, 0], [np.nan, 1]])}
    result = weights_of_evidence(event, evidence)
    assert result.valid_mask.tolist() == [[True, True], [False, True]]
    assert np.isnan(result.probability[1, 0])


def test_study_area_mask_excludes_cells_from_estimation_and_scoring():
    event = np.array([[1, 1, 0, 0]])
    evidence = {"a": np.array([[1, 0, 1, 0]])}
    area = np.array([[True, True, True, False]])
    result = weights_of_evidence(event, evidence, study_area=area)
    assert result.valid_mask.tolist() == [[True, True, True, False]]
    assert result.prior_probability == pytest.approx(2 / 3)
    assert np.isnan(result.probability[0, 3])


def test_event_and_evidence_must_be_binary_or_nodata():
    with pytest.raises(ValueError, match="binary"):
        weights_of_evidence(np.array([[1, 2, 0]]), {"a": np.array([[1, 0, 0]])})
    with pytest.raises(ValueError, match="binary"):
        weights_of_evidence(np.array([[1, 0, 0]]), {"a": np.array([[1, 0, 0.5]])})


def test_shapes_and_mapping_contract_are_enforced():
    with pytest.raises(ValueError, match="same shape"):
        weights_of_evidence(np.ones((2, 2)), {"a": np.ones((1, 2))})
    with pytest.raises(ValueError, match="non-empty mapping"):
        weights_of_evidence(np.ones((2, 2)), {})


def test_study_area_must_be_boolean_and_aligned():
    event = np.array([[1, 0], [1, 0]])
    evidence = {"a": np.array([[1, 0], [1, 0]])}
    with pytest.raises(ValueError, match="Boolean"):
        weights_of_evidence(event, evidence, study_area=np.ones((2, 2)))
    with pytest.raises(ValueError, match="same shape"):
        weights_of_evidence(event, evidence, study_area=np.ones((1, 2), dtype=bool))


def test_pseudocount_must_be_finite_and_nonnegative():
    event = np.array([[1, 0]])
    evidence = {"a": np.array([[1, 0]])}
    for value in (-0.1, np.nan, np.inf):
        with pytest.raises(ValueError, match="pseudocount"):
            weights_of_evidence(event, evidence, pseudocount=value)


def test_study_area_must_contain_both_event_classes():
    event = np.array([[1, 1, 0, 0]])
    evidence = {"a": np.array([[1, 0, 1, 0]])}
    with pytest.raises(ValueError, match="both event and non-event"):
        weights_of_evidence(event, evidence, study_area=np.array([[True, True, False, False]]))
