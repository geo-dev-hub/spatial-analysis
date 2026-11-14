import numpy as np
import pytest
from bayesian_optimization import gp_ucb_select

def test_prior_prefers_first_candidate_under_tie():
    out=gp_ucb_select([],[],[[0,0],[1,0]],length_scale=1,beta=0)
    assert out["selected_index"]==0
    np.testing.assert_allclose(out["posterior_std"],[1,1])

def test_posterior_uncertainty_is_lower_near_observation():
    out=gp_ucb_select([[0,0]],[2],[[0,0],[10,0]],length_scale=1,noise_variance=1e-8,beta=0)
    assert out["posterior_std"][0]<out["posterior_std"][1]
    assert out["posterior_mean"][0]>out["posterior_mean"][1]

def test_ucb_exploration_can_select_distant_uncertain_site():
    out=gp_ucb_select([[0,0]],[0],[[0,0],[10,0]],length_scale=1,beta=9)
    assert out["selected_index"]==1

def test_invalid_inputs_rejected():
    with pytest.raises(ValueError):gp_ucb_select([[0,0]],[1,2],[[1,1]],length_scale=1)
    with pytest.raises(ValueError):gp_ucb_select([],[],[[0,0]],length_scale=0)
    with pytest.raises(ValueError):gp_ucb_select([],[],[[0,0]],length_scale=1,beta=-1)
