# Intern walkthrough: nearest-neighbour and triangulation gridding

Scattered samples have coordinates p_i=(x_i,y_i) and scalar values z_i. A regular grid is a requested set of query locations, not a new observation set.

## Nearest neighbour
Build a k-d tree over sample coordinates. For each grid node q, find the sample i minimising Euclidean distance and assign z_i. An optional maximum distance returns NoData for unsupported nodes. This produces a piecewise-constant Voronoi partition.

## Delaunay triangulation interpolation
Construct a Delaunay triangulation of the sample locations. Locate the triangle containing each grid node. Compute barycentric coordinates (w_1,w_2,w_3), which sum to one, and interpolate z(q)=sum(w_i z_i). Nodes outside the convex hull receive the explicit fill value; no extrapolation is invented.

The affine-plane test is important: barycentric interpolation must exactly reproduce any function z=ax+by+c inside the triangulated domain, up to floating-point arithmetic. The methods are not substitutes for minimum-curvature gridding or kriging; their assumptions and smoothness differ.


## Thin-plate-spline minimum-bending-energy interpolation

The package also includes a 2D thin-plate-spline radial-basis interpolator. Its radial kernel is \(\phi(r)=r^2\log r\), augmented by an affine polynomial tail. The associated bending-energy functional is

\[
J[f]=\iint\left(f_{xx}^2+2f_{xy}^2+f_{yy}^2\right)\,dx\,dy.
\]

With zero smoothing it interpolates the observations; positive smoothing trades exact fit for a smoother surface. This is a minimum-bending-energy thin-plate spline, not a reproduction of the classic Briggs iterative minimum-curvature scheme. It can extrapolate outside the convex hull, so edge values need particular scrutiny.


## 4. Ordinary kriging with a fixed exponential covariance

The implementation builds the ordinary-kriging system from the supplied exponential covariance model

\[
C(h)=s^2\exp(-h/a),
\]

where \(a\) is the range parameter and \(s^2\) is the structured sill. The nugget is added to the observation covariance diagonal. For each query location, solve the augmented system enforcing weights that sum to one. The result includes both the weighted prediction and the model-based kriging variance.

The covariance parameters are inputs, not estimated outputs. A poor variogram model produces poor predictions and misleading variances. The dense inverse is pedagogical and intended for small sample sets; production systems need numerically stable factorisation, neighbourhood selection and scalable solvers. The returned variance is conditional on the supplied covariance model and does not include variogram-parameter uncertainty.
