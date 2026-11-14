import numpy as np
import pytest

from electre_i import electre_i_relation


def test_weighted_concordance_and_discordance_for_a_pair():
    performance = np.array([
        [8, 7, 4],
        [6, 8, 5],
        [5, 4, 7],
    ], dtype=float)
    result = electre_i_relation(
        performance, [0.5, 0.3, 0.2],
        ["benefit", "benefit", "cost"],
        concordance_threshold=0.6,
        discordance_threshold=0.3,
    )
    assert result.concordance[0, 1] == pytest.approx(0.7)
    assert result.discordance[0, 1] == pytest.approx(0.25)
    assert result.outranks[0, 1]
    assert not result.outranks[1, 0]


def test_cost_direction_is_oriented_correctly():
    performance = np.array([[10, 5], [8, 7]], dtype=float)
    result = electre_i_relation(
        performance, [0.5, 0.5], ["benefit", "cost"],
        concordance_threshold=0.5, discordance_threshold=1.0,
    )
    assert result.concordance[0, 1] == pytest.approx(1.0)
    assert result.concordance[1, 0] == pytest.approx(0.0)


def test_weights_are_normalised_and_zero_weight_criteria_do_not_contribute():
    performance = np.array([[3, 0], [2, 100]], dtype=float)
    result = electre_i_relation(performance, [4, 0], ["benefit", "benefit"])
    np.testing.assert_allclose(result.normalised_weights, [1.0, 0.0])
    assert result.concordance[0, 1] == pytest.approx(1.0)


def test_relation_is_reflexive_and_can_be_incomplete():
    performance = np.array([[3, 1], [1, 3], [2, 2]], dtype=float)
    result = electre_i_relation(
        performance, [0.5, 0.5], ["benefit", "benefit"],
        concordance_threshold=0.75, discordance_threshold=0.25,
    )
    assert np.all(np.diag(result.outranks))
    assert not result.outranks[0, 1]
    assert not result.outranks[1, 0]


def test_pairwise_ties_produce_full_concordance_and_zero_discordance():
    performance = np.array([[1, 2], [1, 2]], dtype=float)
    result = electre_i_relation(performance, [1, 1], ["benefit", "cost"])
    assert result.concordance[0, 1] == pytest.approx(1.0)
    assert result.discordance[0, 1] == pytest.approx(0.0)
    assert result.outranks[0, 1]


def test_constant_criterion_has_no_discordance_range():
    performance = np.array([[1, 5], [1, 5]], dtype=float)
    result = electre_i_relation(
        performance, [0.5, 0.5], ["benefit", "benefit"],
        concordance_threshold=0.5, discordance_threshold=0.0,
    )
    assert result.discordance[0, 1] == pytest.approx(0.0)


@pytest.mark.parametrize("threshold", [-0.1, 1.1, np.nan])
def test_invalid_thresholds_are_rejected(threshold):
    with pytest.raises(ValueError):
        electre_i_relation([[1], [2]], [1], ["benefit"],
                           concordance_threshold=threshold)


def test_invalid_performance_weights_and_directions_are_rejected():
    with pytest.raises(ValueError, match="finite"):
        electre_i_relation([[1], [np.inf]], [1], ["benefit"])
    with pytest.raises(ValueError, match="non-negative"):
        electre_i_relation([[1], [2]], [-1], ["benefit"])
    with pytest.raises(ValueError, match="positive"):
        electre_i_relation([[1], [2]], [0], ["benefit"])
    with pytest.raises(ValueError, match="directions"):
        electre_i_relation([[1], [2]], [1], ["maximise"])


def test_input_dimensions_and_names_are_checked():
    with pytest.raises(ValueError, match="at least two alternatives"):
        electre_i_relation([[1]], [1], ["benefit"])
    with pytest.raises(ValueError, match="one value per criterion"):
        electre_i_relation([[1, 2], [2, 3]], [1], ["benefit", "benefit"])
    with pytest.raises(ValueError, match="unique"):
        electre_i_relation([[1], [2]], [1], ["benefit"], alternative_names=["X", "X"])
