# Scattered-point gridding algorithms

Gridding converts irregularly located samples into values on a requested regular grid. The interpolation rule is part of the model: different methods make different assumptions about local support, smoothness and extrapolation.

## Nearest-neighbour gridding

For each grid node q, choose the sample p_i with minimum Euclidean distance and assign its value z_i. A k-d tree accelerates repeated nearest-neighbour queries. The result is piecewise constant over Voronoi regions. An optional maximum distance masks grid nodes unsupported by nearby observations.

## Delaunay triangulation gridding

Construct a Delaunay triangulation of the sample locations. For a grid node inside a triangle with vertices p_1,p_2,p_3, compute barycentric coordinates w_i and interpolate

\[
z(q)=w_1z_1+w_2z_2+w_3z_3,\qquad \sum_iw_i=1.
\]

The interpolant is piecewise linear and reproduces affine planes exactly within the convex hull. Nodes outside the hull receive an explicit fill value; this implementation does not extrapolate.

## What is not implemented here

These two methods are not minimum-curvature gridding, kriging, natural-neighbour interpolation or a general geophysical surface model. Minimum curvature requires a separately specified discretisation, boundary conditions and convergence criterion. Kriging additionally requires a covariance/variogram model and uncertainty calculation.

## Runnable material

- [Python implementation](../implementations/python/geophysical-gridding/geophysical_gridding.py)
- [Tests](../implementations/python/geophysical-gridding/test_geophysical_gridding.py)
- [Intern walkthrough](../implementations/python/geophysical-gridding/implementation-walkthrough.md)
- [Comparison lab](../notebooks/geophysical-gridding-lab.ipynb)

The implementation uses SciPy's Delaunay triangulation and cKDTree for the geometric primitives; the barycentric interpolation and grid contracts are explicit in the teaching code.
