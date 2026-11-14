# Spatial distribution shift: two-sample tests and domain diagnostics

Spatial prediction often moves from a **source domain** (where observations were collected and a model was trained) to a **target domain** (where predictions or decisions will be made). The source and target may differ in geography, environmental covariates, sampling design, measurement process or the relationship between predictors and outcomes.

A distribution-shift diagnostic asks whether the observed source and target samples are distinguishable under a chosen representation and test. It does not, by itself, establish why they differ, prove that a model's error has changed, or tell us how to repair the model.

## 1. Define the shift before choosing a statistic

Let source observations be drawn from (P_s(X,Y)) and target observations from (P_t(X,Y)).

| Shift concept | What changes | What a two-sample test can inspect |
|---|---|---|
| Covariate shift | (P_s(X) \ne P_t(X)), while (P(Y\mid X)) is assumed stable | Predictor distributions |
| Label / prior shift | (P_s(Y) \ne P_t(Y)), with a stable (P(X\mid Y)) assumption | Outcome frequencies, when target labels exist |
| Concept shift | (P_s(Y\mid X) \ne P_t(Y\mid X)) | Requires labelled target information or additional assumptions; comparing X alone cannot detect it |
| Support / extrapolation shift | Target predictor combinations are poorly represented in source data | Support, nearest-neighbour and applicability diagnostics |
| Sampling / measurement shift | Inclusion probabilities, sensors, protocols or data processing differ | Sampling metadata and measurement diagnostics, not just a generic distance |

Spatial data add another layer: (X(s)) and (Y(s)) may be autocorrelated, non-stationary or clustered by sampling design. Nearby pixels are not automatically independent replicates. A large raster does not necessarily provide a large effective sample size.

Start by specifying the deployment question: prediction in a new region, a later period, a new sensor, a changed population, or a new environmental regime. The appropriate target sample and validation design depend on that question.

## 2. Maximum Mean Discrepancy (MMD)

MMD compares two distributions through their mean embeddings in a reproducing-kernel Hilbert space. For a function class \(\mathcal{F}\),

\[
\operatorname{MMD}(P,Q)
=\sup_{f\in\mathcal{F}}
\left|\mathbb{E}_{X\sim P}[f(X)]
-\mathbb{E}_{Y\sim Q}[f(Y)]\right|.
\]

When \(\mathcal{F}\) is the unit ball of an RKHS with kernel \(k\), the squared population discrepancy is

\[
\operatorname{MMD}^2(P,Q)
=\mathbb{E}[k(X,X')]
+\mathbb{E}[k(Y,Y')]
-2\mathbb{E}[k(X,Y)],
\]

where \(X,X'\) are independent draws from \(P\), and \(Y,Y'\) are independent draws from \(Q\).

For independent samples \(x_1,\ldots,x_m\) and \(y_1,\ldots,y_n\), the unbiased U-statistic estimate is

\[
\widehat{\operatorname{MMD}}_u^2 =
\frac{1}{m(m-1)}\sum_{i\ne j} k(x_i,x_j)
+\frac{1}{n(n-1)}\sum_{i\ne j} k(y_i,y_j)
-\frac{2}{mn}\sum_{i,j}k(x_i,y_j).
\]

The unbiased estimate can be negative in finite samples; that is not an implementation error. The population squared discrepancy is non-negative. Do not truncate the estimator to zero before a test unless the chosen procedure explicitly requires it.

A common starting kernel for scaled continuous predictors is the Gaussian RBF kernel:

\[
k_\sigma(x,y)=
\exp\left(-\frac{\lVert x-y\rVert^2}{2\sigma^2}\right).
\]

A characteristic kernel such as the Gaussian RBF can distinguish different probability distributions at the population level under its conditions. In practice, results depend on feature scaling, kernel family and bandwidth. Standardise using training/source information only; do not leak target outcomes or held-out test labels into model fitting or threshold selection. A median-distance bandwidth is a heuristic, not a universal optimum. Report sensitivity across plausible bandwidths.

The unbiased estimator above is derived for independent samples. A standard random permutation test is not automatically valid for spatially autocorrelated observations. Its null distribution relies on exchangeability of the pooled sample labels. For spatial data, the permutation unit and exchangeability assumptions must reflect the sampling design: for example, whole spatial blocks or independently sampled regions may be the relevant units. Blocks must be defined before looking at the test result, and their size must be justified against the dependence range and deployment question.

## 3. Energy distance

Energy distance compares distributions using expected pairwise distances:

\[
\mathcal{E}(P,Q)=
2\mathbb{E}\lVert X-Y\rVert
-\mathbb{E}\lVert X-X'\rVert
-\mathbb{E}\lVert Y-Y'\rVert.
\]

Under suitable conditions and a Euclidean metric, this is a non-negative measure that is zero exactly when the distributions agree. Its sample version uses cross-sample distances minus within-sample distances. Like MMD, the conventional two-sample test requires an appropriate null calibration; spatial dependence cannot be ignored simply because the statistic is distance-based.

Energy distance is useful as a complementary discrepancy because it does not require selecting an RKHS kernel bandwidth. Its result still depends on the feature metric and scaling. A Euclidean distance over mixed units (metres, degrees Celsius, elevation and categorical codes) is not meaningful without a defensible representation.

## 4. Domain-classifier diagnostics

Pool source and target predictor records, attach a domain label (source or target), and train a classifier to predict that label. Evaluate it on held-out data using a split that matches the intended deployment setting.

- A domain AUC near 0.5 indicates that the chosen classifier did not reliably separate the domains under this design.
- A high AUC indicates that the classifier can distinguish them; inspect which predictors, regions or periods drive that distinction.
- AUC is a discrimination measure, not a calibrated divergence, and depends on classifier capacity, sample size, class balance and validation design.

Do not randomly split adjacent pixels between classifier training and testing and then interpret a high AUC as independent evidence. Spatial leakage can inflate performance, and random splitting can make the test unrepresentative of a new-region deployment. Use region-, block- or time-aware splits where they match the question. A domain classifier is a diagnostic, not a proof that covariate shift is the only shift present.

## 5. Applicability and weighting are related, but distinct

**Area of Applicability (AOA)** methods ask where target predictor combinations are sufficiently similar to the training data for the model's validation error to be relevant. Meyer and Pebesma's dissimilarity-index approach weights predictor distances by model relevance and derives an applicability threshold in relation to the cross-validation design. AOA is an extrapolation diagnostic; it is not a distribution-equality test and is not a guarantee of accurate predictions inside the mapped area.

**Kernel Mean Matching (KMM)** chooses weights on source samples to make their kernel mean embedding resemble the target embedding. This is a reweighting strategy, not merely a test that source and target differ. It can be useful under covariate-shift assumptions, but requires overlap/support and weight-regularity considerations. Inspect the resulting weights, effective sample size and sensitivity. Extreme or concentrated weights can make an estimate unstable.

A 2026 study by Serov, Koldasbayeva and Zaytsev evaluates KMM for risk estimation under spatial distribution shifts. Treat it as a recent empirical contribution, not a universal guarantee that KMM will dominate in every geography, feature representation or deployment regime.

Spatial cross-validation and shift diagnostics answer different questions:

- Spatial cross-validation estimates performance under a chosen structured holdout.
- A two-sample test measures distinguishability between selected source and target samples.
- AOA flags predictor-space extrapolation relative to training support.
- Reweighting changes how source errors contribute to an estimated target risk.

Use them together where appropriate; none substitutes for the others.

## 6. A defensible spatial shift-analysis workflow

1. **Write the target estimand.** Define the target region/time/population and whether the goal is to describe predictor shift, estimate target risk, or decide where predictions are applicable.
2. **Audit provenance.** Align feature definitions, units, CRS, resolution, sensor processing, missingness, sampling frame and time windows.
3. **Separate the roles of variables.** Identify predictors, outcomes, identifiers, spatial coordinates and variables that may encode the sampling process. Do not let an ID or domain label become a shortcut feature.
4. **Map first.** Plot source and target samples, sampling intensity, environmental gradients and missing-data patterns. A scalar discrepancy can conceal where the difference occurs.
5. **Choose complementary diagnostics.** For example, MMD or energy distance for multivariate discrepancies, domain-classifier AUC for an interpretable discrimination check, and AOA for extrapolation support.
6. **Respect dependence.** Define blocks or independent sampling units from the study design and spatial dependence scale. Use a null procedure that preserves the dependence structure; do not permute individual pixels by default.
7. **Check scale and representation.** Repeat across defensible feature subsets, bandwidths and spatial aggregation scales. Report whether the conclusion is stable.
8. **Connect diagnostics to validation.** Evaluate model error on region/time holdouts representative of deployment. If reweighting, report weight distribution and effective sample size.
9. **Communicate uncertainty.** Report sample counts, independent units, confidence intervals or null distributions, effect sizes, test settings and known limits. A small p-value is not a measure of practical importance.

## 7. Common failure modes

- Treating every raster cell as an independent observation.
- Using random pixel permutations despite spatial autocorrelation.
- Interpreting a non-significant test as proof that source and target are equivalent.
- Treating domain-classifier AUC as a calibrated measure of divergence.
- Scaling predictors with information from the held-out target set.
- Comparing raw longitude/latitude degrees with physical distances without a suitable metric.
- Confusing predictor shift with concept shift.
- Assuming covariate reweighting repairs absent target support.
- Reporting a test p-value without an effect size, sample design or map.
- Treating AOA as a guarantee of prediction quality rather than a statement about applicability relative to the validation design.

## Further reading

- Gretton, A., Borgwardt, K. M., Rasch, M. J., Schölkopf, B. and Smola, A. (2012). “A Kernel Two-Sample Test.” *Journal of Machine Learning Research*, 13, 723–773. [Publisher paper](https://jmlr.org/papers/v13/gretton12a.html).
- Meyer, H. and Pebesma, E. (2021). “Predicting into unknown space? Estimating the area of applicability of spatial prediction models.” *Methods in Ecology and Evolution*, 12, 1620–1633. [DOI 10.1111/2041-210X.13650](https://doi.org/10.1111/2041-210X.13650).
- Roberts, D. R. et al. (2017). “Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure.” *Ecography*, 40(8), 913–929. [DOI 10.1111/ecog.02881](https://doi.org/10.1111/ecog.02881).
- Serov, E., Koldasbayeva, D. and Zaytsev, A. (2026). “Kernel mean matching enhances risk estimation under spatial distribution shifts.” *Scientific Reports*, 16, 6921. [DOI 10.1038/s41598-026-36740-7](https://doi.org/10.1038/s41598-026-36740-7).

## Scope

This is a method-selection and study-design guide. It does not claim to provide a tested MMD implementation, a spatial permutation engine, a KMM optimiser or a complete AOA implementation. Those are separate implementation targets with different assumptions and validation requirements.
