# Exercise: Ripley's K/L and simulation envelopes

## Part A — Edge effects

1. Draw a rectangular observation window and place one event near its left edge.
2. Explain which neighbours are unobserved beyond the boundary.
3. Calculate the translation overlap area for a displacement of (1, 0) in a 4×3 window.
4. Explain why the translation weight increases as overlap decreases.

## Part B — Conditional CSR

1. Explain what is held fixed when the package simulates conditional CSR.
2. Why are the simulated event locations uniform in the study window?
3. Why must the same edge correction and radii be used for the observed and simulated curves?
4. What is the smallest possible p-value with 99 simulations?

## Part C — Pointwise versus global inference

1. Plot the observed L(r) curve with the pointwise simulation quantile bands.
2. Explain why a pointwise band does not control the chance of an excursion somewhere across the full radius interval.
3. Describe the studentised maximum-deviation statistic.
4. Why does changing the radius interval change the global test?
5. Why is the global test not a complete rank-envelope test?

## Part D — Model criticism

1. Give an example of a spatial process for which homogeneous CSR is a poor null model.
2. What changes if intensity varies across the study window?
3. Why should the analyst choose the radius interval before interpreting the result?
4. What additional complications arise when model parameters are estimated from the observed point pattern?

Run the [Ripley's K/L notebook](../notebooks/ripley-k-lab.ipynb), inspect the implementation and record the seed, number of simulations, alpha, radius interval, study window and null model. Do not report pointwise bands as simultaneous confidence bands.
