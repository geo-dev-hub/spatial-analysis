import numpy as np
import pytest

from fuzzy_overlay import boolean_overlay, fuzzy_overlay


def test_boolean_and_and_or():
    a = np.array([[True, True], [False, False]])
    b = np.array([[True, False], [True, False]])
    np.testing.assert_array_equal(boolean_overlay([a, b]), [[True, False], [False, False]])
    np.testing.assert_array_equal(boolean_overlay([a, b], "or"), [[True, True], [True, False]])


def test_boolean_rejects_non_boolean_and_unknown_operation():
    with pytest.raises(ValueError, match="Boolean dtype"):
        boolean_overlay([np.array([[0, 1]])])
    with pytest.raises(ValueError, match="operation"):
        boolean_overlay([np.array([[True]])], "xor")


def test_fuzzy_min_product_max_and_probabilistic_sum():
    layers = [np.array([[0.2, 0.8]]), np.array([[0.7, 0.5]])]
    np.testing.assert_allclose(fuzzy_overlay(layers, "min"), [[0.2, 0.5]])
    np.testing.assert_allclose(fuzzy_overlay(layers, "product"), [[0.14, 0.4]])
    np.testing.assert_allclose(fuzzy_overlay(layers, "max"), [[0.7, 0.8]])
    np.testing.assert_allclose(fuzzy_overlay(layers, "probabilistic_sum"), [[0.76, 0.9]])


def test_gamma_endpoints_are_product_and_probabilistic_sum():
    layers = [np.array([[0.2, 0.8]]), np.array([[0.7, 0.5]])]
    np.testing.assert_allclose(fuzzy_overlay(layers, gamma=0), fuzzy_overlay(layers, "product"))
    np.testing.assert_allclose(fuzzy_overlay(layers, gamma=1), fuzzy_overlay(layers, "probabilistic_sum"))


def test_gamma_must_be_bounded():
    with pytest.raises(ValueError, match="gamma"):
        fuzzy_overlay([np.ones((1, 1))], gamma=1.1)


def test_strict_nodata_propagation():
    layers = [np.array([[0.4, np.nan]]), np.array([[0.5, 0.7]])]
    result = fuzzy_overlay(layers, "min")
    assert result[0, 0] == pytest.approx(0.4)
    assert np.isnan(result[0, 1])


def test_shapes_and_ranges_are_validated():
    with pytest.raises(ValueError, match="same shape"):
        fuzzy_overlay([np.ones((2, 2)), np.ones((1, 2))])
    with pytest.raises(ValueError, match=r"\[0, 1\]"):
        fuzzy_overlay([np.array([[1.2]])])
