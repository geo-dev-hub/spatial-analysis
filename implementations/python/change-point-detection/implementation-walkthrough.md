# Intern walkthrough: CUSUM, binary segmentation and PELT

All three examples use a deliberately narrow target: univariate piecewise-constant mean changes. This makes their different inferential questions visible.

For a segment [a,b), the cost is SSE = sum((y_t - segment_mean)^2). Prefix sums and squared-prefix sums evaluate this cost in constant time.

## CUSUM
Maintain upper and lower evidence:
S+_t=max(0,S+_(t-1)+y_t-mu0-k)
S-_t=max(0,S-_(t-1)+mu0-y_t-k)
An alarm is emitted when either exceeds its threshold. Thresholds require calibration for the monitoring process.

## Binary segmentation
For each current interval, find the split with the greatest reduction in SSE. Accept only when the gain exceeds the supplied penalty, then process the two subintervals. The greedy choice is not generally globally optimal.

## PELT
Minimise sum of segment costs plus beta times the number of changes. Dynamic programming stores the best objective for every prefix and its preceding change. The SSE cost satisfies the pruning condition with K=0. A brute-force test enumerates all admissible partitions on a small series to check the result. Worst-case runtime remains quadratic.

A detected shift is not a causal explanation. Seasonality, serial dependence, cloud contamination, sensor transitions and spatial multiplicity need separate treatment.


## Pettitt's test\n\nFor every split t, compare all observations on the left with all observations on the right. The signed statistic is the sum of pairwise signs; equivalently, with average ranks for ties, U_t = 2 sum(r_i, i≤t) − t(n+1). Select the split maximising |U_t|. The returned p-value uses the conventional large-sample approximation 2 exp(−6K²/(n³+n²)), capped at one. The selected split is a candidate, not proof of a physical event. The standard null assumes independent observations; autocorrelation and spatial multiple testing need adjusted inference.\n\n## Bayesian online change-point detection

Maintain a posterior over run length r, the number of observations since the latest change. The growth branch extends each run with probability 1-H and its posterior predictive likelihood. The change branch resets to run length zero with hazard H and the prior predictive likelihood. Normalise the combined masses to obtain P(r_t | y_1:t).

This implementation uses a Normal prior for the segment mean and known Gaussian observation variance, so predictive likelihoods and posterior updates are conjugate. A constant hazard implies a geometric prior on segment duration. The posterior mass at run length zero is the online change probability. This is not retrospective global segmentation.
