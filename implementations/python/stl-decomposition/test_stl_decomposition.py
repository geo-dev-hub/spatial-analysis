import numpy as np
import pytest
from stl_decomposition import stl_decompose

def series(n=120, period=12):
    t=np.arange(n)
    return 0.03*t + 2*np.sin(2*np.pi*t/period)

def test_components_reconstruct_observations():
    y=series()
    p=stl_decompose(y,12)
    np.testing.assert_allclose(np.array(p["trend"])+p["seasonal"]+p["resid"],y,atol=1e-10)

def test_component_lengths_and_robust_flag():
    p=stl_decompose(series(96),12,robust=True)
    assert len(p["trend"])==96 and len(p["seasonal"])==96 and len(p["resid"])==96
    assert p["robust"] is True

def test_seasonal_component_repeats_at_requested_period():
    s=np.array(stl_decompose(series(240),12)["seasonal"])
    np.testing.assert_allclose(s[36:-36],s[48:-24],atol=0.25)

@pytest.mark.parametrize("values,period", [([1,2],2),([1,float("nan"),3,4],2),([1,2,3,4],0),([1,2,3,4],3)])
def test_invalid_series(values,period):
    with pytest.raises(ValueError): stl_decompose(values,period)

@pytest.mark.parametrize("seasonal",[2,4,0])
def test_invalid_seasonal_window(seasonal):
    with pytest.raises(ValueError): stl_decompose(series(),12,seasonal=seasonal)
