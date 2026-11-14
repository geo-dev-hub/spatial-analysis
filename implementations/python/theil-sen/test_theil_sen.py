import pytest
from theil_sen import theil_sen

def test_exact_linear_trend():
    result=theil_sen([0,1,2,3],[2,5,8,11])
    assert result["slope"]==3
    assert result["intercept"]==2
    assert result["pair_count"]==6

def test_robust_to_one_extreme_observation():
    result=theil_sen([0,1,2,3,4],[0,1,2,3,1000])
    assert result["slope"]==1
    assert result["intercept"]==0

def test_irregular_time_uses_elapsed_time():
    result=theil_sen([0,2,5],[1,5,11])
    assert result["slope"]==2
    assert result["intercept"]==1

def test_duplicate_times_are_excluded_from_slope_pairs():
    result=theil_sen([0,0,1],[1,3,5])
    assert result["pair_count"]==2
    assert result["slope"]==3

@pytest.mark.parametrize("times,values",[
    ([1],[2]),([1,1],[2,3]),([1,2],[2]),([1,float("nan")],[2,3])
])
def test_invalid_inputs(times,values):
    with pytest.raises(ValueError):theil_sen(times,values)
