# Geophysical gridding baselines

Two scattered-point interpolation methods for regular output grids:
- nearest-neighbour assignment using a spatial k-d tree, optionally masking nodes beyond a maximum distance;
- piecewise-linear interpolation over a Delaunay triangulation using barycentric coordinates, with an explicit outside-convex-hull fill value.

These are not minimum-curvature gridding. They assume planar coordinates in consistent units. Nearest-neighbour creates Voronoi regions; triangulation interpolation is continuous across shared edges but has piecewise-constant gradients within each triangle. Sparse or uneven sampling can create artefacts and extrapolation is not performed.

Run python -m pip install -r requirements.txt and python -m pytest -q.
