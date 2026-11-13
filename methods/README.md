# Methods and analytical foundations

Not every useful entry in the source compendium is an algorithm. Some are mathematical objects, modelling choices, measurement systems or analysis workflows that several algorithms depend on.

This directory holds those foundational methods separately from individual algorithm records.

## Available foundations

- [Helmert seven-parameter transformation](helmert-7-parameter.md) — transform geocentric XYZ coordinates using the explicitly named Position Vector rotation convention.

- [Masked autoencoding](masked-autoencoding.md) — reconstruct hidden patch content through an encoder-decoder pretraining objective; includes a scoped masking mechanics example.

- [Spatial cross-validation](spatial-cross-validation.md) — design geographic holdouts and buffered folds that better match the intended deployment setting.

- [Spatial weights matrix](spatial-weights-matrix.md) — define which spatial units are neighbours, how strongly they are connected and how those relationships are transformed.
- [ELECTRE outranking](electre-outranking.md) — compare discrete alternatives through concordance, discordance and outranking relations; this is a method-family overview, not an implementation.
- [TOPSIS](topsis.md) — rank a finite set of alternatives by distance from positive and negative ideal solutions.
- [Ordered Weighted Averaging](ordered-weighted-averaging.md) — aggregate ranked criterion values using order weights, distinct from named criterion importance weights.
- [Boolean and fuzzy overlay](boolean-and-fuzzy-overlay.md) — distinguish hard logical constraints from graded membership and compare fuzzy combination operators.
- [Analytic Hierarchy Process](analytic-hierarchy-process.md) — derive relative criterion priorities from reciprocal pairwise judgements and inspect consistency diagnostics.
- [Weighted linear combination](weighted-linear-combination.md) — combine standardised spatial criteria using relative weights, while keeping hard constraints and sensitivity analysis explicit.

## How to use these records

Each record should explain the question the method helps answer, its assumptions, its mathematical form, the choices that affect results, a reproducible example and its limitations. Where a method is a modelling choice rather than a single algorithm, say so explicitly.
