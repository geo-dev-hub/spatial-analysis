# Gaussian-plume emission inversion: implementation walkthrough

## What is being estimated?

Given a methane column-enhancement raster and a specified source location, wind direction, wind speed and lateral-dispersion model, estimate a non-negative emission rate Q (kg/s) and a constant column-background term b (kg/m²).

This is a bounded inverse problem. It does not search for the source location or infer wind and dispersion from the image.

## Forward model

Coordinates are projected into downwind distance x and crosswind distance y. For downwind cells:

\[
\sigma_y(x)=\sqrt{\sigma_{y0}^2+(a x)^2}
\]

\[
K(x,y)=\frac{1}{\sqrt{2\pi}\,U\,\sigma_y(x)}
\exp\left(-\frac{y^2}{2\sigma_y(x)^2}\right)
\]

\[
\widehat C(x,y)=QK(x,y)+b.
\]

The kernel is zero upwind. Since the model is linear in Q and b, form a two-column design matrix [K, 1] and solve bounded least squares with Q >= 0; background remains unconstrained.

## Implementation choices

The forward-model kernel is separated from the inverse solver. The solver validates matching finite grids, checks identifiability, and uses SciPy bounded linear least squares. It returns fitted components and residuals for inspection.

## Important limitations

- Coordinates must be projected into a consistent length unit; wind is m/s. Use metres for the stated kg/s output.
- Wind direction is assumed already aligned with the x-axis. Rotate coordinates before calling for another direction.
- Source location, wind speed, initial lateral spread and dispersion-growth coefficient are fixed inputs.
- This vertically integrated Gaussian model is a simplified steady-plume approximation. It omits chemistry, deposition, terrain, variable winds, finite satellite footprints, retrieval bias, plume intermittency and uncertainty propagation.
- A good fit does not prove the assumed source or physics is correct. Inspect residuals and test sensitivity to inputs.
- This is not a full 3D Gaussian concentration equation and is not an operational emissions estimate without domain validation.

## Reproduce

Install requirements.txt, then run python -m pytest -q. The notebook generates a synthetic plume with known emission rate and background, adds noise, and recovers the parameters.
