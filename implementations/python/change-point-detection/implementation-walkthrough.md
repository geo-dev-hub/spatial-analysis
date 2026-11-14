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
