# Domain-classifier diagnostic for distribution shift

This package trains a classifier to distinguish source-domain feature rows from target-domain feature rows, then evaluates out-of-fold probabilities with ROC AUC and balanced accuracy.

AUC near 0.5 means this logistic-regression model has difficulty distinguishing the two domains in the supplied feature representation. A higher AUC indicates stronger distinguishability. This is a model-dependent diagnostic, not a calibrated hypothesis test.

## Leakage control

Feature scaling is inside a scikit-learn pipeline and is therefore fitted separately within each training fold. If spatial/temporal groups are supplied, StratifiedGroupKFold keeps each group in one fold. Without groups, ordinary stratified folds are used; spatial dependence may make that evaluation optimistic.

## Limits

- This tests distinguishability of X, not concept shift in P(Y|X).
- A low AUC does not prove the domains are identical; a different classifier, feature representation or nonlinear boundary may reveal differences.
- A high AUC does not identify the cause of shift or guarantee prediction error will increase.
- Feature engineering, scaling, feature selection and hyperparameter selection must not use held-out folds.
- Groups must encode meaningful independent spatial/temporal units. Grouped folds do not automatically make a valid spatial permutation test.
- It does not estimate density ratios or implement importance weighting/KMM.

Install with pip install -r requirements.txt; run python -m pytest -q. See walkthrough.md and the notebook.
