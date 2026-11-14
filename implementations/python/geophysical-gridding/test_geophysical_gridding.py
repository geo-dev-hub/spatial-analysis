import numpy as np
import pytest
from geophysical_gridding import nearest_neighbor_grid,triangulation_grid

POINTS=np.array([[0,0],[2,0],[0,2],[2,2]],dtype=float)
VALUES=np.array([1,5,-5,-1],dtype=float)

def test_nearest_neighbor_returns_sample_value_at_sample_node():
    out=nearest_neighbor_grid(POINTS,VALUES,[0,2],[0,2])
    assert out==pytest.approx([[1,5],[-5,-1]])

def test_nearest_neighbor_max_distance_masks_far_nodes():
    out=nearest_neighbor_grid(POINTS,VALUES,[0,10],[0],max_distance=1)
    assert out[0,0]==1 and np.isnan(out[0,1])

def test_triangulation_reproduces_affine_plane():
    p=np.array([[0,0],[2,0],[0,2],[2,2],[1,.5]])
    v=2*p[:,0]-3*p[:,1]+1
    out=triangulation_grid(p,v,[.25,.75,1.25],[.25,.75,1.25])
    x,y=np.meshgrid([.25,.75,1.25],[.25,.75,1.25])
    assert out==pytest.approx(2*x-3*y+1)

def test_triangulation_fills_outside_convex_hull():
    out=triangulation_grid(POINTS,VALUES,[-1,1,3],[1],fill_value=-999)
    assert out[0,0]==-999 and out[0,2]==-999

def test_invalid_and_degenerate_samples_rejected():
    with pytest.raises(ValueError):nearest_neighbor_grid([[0,0],[0,0]],[1,2],[0],[0])
    with pytest.raises(ValueError):triangulation_grid([[0,0],[1,1],[2,2]],[1,2,3],[0],[0])
