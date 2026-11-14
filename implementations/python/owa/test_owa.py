import numpy as np
import pytest

from owa import ordered_weighted_averaging, orness


def test_standard_owa_uses_descending_value_order():
    layers = [np.array([[0.1, 0.8]]), np.array([[1.0, 0.4]])]
    result = ordered_weighted_averaging(layers, [0.75, 0.25])
    np.testing.assert_allclose(result, [[0.775, 0.7]])


def test_equal_order_weights_equal_arithmetic_mean():
    layers = [np.array([[0.1]]), np.array([[0.8]]), np.array([[0.4]])]
    result = ordered_weighted_averaging(layers, [1/3, 1/3, 1/3])
    np.testing.assert_allclose(result, [[1.3/3]])


def test_order_extremes_are_max_and_min():
    layers = [np.array([[0.1, 0.8]]), np.array([[1.0, 0.4]])]
    np.testing.assert_allclose(ordered_weighted_averaging(layers, [1, 0]), [[1.0, 0.8]])
    np.testing.assert_allclose(ordered_weighted_averaging(layers, [0, 1]), [[0.1, 0.4]])


def test_gis_weighted_owa_reorders_criterion_weights_with_values():
    layers = [np.array([[0.1]]), np.array([[0.8]]), np.array([[1.0]]), np.array([[0.4]])]
    result = ordered_weighted_averaging(layers, [0.25]*4, [0.2, 0.4, 0.3, 0.1])
    np.testing.assert_allclose(result, [[0.68]])


def test_orness_endpoints_and_neutral_vector():
    assert orness([1, 0, 0]) == pytest.approx(1)
    assert orness([0, 0, 1]) == pytest.approx(0)
    assert orness([1/3]*3) == pytest.approx(0.5)
    assert orness([1]) is None


def test_strict_nodata_and_invalid_inputs():
    result = ordered_weighted_averaging([np.array([[0.4, np.nan]]), np.array([[0.5, 0.7]])], [0.5, 0.5])
    assert result[0, 0] == pytest.approx(0.45)
    assert np.isnan(result[0, 1])
    with pytest.raises(ValueError):
        ordered_weighted_averaging([np.ones((1, 1))], [0.5])
    with pytest.raises(ValueError):
        ordered_weighted_averaging([np.ones((1, 1))], [1.0], [0.0])
    with pytest.raises(ValueError):
        ordered_weighted_averaging([np.array([[1.1]])], [1.0])
