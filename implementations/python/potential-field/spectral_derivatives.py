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


def euler_deconvolution_window(
    field, dTdx, dTdy, dTdz, x_coordinates, y_coordinates,
    observation_z, structural_index,
):
    """Estimate source (x0,y0,z0) and regional base level B in one window.

    Solves the linear Euler homogeneity equation by least squares:
      x0*T_x + y0*T_y + z0*T_z + N*B
        = x*T_x + y*T_y + z*T_z + N*T
    All arrays must describe the same 2D window. Coordinates and observation_z
    use consistent length units. At least four independent equations are
    required; rank-deficient windows are rejected rather than pseudoinverted.
    """
    arrays = [np.asarray(a, dtype=float) for a in
              (field, dTdx, dTdy, dTdz, x_coordinates, y_coordinates)]
    if any(a.ndim != 2 or a.shape != arrays[0].shape for a in arrays):
        raise ValueError("field, derivatives and coordinate grids must share a 2D shape")
    if arrays[0].size < 4 or any(not np.all(np.isfinite(a)) for a in arrays):
        raise ValueError("window must contain at least four finite samples")
    z_obs = float(observation_z)
    index = float(structural_index)
    if not np.isfinite(z_obs) or not np.isfinite(index) or index == 0:
        raise ValueError("observation_z must be finite and structural_index finite and non-zero")
    T, Tx, Ty, Tz, X, Y = [a.ravel() for a in arrays]
    Z = np.full(T.shape, z_obs, dtype=float)
    design = np.column_stack((Tx, Ty, Tz, np.full(T.shape, index)))
    rhs = X * Tx + Y * Ty + Z * Tz + index * T
    solution, _, rank, _ = np.linalg.lstsq(design, rhs, rcond=None)
    if rank < 4:
        raise ValueError("Euler window is rank deficient; source parameters are not identifiable")
    residual = design @ solution - rhs
    return {
        "x0": float(solution[0]),
        "y0": float(solution[1]),
        "z0": float(solution[2]),
        "base_level": float(solution[3]),
        "rms_residual": float(np.sqrt(np.mean(residual * residual))),
        "sample_count": int(T.size),
        "structural_index": index,
    }


def downward_continuation_regularized(values, dx, dy, height, regularization):
    """Continue a potential field downward with Tikhonov spectral regularisation.

    For non-zero Fourier modes this is the Tikhonov inverse of upward
    continuation A(k)=exp(-k*height): H=A/(A**2+lambda). The DC component
    (mean) is preserved exactly. regularization must be positive; larger
    values suppress unstable high-wavenumber amplification more strongly.
    """
    z, dx, dy = _grid(values, dx, dy)
    height = float(height)
    lam = float(regularization)
    if not np.isfinite(height) or height < 0:
        raise ValueError("height must be finite and non-negative")
    if not np.isfinite(lam) or lam <= 0:
        raise ValueError("regularization must be finite and positive")
    if height == 0:
        return z.copy()
    _, _, K = _wavenumbers(z.shape, dx, dy)
    kh = K * height
    # Log-domain denominator avoids overflow for large downward distances.
    transfer = np.exp(kh - np.logaddexp(0.0, np.log(lam) + 2.0 * kh))
    transfer[0, 0] = 1.0  # Preserve the regional mean rather than regularising DC.
    return np.fft.ifft2(np.fft.fft2(z) * transfer).real
