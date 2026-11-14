import numpy as np
import pytest
from crps_decomposition import crps_brier_decomposition
from ensemble_verification import mean_crps_ensemble


def test_decomposition_adds_up_to_direct_integrated_brier_score():
    obs=[0.0,1.0,2.0,3.0,1.5]
    ens=[[0.2,0.4,0.8],[0.8,1.2,1.4],[1.5,2.2,2.8],[2.2,3.2,3.8],[1.0,1.5,2.0]]
    result=crps_brier_decomposition(obs,ens,n_thresholds=2001)
    assert result["crps"]==pytest.approx(result["direct_integrated_brier"],abs=1e-12)
    assert abs(result["decomposition_residual"])<1e-12
    assert result["reliability"]>=0
    assert result["resolution"]>=0
    assert result["uncertainty"]>=0


def test_dense_threshold_quadrature_approaches_empirical_ensemble_crps():
    obs=[0.0,1.0,2.0]
    ens=[[-1.0,0.5],[0.5,1.5],[1.0,3.0]]
    result=crps_brier_decomposition(obs,ens,n_thresholds=20001)
    direct=mean_crps_ensemble(obs,ens)
    assert result["crps"]==pytest.approx(direct,abs=2e-3)


def test_perfect_constant_ensemble_has_zero_decomposition():
    result=crps_brier_decomposition([4,4],[[4,4],[4,4]])
    assert result["crps"]==0
    assert result["reliability"]==0
    assert result["resolution"]==0
    assert result["uncertainty"]==0


def test_custom_threshold_grid_and_validation():
    result=crps_brier_decomposition([0,1],[[0,1],[0,1]],thresholds=[-1,0,0.5,1,2])
    assert result["crps"]==pytest.approx(result["direct_integrated_brier"])
    with pytest.raises(ValueError):
        crps_brier_decomposition([0,1],[[0],[1]],thresholds=[0,0])
    with pytest.raises(ValueError):
        crps_brier_decomposition([0,1],[[0],[1]],n_thresholds=1)
