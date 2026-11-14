import pytest
from adaptive_sampling import adaptive_cluster_sample

def test_positive_unit_recruits_neighbourhood_recursively():
    values=[0,5,0,6,0]
    graph=[[1],[0,2],[1,3],[2,4],[3]]
    result=adaptive_cluster_sample(values,graph,[0],threshold=5)
    assert result.initial_indices==(0,)
    assert result.sampled_indices==(0,1,2,3,4)
    assert result.recruited_indices==(1,2,3,4)

def test_nonqualifying_initial_unit_does_not_expand():
    result=adaptive_cluster_sample([1,0,0],[[1],[0,2],[1]],[0],threshold=2)
    assert result.sampled_indices==(0,)
    assert result.recruited_indices==()

def test_multiple_initial_units_and_cycles_do_not_duplicate():
    graph=[[1,2],[0,2],[0,1,3],[2]]
    result=adaptive_cluster_sample([5,0,5,0],graph,[0,2],threshold=5)
    assert result.sampled_indices==(0,1,2,3)
    assert len(result.sampled_indices)==len(set(result.sampled_indices))

def test_asymmetric_network_rejected():
    with pytest.raises(ValueError):
        adaptive_cluster_sample([1,2],[[1],[]],[0],1)

def test_invalid_inputs_rejected():
    with pytest.raises(ValueError):adaptive_cluster_sample([],[],[0],1)
    with pytest.raises(ValueError):adaptive_cluster_sample([1,2],[[1],[0]],[],1)
    with pytest.raises(ValueError):adaptive_cluster_sample([1,2],[[1],[0]],[2],1)
