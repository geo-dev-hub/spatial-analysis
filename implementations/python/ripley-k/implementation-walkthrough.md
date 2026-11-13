# Intern walkthrough: Ripley's K and L functions

## 1. Count pairs within a distance

For each radius r, count all ordered pairs of distinct events whose distance is at most r. If an unordered pair is within the radius, it contributes two ordered pairs: i to j and j to i.

## 2. Estimate K(r)

For n events in a study window of area A, the uncorrected estimator is:

$$
\hat K(r)=\frac{A}{n^2}\sum_{i\ne j}\mathbf{1}(d_{ij}\le r)
$$

Under homogeneous Poisson complete spatial randomness on the infinite plane, the theoretical value is:

$$
K(r)=\pi r^2
$$

## 3. Transform to L(r)

A common variance-stabilising transform is:

$$
L(r)=\sqrt{\frac{K(r)}{\pi}}
$$

Under the same CSR reference, L(r)=r. The difference L(r)-r is sometimes plotted as a descriptive comparison, but inference requires an appropriate edge correction and simulation or analytical reference.

## 4. Implementation strategy

The teaching implementation calculates all unique pair distances once, sorts them, and uses binary search to count distances at or below each requested radius. This is efficient across multiple radii but stores O(n²) distances.

## 5. Edge effects are not optional in serious analysis

For points near the observation-window boundary, potential neighbours outside the window are unobserved. The uncorrected estimator can therefore be biased. Common corrections include translation, isotropic and border corrections; each has assumptions and different behaviour.

This package applies none of them. It does not produce confidence envelopes or p-values. Do not use it to claim statistically significant clustering.

## 6. Validate and extend

Tests cover inclusive radius thresholds, ordered-pair counting, monotonicity and invalid inputs. Extensions should add one edge correction at a time, compare it with a reference implementation and use simulation envelopes under a clearly stated null model.
