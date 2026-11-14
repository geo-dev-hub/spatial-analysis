import numpy as np
import pytest
from distribution_shift import mmd_squared,energy_distance,mmd_permutation_test

def test_separated_samples_have_positive_divergence():
    x=np.array([[0,0],[.1,0],[0,.1],[.1,.1]])
    y=x+4
    assert mmd_squared(x,y,bandwidth=1)>0
    assert energy_distance(x,y)>0

def test_permutation_test_is_reproducible_and_bounded():
    x=np.array([[0],[.1],[.2],[.3]])
    y=np.array([[2],[2.1],[2.2],[2.3]])
    a=mmd_permutation_test(x,y,1,n_permutations=49,random_state=7)
    b=mmd_permutation_test(x,y,1,n_permutations=49,random_state=7)
    assert a["p_value"]==b["p_value"]
    assert 0<a["p_value"]<=1
    assert np.array_equal(a["null_statistics"],b["null_statistics"])

def test_identical_samples_have_small_population_signal():
    x=np.array([[0,0],[1,0],[0,1],[1,1]],dtype=float)
    assert abs(mmd_squared(x,x,1))<1e-12
    assert energy_distance(x,x)==pytest.approx(0)

@pytest.mark.parametrize("fn,args",[(mmd_squared,(1,)),(energy_distance,())])
def test_invalid_samples_rejected(fn,args):
    with pytest.raises(ValueError):fn([[1],[2]],[[1,2],[2,3]],*args)

def test_invalid_bandwidth_and_permutations():
    with pytest.raises(ValueError):mmd_squared([[0],[1]],[[2],[3]],0)
    with pytest.raises(ValueError):mmd_permutation_test([[0],[1]],[[2],[3]],1,0)
