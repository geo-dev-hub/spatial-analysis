import numpy as np
import pytest
from hillshade import hillshade_from_slope_aspect

def test_flat_surface_illumination_depends_on_sun_altitude():
    result=hillshade_from_slope_aspect([[0]],[[np.nan]],sun_altitude_degrees=30)
    np.testing.assert_allclose(result,[[0.5]])

def test_slope_facing_toward_sun_is_bright():
    result=hillshade_from_slope_aspect([[45]],[[270]],sun_azimuth_degrees=270,sun_altitude_degrees=45)
    np.testing.assert_allclose(result,[[1.0]])

def test_slope_facing_away_from_sun_is_dark():
    result=hillshade_from_slope_aspect([[45]],[[270]],sun_azimuth_degrees=90,sun_altitude_degrees=45)
    np.testing.assert_allclose(result,[[0.0]])

def test_missing_derivatives_remain_nan():
    result=hillshade_from_slope_aspect([[np.nan,0]],[[np.nan,np.nan]])
    assert np.isnan(result[0,0])
    assert np.isfinite(result[0,1])

def test_shape_and_sun_angle_validation():
    with pytest.raises(ValueError,match="same shape"):
        hillshade_from_slope_aspect([[0]],[[0,1]])
    with pytest.raises(ValueError,match="altitude"):
        hillshade_from_slope_aspect([[0]],[[np.nan]],sun_altitude_degrees=91)
    with pytest.raises(ValueError,match="slope"):
        hillshade_from_slope_aspect([[91]],[[0]])
