# Intern walkthrough: nearest-neighbour and triangulation gridding

Scattered samples have coordinates p_i=(x_i,y_i) and scalar values z_i. A regular grid is a requested set of query locations, not a new observation set.

## Nearest neighbour
Build a k-d tree over sample coordinates. For each grid node q, find the sample i minimising Euclidean distance and assign z_i. An optional maximum distance returns NoData for unsupported nodes. This produces a piecewise-constant Voronoi partition.

## Delaunay triangulation interpolation
Construct a Delaunay triangulation of the sample locations. Locate the triangle containing each grid node. Compute barycentric coordinates (w_1,w_2,w_3), which sum to one, and interpolate z(q)=sum(w_i z_i). Nodes outside the convex hull receive the explicit fill value; no extrapolation is invented.

The affine-plane test is important: barycentric interpolation must exactly reproduce any function z=ax+by+c inside the triangulated domain, up to floating-point arithmetic. The methods are not substitutes for minimum-curvature gridding or kriging; their assumptions and smoothness differ.
