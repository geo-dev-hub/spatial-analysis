import numpy as np
import pytest
from terrain_derivatives import horn_slope_aspect

def test_east_rising_plane_has_westward_aspect():
    result=horn_slope_aspect(np.tile(np.arange(5,dtype=float),(5,1)))
    np.testing.assert_allclose(result["slope_degrees"][2,2],45)
    np.testing.assert_allclose(result["slope_percent"][2,2],100)
    np.testing.assert_allclose(result["aspect_degrees"][2,2],270)

def test_north_rising_plane_has_southward_aspect():
    dem=np.tile(np.arange(5,0,-1,dtype=float)[:,None],(1,5))
    result=horn_slope_aspect(dem)
    np.testing.assert_allclose(result["slope_degrees"][2,2],45)
    np.testing.assert_allclose(result["aspect_degrees"][2,2],180)

def test_rectangular_spacing_and_vertical_conversion():
    dem=np.tile(np.arange(5,dtype=float),(5,1))
    result=horn_slope_aspect(dem,cell_size_x=2,cell_size_y=5,z_factor=2)
    np.testing.assert_allclose(result["slope_percent"][2,2],100)
    np.testing.assert_allclose(result["aspect_degrees"][2,2],270)

def test_flat_has_zero_slope_and_undefined_aspect():
    result=horn_slope_aspect(np.ones((5,5)))
    assert result["slope_degrees"][2,2]==0
    assert result["slope_percent"][2,2]==0
    assert np.isnan(result["aspect_degrees"][2,2])

def test_edges_and_nodata_windows_are_nan():
    dem=np.ones((5,5)); dem[2,2]=np.nan
    result=horn_slope_aspect(dem)
    assert np.isnan(result["slope_degrees"][0,0])
    assert np.isnan(result["slope_degrees"][2,2])
    assert np.isnan(result["slope_degrees"][1,1])
    assert np.isnan(result["slope_degrees"][3,3])

def test_small_grids_return_nan_outputs():
    result=horn_slope_aspect(np.ones((2,4)))
    assert all(np.isnan(a).all() for a in result.values())

@pytest.mark.parametrize("kwargs",[{"cell_size_x":0},{"cell_size_y":-1},{"z_factor":0},{"cell_size_x":float("inf")}])
def test_invalid_spacing_rejected(kwargs):
    with pytest.raises(ValueError): horn_slope_aspect(np.ones((3,3)),**kwargs)

def test_non_2d_input_rejected():
    with pytest.raises(ValueError,match="2D"): horn_slope_aspect([1,2,3])
