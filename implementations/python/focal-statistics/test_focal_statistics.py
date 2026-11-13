import numpy as np
import pytest

from focal_statistics import focal_mean


def test_three_by_three_focal_mean_and_counts():
    data = np.arange(1, 10, dtype=float).reshape(3, 3)
    means, counts = focal_mean(data, window_size=3)
    assert means[1, 1] == pytest.approx(5)
    assert counts[1, 1] == 9
    assert means[0, 0] == pytest.approx(3)
    assert counts[0, 0] == 4


def test_window_size_one_returns_original_values():
    data = np.array([[1, 2], [3, 4]], dtype=float)
    means, counts = focal_mean(data, window_size=1)
    np.testing.assert_allclose(means, data)
    np.testing.assert_array_equal(counts, 1)


def test_nodata_and_nonfinite_values_are_ignored():
    data = np.array([[1, -9999, 3], [4, np.nan, 6], [7, 8, np.inf]], dtype=float)
    means, counts = focal_mean(data, window_size=3, nodata=-9999)
    assert counts[1, 1] == 6
    assert means[1, 1] == pytest.approx((1 + 3 + 4 + 6 + 7 + 8) / 6)


def test_valid_mask_and_minimum_count_are_applied():
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
    mask = np.zeros_like(data, dtype=bool)
    mask[1, 1] = True
    means, counts = focal_mean(data, window_size=3, valid_mask=mask, min_count=2)
    assert counts[1, 1] == 1
    assert np.isnan(means[1, 1])
    means, counts = focal_mean(data, window_size=3, valid_mask=mask, min_count=1)
    assert means[0, 0] == 5
    assert counts[0, 0] == 1


def test_all_invalid_neighbourhood_returns_nan_and_zero_count():
    means, counts = focal_mean([[np.nan, np.nan]], window_size=3)
    assert np.isnan(means).all()
    np.testing.assert_array_equal(counts, 0)


@pytest.mark.parametrize("window", [0, -1, 2, 4, True, 3.0])
def test_invalid_window_size_is_rejected(window):
    with pytest.raises(ValueError, match="window_size"):
        focal_mean([[1]], window_size=window)


@pytest.mark.parametrize("minimum", [0, -1, True, 1.5])
def test_invalid_min_count_is_rejected(minimum):
    with pytest.raises(ValueError, match="min_count"):
        focal_mean([[1]], min_count=minimum)


def test_mask_shape_and_input_dimensions_are_checked():
    with pytest.raises(ValueError, match="valid_mask"):
        focal_mean([[1, 2]], valid_mask=[[True]])
    with pytest.raises(ValueError, match="2D"):
        focal_mean([1, 2, 3])
