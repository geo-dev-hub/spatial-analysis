# Implementation walkthrough: triple collocation

This walkthrough follows the code in `triple_collocation.py`. The aim is to make each numerical decision reproducible.

## 1. Start with the data contract

The function receives three one-dimensional arrays. Equal length is necessary because row 17 in each array must refer to the same matched observation. It is not sufficient to establish that the observations are genuinely comparable; that work belongs in the data-preparation workflow.

## 2. Validate and align

Each input is converted to a floating-point NumPy array. The function rejects matrices and unequal lengths. It then stacks the three arrays into one table and retains only rows where all three values are finite.

Why use a common sample? Each covariance must describe the same set of observations. Pairwise deletion could calculate each covariance from a different subset, breaking the algebra that links the three covariances.

## 3. Estimate covariance

`np.cov(..., rowvar=False, ddof=1)` returns the sample covariance matrix. The diagonal contains the three sample variances; the off-diagonal entries contain pairwise sample covariances.

## 4. Calculate each error variance

For product 1:

[
\hat\sigma_{e_1}^{2}=s_1^2-\frac{s_{12}s_{13}}{s_{23}}.
]

The other two estimates follow by cycling the product indices. Each result remains in that product's units squared.

## 5. Protect against an unidentified ratio

If a denominator covariance is zero or extremely small, the estimate is undefined or numerically unstable. The function raises a clear error. The tolerance is an absolute covariance threshold, so users working at very different scales may need to choose a scale-appropriate value.

## 6. Keep uncomfortable results visible

A negative estimate is not a physically meaningful negative noise variance. It is a warning that sampling variation or violated assumptions make the classical decomposition inconsistent with this sample. The implementation does not silently replace it with zero.

## 7. Reproduce the tests

Run:

```bash
python -m pytest implementations/python/triple-collocation/test_triple_collocation.py
```

The tests cover recovery on synthetic data, joint complete-case filtering, negative estimates, shape and length validation, insufficient observations, zero covariance and invalid tolerance.

## Scope boundary

This package does not estimate uncertainty intervals, perform spatial/temporal matching, fit extended TC models or diagnose correlated errors. Those require additional statistical and domain-specific decisions.
