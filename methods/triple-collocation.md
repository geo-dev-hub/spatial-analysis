# Triple collocation: estimate product error without a trusted reference

Triple collocation (TC) estimates the random-error variance of three collocated measurement products. It is useful in Earth observation when three systems observe the same geophysical variable but no independent, high-quality reference is available.

It is not a way to discover the true value, and it does not make three related products independent. Its estimates are only meaningful when the measurement model and error assumptions are defensible.

## Learning objectives

By the end of this lesson, you should be able to:

- explain the linear measurement model used by classical TC;
- derive the three error-variance estimates from sample covariances;
- prepare matched observations without silently pairing different places or times;
- interpret negative or unstable estimates as diagnostics, not values to clip;
- explain why shared retrieval inputs can invalidate the independence assumption.

## 1. The measurement model

For three systems, write

\[
X_i = a_i + b_i T + \varepsilon_i, \qquad i\in\{1,2,3\},
\]

where:

- \(T\) is the unknown geophysical signal;
- \(a_i\) is an additive offset;
- \(b_i\) is a multiplicative gain;
- \(\varepsilon_i\) is the random error for system \(i\).

The classical formulation assumes that the errors have zero mean, are uncorrelated with the true signal, and are mutually uncorrelated across systems. The relationship between each product and the underlying signal is assumed to be adequately linear over the analysed sample, with sufficiently stable signal and error statistics.

The three products must represent the same variable over matched support. Matching timestamps alone is not enough if their footprints, resolutions, temporal compositing windows or physical definitions differ.

## 2. Derive the error variance

Let \(C_{ij}=\operatorname{Cov}(X_i,X_j)\). Under the assumptions above, for distinct systems,

\[
C_{ij}=b_i b_j\operatorname{Var}(T).
\]

The variance of product \(i\) is

\[
\operatorname{Var}(X_i)=b_i^2\operatorname{Var}(T)+\operatorname{Var}(\varepsilon_i).
\]

Use the cross-covariances to estimate the signal component in product \(i\)'s scale:

\[
\frac{C_{ij}C_{ik}}{C_{jk}}
=
\frac{(b_i b_j V_T)(b_i b_k V_T)}{b_j b_k V_T}
=b_i^2 V_T.
\]

Subtract this from the observed variance:

\[
\boxed{
\widehat{\sigma}_{\varepsilon_i}^{2}
=s_i^2-\frac{s_{ij}s_{ik}}{s_{jk}}
}
\]

where \(s_i^2\) and \(s_{ij}\) are sample variances and covariances. For three products, calculate one estimate for each product by cycling the indices:

\[
\begin{aligned}
\widehat{\sigma}_{\varepsilon_1}^{2}
&=s_1^2-\frac{s_{12}s_{13}}{s_{23}},\\
\widehat{\sigma}_{\varepsilon_2}^{2}
&=s_2^2-\frac{s_{12}s_{23}}{s_{13}},\\
\widehat{\sigma}_{\varepsilon_3}^{2}
&=s_3^2-\frac{s_{13}s_{23}}{s_{12}}.
\end{aligned}
\]

These are error variances in each product's own measurement units squared. They are not directly comparable if the products use different units or scales. A common scaled-error metric may be useful for comparison, but it requires additional interpretation.

## 3. A small numerical example

The example below constructs a latent signal and three independent noisy products. The latent signal is visible only because this is a simulation; real applications do not have it.

```python
import numpy as np
from triple_collocation import triple_collocation

rng = np.random.default_rng(2026)
truth = rng.normal(loc=0.25, scale=0.12, size=5000)

x = 0.3 + 1.0 * truth + rng.normal(0, 0.04, truth.size)
y = -0.1 + 1.4 * truth + rng.normal(0, 0.07, truth.size)
z = 0.8 + 0.7 * truth + rng.normal(0, 0.05, truth.size)

result = triple_collocation(x, y, z)
print(result.error_variances)
```

The estimates should be close to the simulated noise variances (0.04², 0.07² and 0.05²), subject to finite-sample variation. Do not expect exact equality.

## 4. Data preparation is part of the method

A defensible collocation table needs one row per matched observation and one column per product. Before estimating TC:

1. Define the physical variable and units.
2. Choose the spatial and temporal support at which products are meaningfully comparable.
3. Apply quality flags and remove invalid retrievals using product-specific rules.
4. Match observations using a documented spatial and temporal tolerance.
5. Record how many observations were discarded and why.
6. Check scatterplots, pairwise correlations, ranges and spatial/temporal coverage.
7. Consider whether products share training data, assimilation inputs, calibration sources or retrieval components.

The teaching implementation accepts three already-collocated one-dimensional arrays. It does not perform geospatial matching, reprojection, aggregation or quality control.

## 5. Diagnostics and failure modes

- **Negative estimate:** do not clip it to zero. It can indicate sampling noise, weak cross-covariance, incompatible supports or violated assumptions.
- **Near-zero denominator covariance:** the estimate becomes unstable. A product may have little shared signal with another, or the sample may not identify the model.
- **Correlated errors:** shared retrieval algorithms, common model forcing, data assimilation or calibration sources can bias estimates.
- **Nonlinear or signal-dependent errors:** one constant error variance may hide poor performance in particular ranges of the target variable.
- **Nonstationarity:** a single estimate can conceal regional, seasonal or regime-specific differences.
- **Different spatial supports:** representativeness error can be mistaken for measurement error.

A positive estimate is not proof that the assumptions hold. Inspect the data-generating process and repeat the analysis across meaningful strata where appropriate.

## 6. What this implementation does and does not do

The NumPy baseline:

- removes rows where any of the three products is non-finite, using one common sample;
- calculates sample covariance with a consistent complete-case set;
- returns the three classical error-variance estimates and the covariance matrix;
- rejects too few observations and near-zero denominator covariances;
- preserves negative estimates so they remain visible as diagnostics.

It does not estimate confidence intervals, correct correlated errors, fit nonlinear error models, identify an optimal product triplet or resolve scale/support mismatch.

## 7. Further reading

- Gruber et al., “Recent advances in (soil moisture) triple collocation analysis” (2016), a review of assumptions and error metrics: https://doi.org/10.1016/j.jag.2015.09.002
- Siu et al. (2024), “Summarizing multiple aspects of triple collocation analysis in a single diagram”: https://doi.org/10.3389/frsen.2024.1395442
- Balasubramaniam and Ruf (2025), analysis of non-ideal error statistics and correlated errors: https://doi.org/10.3390/rs17223751

The 2025 study is a useful reminder that correlated errors and scale deviations can materially affect classical estimates. Read the assumptions in each paper rather than treating TC as a universal validation score.

## Check your understanding

1. Why does the formula use cross-covariances rather than the variance of each product alone?
2. Why must all three products use the same matched rows?
3. What might a negative error-variance estimate tell you?
4. Give two realistic reasons why errors from two satellite products might be correlated.
5. Why is an error variance in product units squared not automatically comparable across products?
6. How could you test whether error behaviour changes between wet and dry conditions?

## Implementation and practice

- [Python implementation and tests](../implementations/python/triple-collocation/README.md)
- [Worked implementation walkthrough](../implementations/python/triple-collocation/implementation-walkthrough.md)
- [Exercise](../exercises/triple-collocation.md)
