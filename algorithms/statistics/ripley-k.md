# Ripley's K and L: point patterns across distance scales

Stable ID: `SA-STAT-RIPLEY-K` · Draft 0.2 · Source compendium section 2, page 3

## The question

At what spatial scales are events more or less concentrated than expected under a chosen point-process model?

Ripley's K summarises the number of other events found within distance r of a typical event, adjusted by overall point intensity. It is a multi-scale statistic: unlike a single nearest-neighbour index, it describes a range of distances.

## K and L functions

For n events in a study window W of area A, an uncorrected estimator is:

$$
\hat K(r)=\frac{A}{n^2}\sum_{i\ne j}\mathbf{1}(d_{ij}\le r).
$$

The sum counts ordered pairs of distinct events whose distance is at most r. Under homogeneous Poisson complete spatial randomness (CSR) on the infinite plane:

$$
K(r)=\pi r^2.
$$

A common transformation is:

$$
L(r)=\sqrt{\frac{K(r)}{\pi}}.
$$

Under the same reference, L(r)=r. The curve L(r)-r is often inspected across scales. A positive value indicates more close pairs than the CSR reference at that scale; a negative value indicates fewer. Formal interpretation requires a defined null model and an appropriate inferential procedure.

## Translation edge correction

A finite observation window omits potential neighbours outside its boundary. Uncorrected pair counts are therefore biased, particularly at larger radii and near the window edge.

For a pair of events separated by displacement h, translation correction weights the pair by:

$$
w(h)=\frac{|W|}{|W\cap(W-h)|}.
$$

For a rectangular window of width a and height b, the overlap area is:

$$
|W\cap(W-h)|=(a-|h_x|)(b-|h_y|),
$$

provided both factors are positive. The corrected estimator replaces each pair indicator with its translation weight:

$$
\hat K_{\mathrm{trans}}(r)=\frac{A}{n^2}
\sum_{i\ne j}
\frac{A}{|W\cap(W-(x_j-x_i))|}
\mathbf{1}(d_{ij}\le r).
$$

This implementation uses the rectangular-window translation correction and rejects a pair displacement with zero overlap. Translation correction assumes stationarity; it is not a universal fix for an inhomogeneous point process.

## Simulation under conditional CSR

The package now provides a Monte Carlo comparison for homogeneous CSR conditional on the observed event count n:

1. Keep the rectangular study window and observed number of events fixed.
2. Generate n independent uniform locations in that window for each simulation.
3. Calculate translation-corrected L(r) for the observed pattern and every simulation using the same radii.
4. Return pointwise simulation quantiles for visual inspection.
5. Calculate a global studentised maximum absolute deviation statistic over the preselected radius vector and its Monte Carlo p-value.

Let T_b(r) denote the L curve for the observed pattern and the simulated patterns. The curves are centred and scaled symmetrically using their joint mean and standard deviation at each radius. The global statistic for curve b is:

$$
T_b=\max_{r\in R}
\left|
\frac{L_b(r)-\bar L(r)}{s(r)}
\right|.
$$

The Monte Carlo p-value is:

$$
p=\frac{1+\sum_{b=1}^{B}\mathbf{1}(T_b\ge T_0)}{B+1}.
$$

The observed curve and simulations are treated symmetrically in the centring and scaling step. The test is global over the radius vector supplied by the analyst. Changing the radius range changes the test.

**Do not confuse the two outputs.** The lower and upper quantile bands are pointwise envelopes; they do not control the probability of an excursion anywhere across the whole radius interval. The reported p-value comes from the separate global maximum-deviation statistic. This is a transparent teaching test, not the full rank-envelope procedures implemented by specialist spatial-statistics software.

The smallest possible Monte Carlo p-value is 1/(B+1). Use enough simulations for the resolution required by the question. A small number of simulations is useful for learning, not for a high-resolution inferential result.

## Complexity and limits

The pair-distance calculation stores O(n²) distances. The simulation extension repeats the calculation B times, so its work is approximately O(B n²) plus the cost of sorting and evaluating the requested radii. It is intended for small planar point patterns.

The null model is homogeneous CSR conditional on n. It does not model an inhomogeneous intensity surface, barriers, anisotropy, clustering processes, inhibition processes or network-constrained movement. It does not implement isotropic or border correction, a rank envelope test, or parameter-estimation adjustments. If model parameters are estimated from the observed pattern, simulation calibration needs additional care.

## Exercises

1. Calculate K(r) for two points at distance one in a 2×2 window.
2. Compare uncorrected and translation-corrected K(r) near a rectangular boundary.
3. Explain why the overlap area appears in the translation weight.
4. Run the conditional CSR simulation and compare the observed L curve with pointwise bands.
5. Explain why pointwise envelopes are not a global test across every radius.
6. Change the radius interval and simulation count. What changes in the global test?
7. Why is homogeneous CSR an unsuitable null model for some real urban point patterns?

## References

- Ripley, B. D. (1976), *The second-order analysis of stationary point processes*, Journal of Applied Probability, 13(2), 255–266.
- Ripley, B. D. (1977), *Modelling spatial patterns*, Journal of the Royal Statistical Society: Series B, 39(2), 172–212.
- Baddeley, A., Diggle, P. J., Hardegen, A., Lawrence, T., Milne, R. K. and Nair, G. (2014), *On tests of spatial pattern based on simulation envelopes*, Ecological Monographs, 84, 477–489. https://doi.org/10.1890/13-2042.1
- Myllymäki, M., Mrkvička, T., Grabarnik, P., Seijo, H. and Hahn, U. (2017), *Global envelope tests for spatial processes*, Journal of the Royal Statistical Society: Series B, 79(2), 381–404. https://doi.org/10.1111/rssb.12172

**Scope:** uncorrected and translation-corrected K/L summaries plus a conditional homogeneous-CSR Monte Carlo teaching test with pointwise bands and a global studentised maximum-deviation p-value. No isotropic/border correction or specialist rank-envelope procedure is implemented.
