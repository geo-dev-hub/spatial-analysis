# Scattered-point gridding algorithms

Gridding converts irregularly located samples into values on a requested regular grid. The interpolation rule is part of the model: different methods make different assumptions about local support, smoothness, covariance and extrapolation.

## 1. Nearest-neighbour gridding

For each grid node \(q\), choose the sample \(p_i\) with minimum Euclidean distance and assign its value:

\[
\hat z(q)=z_{i^*},\qquad i^*=\arg\min_i\|q-p_i\|.
\]

A k-d tree accelerates repeated queries. The result is piecewise constant over Voronoi regions. An optional maximum distance masks grid nodes unsupported by nearby observations.

## 2. Delaunay triangulation gridding

Construct a Delaunay triangulation of the sample locations. For a grid node inside a triangle with vertices \(p_1,p_2,p_3\), compute barycentric coordinates \(w_i\) and interpolate:

\[
q=\sum_iw_ip_i,\qquad
\hat z(q)=\sum_iw_iz_i,\qquad \sum_iw_i=1.
\]

The interpolant is piecewise linear and reproduces affine planes exactly within the convex hull. Nodes outside the hull receive an explicit fill value; this implementation does not extrapolate.

## 3. Thin-plate-spline minimum-bending-energy interpolation

A thin-plate spline uses the radial kernel \(\phi(r)=r^2\log r\) with an affine polynomial tail. Its smoothness is associated with minimising the two-dimensional bending-energy functional:

\[
J[f]=\iint_{\mathbb R^2}\left(f_{xx}^2+2f_{xy}^2+f_{yy}^2\right)\,dx\,dy.
\]

Zero smoothing interpolates the samples; positive smoothing allows residual error in exchange for a smoother surface. This is a minimum-bending-energy thin-plate spline and a minimum-curvature-style method, but it is not the classic Briggs iterative minimum-curvature gridding algorithm. The distinction matters because implementations can differ in boundary conditions, tension, iteration and convergence.

## 4. Ordinary kriging with a fixed exponential covariance

The package implements ordinary kriging using a caller-supplied exponential covariance model:

\[
C(h)=s^2\exp(-h/a),
\]

where \(a\) is the range and \(s^2\) is the structured sill. A nugget is added to the observation covariance diagonal. The ordinary-kriging system constrains the weights to sum to one and returns both a prediction and a conditional kriging variance.

The implementation does not fit the variogram. Range, sill and nugget are assumed inputs, so the predictions and variances are conditional on those choices. The dense solver is intended for small teaching datasets, not large surveys; variogram-parameter uncertainty is not included.

## Comparing the four methods

| Method | Surface behaviour | Outside convex hull |
|---|---|---|
| Nearest neighbour | Piecewise constant; preserves sample values | Defined everywhere; optional distance mask |
| Delaunay linear | Piecewise planar; continuous, gradient changes at triangle edges | Fill value; no extrapolation |
| Thin-plate spline | Smooth minimum-bending-energy surface; smoothing controls fit | Extrapolates; edge estimates can be unstable |
| Ordinary kriging | Covariance-weighted estimate with model-based conditional variance | Defined by the covariance model |

Kriging is not automatically superior to deterministic interpolation. Its usefulness depends on a defensible covariance model, sampling design and validation. A fair comparison should use spatially blocked validation and report prediction error as well as uncertainty calibration.

## What remains outside this package

- The classic Briggs iterative minimum-curvature algorithm and a verified equivalence comparison against the thin-plate spline.
- Variogram fitting, anisotropic covariance models, universal kriging and scalable large-data kriging.
- Natural-neighbour interpolation and explicit uncertainty models for the deterministic interpolators.

## Runnable material

- [Python package](../implementations/python/geophysical-gridding/README.md)
- [Tests](../implementations/python/geophysical-gridding/test_geophysical_gridding.py)
- [Implementation walkthrough](../implementations/python/geophysical-gridding/implementation-walkthrough.md)
- [Comparison lab](../notebooks/geophysical-gridding-lab.ipynb)

**Coordinate contract:** use projected planar coordinates in consistent linear units. Interpolation is not a substitute for survey design, outlier handling, uncertainty modelling or geological interpretation.


## References and method distinction

- Briggs, I. C. (1974). [Machine contouring using minimum curvature](https://doi.org/10.1190/1.1440410). *Geophysics*, 39(1), 39–48. The paper derives finite-difference equations from minimum total curvature and outlines an iterative solution for scattered observations.
- U.S. Geological Survey. (1981). [A program for minimum-curvature gridding of randomly spaced data](https://pubs.usgs.gov/of/1981/1224/report.pdf). Open-File Report 81-1224. Describes the biharmonic difference equation and iterative solution associated with Briggs.
- Smith, W. H. F., and Wessel, P. (1990). [Gridding with continuous curvature splines in tension](https://doi.org/10.1190/1.1442835). *Geophysics*, 55(3), 293–305.

These references describe why the thin-plate spline is mathematically related to minimum-curvature ideas, but the current RBF implementation is not claimed to reproduce Briggs's grid-based iterative algorithm. The distinction is retained in the ledger until a reference-matched Briggs implementation and convergence tests are added.
