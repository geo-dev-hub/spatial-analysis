"""Spectral derivatives, continuation and edge attributes for regular grids."""
from __future__ import annotations
import numpy as np


def _grid(values, dx, dy):
    z = np.asarray(values, dtype=float)
    if z.ndim != 2 or min(z.shape) < 2 or not np.all(np.isfinite(z)):
        raise ValueError("field must be a finite 2D grid at least 2x2")
    dx, dy = float(dx), float(dy)
    if not np.isfinite(dx) or not np.isfinite(dy) or dx <= 0 or dy <= 0:
        raise ValueError("grid spacings must be finite and positive")
    return z, dx, dy


def _wavenumbers(shape, dx, dy):
    ny, nx = shape
    kx = 2 * np.pi * np.fft.fftfreq(nx, d=dx)
    ky = 2 * np.pi * np.fft.fftfreq(ny, d=dy)
    KX, KY = np.meshgrid(kx, ky)
    return KX, KY, np.hypot(KX, KY)


def spectral_derivatives(values, dx, dy):
    """Return x, y and first vertical derivatives using Fourier operators.

    Assumes a uniformly spaced grid and periodic FFT boundary conditions.
    The vertical derivative uses the positive radial wavenumber operator.
    """
    z, dx, dy = _grid(values, dx, dy)
    KX, KY, K = _wavenumbers(z.shape, dx, dy)
    F = np.fft.fft2(z)
    gx = np.fft.ifft2(1j * KX * F).real
    gy = np.fft.ifft2(1j * KY * F).real
    gz = np.fft.ifft2(K * F).real
    return gx, gy, gz


def upward_continuation(values, dx, dy, height):
    """Continue a potential field upward by positive height on a regular grid.

    In Fourier space each mode is attenuated by exp(-k * height), where
    k=sqrt(kx**2+ky**2). Height uses the same linear unit as dx and dy.
    """
    z, dx, dy = _grid(values, dx, dy)
    height = float(height)
    if not np.isfinite(height) or height < 0:
        raise ValueError("height must be finite and non-negative")
    _, _, K = _wavenumbers(z.shape, dx, dy)
    continued = np.fft.ifft2(np.fft.fft2(z) * np.exp(-K * height)).real
    return continued


def analytic_signal_amplitude(values, dx, dy):
    """3D analytic-signal amplitude from x, y and vertical derivatives."""
    gx, gy, gz = spectral_derivatives(values, dx, dy)
    return np.sqrt(gx * gx + gy * gy + gz * gz)


def tilt_angle(values, dx, dy):
    """Tilt derivative atan2(vertical derivative, total horizontal gradient)."""
    gx, gy, gz = spectral_derivatives(values, dx, dy)
    return np.arctan2(gz, np.hypot(gx, gy))
