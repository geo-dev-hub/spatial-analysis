# Ripley's K and L functions for planar point patterns

Stable ID: `SA-STAT-RIPLEY-K` · Draft 0.1 · Source compendium section 2, page 3

## The question

At what spatial scales are events more or less concentrated than expected under a chosen point-process reference?

Ripley's K function summarises the number of other events found within distance r of a typical event, adjusted by overall point intensity. It is a multi-scale point-pattern statistic: unlike a single nearest-neighbour index, it describes a range of distances.

## K function

For n events in a study window of area A, an uncorrected estimator is:

$$
\hat K(r)=\frac{A}{n^2}\sum_{i\ne j}\mathbf{1}(d_{ij}\le r)
$$

The sum counts ordered pairs of distinct events whose distance is at most r. Under homogeneous Poisson complete spatial randomness (CSR) on the infinite plane:

$$
K(r)=\pi r^2
$$

## L transformation

A common transformation is:

$$
L(r)=\sqrt{\frac{K(r)}{\pi}}
$$

Under the same reference, L(r)=r. The curve L(r)-r is often inspected across scales. A positive value suggests more pairs within distance r than the CSR expectation; a negative value suggests fewer. A formal claim requires an appropriate inferential procedure.

## Edge correction matters

A finite observation window omits potential neighbours outside its boundary. Uncorrected pair counts are therefore biased, particularly at larger radii and near the window edge.

Common approaches include translation correction, isotropic correction and border correction. They are not interchangeable and each depends on the observation-window geometry. The [teaching implementation](../../implementations/python/ripley-k/README.md) deliberately implements only the uncorrected estimator so the pair-counting and K/L transformations remain visible.

It does not calculate confidence envelopes, Monte Carlo p-values or significance tests. Do not interpret the uncorrected curve as inferential evidence.

## Complexity and limits

The implementation stores all unique pair distances, requiring O(n²) memory. It sorts them once and uses binary search for each radius. It is a small-data teaching baseline, not a scalable spatial-index implementation.

The CSR reference assumes a homogeneous Poisson process. Inhomogeneous intensity, barriers, anisotropy and network-constrained movement require different models.

## Exercises

1. Calculate K(r) for two points at distance one in a 2×2 window.
2. Plot K(r) and πr² for a synthetic point pattern.
3. Transform K to L and compare L(r)-r across distance scales.
4. Explain why the uncorrected estimator is biased near the boundary.
5. Compare translation and isotropic edge correction conceptually.
6. Why does a positive L(r)-r curve not automatically prove statistically significant clustering?

## References

- Ripley, B. D. (1976), *The second-order analysis of stationary point processes*, Journal of Applied Probability, 13(2), 255–266.
- Ripley, B. D. (1977), *Modelling spatial patterns*, Journal of the Royal Statistical Society: Series B, 39(2), 172–212.

**Scope:** uncorrected and translation-corrected K/L summaries for planar point patterns; no isotropic/border correction, confidence envelope or inferential test is implemented.
