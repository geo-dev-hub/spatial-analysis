"""NumPy teaching utilities for MAE-style random patch masking."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray


@dataclass(frozen=True)
class MaskingResult:
    visible_tokens: NDArray[np.float64]
    mask: NDArray[np.int64]
    restore_indices: NDArray[np.int64]
    kept_indices: NDArray[np.int64]


def random_patch_masking(
    tokens: ArrayLike,
    mask_ratio: float = 0.75,
    seed: int = 0,
) -> MaskingResult:
    """Select visible tokens independently per sample and record restore order.

    tokens has shape (batch, patches, features). A mask value of 0 denotes
    visible; 1 denotes masked, in the original patch order. At least one
    visible token is retained per sample.
    """
    x = np.asarray(tokens, dtype=np.float64)
    if x.ndim != 3 or 0 in x.shape:
        raise ValueError("tokens must be a non-empty (batch, patches, features) array")
    if not np.all(np.isfinite(x)):
        raise ValueError("tokens must be finite")
    if not np.isfinite(mask_ratio) or not 0 <= mask_ratio < 1:
        raise ValueError("mask_ratio must be finite and in [0, 1)")
    if not isinstance(seed, (int, np.integer)):
        raise ValueError("seed must be an integer")

    batch, patches, _ = x.shape
    keep_count = max(1, int(patches * (1.0 - float(mask_ratio))))
    rng = np.random.default_rng(int(seed))
    noise = rng.random((batch, patches))
    shuffled_indices = np.argsort(noise, axis=1)
    restore_indices = np.argsort(shuffled_indices, axis=1)
    kept_indices = shuffled_indices[:, :keep_count]
    visible = np.take_along_axis(x, kept_indices[:, :, None], axis=1)

    shuffled_mask = np.ones((batch, patches), dtype=np.int64)
    shuffled_mask[:, :keep_count] = 0
    mask = np.take_along_axis(shuffled_mask, restore_indices, axis=1)
    return MaskingResult(visible, mask, restore_indices, kept_indices)


def restore_masked_sequence(
    visible_tokens: ArrayLike,
    mask_token: ArrayLike,
    restore_indices: ArrayLike,
) -> NDArray[np.float64]:
    """Restore original sequence order by inserting one mask token per hidden patch."""
    visible = np.asarray(visible_tokens, dtype=np.float64)
    token = np.asarray(mask_token, dtype=np.float64)
    restore = np.asarray(restore_indices)
    if visible.ndim != 3 or 0 in visible.shape:
        raise ValueError("visible_tokens must be a non-empty (batch, visible, features) array")
    if token.shape not in ((visible.shape[2],), (1, 1, visible.shape[2])):
        raise ValueError("mask_token must have shape (features,) or (1, 1, features)")
    if not np.all(np.isfinite(visible)) or not np.all(np.isfinite(token)):
        raise ValueError("tokens must be finite")
    if restore.ndim != 2 or restore.shape[0] != visible.shape[0]:
        raise ValueError("restore_indices must have shape (batch, patches)")
    if not np.issubdtype(restore.dtype, np.integer):
        raise ValueError("restore_indices must contain integers")
    batch, visible_count, features = visible.shape
    patches = restore.shape[1]
    if visible_count > patches or np.any(restore < 0) or np.any(restore >= patches):
        raise ValueError("restore_indices contain invalid positions")
    expected = np.arange(patches)
    for row in restore:
        if not np.array_equal(np.sort(row), expected):
            raise ValueError("each restore_indices row must be a permutation of patch positions")
    masked_count = patches - visible_count
    mask_values = np.broadcast_to(token.reshape(1, 1, features), (batch, masked_count, features))
    shuffled = np.concatenate((visible, mask_values), axis=1)
    return np.take_along_axis(shuffled, restore[:, :, None], axis=1)
