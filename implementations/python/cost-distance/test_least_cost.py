import numpy as np
import pytest
from least_cost import least_cost_distance

def test_uniform_cost_surface_matches_euclidean_path_lengths():
    result=least_cost_distance(np.ones((3,3)),[(1,1)])
    assert result[1,2]==1
    np.testing.assert_allclose(result[0,0],2**0.5)
    four=least_cost_distance(np.ones((3,3)),[(1,1)],connectivity=4)
    assert four[0,0]==2

def test_rectangular_cell_spacing_changes_diagonal_cost():
    result=least_cost_distance(np.ones((3,3)),[(1,1)],cell_size_x=2,cell_size_y=1)
    np.testing.assert_allclose(result[0,2],np.hypot(2,1))
    np.testing.assert_allclose(result[0,0],np.hypot(2,1))

def test_high_cost_cells_are_avoided_when_detour_is_cheaper():
    cost=np.ones((3,5)); cost[:,2]=100
    result=least_cost_distance(cost,[(1,0)],connectivity=4)
    assert result[1,4] < 200

def test_nodata_is_a_barrier_and_unreachable_valid_cells_are_infinite():
    cost=np.array([[1,np.nan,1],[1,np.nan,1],[1,np.nan,1]],float)
    result=least_cost_distance(cost,[(1,0)])
    assert np.isinf(result[1,2])
    assert np.isnan(result[1,1])

def test_multiple_sources_choose_lowest_accumulated_cost():
    result=least_cost_distance(np.ones((1,5)),[(0,0),(0,4)],connectivity=4)
    np.testing.assert_allclose(result,[[0,1,2,1,0]])

def test_corner_cutting_can_be_forbidden():
    cost=np.array([[1,np.nan],[np.nan,1]],float)
    blocked=least_cost_distance(cost,[(0,0)],prevent_corner_cutting=True)
    allowed=least_cost_distance(cost,[(0,0)],prevent_corner_cutting=False)
    assert np.isinf(blocked[1,1])
    assert np.isfinite(allowed[1,1])

def test_invalid_sources_costs_and_parameters_are_rejected():
    with pytest.raises(ValueError,match="at least one"):
        least_cost_distance([[1]],[])
    with pytest.raises(ValueError,match="outside"):
        least_cost_distance([[1]],[(1,0)])
    with pytest.raises(ValueError,match="valid"):
        least_cost_distance([[np.nan]],[(0,0)])
    with pytest.raises(ValueError,match="non-negative"):
        least_cost_distance([[-1]],[(0,0)])
    with pytest.raises(ValueError,match="connectivity"):
        least_cost_distance([[1]],[(0,0)],connectivity=6)
