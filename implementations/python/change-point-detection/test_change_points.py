import pytest
from itertools import combinations
from change_points import binary_segmentation,cusum,pelt_mean

def test_binary_segmentation_one_shift():
    assert binary_segmentation([0.0]*8+[5.0]*8,1.0,2)==[8]
def test_binary_segmentation_multiple_shifts():
    got=binary_segmentation([0.0]*6+[4.0]*6+[-2.0]*6,1.0,2)
    assert 6 in got and 12 in got and got==sorted(got)
def test_pelt_one_shift():
    assert pelt_mean([0.0]*8+[5.0]*8,2.0,2)==[8]
def test_pelt_matches_exhaustive_partition_search():
    data=[0.0,.2,-.1,3.0,3.2,2.9,-1.0,-.8];penalty=1.5
    got=pelt_mean(data,penalty,2)
    def sse(a,b):
        z=data[a:b];m=sum(z)/len(z);return sum((x-m)**2 for x in z)
    candidates=[]
    for count in range(4):
        for cps in combinations(range(2,len(data)-1),count):
            bounds=(0,)+cps+(len(data),)
            if all(b-a>=2 for a,b in zip(bounds,bounds[1:])):
                candidates.append((sum(sse(a,b) for a,b in zip(bounds,bounds[1:]))+penalty*count,list(cps)))
    assert got==min(candidates,key=lambda x:x[0])[1]
def test_cusum_both_directions():
    assert cusum([0]*5+[3]*5,0,.5,2)[0][1]=="up"
    assert cusum([0]*5+[-3]*5,0,.5,2)[0][1]=="down"
@pytest.mark.parametrize("fn,args",[(binary_segmentation,{"penalty":-1}),(pelt_mean,{"penalty":-1}),(cusum,{"target_mean":0,"allowance":-1,"threshold":1})])
def test_bad_parameters(fn,args):
    with pytest.raises(ValueError):fn([1,2,3,4],**args)
def test_nonfinite_series():
    with pytest.raises(ValueError):pelt_mean([1,float("nan"),2],1)


from change_points import pettitt_test

def _pettitt_direct(values):
    n=len(values)
    stats=[]
    for split in range(1,n):
        u=sum((1 if values[i]>values[j] else -1 if values[i]<values[j] else 0)
              for i in range(split) for j in range(split,n))
        stats.append(u)
    return stats

def test_pettitt_detects_single_upward_shift():
    result=pettitt_test([0.0]*8+[5.0]*8)
    assert result["change_index"]==8
    assert result["statistic"]<0
    assert result["p_value_approx"]<0.05

def test_pettitt_matches_pairwise_definition_with_ties():
    values=[1,1,2,2,5,5,6,6]
    result=pettitt_test(values)
    direct=_pettitt_direct(values)
    assert result["K"]==max(abs(x) for x in direct)
    assert result["statistic"]==direct[result["change_index"]-1]

def test_pettitt_is_invariant_to_strictly_increasing_transform():
    values=[0,0,1,1,4,4,5,5]
    transformed=[3*x+7 for x in values]
    a,b=pettitt_test(values),pettitt_test(transformed)
    assert a["change_index"]==b["change_index"]
    assert a["K"]==b["K"]

def test_pettitt_rejects_too_short_and_nonfinite_series():
    with pytest.raises(ValueError):pettitt_test([1.0])
    with pytest.raises(ValueError):pettitt_test([1.0,float("inf")])
