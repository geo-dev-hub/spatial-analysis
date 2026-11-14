import numpy as np
import pytest
from nndm import nndm_loo

def test_regular_grid_remains_ordinary_loo_when_prediction_distances_are_not_shorter():
    x,y=np.meshgrid(np.arange(5)*10.,np.arange(5)*10.)
    train=np.column_stack([x.ravel(),y.ravel()])
    pred=np.column_stack([np.linspace(0,40,30),np.linspace(0,40,30)])
    result=nndm_loo(train,pred,autocorrelation_range=5,min_train=.5)
    assert result["n_removed"]==0
    assert all(len(f["train"])==len(train)-1 for f in result["folds"])

def test_clustered_samples_trigger_additional_exclusions():
    rng=np.random.default_rng(5)
    centres=np.array([[0.,0.],[100.,0.],[0.,100.],[100.,100.]])
    train=np.vstack([c+rng.normal(0,2,size=(10,2)) for c in centres])
    pred=rng.uniform(-10,110,size=(500,2))
    result=nndm_loo(train,pred,autocorrelation_range=30,min_train=.5)
    assert result["n_removed"]>0
    assert len(result["folds"])==len(train)
    for j,f in enumerate(result["folds"]):
        assert f["test"].tolist()==[j]
        assert len(f["train"])>=int(np.ceil(.5*len(train)))
        assert j not in f["train"]
        assert not set(f["excluded"]) & set(f["train"])

def test_extrapolation_reduces_to_phi_buffered_loo():
    rng=np.random.default_rng(11)
    train=rng.uniform(0,10,size=(12,2))
    pred=rng.uniform(100,110,size=(100,2))
    phi=15
    result=nndm_loo(train,pred,autocorrelation_range=phi,min_train=.2)
    for j,f in enumerate(result["folds"]):
        assert len(f["train"])>=3
        assert j not in f["train"]

def test_zero_range_is_ordinary_loo_and_validates_inputs():
    x=np.arange(20,dtype=float).reshape(10,2)
    result=nndm_loo(x,x,autocorrelation_range=0)
    assert result["n_removed"]==0
    with pytest.raises(ValueError): nndm_loo(x,x,autocorrelation_range=-1)
    with pytest.raises(ValueError): nndm_loo(x,x,min_train=0)
