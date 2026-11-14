# Intern walkthrough: potential-field derivatives

A regular grid can be represented by its 2D discrete Fourier transform. Horizontal differentiation multiplies each Fourier coefficient by i kx or i ky. The first vertical derivative of a potential field uses the radial wavenumber k=sqrt(kx^2+ky^2) under the standard spectral potential-field convention.

## Upward continuation

For a harmonic potential field, upward continuation by height h attenuates each Fourier mode by exp(-kh), where k=sqrt(kx^2+ky^2). The zero-wavenumber mean is unchanged. A periodic cosine test checks the exact attenuation of a known mode. Height and grid spacing must use the same length unit. This operator is a smoothing continuation; it does not solve the unstable downward-continuation problem.

The analytic-signal amplitude combines all three directional derivatives:
A=sqrt((dT/dx)^2+(dT/dy)^2+(dT/dz)^2).
The tilt derivative is atan2(dT/dz, sqrt((dT/dx)^2+(dT/dy)^2)).

The FFT assumes periodic boundaries. A discontinuity between opposite grid edges creates ringing, so real survey grids need suitable padding, tapering and boundary checks. The tests compare spectral derivatives against an exact periodic cosine and check attribute ranges.
