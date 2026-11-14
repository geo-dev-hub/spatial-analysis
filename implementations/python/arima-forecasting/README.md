# ARIMA and seasonal ARIMA forecasting

A transparent teaching wrapper around `statsmodels.tsa.arima.model.ARIMA`.
It supports non-seasonal ARIMA(p,d,q) and seasonal ARIMA via an explicit
`seasonal_order=(P,D,Q,s)`.

```python
from arima_forecasting import fit_arima
result = fit_arima(values, order=(1,1,1), steps=12)
forecast = result["forecast"]
interval = result["confidence_interval"]
```

Install dependencies with `python -m pip install -r requirements.txt`;
run `python -m pytest -q`.

The wrapper returns in-sample fitted values, forecasts, model-based confidence
intervals, AIC/BIC and the optimizer convergence flag. It does not select
orders, guarantee stationarity, diagnose residuals, model spatial dependence,
or establish forecast skill. Choose orders using training data only; inspect
residual autocorrelation; compare against naïve and seasonal-naïve baselines;
and evaluate with rolling-origin splits. Confidence intervals inherit model
assumptions and should be checked for calibration.

The underlying state-space likelihood and optimizer are provided by
statsmodels; this repository package is an educational interface, not an
independent ARIMA implementation.
