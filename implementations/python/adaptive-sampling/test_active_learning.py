import pytest
from active_learning import select_uncertain_spatial_sites

def test_selects_highest_uncertainty_candidates():
    out=select_uncertain_spatial_sites([[0,0],[10,0],[20,0]],[.1,.9,.5],2)
    assert out["selected_indices"]==[1,2]

def test_minimum_distance_enforces_spatial_diversity():
    out=select_uncertain_spatial_sites([[0,0],[.5,0],[5,0]],[.9,.8,.7],2,min_distance=1)
    assert out["selected_indices"]==[0,2]

def test_cost_adjusted_uncertainty():
    out=select_uncertain_spatial_sites([[0,0],[1,0],[2,0]],[.9,.8,.4],1,costs=[3,1,1])
    assert out["selected_indices"]==[1]

def test_infeasible_batch_is_reported():
    with pytest.raises(ValueError,match="permits only"):
        select_uncertain_spatial_sites([[0,0],[.1,0],[.2,0]],[1,1,1],3,min_distance=1)

def test_invalid_inputs_rejected():
    with pytest.raises(ValueError):select_uncertain_spatial_sites([[0,0]],[1],0)
    with pytest.raises(ValueError):select_uncertain_spatial_sites([[0,0]],[1],1,costs=[0])
    with pytest.raises(ValueError):select_uncertain_spatial_sites([[0,0]],[1],1,min_distance=-1)
