import numpy as np
import pytest
from kalman_smoothing import kalman_rts_smoother

def model(y):
    return kalman_rts_smoother(y,[[1.0]],[[1.0]],[[0.1]],[[1.0]],[0.0],[[1.0]])

def test_filter_and_smoother_shapes_and_finite_values():
    out=model([0.2,0.4,0.1,0.3])
    assert out["filtered_means"].shape==(4,1)
    assert out["smoothed_covariances"].shape==(4,1,1)
    assert np.all(np.isfinite(out["smoothed_means"]))

def test_rts_smoother_uses_future_observations():
    out=model([0.0,10.0,0.0])
    assert out["smoothed_means"][1,0] < out["filtered_means"][1,0]
    assert out["smoothed_means"][1,0] > out["smoothed_means"][2,0]

def test_missing_observation_performs_prediction_only():
    out=model([1.0,float("nan"),1.0])
    assert np.isfinite(out["filtered_means"][1,0])
    assert out["filtered_covariances"][1,0,0] > out["filtered_covariances"][0,0,0]

def test_multidimensional_constant_velocity_model():
    F=[[1,1],[0,1]];H=[[1,0]]
    out=kalman_rts_smoother([0,1,2,3],F,H,[[.01,0],[0,.01]],[[.1]],[0,0],[[1,0],[0,1]])
    assert out["smoothed_means"].shape==(4,2)

def test_invalid_covariance_rejected():
    with pytest.raises(ValueError):
        kalman_rts_smoother([1,2],[[1]],[[1]],[[-1]],[[1]],[0],[[1]])

def test_invalid_observation_shape_rejected():
    with pytest.raises(ValueError):
        kalman_rts_smoother([[1,2]],[[1]],[[1]],[[1]],[[1]],[0],[[1]])
