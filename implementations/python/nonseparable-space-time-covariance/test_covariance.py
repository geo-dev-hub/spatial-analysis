import numpy as np
import pytest
from covariance import gneiting_covariance, gneiting_covariance_matrix, covariance_matrix_diagnostics

def test_zero_lags_equal_variance():
    assert gneiting_covariance(0,0,variance=3.5)==pytest.approx(3.5)

def test_lag_symmetry():
    assert gneiting_covariance(2,4)==pytest.approx(gneiting_covariance(2,-4))

def test_beta_zero_has_no_temporal_decay():
    assert gneiting_covariance(1.7,0,beta=0)==pytest.approx(gneiting_covariance(1.7,100,beta=0))

def test_time_lag_changes_covariance_when_beta_positive():
    assert gneiting_covariance(1,2,beta=1)<gneiting_covariance(1,0,beta=1)

def test_irregular_covariance_matrix_is_psd():
    xy=np.array([[0,0],[1,0],[0,2],[2,1],[3,0]],float); t=np.array([0,.5,1.5,2,4])
    K=gneiting_covariance_matrix(xy,t,alpha=.7,beta=.8)
    d=covariance_matrix_diagnostics(K)
    assert d["symmetric"] and d["positive_semidefinite"]

def test_duplicate_observations_have_duplicate_rows():
    K=gneiting_covariance_matrix([[0,0],[1,0],[0,0]],[0,1,0])
    assert np.allclose(K[0],K[2])

@pytest.mark.parametrize("kw",[{"variance":-1},{"spatial_scale":0},{"temporal_scale":0},{"alpha":0},{"alpha":1.1},{"beta":-.1},{"beta":1.1},{"spatial_dimension":0}])
def test_invalid_parameters(kw):
    with pytest.raises(ValueError): gneiting_covariance(1,1,**kw)

@pytest.mark.parametrize("h,u",[(-1,0),(np.nan,0),(1,np.inf)])
def test_invalid_lags(h,u):
    with pytest.raises(ValueError): gneiting_covariance(h,u)
