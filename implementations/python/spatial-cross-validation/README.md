# Spatial block cross-validation in Python

A NumPy-only, transparent implementation for teaching spatial validation with point observations. It assigns observations to fixed planar grid blocks, assigns whole blocks to folds, and optionally removes training points closer than a specified distance to test points.

## Install and test

    python -m pip install numpy pytest
    python -m pytest -q

## Example

    import numpy as np
    from spatial_cross_validation import spatial_block_folds

    # Coordinates are projected metres in this hypothetical example.
    xy = np.array([
        [500_000, 9_800_000], [500_300, 9_800_200],
        [501_100, 9_800_100], [501_400, 9_800_300],
        [502_200, 9_800_100], [502_500, 9_800_300],
        [503_100, 9_800_200], [503_400, 9_800_400],
    ], dtype=float)

    folds = spatial_block_folds(
        xy,
        n_splits=4,
        block_size=1_000,
        buffer_distance=250,
        origin=(500_000, 9_800_000),
        seed=42,
    )

    for number, fold in enumerate(folds, start=1):
        print(
            number,
            "train", len(fold.train_indices),
            "test", len(fold.test_indices),
            "excluded", len(fold.excluded_indices),
        )

## Output contract

Each SpatialFold contains three arrays of integer row indices:
- train_indices: observations available for fitting in this fold;
- test_indices: observations reserved for evaluating this fold;
- excluded_indices: candidate training observations removed by the buffer.

Test observations are assigned exactly once across returned folds. Whole grid blocks stay together. Buffered observations are not silently moved into the test set.

## Important assumptions

- Coordinates must be finite planar x/y values in a suitable projected CRS. Block size and buffer distance use the coordinate units.
- block_size may be one scalar (square blocks) or (width, height).
- Grid origin affects block membership; report it and test sensitivity to reasonable shifts.
- Whole blocks are assigned to folds using a seeded random permutation. This is reproducible but does not guarantee contiguous test regions.
- Buffer distance is measured from each candidate training point to its nearest test point. The direct calculation is intended for small datasets.
- A large buffer can remove all training data in a fold; the function raises an error instead of silently returning an invalid split.
- This is a splitter, not a complete model-validation pipeline. Fit preprocessing and tune hyperparameters inside training folds only.

Read the [spatial cross-validation lesson](../../../methods/spatial-cross-validation.md) and [intern walkthrough](implementation-walkthrough.md).


## Additional splitters

The package also includes buffered leave-one-out (one test observation per fold, with nearby candidate training observations excluded) and spatial k-fold by clustering (deterministic farthest-first k-means on projected coordinates, with each cluster held out as one fold).

Cluster folds need not be equal-sized, contiguous or aligned with meaningful administrative/ecological regions. They are a reproducible grouping baseline, not NNDM/kNNDM. Buffered leave-one-out is O(n²) and intended for teaching-sized samples.


- [Cluster, buffered LOO and block-split lab](../../../notebooks/spatial-cross-validation-splitters-lab.ipynb)
