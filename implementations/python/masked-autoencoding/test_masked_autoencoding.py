import numpy as np
import pytest

from masked_autoencoding import random_patch_masking, restore_masked_sequence


def test_masking_keeps_expected_number_of_visible_tokens():
    x = np.arange(2 * 8 * 3, dtype=float).reshape(2, 8, 3)
    result = random_patch_masking(x, mask_ratio=0.75, seed=3)
    assert result.visible_tokens.shape == (2, 2, 3)
    assert result.mask.shape == (2, 8)
    np.testing.assert_array_equal(np.sum(result.mask == 0, axis=1), [2, 2])
    np.testing.assert_array_equal(np.sum(result.mask == 1, axis=1), [6, 6])


def test_masking_is_deterministic_for_a_fixed_seed():
    x = np.arange(60, dtype=float).reshape(2, 10, 3)
    a = random_patch_masking(x, 0.6, seed=42)
    b = random_patch_masking(x, 0.6, seed=42)
    np.testing.assert_array_equal(a.kept_indices, b.kept_indices)
    np.testing.assert_array_equal(a.mask, b.mask)
    np.testing.assert_allclose(a.visible_tokens, b.visible_tokens)


def test_masking_is_independent_per_batch_item():
    x = np.zeros((3, 12, 2))
    result = random_patch_masking(x, 0.5, seed=11)
    assert not np.array_equal(result.kept_indices[0], result.kept_indices[1])


def test_zero_mask_ratio_keeps_all_tokens():
    x = np.arange(12, dtype=float).reshape(1, 4, 3)
    result = random_patch_masking(x, 0, seed=1)
    np.testing.assert_allclose(result.visible_tokens, x)
    np.testing.assert_array_equal(result.mask, [[0, 0, 0, 0]])


def test_restoration_places_mask_tokens_in_original_order():
    x = np.arange(2 * 8 * 3, dtype=float).reshape(2, 8, 3)
    result = random_patch_masking(x, 0.75, seed=3)
    restored = restore_masked_sequence(result.visible_tokens, [-1, -1, -1], result.restore_indices)
    for row in range(2):
        visible_positions = np.flatnonzero(result.mask[row] == 0)
        np.testing.assert_allclose(restored[row, visible_positions], x[row, visible_positions])
        masked_positions = np.flatnonzero(result.mask[row] == 1)
        np.testing.assert_allclose(restored[row, masked_positions], -1)


@pytest.mark.parametrize("ratio", [-0.1, 1, float("nan")])
def test_invalid_mask_ratios_are_rejected(ratio):
    with pytest.raises(ValueError):
        random_patch_masking(np.ones((1, 4, 2)), ratio)


def test_invalid_token_arrays_and_seeds_are_rejected():
    with pytest.raises(ValueError):
        random_patch_masking(np.ones((4, 2)), 0.5)
    with pytest.raises(ValueError):
        random_patch_masking(np.ones((1, 4, 2)), 0.5, seed=1.2)
    with pytest.raises(ValueError):
        random_patch_masking(np.full((1, 4, 2), np.nan), 0.5)


def test_invalid_restore_contracts_are_rejected():
    with pytest.raises(ValueError):
        restore_masked_sequence(np.ones((1, 2, 3)), [0, 0], [[0, 1, 2]])
    with pytest.raises(ValueError):
        restore_masked_sequence(np.ones((1, 2, 3)), [0, 0, 0], [[0, 0, 2]])
