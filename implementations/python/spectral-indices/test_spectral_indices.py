import numpy as np
import pytest

from spectral_indices import ndvi


def test_ndvi_calculates_known_reflectance_values():
    nir = np.array([[0.6, 0.4]])
    red = np.array([[0.2, 0.2]])
    result = ndvi(nir, red)
    np.testing.assert_allclose(result, [[0.5, 1 / 3]])


def test_ndvi_zero_denominator_becomes_nan():
    result = ndvi(np.array([0.2, -0.2]), np.array([-0.2, 0.2]))
    assert np.isnan(result).all()


def test_ndvi_preserves_non_finite_pixels_as_nan():
    result = ndvi(np.array([0.5, np.nan, np.inf]), np.array([0.1, 0.2, 0.1]))
    assert result[0] == pytest.approx(2 / 3)
    assert np.isnan(result[1:]).all()


def test_ndvi_supports_nodata_and_valid_mask():
    nir = np.array([[0.6, -9999], [0.4, 0.5]])
    red = np.array([[0.2, 0.1], [0.2, 0.1]])
    valid = np.array([[True, True], [False, True]])
    result = ndvi(nir, red, nodata=-9999, valid_mask=valid)
    assert result[0, 0] == pytest.approx(0.5)
    assert np.isnan(result[0, 1])
    assert np.isnan(result[1, 0])
    assert result[1, 1] == pytest.approx(2 / 3)


def test_ndvi_does_not_clip_negative_reflectance_or_index():
    result = ndvi(np.array([-0.2]), np.array([0.1]))
    assert result[0] == pytest.approx(3.0)


def test_ndvi_rejects_shape_mismatch():
    with pytest.raises(ValueError, match="same shape"):
        ndvi(np.ones((2, 2)), np.ones((2, 3)))


def test_ndvi_rejects_valid_mask_shape_mismatch():
    with pytest.raises(ValueError, match="valid_mask"):
        ndvi(np.ones((2, 2)), np.ones((2, 2)), valid_mask=np.ones((4, 4)))
