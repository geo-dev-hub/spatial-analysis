# Potential-field spectral derivatives

NumPy teaching implementations for regular, uniformly spaced 2D grids:
- first horizontal derivatives in x and y using Fourier differentiation;
- first vertical derivative using the positive radial-wavenumber operator;
- upward continuation by a Fourier-domain exponential attenuation operator;
- windowed Euler deconvolution by least-squares solution of the homogeneity equation;
- 3D analytic-signal amplitude;
- tilt derivative.

The grid is assumed periodic by the FFT. Edge discontinuities cause spectral ringing; pad/taper and inspect boundary effects for real surveys. Inputs must be finite, regular grids with positive dx and dy. The vertical derivative follows the common potential-field spectral convention; it is not a general derivative in an arbitrary z coordinate.

Run python -m pip install -r requirements.txt and python -m pytest -q. Upward continuation is implemented with explicit height and periodic-boundary assumptions. Downward continuation, Werner deconvolution and matched filtering remain open. Euler estimates depend strongly on the supplied structural index and window quality; they are not unique geological interpretations.
