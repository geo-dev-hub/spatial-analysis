import numpy as np
import pytest
from terrain_indices import topographic_wetness_index

def test_matches_conventional_log_area_over_tangent_slope():
    area=np.array([[10.0]])
    slope=np.array([[30.0]])
    result=topographic_wetness_index(area,slope)
    expected = np.log(10 / np.tan(np.radians(30)))
    np.testing.assert_allclose(result, np.array([[expected]]))

def test_flat_slope_uses_declared_positive_floor():
    result=topographic_wetness_index([[10]],[[0]],slope_floor_degrees=1)
    expected = np.log(10 / np.tan(np.radians(1)))
    np.testing.assert_allclose(result, np.array([[expected]]))

def test_nonpositive_area_and_nodata_are_masked():
    result=topographic_wetness_index([[0,np.nan,10]],[[20,20,np.nan]])
    assert np.isnan(result).all()

def test_shape_slope_and_floor_contracts():
    with pytest.raises(ValueError,match="same shape"):
        topographic_wetness_index([[1]],[[1,2]])
    with pytest.raises(ValueError,match="\[0, 90\)"):
        topographic_wetness_index([[1]],[[90]])
    with pytest.raises(ValueError,match="slope_floor"):
        topographic_wetness_index([[1]],[[10]],slope_floor_degrees=0)
    with pytest.raises(ValueError,match="slope_floor"):
        topographic_wetness_index([[1]],[[10]],slope_floor_degrees="flat")
