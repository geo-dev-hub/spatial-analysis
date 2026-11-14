# Potential-field derivatives: spectral operators and edge attributes

Potential-field interpretation uses spatial derivatives to emphasise boundaries and changes in source geometry. A derivative map is not a direct image of geology: it is a transformed observation whose appearance depends on survey height, grid spacing, continuation, noise and edge treatment.

## 1. Spectral derivatives on a regular grid

For a uniformly sampled grid T(x,y), take its two-dimensional Fourier transform \(\widehat T(k_x,k_y)\). Horizontal derivatives follow from the Fourier differentiation theorem:

\[
\widehat{T_x}=i k_x\widehat T,\qquad
\widehat{T_y}=i k_y\widehat T.
\]

For a harmonic potential field continued vertically, the first vertical derivative uses the radial wavenumber operator:

\[
\widehat{T_z}=k\widehat T,\qquad
k=\sqrt{k_x^2+k_y^2}.
\]

The sign convention depends on whether the vertical axis is positive upward or downward and on whether the operation is described as upward continuation or derivative. This teaching implementation uses the positive radial-wavenumber amplitude convention and states it explicitly. It sets the zero-frequency derivative to zero.

## 2. Upward continuation

For a potential field continued upward by height h, each Fourier component is multiplied by

\\[
\\widehat{T_h}(k_x,k_y)=e^{-kh}\\widehat T(k_x,k_y),\\qquad k=\\sqrt{k_x^2+k_y^2}.
\\]

High wavenumbers are attenuated more strongly, so upward continuation smooths the field and suppresses short-wavelength features. The implementation assumes a regular grid and periodic FFT boundaries; height and grid spacing must share a unit. Downward continuation multiplies high frequencies by an exponentially growing factor and is unstable without explicit regularisation, so it is not treated as the inverse of this routine.

## 3. Analytic-signal amplitude

The 3D analytic-signal amplitude is

\[
A=\sqrt{T_x^2+T_y^2+T_z^2}.
\]

It combines the horizontal and vertical derivative magnitudes. It can help delineate edges of magnetic sources, but it does not uniquely identify source depth, geometry or lithology. Noise is amplified by differentiation, especially at high wavenumbers.

## 4. Tilt derivative

The tilt angle is

\[
\theta=\tan^{-1}\left(\frac{T_z}{\sqrt{T_x^2+T_y^2}}\right),
\]

implemented with the two-argument arctangent to preserve quadrant information. It normalises the vertical derivative by the total horizontal gradient and returns values in \([-\pi/2,\pi/2]\). The zero-gradient case and noise floor require care.

## 5. Grid and boundary assumptions

The FFT implementation assumes:
- a regular, uniformly spaced Cartesian grid;
- finite values and known positive cell spacings;
- periodic boundary conditions implied by the discrete Fourier transform;
- consistent units for x, y and the field.

A real survey grid is rarely periodic. Edge mismatch creates spectral ringing. Pad and taper where appropriate, compare alternative edge treatments, inspect the border, and avoid interpreting artefacts as geological contacts. Do not apply these operators to geographic degrees without a suitable projection or local metric treatment.

## 6. Euler deconvolution

Euler deconvolution uses the homogeneity equation for a potential field and a chosen structural index N:

\\[
(x-x_0)T_x+(y-y_0)T_y+(z-z_0)T_z=N(B-T).
\\]

Rearrangement produces a linear least-squares system for source coordinates (x0,y0,z0) and base level B. The companion function solves one supplied 2D window and rejects rank-deficient systems. It requires the derivatives and coordinates on the same grid, a known structural index, and a consistent observation height.

Euler estimates are not unique geological answers. They can be unstable or misleading when the structural index is wrong, regional field is not removed, multiple sources overlap, the window is poorly conditioned, or noise dominates derivatives. Inspect residuals, solution stability across window sizes and structural indices, and geological plausibility. Do not report a single solution without those checks.

## 7. Runnable teaching implementation

The companion package provides horizontal derivatives, the radial-wavenumber vertical derivative, upward continuation, analytic-signal amplitude and tilt angle, plus windowed Euler deconvolution. Tests compare the spectral operators with a periodic cosine of known wavenumber.

- [Implementation and contract](../implementations/python/potential-field/README.md)
- [Tests](../implementations/python/potential-field/test_spectral_derivatives.py)
- [Walkthrough](../implementations/python/potential-field/implementation-walkthrough.md)
- [Synthetic grid lab](../notebooks/potential-field-derivatives-lab.ipynb)

## References

- Nabighian, M. N. (1972). The analytic signal of two-dimensional magnetic bodies with polygonal cross-section: its properties and use for automated anomaly interpretation. *Geophysics*, 37(3), 507–517.
- Miller, H. G., and Singh, V. (1994). Potential field tilt—a new concept for location of potential field sources. *Journal of Applied Geophysics*, 32, 213–217.
- Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic Applications*. Cambridge University Press.

**Scope:** this is a regular-grid derivative/attribute baseline. Downward continuation, Werner deconvolution, matched filtering, inversion and source-geometry estimation remain distinct algorithms and are not implemented here.
