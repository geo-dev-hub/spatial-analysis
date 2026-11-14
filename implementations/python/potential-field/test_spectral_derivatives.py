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
