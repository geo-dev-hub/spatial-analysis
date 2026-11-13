# Ordinary kriging: estimate a value using spatial dependence

- **Stable ID:** `SA-GEOSTATISTICS-ORDINARY-KRIGING`
- **Kind:** method
- **Domain:** geostatistics and spatial prediction
- **Status:** researched; PyKrige example and notebook prepared; independent review pending
- **Version:** 0.1
- **Source inventory:** Section 3, page 4 — kriging variants
- **Prerequisites:** [Empirical semivariogram](../../methods/empirical-semivariogram.md); [Inverse distance weighting](inverse-distance-weighting.md)
- **Related records:** covariance models, variogram fitting and spatial validation (planned)

## What if distance alone is not enough?

IDW assumes nearby observations should count more. But it does not learn how the measured phenomenon varies across space. It does not distinguish a smooth process from a rough one, or tell you whether the relationship changes with direction.

Ordinary kriging takes another step. It uses a model of spatial dependence—usually expressed through a variogram or covariance function—to calculate weights for nearby observations. It also provides a model-based estimate of prediction variance.

## The central idea

Ordinary kriging estimates a value at an unmeasured location as a weighted sum of observed values:

$$
\hat Z(\mathbf{s}_0)=\sum_{i=1}^{n}\lambda_i Z(\mathbf{s}_i).
$$

The weights are not simply inverse distances. They are calculated from the spatial dependence model and the geometry of the observations relative to the target.

Ordinary kriging assumes an unknown but constant local mean over the neighbourhood used for prediction. The weights are constrained to sum to one:

$$
\sum_{i=1}^{n}\lambda_i=1.
$$

That constraint gives an unbiased linear estimator under the model assumptions.

## The kriging system

Using a semivariogram convention, the ordinary kriging equations can be written as

$$
\sum_{j=1}^{n}\lambda_j\gamma(\mathbf{s}_i-\mathbf{s}_j)+\mu
=\gamma(\mathbf{s}_i-\mathbf{s}_0),
\qquad i=1,\ldots,n,
$$

together with

$$
\sum_{j=1}^{n}\lambda_j=1.
$$

Here:
- $\gamma(\mathbf{s}_i-\mathbf{s}_j)$ is the modelled semivariance between observations $i$ and $j$;
- $\gamma(\mathbf{s}_i-\mathbf{s}_0)$ is the modelled semivariance between observation $i$ and the target;
- $\lambda_j$ is the weight assigned to observation $j$;
- $\mu$ is the Lagrange multiplier enforcing the sum-to-one constraint.

The system balances the spatial dependence between observations against their relationship to the prediction location. The multiplier convention varies between presentations; the equations and variance formula must use the same convention.

Under the displayed convention, the ordinary kriging variance is

$$
\sigma^2_{OK}(\mathbf{s}_0)=
\sum_{i=1}^{n}\lambda_i\gamma(\mathbf{s}_i-\mathbf{s}_0)+\mu.
$$

This is a model-based measure of prediction uncertainty under the fitted variogram and stated assumptions. It is not a complete account of uncertainty in the data, model choice, variogram parameters or future observations.

## What the variogram contributes

The [empirical semivariogram](../../methods/empirical-semivariogram.md) describes how observed differences change with separation distance. Ordinary kriging needs a theoretical variogram model that can be evaluated at the distances and directions in the kriging system.

Common bounded models include spherical, exponential and Gaussian forms. They differ in how quickly semivariance rises from the nugget toward the sill. Their parameter conventions—including what a package calls the range—can differ.

Do not select a model only because its curve looks close to the empirical points. Check pair counts, directional structure, trend, model validity and predictive performance.

## A practical workflow

1. Explore the data and confirm the spatial support, units and coordinate system.
2. Investigate trend and decide whether the ordinary-kriging constant-mean assumption is plausible locally.
3. Calculate empirical semivariograms and inspect directional behaviour.
4. Choose a permissible theoretical variogram family and fit its parameters.
5. Define the neighbourhood used for each prediction.
6. Solve the kriging system at target locations.
7. Map predictions and kriging variance separately.
8. Validate predictions at withheld locations; compare with simple baselines such as the mean and IDW.
9. Inspect residuals and report the model, parameters, neighbourhood, CRS and validation design.

## What the variance map means

Kriging variance is influenced by the sampling geometry and the fitted variogram model. It commonly increases where observations are sparse or the target is far from sampled locations. Under ordinary kriging with fixed locations and a fixed variogram model, it does not depend directly on the observed values themselves.

That does not mean the variance map captures every source of uncertainty. It generally does not include uncertainty from choosing the variogram family, estimating its parameters, measurement error beyond what the model represents, or a misspecified mean/trend structure.

## Where it can go wrong

| Situation | Why it matters | What to check |
|---|---|---|
| The local mean is not approximately constant | Ordinary kriging's mean assumption is inappropriate | Model trend or consider universal/regression kriging |
| Variogram model is poorly chosen | Weights and variance depend on it | Compare plausible models and validate predictions |
| Trend is left in the residual structure | Empirical semivariance may keep increasing with distance | Inspect trend and residual variograms |
| Sampling is clustered | Predictions may be dominated by dense areas | Use neighbourhood limits and spatial validation |
| Anisotropy is ignored | Directional dependence is collapsed into one curve | Inspect directional variograms and model anisotropy |
| Coordinates use unsuitable units | Distances and variogram range become meaningless | Use a defensible projected or geodesic distance model |
| Duplicate or near-duplicate points cause instability | The kriging matrix may be ill-conditioned | Inspect duplicates and consider a pseudo-inverse only with a stated reason |
| Kriging variance is called total uncertainty | It is conditional on the model and parameters | Report omitted uncertainty sources separately |

## Compare it with IDW

| Question | IDW | Ordinary kriging |
|---|---|---|
| What controls the weights? | Distance and a chosen power | Variogram/covariance model and observation geometry |
| Does it model spatial dependence? | No explicit stochastic dependence model | Yes, through the variogram or covariance |
| Does it estimate model-based prediction variance? | No | Yes |
| Does it require variogram fitting? | No | Yes |
| Can it be exact at observed locations? | Under its zero-distance convention | Depends on nugget and exact-value settings |

Neither method is automatically best. Compare them using a validation design that reflects where future predictions will be made.

## Runnable material

- [PyKrige example, tests and walkthrough](../../implementations/python/ordinary-kriging/README.md)
- [Interactive ordinary kriging lab](../../notebooks/ordinary-kriging-lab.ipynb)

The example uses PyKrige as a maintained implementation rather than presenting a short custom solver as a production kriging engine. Its API and variogram parameter conventions are version-specific.

## Try it

- **Predict:** Where would you expect kriging variance to be largest in the example?
- **Change:** Switch between spherical, exponential and Gaussian variograms. What changes in the prediction surface?
- **Compare:** Run IDW and ordinary kriging on the same observations and compare spatially blocked validation errors.
- **Investigate:** Add a trend to the synthetic data. Does ordinary kriging still look appropriate?
- **Explain:** Why can two locations with similar nearest-neighbour distances still have different kriging variances?

## References

1. Matheron, G. (1963). “Principles of geostatistics.” *Economic Geology*, 58(8), 1246–1266.
2. Hengl, T. (2007). *A Practical Guide to Geostatistical Mapping of Environmental Variables*. European Commission, Joint Research Centre. [Open PDF](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC38153/eur22904en.pdf).
3. PyKrige documentation. [Ordinary kriging example](https://geostat-framework.readthedocs.io/projects/pykrige/en/latest/examples/00_ordinary.html), [OrdinaryKriging API](https://geostat-framework.readthedocs.io/projects/pykrige/en/stable/generated/pykrige.ok.OrdinaryKriging.html), and [variogram models](https://geostat-framework.readthedocs.io/projects/pykrige/en/stable/variogram_models.html). These support the package-specific implementation notes; they do not replace the geostatistical assumptions.

## What remains to be checked

- Independently review the ordinary-kriging system and variance derivation.
- Compare PyKrige outputs with a second geostatistical implementation on a small reference dataset.
- Add a documented real dataset and spatially blocked validation before making applied performance claims.
- Extend the path with universal kriging and regression kriging as separate records.

## Change history

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-11-13 | Initial explanation and PyKrige teaching workflow |
