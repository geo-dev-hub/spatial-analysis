from itertools import permutations

import pytest

from geary_c import gearys_c


CHAIN_WEIGHTS = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
]


def test_similar_neighbours_produce_geary_below_one():
    assert gearys_c([1, 2, 3, 4], CHAIN_WEIGHTS) == pytest.approx(0.3)


def test_alternating_neighbours_produce_geary_above_one():
    assert gearys_c([1, 4, 1, 4], CHAIN_WEIGHTS) == pytest.approx(1.5)


def test_two_connected_units_have_geary_equal_to_one():
    assert gearys_c([1, 2], [[0, 1], [1, 0]]) == pytest.approx(1.0)


def test_statistic_is_invariant_to_translation_and_positive_scaling():
    expected = gearys_c([1, 2, 3, 4], CHAIN_WEIGHTS)
    assert gearys_c([11, 12, 13, 14], CHAIN_WEIGHTS) == pytest.approx(expected)
    assert gearys_c([2, 4, 6, 8], CHAIN_WEIGHTS) == pytest.approx(expected)


def test_statistic_is_invariant_to_positive_weight_scaling():
    scaled = [[10 * value for value in row] for row in CHAIN_WEIGHTS]
    assert gearys_c([1, 2, 3, 4], scaled) == pytest.approx(
        gearys_c([1, 2, 3, 4], CHAIN_WEIGHTS)
    )


def test_mean_over_all_permutations_is_one_for_symmetric_weights():
    values = [1, 2, 3, 4]
    simulated = [gearys_c(p, CHAIN_WEIGHTS) for p in permutations(values)]
    assert sum(simulated) / len(simulated) == pytest.approx(1.0)


def test_asymmetric_weights_are_accepted():
    weights = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
    assert gearys_c([1, 2, 3], weights) == pytest.approx(0.5)


def test_constant_values_are_undefined():
    with pytest.raises(ValueError, match="constant"):
        gearys_c([4, 4, 4, 4], CHAIN_WEIGHTS)


def test_zero_weights_are_rejected():
    with pytest.raises(ValueError, match="positive weight"):
        gearys_c([1, 2, 3, 4], [[0] * 4 for _ in range(4)])


def test_misaligned_weights_are_rejected():
    with pytest.raises(ValueError, match="one row"):
        gearys_c([1, 2, 3], CHAIN_WEIGHTS)


def test_non_square_weights_are_rejected():
    with pytest.raises(ValueError, match="square"):
        gearys_c([1, 2, 3], [[0, 1, 0], [1, 0], [0, 1, 0]])


def test_nonzero_self_weights_are_rejected():
    weights = [row[:] for row in CHAIN_WEIGHTS]
    weights[0][0] = 1
    with pytest.raises(ValueError, match="self-weights"):
        gearys_c([1, 2, 3, 4], weights)


def test_negative_weights_are_rejected():
    weights = [row[:] for row in CHAIN_WEIGHTS]
    weights[0][1] = -1
    with pytest.raises(ValueError, match="non-negative"):
        gearys_c([1, 2, 3, 4], weights)


def test_non_finite_values_are_rejected():
    with pytest.raises(ValueError, match="finite"):
        gearys_c([1, 2, float("nan"), 4], CHAIN_WEIGHTS)


def test_non_finite_weights_are_rejected():
    weights = [row[:] for row in CHAIN_WEIGHTS]
    weights[0][1] = float("inf")
    with pytest.raises(ValueError, match="finite"):
        gearys_c([1, 2, 3, 4], weights)


def test_too_few_observations_are_rejected():
    with pytest.raises(ValueError, match="at least two"):
        gearys_c([1], [[0]])
