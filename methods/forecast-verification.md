# Forecast verification: categorical, probabilistic and spatial methods

Forecast verification compares predictions with observations to assess performance. For spatial forecasts, a single grid-cell score can be misleading: a realistic rainfall field shifted a few kilometres may score poorly under exact grid matching, while a smooth forecast can obtain a deceptively good score by predicting the climatological average.

This guide separates categorical contingency-table scores, probabilistic scoring rules, neighbourhood verification and object-based diagnostics. Each answers a different question.

## 1. Establish a fair verification design

Before calculating scores, align the forecast and observation in:

- valid time and accumulation interval;
- coordinate reference system, grid and resolution;
- units, thresholds and masks;
- observation availability and quality control;
- forecast lead time and issue time.

Use only information available at the forecast issue time. Compare forecasts on the same valid cases, and report sample size. A model can appear better simply because it is evaluated on easier dates or a different set of missing observations.

Verification should be stratified by lead time, season, region, event magnitude and relevant observation quality. Use a baseline such as climatology, persistence or a reference model.

## 2. Categorical scores: contingency tables

For a binary event, count hits H, misses M, false alarms F and correct negatives C.

| | Observed event | Observed no event |
|---|---:|---:|
| Forecast event | Hit (H) | False alarm (F) |
| Forecast no event | Miss (M) | Correct negative (C) |

Common scores include:

**Probability of detection (POD)**

$$
POD=\frac{H}{H+M}.
$$

The fraction of observed events that were forecast. It does not penalise false alarms.

**False alarm ratio (FAR)**

$$
FAR=\frac{F}{H+F}.
$$

The fraction of forecast events that did not occur. It is not the same as the false-positive rate, which is F/(F+C).

**Critical success index (CSI)**

$$
CSI=\frac{H}{H+M+F}.
$$

This combines hits, misses and false alarms while ignoring correct negatives.

**Equitable threat score (ETS)**

$$
ETS=\frac{H-H_r}{H+M+F-H_r},
\qquad
H_r=\frac{(H+M)(H+F)}{H+M+F+C}.
$$

ETS adjusts hits for the expected random hits under the table's marginal totals. It is not a complete correction for all forecast biases or event-frequency effects.

Always show the contingency counts alongside the derived scores. POD can be high when a forecast issues many false alarms; FAR can be low when very few events are forecast.

## 3. Probabilistic scores: Brier score and ROC

For binary outcomes oᵢ∈{0,1} and forecast probabilities pᵢ, the Brier score is

$$
BS=\frac{1}{N}\sum_{i=1}^{N}(p_i-o_i)^2.
$$

Lower is better. The Brier score is a strictly proper scoring rule for binary probabilities: in expectation it rewards honest probabilities. It reflects both calibration and resolution, with uncertainty also depending on event frequency.

A reliability diagram groups forecasts by probability and compares mean forecast probability with observed event frequency. A well-calibrated forecast lies near the diagonal. Reliability alone is not sufficient: a forecast that always issues the climatological event rate may be calibrated but uninformative.

The receiver operating characteristic (ROC) curve plots hit rate against false-positive rate as the probability threshold changes. Area under the ROC curve (AUC) measures ranking/discrimination: the chance that a randomly selected event receives a higher forecast score than a randomly selected non-event, under the usual interpretation. AUC does not measure calibration and can remain high for probabilities that are systematically overconfident.

## 4. Continuous ranked probability score (CRPS)

For a predictive cumulative distribution F and observation x, the CRPS is

$$
CRPS(F,x)=\int_{-\infty}^{\infty}
\left(F(z)-\mathbb{1}\{z\geq x\}\right)^2 dz.
$$

Lower is better. CRPS evaluates the full predictive distribution and generalises absolute error for deterministic forecasts. It is a proper scoring rule, so in expectation it encourages truthful predictive distributions.

For an ensemble, estimate the score from the empirical distribution or use an appropriate sample-based formula. Ensemble size and dependence matter: repeated or under-dispersed ensemble members can distort uncertainty assessment.

## 5. Rank histograms and calibration diagnostics

For an ensemble forecast with m members and one observation, rank the observation among the sorted members. Repeating this across cases produces a rank histogram.

A flat histogram is consistent with ensemble reliability under idealised assumptions. A U-shape can indicate under-dispersion; a dome shape can indicate over-dispersion; skew can indicate bias. These patterns are diagnostics, not unique diagnoses: finite samples, ties, discrete variables, changing climatology and dependence can also shape the histogram.

Pair rank histograms with spread-skill relationships, reliability diagrams, PIT histograms for continuous predictive distributions and proper scoring rules.

## 6. Fractions Skill Score (FSS): verify at a spatial scale

Traditional gridpoint verification asks whether the event occurred at the exact same cell. FSS instead compares the fraction of grid cells exceeding a threshold within neighbourhoods around each location.

Let Pᵢ and Oᵢ be forecast and observed event fractions for neighbourhood i. A common form is

$$
FSS=1-
\frac{\sum_i(P_i-O_i)^2}
{\sum_i P_i^2+\sum_i O_i^2}.
$$

FSS is 1 for a perfect match and approaches 0 for poor agreement relative to the score's reference behaviour. It is scale-selective: changing the neighbourhood size changes the question being asked. Small neighbourhoods test precise placement; larger neighbourhoods test broader spatial organisation.

FSS does not mean that the forecast is “correct” at every location inside a neighbourhood. Report the event threshold, neighbourhood size in physical units, grid spacing, domain and reference/skill interpretation. Do not compare FSS values across studies without checking those choices. A tested regular-grid teaching baseline is available in the [Fractions Skill Score module](../implementations/python/forecast-verification/README.md#spatial-neighbourhood-verification-fractions-skill-score), with a [scale-verification lab](../notebooks/forecast-fractions-skill-score-lab.ipynb); its windows are specified in cells and its edge policy is explicit.

## 7. SAL: structure, amplitude and location

SAL is an object-based diagnostic for quantitative precipitation forecasts. It has three components:

- **S — Structure:** compares the shape and spatial distribution of precipitation objects.
- **A — Amplitude:** compares domain-mean precipitation magnitude.
- **L — Location:** compares the spatial displacement of the precipitation field's centre of mass and objects.

The components provide interpretable diagnostics that a single scalar score cannot. A forecast can have approximately correct total rainfall (A near zero) but poor structure or location. SAL depends on the object-identification and domain choices, so those settings must be reported.

SAL was designed for quantitative precipitation fields. Do not assume that its thresholds and object definitions transfer unchanged to arbitrary spatial variables.

## 8. MODE and object-based verification

The Method for Object-Based Diagnostic Evaluation (MODE) identifies forecast and observed objects using thresholds and spatial processing, then compares attributes such as area, centroid, orientation, intensity and similarity. It can support matching and merging/splitting analyses to diagnose displacement and morphology errors.

Object-based verification helps explain why a forecast misses a feature, but object definitions introduce parameters: threshold, smoothing, convolution radius, minimum area and matching criteria. Different settings can produce different objects and pairings. Report the settings and retain a field-based score alongside object diagnostics.\n\nA bounded [MODE-inspired teaching implementation](../implementations/python/forecast-verification/object_verification.py), with [tests](../implementations/python/forecast-verification/test_object_verification.py) and a [lab](../notebooks/mode-inspired-object-verification-lab.ipynb), performs Gaussian smoothing, thresholding, connected-component extraction, attribute measurement and minimum-cost one-to-one matching. It is not a full MODE reproduction: within-field merging, fuzzy-interest matching, cluster objects and temporal tracking are not implemented.

## 9. Match the metric to the question

| Question | Useful method | What it does not tell you alone |
|---|---|---|
| Did we detect observed events? | POD | False-alarm burden |
| How often were forecast events false? | FAR | Missed events |
| How good are thresholded event forecasts overall? | CSI / ETS | Probability calibration |
| Are binary probabilities honest? | Brier score and reliability diagram | Spatial displacement by itself |
| Can forecasts rank events? | ROC / AUC | Calibration or decision value |
| Is the full predictive distribution useful? | CRPS | Spatial structure unless applied to spatial objects/fields |
| Is ensemble spread calibrated? | Rank histogram and spread-skill | Full conditional calibration |
| How does skill change with spatial scale? | FSS | Exact object identity and detailed morphology |
| Is precipitation shape, magnitude or location wrong? | SAL | All aspects of field error in one number |
| Which forecast objects match observed objects? | MODE | Sensitivity to object-definition parameters |

## 10. Common traps

- Optimising a threshold on the test set and reporting the same test score.
- Reporting only one metric and hiding trade-offs between misses and false alarms.
- Using AUC as evidence that probabilities are calibrated.
- Treating a flat rank histogram as proof of all aspects of ensemble reliability.
- Comparing FSS without reporting neighbourhood size and event threshold.
- Treating object-based metrics as parameter-free or objective.
- Ignoring event base rates and sample size.
- Mixing different valid times, accumulation periods, masks or grids.
- Reporting only pooled scores when performance varies sharply by region or lead time.
- Treating a statistically better score as automatically operationally useful.

## 11. Validation and uncertainty

Use a held-out period or rolling-origin evaluation. For spatial forecast systems, preserve spatial structure when bootstrapping or estimating uncertainty: resampling individual grid cells independently can understate uncertainty because neighbouring cells are correlated.

Report confidence intervals, case counts and score distributions across events. Stratify by lead time and severity. Where possible, compare paired forecasts on the same cases and use resampling units that reflect the dependence structure (for example, whole events, days or spatial blocks).

A strong verification report combines:
1. a baseline comparison;
2. categorical performance at operational thresholds;
3. probabilistic calibration and proper scores;
4. spatial scale or object diagnostics;
5. uncertainty intervals and case counts.

## Further reading

- Roberts, N. (2008), “Assessing the spatial and temporal variation in the skill of precipitation forecasts from an NWP model,” *Meteorological Applications*, 15, 163–169. [DOI 10.1002/met.57](https://doi.org/10.1002/met.57), on scale-selective fractions skill score.
- Wernli, H., Paulat, M., Hagen, M. and Frei, C. (2008), “SAL—A Novel Quality Measure for the Verification of Quantitative Precipitation Forecasts,” *Monthly Weather Review*, 136, 4470–4487. [DOI 10.1175/2008MWR2415.1](https://doi.org/10.1175/2008MWR2415.1).
- Davis, C., Brown, B. and Bullock, R. (2006), “Object-Based Verification of Precipitation Forecasts. Part I: Methodology and Application to Mesoscale Rain Areas,” *Monthly Weather Review*, 134, 1772–1784. [DOI 10.1175/MWR3145.1](https://doi.org/10.1175/MWR3145.1).
- Gneiting, T. and Raftery, A. E. (2007), “Strictly Proper Scoring Rules, Prediction, and Estimation,” *Journal of the American Statistical Association*, 102(477), 359–378. [DOI 10.1198/016214506000001437](https://doi.org/10.1198/016214506000001437).

## Scope

**Implemented teaching baseline:** [contingency-table scores, Brier score/skill, reliability bins and tied-rank ROC AUC](../implementations/python/forecast-verification/README.md), empirical ensemble CRPS and expected rank histograms with fractional tie handling, plus [tests](../implementations/python/forecast-verification/test_forecast_verification.py), an [intern walkthrough](../implementations/python/forecast-verification/implementation-walkthrough.md) and executable labs. Fractions Skill Score has a tested regular-grid baseline with explicit cell-window and edge policies. CRPS decomposition, SAL and MODE remain open. Spatial metrics require separate grid, neighbourhood, object and boundary contracts; they should not be represented by one generic vector function.


## Ensemble verification additions

The companion package now also provides empirical ensemble CRPS per case and its mean, plus an expected rank histogram. Ties are fractionally distributed over admissible ranks, yielding a deterministic version of random tie handling. The implementation states its finite rectangular-ensemble contract and does not silently substitute the fair-CRPS estimator.

- [Ensemble metrics implementation](../implementations/python/forecast-verification/ensemble_verification.py)
- [Tests](../implementations/python/forecast-verification/test_ensemble_verification.py)
- [Walkthrough](../implementations/python/forecast-verification/ensemble-verification-walkthrough.md)
- [Ensemble verification lab](../notebooks/ensemble-forecast-verification-lab.ipynb)


## MODE-inspired object verification baseline

The [teaching implementation](../implementations/python/forecast-verification/object_verification.py), with [tests](../implementations/python/forecast-verification/test_object_verification.py) and a [lab notebook](../notebooks/mode-inspired-object-verification-lab.ipynb), performs optional Gaussian smoothing, thresholding, connected-component extraction, object-attribute measurement and minimum-cost one-to-one matching. It is a bounded MODE-inspired baseline, not a full MET/MODE reproduction: within-field merging, fuzzy-interest matching, cluster objects and temporal tracking are not implemented.
