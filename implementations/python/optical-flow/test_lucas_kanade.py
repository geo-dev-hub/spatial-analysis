import numpy as np
import pytest
from scipy.ndimage import shift
from lucas_kanade import lucas_kanade

def test_recovers_small_horizontal_translation():
    y,x=np.mgrid[0:64,0:64]
    first=np.sin(.25*x)+np.cos(.2*y)+.3*np.sin(.18*x+.31*y)
    second=shift(first,(0,.5),order=3,mode="wrap")
    out=lucas_kanade(first,second,window_size= 9)
    region=np.s_[10:-10,10:-10]
    valid=out["valid"][region]
    assert valid.sum()>100
    assert np.nanmedian(out["u"][region])==pytest.approx(.5,abs=.12)
    assert np.nanmedian(out["v"][region])==pytest.approx(0,abs=.12)

def test_constant_frames_have_no_valid_flow():
    out=lucas_kanade(np.ones((12,12)),np.ones((12,12)))
    assert not out["valid"].any()
    assert np.isnan(out["u"]).all() and np.isnan(out["v"]).all()

def test_output_shapes():
    out=lucas_kanade(np.random.default_rng(1).normal(size=(20,21)),np.random.default_rng(2).normal(size=(20,21)))
    assert out["u"].shape==(20,21) and out["valid"].shape==(20,21)

def test_invalid_inputs():
    with pytest.raises(ValueError):lucas_kanade([[1,2]],[[1,2]])
    with pytest.raises(ValueError):lucas_kanade(np.ones((3,3)),np.ones((3,3)),window_size=2)
    with pytest.raises(ValueError):lucas_kanade(np.ones((3,3)),np.ones((3,3)),min_determinant=-1)
