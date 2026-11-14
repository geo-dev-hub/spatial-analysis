# Trend, seasonality and forecasting for spatial time series

A time series is an ordered sequence of observations. Spatial time series add a location dimension: a pixel, sensor, station, administrative area, road segment or moving object is observed repeatedly through time.

The methods in this guide answer different questions. STL decomposes a series; Theil–Sen estimates a robust trend slope; Pettitt tests for a single distributional change; ARIMA models temporal dependence and forecasts; Prophet builds a decomposable forecasting model; and a Kalman filter estimates a latent state as observations arrive. They are not interchangeable.

## 1. Start with the data-generating structure

A useful conceptual decomposition is

$$
y_t=T_t+S_t+R_t,
$$

where T is trend, S is seasonality and R is remainder. This additive form is a model choice. If seasonal variation grows with the level, a multiplicative model or a transformation may be more appropriate.

Before fitting anything, inspect:

- sampling interval, time zone and calendar;
- gaps, duplicates, irregular timestamps and quality flags;
- missing observations versus true zero values;
- outliers, sensor changes and calibration drift;
- trend, seasonal period, autocorrelation and changing variance;
- whether observations are independent across locations.

For satellite series, cloud masking, compositing windows, view geometry and sensor harmonisation can create apparent temporal structure. Preserve QA flags and do not fill missing observations with zero.

## 2. STL: Seasonal-Trend decomposition using LOESS

STL uses locally weighted regression (LOESS) to estimate trend and seasonal components iteratively. It can accommodate a range of seasonal periods, allow the seasonal pattern to evolve over time and use robust weights to reduce the influence of outliers.

The decomposition is

$$
y_t=T_t+S_t+R_t.
$$

The analyst controls smoothing windows. A narrow seasonal window allows the seasonal pattern to change quickly; a wider window makes it more stable. The trend window controls the smoothness of the trend-cycle.

**Strengths:** flexible seasonal period, robust option, interpretable components and useful diagnostics.

**Limitations:** standard STL is additive; calendar effects are not automatically modelled; smoothing choices affect the decomposition; the remainder is not automatically white noise.

STL is a decomposition procedure, not a forecasting model by itself. Forecasting often combines the components with a separate model for the seasonally adjusted remainder.

## 3. Theil–Sen: robust trend slope

For observations (tᵢ,yᵢ), the Theil–Sen slope is the median of all pairwise slopes:

$$
\hat\beta_1=
\operatorname{median}_{i<j,\ t_i\ne t_j}
\left(\frac{y_j-y_i}{t_j-t_i}\right).
$$

An intercept can be estimated as

$$
\hat\beta_0=\operatorname{median}_i(y_i-\hat\beta_1t_i).
$$

Because the estimator uses a median rather than least-squares squared residuals, it is less sensitive to isolated extreme values. It is a useful descriptive trend estimator for environmental series.

**Important:** robust to outliers does not mean immune to autocorrelation, seasonality, step changes or non-monotonic behaviour. Estimate a trend on seasonally adjusted data where justified, and use inference methods that account for serial dependence when testing significance. For irregular timestamps, use actual elapsed time rather than row number.

## 4. Pettitt test: a single non-parametric change point

Pettitt's test is a rank-based procedure for testing a single change in location within an ordered sequence. It compares observations before and after each candidate split using a Mann–Whitney-type statistic and selects the split with the strongest evidence.

A common statistic is

$$
U_t=\sum_{i=1}^{t}\sum_{j=t+1}^{n}\operatorname{sgn}(y_i-y_j),
\qquad
K=\max_{1\leq t<n}|U_t|.
$$

It is non-parametric in the sense that it does not require a Gaussian location model. However, the standard test assumes independent observations under its null calibration. Serial correlation can inflate false positives, and a smooth trend can be mistaken for an abrupt change. It targets one change, not a full multi-break segmentation.

Use it as a single-break diagnostic, with attention to trend removal, autocorrelation and multiple testing across many locations.

## 5. ARIMA: model temporal dependence

An autoregressive integrated moving-average model combines differencing, autoregression and moving-average terms. In backshift notation, a non-seasonal ARIMA(p,d,q) can be written as

$$
\phi(B)(1-B)^d y_t=c+\theta(B)\varepsilon_t,
$$

where B is the backshift operator, φ and θ are autoregressive and moving-average polynomials, d is the differencing order and ε is an innovation process.

Seasonal ARIMA adds seasonal autoregressive, differencing and moving-average terms at a specified period. The model is useful when the series has temporal dependence that can be represented through these components.

The practical workflow includes stationarity and differencing assessment, model identification, parameter estimation, residual diagnostics and genuine out-of-sample evaluation. Differencing too much can destroy information; residual autocorrelation indicates that the model has not captured all temporal structure.

ARIMA is not inherently spatial. Fitting one independent ARIMA model per pixel ignores spatial dependence and can be computationally expensive. For spatial fields, consider hierarchical, spatiotemporal or shared-parameter models when cross-location structure matters.

## 6. Prophet: decomposable forecasting model

Prophet was introduced as a practical forecasting approach for many business time series. Its model combines a piecewise trend, periodic seasonal components and holiday/event effects, with additional regressors where appropriate.

A simplified representation is

$$
y(t)=g(t)+s(t)+h(t)+\varepsilon_t,
$$

where g is trend, s is seasonality and h represents holiday or event effects.

Its strengths include interpretable components, configurable changepoints in the trend and a workflow designed for analysts managing many series. It is not a universal forecasting benchmark. Performance depends on the series, priors, changepoint flexibility, seasonal structure and evaluation design. It may perform poorly when the data-generating process differs from its assumptions or when there is limited history.

For geospatial applications, event calendars may encode policy or infrastructure changes, but these must be known at forecast time. Do not use future information as a regressor in a historical backtest.

## 7. Kalman filtering: estimate a latent evolving state

A linear state-space model separates the latent process from noisy observations:

$$
x_t=F_tx_{t-1}+w_t,\
y_t=H_tx_t+v_t,
$$

where xₜ is the latent state, Fₜ is the transition matrix, Hₜ maps the state to observations, and wₜ and vₜ are process and observation noise with covariance matrices Qₜ and Rₜ.

The Kalman filter alternates prediction and measurement update. In the prediction step,

$$
\hat x_{t|t-1}=F_t\hat x_{t-1|t-1},
$$

$$
P_{t|t-1}=F_tP_{t-1|t-1}F_t^T+Q_t.
$$

For an observation, compute the innovation and update the state estimate and covariance. If an observation is missing, the prediction step can still advance the state without a measurement update.

A filter is causal: it uses observations available up to the current time. A smoother uses later observations to revise past state estimates. For non-linear or non-Gaussian systems, extended, unscented or particle filters may be more appropriate than the standard linear Gaussian Kalman filter.

For environmental monitoring, state variables might represent level, trend and seasonal components. For trajectories, they might represent position and velocity. The transition model and covariance parameters encode assumptions about how the system evolves.

## 8. Choose by the question

| Question | Candidate method | Output |
|---|---|---|
| What are the smooth trend and seasonal components? | STL | Trend, seasonal and remainder series |
| What is the robust monotonic slope? | Theil–Sen | Slope and intercept estimate |
| Is there evidence for one abrupt location shift? | Pettitt | Candidate split and test statistic |
| Can temporal autocorrelation support forecasts? | ARIMA / SARIMA | Model and forecast distribution |
| Can trend, seasonality and events support scalable forecasts? | Prophet | Decomposable forecast |
| What is the current latent state given noisy observations? | Kalman filter | State and covariance estimate |

## 9. Spatial evaluation and leakage

Time-series validation must respect time order. Randomly splitting individual observations can leak future information into training. For a forecast horizon H, use rolling-origin or expanding-window evaluation: fit only on observations up to a cutoff, forecast the next H steps, then move the cutoff forward.

For spatial collections, also hold out locations or regions when the intended deployment is to unseen places. A good design may need both temporal and spatial separation.

Report errors by horizon, season, region, land-cover class, sensor and data-quality stratum. Compare with simple baselines such as last observation, seasonal naïve and historical mean. A complex model that does not beat a transparent baseline is not automatically useful.

Avoid comparing forecasts on different sets of dates because of missingness. Record how missing values are treated, whether forecast intervals are calibrated, and whether model selection used the test period.

## 10. Reproducible tests

Use synthetic series with known components: linear and nonlinear trends; stable and changing seasonality; a step change; autocorrelated residuals; outliers; missing blocks; irregular timestamps; and a sensor offset.

Check that:
- STL reconstructs the observed series from trend + seasonal + remainder within numerical tolerance.
- Theil–Sen recovers the known slope under contamination and irregular time intervals.
- Pettitt has a controlled false-positive rate under its null assumptions and is tested separately under autocorrelation.
- ARIMA residuals are checked for remaining autocorrelation and forecast errors are measured out of sample.
- Prophet regressors and events are available at forecast time only.
- Kalman updates reduce uncertainty when informative observations arrive, and missing observations do not create fake measurements.

## Further reading

- Cleveland, R. B., Cleveland, W. S., McRae, J. E. and Terpenning, I. (1990), “STL: A Seasonal-Trend Decomposition Procedure Based on Loess,” *Journal of Official Statistics*, 6(1), 3–73. See the [statsmodels STL example](https://www.statsmodels.org/stable/examples/notebooks/generated/stl_decomposition.html) and [Forecasting: Principles and Practice STL chapter](https://otexts.robjhyndman.com/fpp2/stl.html).
- Sen, P. K. (1968), “Estimates of the Regression Coefficient Based on Kendall's Tau,” *Journal of the American Statistical Association*, 63(324), 1379–1389. [DOI 10.1080/01621459.1968.10480934](https://doi.org/10.1080/01621459.1968.10480934).
- Pettitt, A. N. (1979), “A Non-Parametric Approach to the Change-Point Problem,” *Journal of the Royal Statistical Society: Series C*, 28(2), 126–135. [DOI 10.2307/2346729](https://doi.org/10.2307/2346729).
- Box, G. E. P., Jenkins, G. M., Reinsel, G. C. and Ljung, G. M. (2015), *Time Series Analysis: Forecasting and Control*, 5th ed., Wiley.
- Taylor, S. J. and Letham, B. (2018), “Forecasting at Scale,” *The American Statistician*, 72(1), 37–45. [DOI 10.1080/00031305.2017.1380080](https://doi.org/10.1080/00031305.2017.1380080).
- Kalman, R. E. (1960), “A New Approach to Linear Filtering and Prediction Problems,” *Journal of Basic Engineering*, 82(1), 35–45. [DOI 10.1115/1.3662552](https://doi.org/10.1115/1.3662552).

## Scope

This is a method-selection and mathematical guide, not a forecasting package. It does not claim to implement STL, Theil–Sen, Pettitt, ARIMA, Prophet or Kalman filtering. These methods have different objectives and assumptions; a future practical module should implement and validate them separately rather than hiding them behind a single generic “time-series” function.
