# Potential-field processing: spectral attributes and source estimates

Potential-field interpretation transforms gravity or magnetic observations to emphasise boundaries and source geometry. A derivative or continuation map is not a direct image of geology: its appearance depends on survey height, grid spacing, noise, boundary treatment and the assumed source model.

## 1. Spectral derivatives on a regular grid

For a uniformly sampled grid \(T(x,y)\), take its two-dimensional Fourier transform \(\widehat T(k_x,k_y)\). Horizontal derivatives follow from the Fourier differentiation theorem:

\[
\widehat{T_x}=ik_x\widehat T,\qquad
\widehat{T_y}=ik_y\widehat T.
\]

For a harmonic potential field, the first vertical derivative uses the radial wavenumber operator:

\[
\widehat{T_z}=k\widehat T,\qquad k=\sqrt{k_x^2+k_y^2}.
\]

The sign convention depends on the vertical-axis direction. The teaching implementation states its positive radial-wavenumber convention and sets the zero-frequency derivative to zero.

## 2. Upward continuation

Continuing upward by height \(h\) attenuates each Fourier mode:

\[
\widehat{T_h}(k_x,k_y)=e^{-kh}\widehat T(k_x,k_y).
\]

High wavenumbers are attenuated more strongly. The implementation assumes a regular grid and periodic FFT boundaries; height and grid spacing must share a length unit.

## 3. Regularised downward continuation

Downward continuation attempts to invert upward continuation. The direct inverse \(e^{kh}\) amplifies high-wavenumber noise exponentially. The implementation uses a Tikhonov inverse for non-zero modes:

\[
H_\lambda(k)=\frac{e^{kh}}{1+\lambda e^{2kh}}.
\]

The zero-frequency mean is preserved separately. The positive regularisation parameter controls the stability–resolution trade-off and is not selected automatically. This is not a unique recovery.

## 4. Analytic-signal amplitude and tilt

The 3D analytic-signal amplitude is

\[
A=\sqrt{T_x^2+T_y^2+T_z^2}.
\]

It can help delineate magnetic-source edges but does not uniquely identify source depth, geometry or lithology. Differentiation amplifies high-frequency noise.

The tilt angle is

\[
\theta=\operatorname{atan2}\left(T_z,\sqrt{T_x^2+T_y^2}\right).
\]

It normalises the vertical derivative by the total horizontal gradient and returns values in \([-\pi/2,\pi/2]\). The zero-gradient case and noise floor require care.

## 5. Windowed Euler deconvolution

Euler deconvolution uses the homogeneity equation for a potential field and a chosen structural index \(N\):

\[
(x-x_0)T_x+(y-y_0)T_y+(z-z_0)T_z=N(B-T).
\]

Rearrangement produces a linear least-squares system for source coordinates \((x_0,y_0,z_0)\) and base level \(B\). The companion function solves one supplied 2D window and rejects rank-deficient systems.

Euler estimates are not unique geological answers. They can be unstable when the structural index is wrong, regional field is not removed, sources overlap, the window is poorly conditioned or derivative noise dominates. Inspect residuals and solution stability across window sizes and structural indices.

## 6. Werner 2D thin-dike deconvolution

The basic Werner thin-dike profile model is

\[
F(x)=\frac{A h+B(x-x_0)}{(x-x_0)^2+h^2},
\]

where \(x_0\) is the horizontal position above the top of the sheet and \(h\) is the depth to its top. Multiplying through and expanding gives a linear system:

\[
x^2F=a_0+a_1x+b_0F+b_1xF,
\]

with \(x_0=b_1/2\), \(h=\sqrt{-b_0-x_0^2}\), \(B=a_1\), and \(A=(a_0+a_1x_0)/h\). The implementation solves an overdetermined system in moving windows (seven samples by default), centers/scales the profile coordinate for conditioning, and records rejected windows, condition numbers and profile RMSE.

This is a bounded single-thin-dike baseline. It expects a residual profile with regional background removed and assumes a level observation plane and a 2D sheet-like source. It does not include the thick-interface horizontal-gradient transformation, polynomial interference terms, multi-source clustering, upward-continuation scale loops, remanence modelling or Marquardt nonlinear refinement. A and B are model coefficients, not susceptibility estimates without the field/orientation physics.

- [Werner implementation](../implementations/python/potential-field/werner_deconvolution.py)
- [Tests](../implementations/python/potential-field/test_werner_deconvolution.py)
- [Walkthrough](../implementations/python/potential-field/werner-deconvolution-walkthrough.md)
- [Synthetic recovery lab](../notebooks/werner-deconvolution-lab.ipynb)

## 7. Grid and boundary assumptions

The FFT operations assume a regular, uniformly spaced Cartesian grid and periodic boundaries. Edge mismatch creates spectral ringing. Pad and taper where appropriate, compare edge treatments and inspect borders. Do not apply these operators to geographic degrees without a suitable projection or local metric treatment.

## Implementation and learning material

- [Python implementation and contract](../implementations/python/potential-field/README.md)
- [Tests](../implementations/python/potential-field/test_spectral_derivatives.py)
- [Walkthrough](../implementations/python/potential-field/implementation-walkthrough.md)
- [Spectral derivatives and edge attributes lab](../notebooks/potential-field-derivatives-lab.ipynb)
- [Upward-continuation lab](../notebooks/potential-field-upward-continuation-lab.ipynb)
- [Regularised downward-continuation lab](../notebooks/potential-field-downward-continuation-lab.ipynb)
- [Euler deconvolution synthetic-recovery lab](../notebooks/euler-deconvolution-lab.ipynb)

## References

- Nabighian, M. N. (1972). The analytic signal of two-dimensional magnetic bodies with polygonal cross-section: its properties and use for automated anomaly interpretation. *Geophysics*, 37(3), 507–517.
- Miller, H. G., and Singh, V. (1994). Potential field tilt—a new concept for location of potential field sources. *Journal of Applied Geophysics*, 32, 213–217.
- Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic Applications*. Cambridge University Press.
- Werner, S. (1953). Original thin-dike formulation, as reproduced in later Werner-deconvolution literature.
- Ku, C. C. & Sharp, J. A. (1983). Werner deconvolution for automated magnetic interpretation and its refinement using Marquardt's inverse modeling. *Geophysics*, 48(6), 754–774. https://doi.org/10.1190/1.1441505.

**Scope:** the package provides regular-grid spectral attributes, upward continuation, regularised downward continuation, windowed Euler deconvolution and a bounded single-thin-dike Werner solver. Potential-field matched filtering and full gravity/magnetic inversion remain open algorithm tasks. The Euler solver is a model-dependent source-location estimate, not a complete inversion.
