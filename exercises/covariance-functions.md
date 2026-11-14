# Exercise: covariance functions and valid matrices

**Starting point:** [Stationary covariance functions](../methods/stationary-covariance-functions.md) and the [covariance implementation](../implementations/python/covariance-functions/README.md).

## 1. Notice

For a fixed variance of 2, compare the exponential and Gaussian correlation values at distances 0, 0.5, 1 and 2 when the range scale is 1. Which model retains more correlation at the middle distances?

## 2. Predict

Before running the code, predict what happens to off-diagonal covariance values when the range scale doubles. Keep the point locations and marginal variance fixed.

## 3. Trace

Choose three sites and calculate their pairwise Euclidean distances by hand. Use the exponential formula to calculate the covariance matrix. Check that the diagonal equals the marginal variance.

## 4. Investigate validity

Run the matrix diagnostics for each of the five models on at least three different point sets. Record the smallest eigenvalue. Explain why a successful finite numerical check does not prove universal positive definiteness.

## 5. Build

Add one more supported Euclidean covariance model. Document its formula, dimension conditions and source. Add tests for symmetry, diagonal variance, positive semidefiniteness on multiple fixtures and invalid parameters.

## 6. Challenge the geometry

Explain why a planar Gaussian covariance formula cannot simply be combined with great-circle distance and assumed valid. Find a spherical covariance construction from the cited literature and write down the conditions that make it valid. Do not implement it until the domain and theorem assumptions are clear.

**Submission:** a short explanation, a reproducible notebook or script, tests and a source note. No external dataset is required.
