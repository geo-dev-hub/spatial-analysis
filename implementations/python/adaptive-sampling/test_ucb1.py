import numpy as np
import pytest
from ucb1 import select_ucb1_arm,run_ucb1

def test_ucb1_selects_untried_arms_first():
    counts=np.array([1,0,0]);means=np.array([0.,0.,0.])
    assert select_ucb1_arm(counts,means,1)==1

def test_ucb1_budget_and_counts_are_consistent():
    out=run_ucb1([0,1,2],budget=30,noise_std=.1,random_state=4)
    assert len(out["choices"])==30 and len(out["rewards"])==30
    assert int(out["counts"].sum())==30
    assert np.all(out["counts"]>=1)

def test_ucb1_is_reproducible():
    a=run_ucb1([0,1,2],100,.2,7);b=run_ucb1([0,1,2],100,.2,7)
    assert a["choices"]==b["choices"] and a["rewards"]==b["rewards"]

def test_ucb1_learns_high_mean_arm_in_simple_stationary_case():
    out=run_ucb1([0,0,2],budget=500,noise_std=.1,random_state=2)
    assert out["counts"][2]>out["counts"][0]
    assert out["counts"][2]>out["counts"][1]

def test_invalid_bandit_inputs_rejected():
    with pytest.raises(ValueError):select_ucb1_arm([0,0],[0,0],1)
    with pytest.raises(ValueError):run_ucb1([],10)
    with pytest.raises(ValueError):run_ucb1([1,2],0)
