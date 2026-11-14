import pytest
from bayesian_online import bayesian_online_changepoint

def test_run_length_posteriors_normalise():
    out=bayesian_online_changepoint([0,.1,-.1,0,4,4.1,3.9],.05,.2)
    assert all(sum(row)==pytest.approx(1.0) for row in out["run_length_posterior"])
    assert len(out["change_probability"])==7 and len(out["map_run_length"])==7

def test_abrupt_shift_increases_change_evidence():
    out=bayesian_online_changepoint([0.0]*20+[5.0]*5,.02,.1,0,1)
    assert max(out["change_probability"][20:])>out["change_probability"][10]

def test_constant_series_does_not_force_change_at_every_step():
    out=bayesian_online_changepoint([0.0]*12,.05,.5)
    assert all(0<=p<=1 for p in out["change_probability"])
    assert out["change_probability"][-1]<.5

@pytest.mark.parametrize("args",[(0,.1),(1,.1),(.1,0),(.1,1,0,0)])
def test_invalid_model_parameters(args):
    with pytest.raises(ValueError):bayesian_online_changepoint([1,2,3],*args)

def test_invalid_series_rejected():
    with pytest.raises(ValueError):bayesian_online_changepoint([1,float("nan")],.1,1)
