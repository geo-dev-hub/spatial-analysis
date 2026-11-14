from __future__ import annotations
from typing import Iterable
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

def fit_arima(values: Iterable[float], order: tuple[int,int,int], steps: int, *, seasonal_order: tuple[int,int,int,int] = (0,0,0,0)):
    """Fit a statsmodels ARIMA/SARIMA model and return forecasts and diagnostics.

    This is a transparent wrapper around statsmodels, not a new optimizer or
    implementation of the state-space likelihood.
    """
    y=np.asarray(list(values),dtype=float)
    if y.ndim != 1 or y.size < 8 or not np.isfinite(y).all():
        raise ValueError("values must be a finite one-dimensional series with >= 8 observations")
    if len(order)!=3 or any(not isinstance(v,int) or v<0 for v in order):
        raise ValueError("order must contain three non-negative integers")
    if len(seasonal_order)!=4 or any(not isinstance(v,int) or v<0 for v in seasonal_order):
        raise ValueError("seasonal_order must contain four non-negative integers")
    if seasonal_order[3] == 1:
        raise ValueError("seasonal period must be zero or at least two")
    if not isinstance(steps,int) or steps<1:
        raise ValueError("steps must be a positive integer")
    p,d,q=order
    if y.size <= p+d+q+1:
        raise ValueError("series is too short for the requested ARIMA order")
    model=ARIMA(y,order=order,seasonal_order=seasonal_order)
    result=model.fit()
    forecast=result.get_forecast(steps=steps)
    interval=forecast.conf_int()
    return {
        "fitted": np.asarray(result.fittedvalues,dtype=float).tolist(),
        "forecast": np.asarray(forecast.predicted_mean,dtype=float).tolist(),
        "confidence_interval": np.asarray(interval,dtype=float).tolist(),
        "aic": float(result.aic),
        "bic": float(result.bic),
        "order": tuple(order),
        "seasonal_order": tuple(seasonal_order),
        "converged": bool(result.mle_retvals.get("converged", True)),
    }
