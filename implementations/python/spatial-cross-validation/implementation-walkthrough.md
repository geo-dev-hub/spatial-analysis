# Intern walkthrough: spatial block cross-validation

## 1. Inspect coordinate inputs

The implementation accepts an (n, 2) numeric array. It does not know whether coordinates are metres, feet or degrees. Check the CRS before calling it. For a local buffer in metres, transform the data into an appropriate projected CRS first.

## 2. Assign each observation to a grid cell

For every point, subtract the grid origin, divide by block width and height, then apply floor. This produces an integer grid coordinate. Negative coordinates are valid: floor assigns them to the cell extending in the negative direction.

The code uses NumPy unique with return_inverse to turn occupied grid coordinates into compact group IDs. The IDs are labels, not geographic coordinates.

## 3. Assign whole blocks to folds

The implementation shuffles the unique occupied block IDs with NumPy's seeded random generator and divides them into n_splits groups. Every point in a block is therefore assigned to the same test fold.

The seed makes the same inputs reproducible. It does not make the fold design scientifically appropriate. Randomly grouped blocks can be scattered across the study area; use a region-held-out or contiguous-block design when that better represents deployment.

## 4. Apply the optional buffer

For each fold, every candidate training point is compared with every test point. The nearest Euclidean distance is calculated. A candidate is retained only if its nearest test point is at least the requested buffer distance away.

The implementation chunks this calculation to avoid constructing the entire candidate-by-test distance matrix at once. It remains a direct O(n_train × n_test) method, so it is intended for small teaching examples. Large projects should use a spatial index or a dedicated spatial cross-validation package.

## 5. Read the three index arrays

- Train indices are used to fit the model and all learned preprocessing.
- Test indices are used only to calculate held-out metrics.
- Excluded indices are neither training nor test observations in this fold.

Never concatenate excluded observations into the test set: they were removed to create separation, not sampled as an evaluation set.

## 6. Check fold diagnostics before modelling

For every fold, report the number of training, test and excluded observations; occupied blocks; response distribution; and geographic extent. A fold with one rare class missing may not support a meaningful classification metric. A fold with no training data is invalid and is rejected.

## 7. Extend the implementation

Try a contiguous region-held-out splitter, add a temporal grouping key, or use a spatial index to accelerate buffer queries. Add tests proving that no block crosses folds and that every test observation is held out exactly once.

## 8. What this code does not do

It does not estimate an autocorrelation range, choose a block width, construct a CRS, fit a model, perform nested hyperparameter tuning, or guarantee that held-out folds are independent. Those are research design decisions.
