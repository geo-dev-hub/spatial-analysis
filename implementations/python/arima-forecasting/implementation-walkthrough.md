# Intern walkthrough: ARIMA forecasting

ARIMA(p,d,q) combines:
- p autoregressive lags of the differenced series;
- d rounds of differencing to address non-stationary level/trend;
- q moving-average lags of innovations.

Seasonal ARIMA adds (P,D,Q,s) terms at seasonal period s. The package passes
these orders directly to statsmodels' state-space ARIMA implementation.

A responsible workflow is: plot and understand the series; establish a
training-only differencing strategy; compare a small candidate set; inspect
residual autocorrelation and stability; forecast beyond the training cutoff;
and evaluate rolling-origin errors against naïve baselines. Do not choose
orders or transformations using the held-out test period.

The wrapper exposes fitted values, forecast means, model confidence intervals,
AIC/BIC and convergence status. It does not automate model selection or
diagnostics. A univariate ARIMA fitted independently at each pixel does not
represent spatial dependence and can be computationally expensive.
