import numpy as np
import pytest
from spectral_derivatives import (
    spectral_derivatives, upward_continuation,
    analytic_signal_amplitude, tilt_angle,
)


def test_spectral_derivative_of_periodic_cosine():
    n = 64
    x = np.arange(n)
    field = np.tile(np.cos(2 * np.pi * x / n), (32, 1))
    gx, gy, gz = spectral_derivatives(field, 1.0, 1.0)
    expected = -2 * np.pi / n * np.sin(2 * np.pi * x / n)
    assert np.max(np.abs(gx[0] - expected)) < 1e-10
    assert np.max(np.abs(gy)) < 1e-10
    assert np.max(np.abs(gz[0] - 2 * np.pi / n * np.cos(2 * np.pi * x / n))) < 1e-10


def test_upward_continuation_attenuates_known_fourier_mode():
    n = 64
    x = np.arange(n)
    height = 3.0
    k = 2 * np.pi / n
    field = np.tile(np.cos(k * x), (32, 1))
    result = upward_continuation(field, 1.0, 1.0, height)
    np.testing.assert_allclose(result, field * np.exp(-k * height), atol=1e-11)


def test_upward_continuation_zero_height_is_identity():
    field = np.arange(64, dtype=float).reshape(8, 8)
    np.testing.assert_allclose(upward_continuation(field, 2, 3, 0), field, atol=1e-12)


@pytest.mark.parametrize("height", [-1, float("nan"), float("inf")])
def test_upward_continuation_rejects_invalid_height(height):
    with pytest.raises(ValueError):
        upward_continuation(np.ones((4, 4)), 1, 1, height)


def test_attributes_shape_and_ranges():
    y, x = np.mgrid[-16:16, -16:16]
    field = np.exp(-(x * x + y * y) / 30.0)
    asa = analytic_signal_amplitude(field, 1, 1)
    tilt = tilt_angle(field, 1, 1)
    assert asa.shape == field.shape and np.all(asa >= 0)
    assert tilt.shape == field.shape
    assert np.all(tilt >= -np.pi / 2) and np.all(tilt <= np.pi / 2)


@pytest.mark.parametrize("dx,dy", [(0, 1), (1, 0), (-1, 1)])
def test_invalid_spacing(dx, dy):
    with pytest.raises(ValueError):
        spectral_derivatives(np.ones((3, 3)), dx, dy)


def test_invalid_grid():
    with pytest.raises(ValueError):
        spectral_derivatives([[1, float("nan")], [2, 3]], 1, 1)
    with pytest.raises(ValueError):
        spectral_derivatives([1, 2, 3], 1, 1)


def test_euler_deconvolution_recovers_synthetic_source_parameters():
    from spectral_derivatives import euler_deconvolution_window
    rng = np.random.default_rng(42)
    x, y = np.meshgrid(np.linspace(-2, 2, 8), np.linspace(-2, 2, 7))
    tx, ty, tz = (rng.normal(size=x.shape) for _ in range(3))
    x0, y0, z0, base, index, zobs = 1.25, -0.75, 3.5, 12.0, 2.0, 0.0
    field = ((x0 - x) * tx + (y0 - y) * ty + (z0 - zobs) * tz) / index + base
    result = euler_deconvolution_window(
        field, tx, ty, tz, x, y, zobs, index
    )
    assert result["x0"] == pytest.approx(x0)
    assert result["y0"] == pytest.approx(y0)
    assert result["z0"] == pytest.approx(z0)
    assert result["base_level"] == pytest.approx(base)
    assert result["rms_residual"] < 1e-10


def test_euler_deconvolution_rejects_rank_deficient_window():
    from spectral_derivatives import euler_deconvolution_window
    x, y = np.meshgrid(np.arange(3.0), np.arange(3.0))
    ones = np.ones_like(x)
    with pytest.raises(ValueError, match="rank deficient"):
        euler_deconvolution_window(ones, ones, ones, ones, x, y, 0, 2)


def test_euler_deconvolution_validates_window_contract():
    from spectral_derivatives import euler_deconvolution_window
    x, y = np.meshgrid(np.arange(2.0), np.arange(2.0))
    a = np.arange(4.0).reshape(2, 2)
    with pytest.raises(ValueError):
        euler_deconvolution_window(a, a, a, a, x, y, 0, 0)


def test_regularized_downward_continuation_recovers_a_low_frequency_mode():
    from spectral_derivatives import downward_continuation_regularized
    n = 64
    x = np.arange(n)
    height, lam = 2.0, 1e-8
    k = 2 * np.pi / n
    surface = np.tile(4.0 + np.cos(k * x), (n, 1))
    observed = np.tile(4.0 + np.exp(-k * height) * np.cos(k * x), (n, 1))
    result = downward_continuation_regularized(observed, 1, 1, height, lam)
    np.testing.assert_allclose(result, surface, atol=2e-6)


def test_regularized_downward_continuation_suppresses_high_frequency_noise():
    from spectral_derivatives import downward_continuation_regularized
    n = 64
    x = np.arange(n)
    height, lam = 3.0, 1e-4
    low_k, high_k = 2 * np.pi / n, np.pi
    observed = np.tile(
        np.exp(-low_k * height) * np.cos(low_k * x)
        + np.exp(-high_k * height) * np.cos(high_k * x),
        (n, 1),
    )
    result = downward_continuation_regularized(observed, 1, 1, height, lam)
    low_amplitude = 2 * np.mean(result[0] * np.cos(low_k * x))
    high_amplitude = 2 * np.mean(result[0] * np.cos(high_k * x))
    assert low_amplitude > 0.9
    assert abs(high_amplitude) < 0.01


def test_regularized_downward_continuation_zero_height_is_identity():
    from spectral_derivatives import downward_continuation_regularized
    field = np.arange(64, dtype=float).reshape(8, 8)
    np.testing.assert_allclose(downward_continuation_regularized(field, 1, 1, 0, 0.1), field)


@pytest.mark.parametrize("height,lam", [(-1, .1), (1, 0), (1, -0.1), (1, float("nan"))])
def test_regularized_downward_continuation_rejects_invalid_parameters(height, lam):
    from spectral_derivatives import downward_continuation_regularized
    with pytest.raises(ValueError):
        downward_continuation_regularized(np.ones((8, 8)), 1, 1, height, lam)
