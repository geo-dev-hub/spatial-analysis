import numpy as np
import pytest
from geophysical_gridding import nearest_neighbor_grid,triangulation_grid

POINTS=np.array([[0,0],[2,0],[0,2],[2,2]],dtype=float)
VALUES=np.array([1,5,-5,-1],dtype=float)

def test_nearest_neighbor_returns_sample_value_at_sample_node():
    out=nearest_neighbor_grid(POINTS,VALUES,[0,2],[0,2])
    np.testing.assert_allclose(out,[[1,5],[-5,-1]])

def test_nearest_neighbor_max_distance_masks_far_nodes():
    out=nearest_neighbor_grid(POINTS,VALUES,[0,10],[0],max_distance=1)
    assert out[0,0]==1 and np.isnan(out[0,1])

def test_triangulation_reproduces_affine_plane():
    p=np.array([[0,0],[2,0],[0,2],[2,2],[1,.5]])
    v=2*p[:,0]-3*p[:,1]+1
    out=triangulation_grid(p,v,[.25,.75,1.25],[.25,.75,1.25])
    x,y=np.meshgrid([.25,.75,1.25],[.25,.75,1.25])
    np.testing.assert_allclose(out,2*x-3*y+1)

def test_triangulation_fills_outside_convex_hull():
    out=triangulation_grid(POINTS,VALUES,[-1,1,3],[1],fill_value=-999)
    assert out[0,0]==-999 and out[0,2]==-999

def test_invalid_and_degenerate_samples_rejected():
    with pytest.raises(ValueError):nearest_neighbor_grid([[0,0],[0,0]],[1,2],[0],[0])
    with pytest.raises(ValueError):triangulation_grid([[0,0],[1,1],[2,2]],[1,2,3],[0],[0])


def test_thin_plate_spline_reproduces_affine_plane_and_sample_values():
    from geophysical_gridding import thin_plate_spline_grid
    p = np.array([[0, 0], [2, 0], [0, 2], [2, 2], [1, .5]], dtype=float)
    v = 2 * p[:, 0] - 3 * p[:, 1] + 1
    out = thin_plate_spline_grid(p, v, [0, 1, 2], [0, 1, 2])
    x, y = np.meshgrid([0, 1, 2], [0, 1, 2])
    np.testing.assert_allclose(out, 2 * x - 3 * y + 1, atol=1e-9)


def test_thin_plate_spline_smoothing_is_finite_and_shape_preserving():
    from geophysical_gridding import thin_plate_spline_grid
    p = np.array([[0, 0], [2, 0], [0, 2], [2, 2], [1, .5]], dtype=float)
    v = np.array([0, 1, 1, 0, 2], dtype=float)
    out = thin_plate_spline_grid(p, v, np.linspace(0, 2, 9), np.linspace(0, 2, 7), smoothing=.1)
    assert out.shape == (7, 9)
    assert np.all(np.isfinite(out))


@pytest.mark.parametrize("smoothing", [-1, float("nan"), float("inf")])
def test_thin_plate_spline_rejects_invalid_smoothing(smoothing):
    from geophysical_gridding import thin_plate_spline_grid
    with pytest.raises(ValueError):
        thin_plate_spline_grid(POINTS, VALUES, [0, 1], [0, 1], smoothing=smoothing)


def test_thin_plate_spline_rejects_collinear_samples():
    from geophysical_gridding import thin_plate_spline_grid
    with pytest.raises(ValueError, match="non-degenerate"):
        thin_plate_spline_grid([[0, 0], [1, 1], [2, 2]], [0, 1, 2], [0, 1], [0, 1])


def test_ordinary_kriging_reproduces_constant_mean_without_nugget():
    from geophysical_gridding import ordinary_kriging_grid
    p = np.array([[0, 0], [1, 0], [0, 1], [1, 1]], dtype=float)
    v = np.full(4, 7.5)
    result = ordinary_kriging_grid(p, v, [0, .5, 1], [0, .5, 1], range_=2, sill=3)
    np.testing.assert_allclose(result["prediction"], 7.5, atol=1e-10)
    assert np.all(result["variance"] >= 0)
    assert result["variance"].shape == (3, 3)


def test_ordinary_kriging_interpolates_sample_nodes_when_nugget_is_zero():
    from geophysical_gridding import ordinary_kriging_grid
    p = np.array([[0, 0], [2, 0], [0, 2], [2, 2]], dtype=float)
    v = np.array([1, 5, -5, -1], dtype=float)
    result = ordinary_kriging_grid(p, v, [0, 2], [0, 2], range_=3, sill=2)
    np.testing.assert_allclose(result["prediction"], v.reshape(2, 2), atol=1e-9)
    assert np.max(result["variance"]) < 1e-8


def test_ordinary_kriging_returns_nonnegative_variance_with_nugget():
    from geophysical_gridding import ordinary_kriging_grid
    result = ordinary_kriging_grid(POINTS, VALUES, [.5, 1], [.5, 1], range_=2, sill=3, nugget=.2)
    assert np.all(np.isfinite(result["prediction"]))
    assert np.all(result["variance"] >= 0)


@pytest.mark.parametrize("range_,sill,nugget", [(0, 1, 0), (1, 0, 0), (1, 1, -1), (float("nan"), 1, 0)])
def test_ordinary_kriging_rejects_invalid_covariance_parameters(range_, sill, nugget):
    from geophysical_gridding import ordinary_kriging_grid
    with pytest.raises(ValueError):
        ordinary_kriging_grid(POINTS, VALUES, [0, 1], [0, 1], range_, sill, nugget)


def test_ordinary_kriging_rejects_single_sample():
    from geophysical_gridding import ordinary_kriging_grid
    with pytest.raises(ValueError):
        ordinary_kriging_grid([[0, 0]], [1], [0], [0], 1, 1)
