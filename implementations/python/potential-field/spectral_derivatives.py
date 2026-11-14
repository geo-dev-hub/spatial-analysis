"""Spectral derivatives and edge attributes for regular potential-field grids."""
from __future__ import annotations
import numpy as np

def _grid(values,dx,dy):
    z=np.asarray(values,dtype=float)
    if z.ndim!=2 or min(z.shape)<2 or not np.all(np.isfinite(z)):raise ValueError("field must be a finite 2D grid at least 2x2")
    dx=float(dx);dy=float(dy)
    if not np.isfinite(dx) or not np.isfinite(dy) or dx<=0 or dy<=0:raise ValueError("grid spacings must be finite and positive")
    return z,dx,dy

def spectral_derivatives(values,dx,dy):
    """Return x, y and first vertical derivatives using Fourier operators.

    Assumes a uniformly spaced grid and periodic FFT boundary conditions.
    The vertical derivative uses the positive radial wavenumber operator
    sqrt(kx^2+ky^2), the common potential-field spectral convention.
    """
    z,dx,dy=_grid(values,dx,dy)
    ny,nx=z.shape
    kx=2*np.pi*np.fft.fftfreq(nx,d=dx)
    ky=2*np.pi*np.fft.fftfreq(ny,d=dy)
    KX,KY=np.meshgrid(kx,ky)
    K=np.hypot(KX,KY)
    F=np.fft.fft2(z)
    gx=np.fft.ifft2(1j*KX*F).real
    gy=np.fft.ifft2(1j*KY*F).real
    gz=np.fft.ifft2(K*F).real
    return gx,gy,gz

def analytic_signal_amplitude(values,dx,dy):
    """3D analytic-signal amplitude sqrt((dT/dx)^2+(dT/dy)^2+(dT/dz)^2)."""
    gx,gy,gz=spectral_derivatives(values,dx,dy)
    return np.sqrt(gx*gx+gy*gy+gz*gz)

def tilt_angle(values,dx,dy):
    """Tilt derivative atan2(vertical derivative, total horizontal gradient)."""
    gx,gy,gz=spectral_derivatives(values,dx,dy)
    return np.arctan2(gz,np.hypot(gx,gy))
