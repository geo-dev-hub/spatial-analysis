# Geophysical gridding baselines

Four scattered-point gridding methods for regular output grids:
- nearest-neighbour assignment using a spatial k-d tree, optionally masking nodes beyond a maximum distance;
- piecewise-linear interpolation over a Delaunay triangulation using barycentric coordinates, with an explicit outside-convex-hull fill value;
- thin-plate-spline radial-basis interpolation, the minimum-bending-energy surface with an affine polynomial tail and optional smoothing;
- ordinary kriging with an explicitly supplied exponential covariance model, returning both prediction and kriging variance.

The thin-plate spline is a minimum-bending-energy (thin-plate) surface and a minimum-curvature-style interpolant. It is not the classic Briggs iterative minimum-curvature gridding algorithm; exact algorithm equivalence is not claimed. They assume planar coordinates in consistent units. Nearest-neighbour creates Voronoi regions; triangulation interpolation is continuous across shared edges but has piecewise-constant gradients within each triangle. Sparse or uneven sampling can create artefacts and extrapolation is not performed.

Run python -m pip install -r requirements.txt and python -m pytest -q.


See the [gridding methods lesson](../../../methods/geophysical-gridding.md) and [implementation walkthrough](implementation-walkthrough.md).

Ordinary kriging does not estimate its own variogram: range, sill and nugget are supplied by the caller. The dense solver is intended for small teaching examples, not large surveys.
