# Methods and analytical foundations

Not every useful entry in the source compendium is an algorithm. Some are mathematical objects, modelling choices, measurement systems or analysis workflows that several algorithms depend on.

This directory holds those foundational methods separately from individual algorithm records.

## Available foundations

- [Adaptive and Bayesian spatial sampling](adaptive-and-bayesian-spatial-sampling.md) — distinguish design-based adaptive cluster sampling from Bayesian optimisation, active learning and spatial bandit designs.

- [Spatial data formats and delivery](spatial-data-formats.md) — choose raster, array, vector, catalogue and tile formats by workload and access pattern.

- [Affine georeferencing](affine-georeferencing.md) — estimate a six-parameter 2D transformation from ground control points and inspect residuals.

- [Helmert seven-parameter transformation](helmert-7-parameter.md) — transform geocentric XYZ coordinates using the explicitly named Position Vector rotation convention.

- [Masked autoencoding](masked-autoencoding.md) — reconstruct hidden patch content through an encoder-decoder pretraining objective; includes a scoped masking mechanics example.

- [Spatial cross-validation](spatial-cross-validation.md) — design geographic holdouts and buffered folds that better match the intended deployment setting.
- [Empirical semivariogram](empirical-semivariogram.md) — summarize how pairwise value differences change with spatial separation before fitting a theoretical variogram.

- [Spatial weights matrix](spatial-weights-matrix.md) — define which spatial units are neighbours, how strongly they are connected and how those relationships are transformed.
- [ELECTRE outranking](electre-outranking.md) — compare discrete alternatives through concordance, discordance and outranking relations; includes a scoped relation builder and exact small-instance kernel enumerator that reports no-kernel and multiple-kernel cases.
- [TOPSIS](topsis.md) — rank a finite set of alternatives by distance from positive and negative ideal solutions.
- [Ordered Weighted Averaging](ordered-weighted-averaging.md) — aggregate ranked criterion values using order weights, distinct from named criterion importance weights.
- [Boolean and fuzzy overlay](boolean-and-fuzzy-overlay.md) — distinguish hard logical constraints from graded membership and compare fuzzy combination operators.
- [Analytic Hierarchy Process](analytic-hierarchy-process.md) — derive relative criterion priorities from reciprocal pairwise judgements and inspect consistency diagnostics.
- [Weighted linear combination](weighted-linear-combination.md) — combine standardised spatial criteria using relative weights, while keeping hard constraints and sensitivity analysis explicit.
- [Weights of evidence](weights-of-evidence.md) — estimate positive and negative associations for binary spatial evidence and combine them in log-odds space under a conditional-independence assumption.

- [Marine heatwave detection](marine-heatwave-detection.md) — identify prolonged threshold exceedances relative to a seasonal baseline, distinguish point events from spatial tracking and inspect missing-data rules.

- [Exact orientation predicate](exact-orientation-predicate.md) — classify 2D point triples with a rational reference predicate and understand why production geometry kernels use adaptive precision.
- [Stationary covariance functions](stationary-covariance-functions.md) — compare Euclidean covariance shapes, check finite covariance matrices and understand why geometry-specific validity conditions matter.
- [Isotropic covariance on the two-sphere](isotropic-covariance-on-the-sphere.md) — construct valid scalar isotropic covariance models from non-negative Legendre coefficients and distinguish spherical from planar distance models.
- [Graph-spectral covariance](graph-spectral-covariance.md) — construct positive-semidefinite covariance matrices on finite undirected graphs from non-negative Laplacian spectral variances, without assuming arbitrary shortest-path kernels are valid.
- [Nonseparable space-time covariance](nonseparable-space-time-covariance.md) — model spatial and temporal dependence jointly with a valid Gneiting-class construction on Euclidean space and linear time.

## How to use these records

Each record should explain the question the method helps answer, its assumptions, its mathematical form, the choices that affect results, a reproducible example and its limitations. Where a method is a modelling choice rather than a single algorithm, say so explicitly.
