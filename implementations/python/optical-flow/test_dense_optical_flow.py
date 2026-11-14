import numpy as np
import pytest
import cv2
from dense_optical_flow import farneback, dis

def translated_pair():
    rng=np.random.default_rng(22)
    first=(rng.random((96,96))*255).astype(np.uint8)
    first=cv2.GaussianBlur(first,(5,5),0)
    matrix=np.float32([[1,0,3],[0,1,-2]])
    second=cv2.warpAffine(first,matrix,(96,96),flags=cv2.INTER_LINEAR,
                          borderMode=cv2.BORDER_REFLECT)
    return first,second

def test_farneback_recovers_translation_direction_and_shape():
    a,b=translated_pair()
    result=farneback(a,b)
    region=np.s_[15:-15,15:-15]
    assert result["u"].shape==a.shape and result["v"].shape==a.shape
    assert np.nanmedian(result["u"][region])==pytest.approx(3,abs=.8)
    assert np.nanmedian(result["v"][region])==pytest.approx(-2,abs=.8)
    assert result["method"]=="farneback"

def test_dis_recovers_translation_direction_and_shape():
    a,b=translated_pair()
    result=dis(a,b,preset="medium")
    region=np.s_[20:-20,20:-20]
    assert result["flow"].shape==(*a.shape,2)
    assert np.nanmedian(result["u"][region])==pytest.approx(3,abs=1.5)
    assert np.nanmedian(result["v"][region])==pytest.approx(-2,abs=1.5)
    assert result["method"]=="dis"

def test_rejects_invalid_parameters_and_frames():
    a=np.zeros((32,32),dtype=np.uint8)
    with pytest.raises(ValueError): farneback(a,a,pyr_scale=1.0)
    with pytest.raises(ValueError): farneback(a,a,winsize=4)
    with pytest.raises(ValueError): dis(a,a,preset="unknown")
    with pytest.raises(ValueError): dis(a,a,patch_stride=0)
    with pytest.raises(ValueError): farneback(np.zeros((4,4)),np.zeros((4,4)))
