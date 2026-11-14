import numpy as np
import pytest
from matched_filtering import matched_bandpass_decomposition

LAYERS = [{"B": 1.0, "z": 2.0, "n": 0}, {"B": 0.8, "z": 12.0, "n": 0}]


def test_component_grids_reconstruct_input_and_preserve_mean():
    y, x = np.mgrid[:32, :40]
    grid = 4 + np.sin(2*np.pi*x/8) + .5*np.cos(2*np.pi*y/20)
    result = matched_bandpass_decomposition(grid, 1, 1, LAYERS)
    np.testing.assert_allclose(result["reconstruction"], grid, atol=1e-10)
    np.testing.assert_allclose(result["components"].sum(axis=0), grid, atol=1e-10)
    assert np.mean(result["components"][0]) == pytest.approx(np.mean(grid), abs=1e-10)
    assert np.mean(result["components"][1]) == pytest.approx(0, abs=1e-10)


def test_filter_weights_sum_to_one_at_nonzero_frequencies():
    grid = np.random.default_rng(4).normal(size=(16, 18))
    result = matched_bandpass_decomposition(grid, 2, 3, LAYERS)
    sums = result["filters"].sum(axis=0)
    np.testing.assert_allclose(sums[1:, :], 1.0, atol=1e-12)
    np.testing.assert_allclose(sums[0, 1:], 1.0, atol=1e-12)
    assert result["filters"][0, 0, 0] == 1.0
    assert result["filters"][1, 0, 0] == 0.0


def test_deeper_layer_model_favours_low_wavenumber():
    grid = np.cos(2*np.pi*np.arange(64)[None, :] / 64) * np.ones((32, 1))
    layers = [{"B": 1, "z": 1, "n": 0}, {"B": 1, "z": 20, "n": 0}]
    result = matched_bandpass_decomposition(grid, 1, 1, layers)
    low = result["filters"][1, 0, 1]
    high = result["filters"][1, 0, 12]
    assert low > high


def test_spectral_exponents_are_supported_and_validated():
    grid = np.ones((8, 8))
    for exponent in (-1, 0, 1):
        result = matched_bandpass_decomposition(
            grid, 1, 1,
            [{"B": 1, "z": 1, "n": exponent}, {"B": 2, "z": 2, "n": 0}],
        )
        np.testing.assert_allclose(result["reconstruction"], grid, atol=1e-12)
    with pytest.raises(ValueError):
        matched_bandpass_decomposition(grid, 1, 1, [{"B": 1, "z": 1, "n": 2}, LAYERS[1]])


@pytest.mark.parametrize("dx,dy", [(0, 1), (1, -1), (float("nan"), 1)])
def test_invalid_grid_spacing_rejected(dx, dy):
    with pytest.raises(ValueError):
        matched_bandpass_decomposition(np.ones((8, 8)), dx, dy, LAYERS)


def test_invalid_model_and_dc_index_rejected():
    grid = np.ones((8, 8))
    with pytest.raises(ValueError):
        matched_bandpass_decomposition(grid, 1, 1, [LAYERS[0]])
    with pytest.raises(ValueError):
        matched_bandpass_decomposition(grid, 1, 1, [{"B": 0, "z": 1, "n": 0}, LAYERS[1]])
    with pytest.raises(ValueError):
        matched_bandpass_decomposition(grid, 1, 1, LAYERS, dc_layer=2)
