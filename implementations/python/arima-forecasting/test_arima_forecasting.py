import numpy as np
import pytest
from arima_forecasting import fit_arima

def test_arima_returns_requested_forecast_and_interval_shapes():
    rng=np.random.default_rng(4)
    y=np.zeros(100)
    noise=rng.normal(0,0.4,100)
    for i in range(1,len(y)): y[i]=0.7*y[i-1]+noise[i]
    result=fit_arima(y,(1,0,0),steps=6)
    assert len(result["forecast"])==6
    assert np.asarray(result["confidence_interval"]).shape==(6,2)
    assert np.isfinite(result["aic"]) and np.isfinite(result["bic"])

def test_arima_differencing_handles_linear_trend():
    t=np.arange(80,dtype=float)
    y=0.5*t+np.random.default_rng(2).normal(0,0.1,80)
    result=fit_arima(y,(1,1,0),steps=4)
    assert len(result["forecast"])==4
    assert result["forecast"][-1]>result["forecast"][0]

def test_seasonal_arima_returns_finite_forecast():
    t=np.arange(120)
    y=10+0.02*t+2*np.sin(2*np.pi*t/12)+np.random.default_rng(8).normal(0,0.15,120)
    result=fit_arima(y,(1,1,0),steps=12,seasonal_order=(1,0,0,12))
    assert len(result["forecast"])==12
    assert np.isfinite(result["forecast"]).all()

@pytest.mark.parametrize("values,order,steps",[
    ([1,2,3],(0,0,0),1),([1,2,3,4,5,6,7,8,float("nan")],(0,0,0),1),
    ([1,2,3,4,5,6,7,8],(-1,0,0),1),([1,2,3,4,5,6,7,8],(0,0,0),0)
])
def test_rejects_invalid_inputs(values,order,steps):
    with pytest.raises(ValueError): fit_arima(values,order,steps)
