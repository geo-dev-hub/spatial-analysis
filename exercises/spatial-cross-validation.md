# Spatial cross-validation exercises

Use the [spatial cross-validation lesson](../methods/spatial-cross-validation.md) and its [Python implementation](../implementations/python/spatial-cross-validation/README.md). Work with a small synthetic point dataset first; do not use sensitive locations.

## 1. Predict the leakage

Create 30 points along a 2 km road corridor, spaced 50 m apart. Randomly split rows into 80% training and 20% test.

- Draw the split on a map.
- Count how many test points have a training point within 100 m.
- Explain why a high score on this split may overstate transfer to another corridor.

## 2. Assign grid blocks

Use the implementation to assign 250 m square blocks.

- Verify that points in the same grid cell share a block.
- Shift the grid origin by 125 m and compare the groups.
- Explain why block origin is part of the validation specification.

## 3. Build buffered folds

Create four folds with a 250 m buffer.

- Record training, test and excluded counts for every fold.
- Confirm that every observation appears in a test set exactly once.
- Confirm that no retained training point is closer than the buffer to a test point.
- Explain why excluded observations are not additional test observations.

## 4. Choose a design for a real deployment question

Choose one: interpolate within a city, predict in a new county, map a new sensor scene, or forecast next season.

- State the prediction target and deployment setting.
- Choose a spatial and/or temporal grouping that reproduces that setting.
- Justify block size and buffer using sampling geometry, sensor footprint and spatial dependence evidence.
- Identify any mismatch between the proposed validation and deployment.

## 5. Prevent preprocessing leakage

Suppose a model uses missing-value imputation, feature scaling, feature selection and hyperparameter tuning.

- Mark which operations must be fitted inside each training fold.
- Draw a nested validation diagram for tuning and final evaluation.
- Explain why fitting the scaler once on all observations leaks information.

## 6. Report geographic transfer

Write a one-page validation report with the CRS, units, block dimensions, origin, fold seed, buffer, excluded counts, per-fold sample sizes, response distribution, metrics and geographic performance gaps.

## Extension

Implement a contiguous region-held-out split or a time-aware spatial split. Do not describe it as equivalent to the grid-grouped random assignment. Add tests for its own invariants and failure modes.
