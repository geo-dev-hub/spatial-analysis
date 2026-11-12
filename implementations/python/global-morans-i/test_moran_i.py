import pytest

from moran_i import morans_i, row_standardize


CHAIN_WEIGHTS = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
]


def test_similar_neighbours_produce_positive_moran_i():
    assert morans_i([1, 2, 3, 4], CHAIN_WEIGHTS) == pytest.approx(1 / 3)


def test_alternating_neighbours_produce_negative_moran_i():
    assert morans_i([1, 4, 1, 4], CHAIN_WEIGHTS) == pytest.approx(-1.0)


def test_row_standardisation_changes_the_statistic():
    weights = row_standardize(CHAIN_WEIGHTS)
    assert morans_i([1, 2, 3, 4], weights) == pytest.approx(0.4)


def test_statistic_is_invariant_to_affine_changes_in_values():
    assert morans_i([1, 2, 3, 4], CHAIN_WEIGHTS) == pytest.approx(
        morans_i([11, 12, 13, 14], CHAIN_WEIGHTS)
    )
    assert morans_i([1, 2, 3, 4], CHAIN_WEIGHTS) == pytest.approx(
        morans_i([2, 4, 6, 8], CHAIN_WEIGHTS)
    )


def test_statistic_is_invariant_to_positive_weight_scaling():
    scaled = [[10 * value for value in row] for row in CHAIN_WEIGHTS]
    assert morans_i([1, 2, 3, 4], CHAIN_WEIGHTS) == pytest.approx(
        morans_i([1, 2, 3, 4], scaled)
    )


def test_row_standardisation_keeps_island_rows_zero():
    weights = [
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 0],
    ]
    assert row_standardize(weights)[2] == [0.0, 0.0, 0.0]


def test_constant_values_are_undefined():
    with pytest.raises(ValueError, match="constant"):
        morans_i([4, 4, 4, 4], CHAIN_WEIGHTS)


def test_zero_weights_are_rejected():
    with pytest.raises(ValueError, match="positive weight"):
        morans_i([1, 2, 3, 4], [[0] * 4 for _ in range(4)])


def test_misaligned_weights_are_rejected():
    with pytest.raises(ValueError, match="one row"):
        morans_i([1, 2, 3], CHAIN_WEIGHTS)


def test_non_square_weights_are_rejected():
    with pytest.raises(ValueError, match="square"):
        morans_i([1, 2, 3], [[0, 1, 0], [1, 0], [0, 1, 0]])


def test_nonzero_self_weights_are_rejected():
    weights = [row[:] for row in CHAIN_WEIGHTS]
    weights[0][0] = 1
    with pytest.raises(ValueError, match="self-weights"):
        morans_i([1, 2, 3, 4], weights)


def test_negative_weights_are_rejected():
    weights = [row[:] for row in CHAIN_WEIGHTS]
    weights[0][1] = -1
    with pytest.raises(ValueError, match="non-negative"):
        morans_i([1, 2, 3, 4], weights)


def test_non_finite_values_are_rejected():
    with pytest.raises(ValueError, match="finite"):
        morans_i([1, 2, float("nan"), 4], CHAIN_WEIGHTS)
