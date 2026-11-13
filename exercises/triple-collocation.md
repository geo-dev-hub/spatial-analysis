# Exercise: validate three Earth-observation products without a reference

## Scenario

Three independently produced gridded products estimate the same environmental variable. You have already matched their values by location and time, but you do not have a trusted reference dataset.

Your task is to use triple collocation carefully, then investigate whether its assumptions are plausible.

## Part A — Reproduce the baseline

1. Install the requirements and run the test suite.
2. Generate three products from a shared synthetic signal with different gains, offsets and noise levels.
3. Estimate the three error variances.
4. Compare estimates with the known simulated noise variances.
5. Increase the sample size and repeat the experiment. Describe how the estimates change.

## Part B — Break the assumptions

1. Add a shared noise component to products 1 and 2. What happens to the estimates?
2. Make the noise variance increase with the signal magnitude.
3. Add a nonlinear response to one product.
4. Restrict the sample to one season and compare it with a second season.
5. Create a product with almost no shared signal and inspect the cross-covariance diagnostic.

Do not assume the estimate must get worse in every small experiment. Record the random seed, sample size and exact data-generating process.

## Part C — Design a real collocation study

Write a one-page protocol covering:

- the target variable and units;
- spatial and temporal matching rules;
- product quality masks;
- differences in footprint, resolution and compositing;
- possible shared inputs or calibration dependencies;
- stationarity and signal-range checks;
- how negative or unstable estimates will be reported;
- how uncertainty and regional variation will be investigated.

## Deliverable

Submit the notebook or script, test output, a short results table and the collocation protocol. Include at least one example where the method's assumptions are doubtful and explain why the result should not be treated as a definitive product ranking.
