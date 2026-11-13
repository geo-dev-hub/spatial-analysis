# Methods and analytical foundations

Not every useful entry in the source compendium is an algorithm. Some are mathematical objects, modelling choices, measurement systems or analysis workflows that several algorithms depend on.

This directory holds those foundational methods separately from individual algorithm records.

## Available foundations

- [Spatial weights matrix](spatial-weights-matrix.md) — define which spatial units are neighbours, how strongly they are connected and how those relationships are transformed.

- [Empirical semivariogram](empirical-semivariogram.md) — measure how observed values differ as the distance between locations changes; a foundation for variogram modelling and kriging.

## How to use these records

Each record should explain the question the method helps answer, its assumptions, its mathematical form, the choices that affect results, a reproducible example and its limitations. Where a method is a modelling choice rather than a single algorithm, say so explicitly.
