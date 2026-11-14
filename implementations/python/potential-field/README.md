# Potential-field spectral derivatives

NumPy teaching implementations for regular, uniformly spaced 2D grids:
- first horizontal derivatives in x and y using Fourier differentiation;
- first vertical derivative using the positive radial-wavenumber operator;
- 3D analytic-signal amplitude;
- tilt derivative.

The grid is assumed periodic by the FFT. Edge discontinuities cause spectral ringing; pad/taper and inspect boundary effects for real surveys. Inputs must be finite, regular grids with positive dx and dy. The vertical derivative follows the common potential-field spectral convention; it is not a general derivative in an arbitrary z coordinate.

Run python -m pip install -r requirements.txt and python -m pytest -q. This package does not perform continuation, inversion, Euler deconvolution or interpret source geometry.
