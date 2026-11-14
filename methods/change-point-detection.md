# Change-point detection in spatial and environmental time series

A change point is a time at which the statistical behaviour of a sequence changes. The change may affect its mean, variance, trend, seasonal pattern, distribution or generating process. In spatial analysis, change-point methods can help identify disturbance, regime shifts, infrastructure changes, sensor failures and transitions in land-surface dynamics.

A detector does not discover the cause of a change. It identifies evidence of a statistical transition under a chosen model. Interpretation requires context, data-quality checks and uncertainty assessment.

## 1. Define the change you want to detect

Let observations be y₁,…,yₙ at ordered times t₁,…,tₙ. A segmentation partitions the sequence into contiguous segments with boundaries τ₁,…,τₘ:

$$
1=\tau_0<\tau_1<\cdots<\tau_m<\tau_{m+1}=n+1.
$$

A simple piecewise-constant mean model is

$$
y_t=\mu_j+\varepsilon_t,
\qquad \tau_{j-1}\leq t<\tau_j.
$$

But many geospatial series are not piecewise constant. They can have seasonal cycles, gradual trends, changing variance, autocorrelation, irregular sampling and missing observations. A mean-shift detector can mistake a seasonal peak, a cloudy observation or a sensor transition for a real land-surface change.

Before choosing an algorithm, state:

- the parameter expected to change (mean, variance, trend, seasonality, distribution or model state);
- whether detection is online (only past data) or retrospective (the whole series);
- whether the number of changes is fixed, penalised or inferred probabilistically;
- the expected minimum segment length and plausible change frequency;
- the observation model, missing-data treatment and temporal sampling assumptions.

## 2. CUSUM: accumulate evidence for a shift

Page's cumulative-sum (CUSUM) scheme is a sequential monitoring method. For a one-sided detector monitoring an upward shift from a reference mean μ₀, a common recursion is

$$
S_t^+=\max\left(0,S_{t-1}^+ + y_t-\mu_0-k\right),
\qquad S_0^+=0,
$$

where k is a reference allowance. Signal when Sₜ⁺ exceeds a decision threshold h. A corresponding lower-tail statistic detects downward shifts.

CUSUM is effective when the target shift and reference distribution are reasonably specified. It is not a universal multiple-change segmentation method. Its false-alarm behaviour depends on the assumed distribution, serial dependence, k, h and monitoring design. A threshold chosen for independent Gaussian observations may be poorly calibrated for autocorrelated satellite or sensor data.

**Use it for:** sequential monitoring of a defined process, such as sensor drift or a known indicator's sustained shift.

**Do not use it for:** exploratory multi-regime segmentation without a clear baseline and calibration plan.

## 3. Binary segmentation: fast recursive search

Binary segmentation begins with the full series. It searches for the most likely single change point under a chosen statistic or segment cost, splits the series at that location, then repeats the search on the resulting segments.

The method is intuitive and can be fast. Its greedy decisions are not generally globally optimal: an early split can prevent the algorithm from finding a better combination of multiple changes. Results also depend on the stopping rule, minimum segment length and penalty/threshold.

**Use it for:** a quick exploratory baseline or when computational simplicity is important.

**Report:** the split statistic, threshold, stopping criterion and whether changes are re-estimated after later splits.

## 4. PELT: penalised optimal segmentation

PELT (Pruned Exact Linear Time) minimises an additive segmentation objective. A common form is

$$
\min_{m,\tau_1,\ldots,\tau_m}
\left[
\sum_{j=0}^{m} C(y_{\tau_j:\tau_{j+1}-1})+\beta m
\right],
$$

where C is the cost of fitting one segment and β penalises additional change points. Dynamic programming solves the optimisation, while pruning removes candidate previous change points that cannot be optimal under stated conditions.

PELT is exact for the specified penalised objective when its assumptions hold. The often-quoted linear computational cost is conditional, not universal: the expected complexity is linear under conditions including suitable cost/pruning properties and a change-point rate that grows appropriately with series length. Worst-case behaviour can be quadratic.

The cost function determines what a change means. Examples include changes in mean, mean and variance, or parameters of a specified distribution. Choosing an unsuitable cost gives a precisely optimised answer to the wrong statistical problem.

**Use it for:** retrospective segmentation when the objective is additive and an optimal penalised partition is required.

## 5. Bayesian online change-point detection (BOCPD)

Adams and MacKay's Bayesian online method maintains a posterior distribution over the current run length rₜ, the number of observations since the most recent change. It updates this distribution as each new observation arrives, combining a predictive likelihood with a hazard model for the probability of a new change.

The posterior is

$$
P(r_t\mid y_{1:t}),
$$

not merely a single estimated boundary. This allows uncertainty about the most recent change to be retained as the series grows.

The result depends on the observation likelihood, parameter priors and hazard function. A constant hazard implies a particular prior expectation for segment duration; it should not be treated as a neutral default. Exact inference over all run lengths can grow in cost, so implementations often truncate or approximate the state space.

**Use it for:** streaming monitoring where a probabilistic estimate of the current regime age is useful.

**Do not confuse it with:** retrospective segmentation of the entire record. It answers an online inference question.

## 6. BEAST: joint change, trend and seasonality inference

BEAST (Bayesian Estimator of Abrupt change, Seasonal change, and Trend) was developed for time-series decomposition, including satellite observations. It uses Bayesian ensemble modelling to represent uncertainty in abrupt changes, trend components and seasonal structure rather than relying on a single fixed decomposition.

This is particularly relevant to vegetation and land-surface series: an abrupt disturbance may occur on top of a changing seasonal cycle and a gradual long-term trend. Modelling those components jointly can be more informative than applying a simple mean-shift detector to raw observations.

BEAST's posterior probabilities and credible intervals describe uncertainty under the model and priors. They do not establish the ecological or human cause of an event. Bayesian computation can also be demanding for high-resolution imagery and large spatial collections.

**Use it for:** retrospective analysis of seasonal environmental series where trend, seasonality and abrupt changes all matter.

## 7. Method comparison

| Method | Online/offline | Main output | Main strength | Important limitation |
|---|---|---|---|---|
| CUSUM | Online | Sequential evidence / alarm | Simple targeted monitoring | Requires calibrated baseline and shift design |
| Binary segmentation | Offline | Recursive set of boundaries | Fast and intuitive | Greedy; not generally globally optimal |
| PELT | Offline | Optimal penalised segmentation | Exact for the specified objective under assumptions | Cost/penalty assumptions; worst-case can exceed linear |
| BOCPD | Online | Posterior over current run length | Probabilistic sequential inference | Sensitive to hazard and likelihood assumptions |
| BEAST | Usually retrospective | Posterior change, trend and seasonal components | Joint decomposition and uncertainty | More modelling and computational complexity |

## 8. Spatial and Earth-observation complications

A time series at one pixel is not independent of neighbouring pixels, and a map of detected changes creates a multiple-testing problem.

- **Seasonality:** align observations by phenological phase or model seasonal components explicitly.
- **Autocorrelation:** serial dependence changes false-alarm rates and uncertainty. Use an appropriate time-series likelihood or calibrate by simulation.
- **Irregular sampling:** methods that assume equally spaced observations need adaptation or an explicit time-aware model.
- **Missingness and clouds:** distinguish missing observations from zero values; cloud masks and quality flags can be informative rather than random.
- **Sensor transitions:** harmonise sensors and test for calibration changes before interpreting a detected breakpoint as environmental change.
- **Spatial dependence:** neighbouring pixels share weather, land cover and processing artefacts. Map-level uncertainty should account for spatial structure.
- **Multiple comparisons:** pixelwise significance thresholds do not control the false discovery rate across millions of locations.
- **Boundary uncertainty:** a date estimate should be reported with uncertainty or a credible interval where the method supports it.
- **Causal interpretation:** combine statistical evidence with independent imagery, field observations, event records or domain knowledge.

A detected boundary should be treated as a candidate event, not an automatic change label.

## 9. Validation design

Use simulated sequences where the true change times and magnitudes are known. Vary:

1. no change (false-alarm test);
2. one abrupt mean shift;
3. variance-only shift;
4. gradual trend break;
5. seasonal amplitude or phase change;
6. multiple close change points;
7. irregular timestamps and missing observations;
8. serially correlated noise;
9. outliers and transient spikes;
10. sensor offsets and quality-mask gaps.

Evaluate more than exact-date accuracy. Report detection probability, false alarms per series, boundary error, delay for online methods, segmentation cost, uncertainty calibration, runtime and sensitivity to tuning parameters. For spatial maps, also evaluate spatial fragmentation and whether detections align with known events without using those events to tune and test on the same data.

## Further reading

- Page, E. S. (1954), “Continuous Inspection Schemes,” *Biometrika*, 41(1–2), 100–115. [DOI 10.1093/biomet/41.1-2.100](https://doi.org/10.1093/biomet/41.1-2.100).
- Killick, R., Fearnhead, P. and Eckley, I. A. (2012), “Optimal Detection of Changepoints With a Linear Computational Cost,” *Journal of the American Statistical Association*, 107(500), 1590–1598. [DOI 10.1080/01621459.2012.737745](https://doi.org/10.1080/01621459.2012.737745).
- Adams, R. P. and MacKay, D. J. C. (2007), “Bayesian Online Changepoint Detection.” [arXiv:0710.3742](https://arxiv.org/abs/0710.3742).
- Zhao, K. et al. (2019), “Detecting change-point, trend, and seasonality in satellite time series data to track abrupt changes and nonlinear dynamics: A Bayesian ensemble algorithm,” *Remote Sensing of Environment*, DOI [10.1016/j.rse.2019.04.034](https://doi.org/10.1016/j.rse.2019.04.034).

## Scope

This guide compares method families and states their modelling assumptions. It does not claim to implement CUSUM, binary segmentation, PELT, BOCPD or BEAST. A practical package should begin with one explicitly chosen cost model, simulated known-change tests, missing-data rules and uncertainty reporting before scaling to spatial image collections.


## Reproducible mean-shift implementations

The companion teaching package now implements three distinct baselines for a univariate, finite, equally weighted sequence:

- **CUSUM:** two-sided Page-style sequential accumulation against a supplied reference mean, allowance and threshold. Threshold calibration is the analyst's responsibility.
- **Binary segmentation:** greedy recursive splitting by reduction in within-segment sum of squares (SSE), accepting a split only when its gain exceeds the supplied penalty.
- **PELT mean:** dynamic programming with pruning for the additive objective consisting of segment SSE plus a penalty per change point. The implementation supports a minimum segment length and is exact for this stated objective up to floating-point arithmetic. Worst-case runtime is quadratic; a universal linear-time claim is not made.

The segmentation algorithms detect piecewise-constant mean changes, not arbitrary distributional changes. They assume finite numeric observations in temporal order. Seasonal structure, serial dependence, irregular time steps, missingness and spatial multiplicity need explicit treatment before operational use.

- [Runnable Python package and tests](../implementations/python/change-point-detection/README.md)
- [Intern walkthrough](../implementations/python/change-point-detection/implementation-walkthrough.md)
- [Synthetic change-point lab](../notebooks/change-point-detection-lab.ipynb)


## Reproducible Bayesian online baseline

A conjugate BOCPD teaching implementation now accompanies the conceptual guide. It tracks the posterior over run length for an unknown segment mean with a Normal prior, known Gaussian observation variance and constant hazard. Tests check posterior normalisation, response to an abrupt synthetic shift and invalid model parameters. The model assumptions are intentionally explicit; this is not a generic BOCPD library or a replacement for BEAST.

- [Implementation](../implementations/python/change-point-detection/bayesian_online.py)
- [Tests](../implementations/python/change-point-detection/test_bayesian_online.py)
- [Bayesian online lab](../notebooks/bayesian-online-change-point-lab.ipynb)
