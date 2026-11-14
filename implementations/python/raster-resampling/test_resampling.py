import numpy as np
import pytest
from resampling import resample_to_shape

def test_nearest_preserves_categorical_values():
    source=np.array([[1,2],[3,4]])
    result=resample_to_shape(source,(4,4),method="nearest")
    assert set(np.unique(result))=={1,2,3,4}

def test_bilinear_preserves_constant_surface():
    result=resample_to_shape(np.full((3,4),7.5),(8,9))
    np.testing.assert_allclose(result,7.5)

def test_bilinear_reproduces_planar_surface_at_mapped_centres():
    source=np.fromfunction(lambda r,c:2*r+3*c,(4,4),dtype=float)
    result=resample_to_shape(source,(7,7))
    # Centre of source and target grids coincide for odd target dimensions.
    np.testing.assert_allclose(result[3,3],7.5,atol=1e-12)

def test_strict_nodata_policy_masks_missing_positive_weight_neighbours():
    source=np.array([[1,np.nan],[3,4]],float)
    result=resample_to_shape(source,(3,3),nodata_policy="strict")
    assert np.isnan(result[1,1])

def test_renormalize_policy_uses_available_bilinear_neighbours():
    source=np.array([[1,np.nan],[3,4]],float)
    result=resample_to_shape(source,(3,3),nodata_policy="renormalize")
    assert np.isfinite(result[1,1])
    np.testing.assert_allclose(result[1,1],8/3)

def test_exact_source_centres_do_not_require_zero_weight_nodata_neighbours():
    source=np.array([[1,np.nan],[3,4]],float)
    result=resample_to_shape(source,(2,2),nodata_policy="strict")
    assert result[0,0]==1

def test_invalid_shape_method_and_policy_are_rejected():
    with pytest.raises(ValueError,match="positive integers"):
        resample_to_shape([[1]],(0,2))
    with pytest.raises(ValueError,match="method"):
        resample_to_shape([[1]],(2,2),method="cubic")
    with pytest.raises(ValueError,match="nodata_policy"):
        resample_to_shape([[1]],(2,2),nodata_policy="ignore")
    with pytest.raises(ValueError,match="2D"):
        resample_to_shape([1,2],(2,2))
