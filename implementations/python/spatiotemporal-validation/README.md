# Leave-location-and-time-out cross-validation

This package implements a strict, target-oriented leave-location-and-time-out (LLTO) fold generator.

For each observed location/time pair, all rows at that pair are the test set. Rows sharing the held-out location or held-out time, but not both, form a buffer excluded from training. Training contains only observations from other locations at other times. Every input row belongs to exactly one test fold. Fold order is deterministic and follows first appearance.

The function returns zero-based row indices for train, test and buffer. Only observed location/time combinations create folds. A fold with no training rows is returned explicitly rather than silently discarded.

## Install and run

    python -m pip install -r requirements.txt
    python -m pytest -q

## Design limits

- Location and time labels are caller-defined groups. The package does not derive spatial clusters, temporal blocks, distance buffers or temporal windows.
- The strict LLTO buffer can be large. Some folds may have no training rows.
- This is not rolling-origin forecasting, leave-one-location-out, leave-one-time-out, NNDM or kNNDM.
- The method tests joint transfer to held-out location/time combinations. It is not automatically right for every prediction target.
- It does not prevent leakage through duplicated entities, derived features, preprocessing or target construction. Fit preprocessing only within each training fold.
- This is a fold-index generator, not a model-training or scoring framework.

See walkthrough.md and the visual lab at ../../../notebooks/spatiotemporal-llto-lab.ipynb.
