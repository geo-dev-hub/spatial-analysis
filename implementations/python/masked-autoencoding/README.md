# Masked patch selection and restoration

A NumPy-only teaching example of two mechanics used in masked-autoencoder pipelines: selecting visible patch tokens and restoring the original sequence order with mask tokens.

## Install and test

    python -m pip install numpy pytest
    python -m pytest -q

## Example

    import numpy as np
    from masked_autoencoding import random_patch_masking, restore_masked_sequence

    # batch=2, patches=16, embedding dimensions=8
    tokens = np.random.default_rng(7).normal(size=(2, 16, 8))
    result = random_patch_masking(tokens, mask_ratio=0.75, seed=42)
    reconstructed_sequence = restore_masked_sequence(
        result.visible_tokens,
        mask_token=np.zeros(8),
        restore_indices=result.restore_indices,
    )

    print(result.visible_tokens.shape)  # (2, 4, 8)
    print(result.mask.shape)            # (2, 16)
    print(reconstructed_sequence.shape) # (2, 16, 8)

## Contract

- Input tokens have shape (batch, patches, features).
- Mask ratio is finite and in [0, 1); at least one visible patch is retained.
- Mask value 0 means visible and 1 means masked, in original sequence order.
- A seeded NumPy generator makes the selected positions reproducible.
- Restoration inserts a caller-supplied mask token and returns the original patch order.

## Limitations

This is not a trained MAE. It does not patchify images, encode visible patches, decode masked patches, calculate a reconstruction loss, handle multispectral/time-specific embeddings, or train a neural network. The returned restored sequence is only a layout scaffold for a decoder.

Read the [masked autoencoding method lesson](../../../methods/masked-autoencoding.md) and [intern walkthrough](implementation-walkthrough.md).
