# Curve construction implementation walkthrough

## Chaikin, Catmull–Rom and Bezier
Chaikin repeatedly inserts weighted points along edges. Catmull–Rom interpolates waypoints using a parameterisation based on chord lengths. Bezier evaluation uses de Casteljau's repeated linear interpolation.

## B-splines: de Boor
A B-spline is determined by control points, degree p and a nondecreasing knot vector. Find the knot span containing u, copy the p+1 active control points, then perform p rounds of affine interpolation. At each round r, update points from right to left using alpha=(u-U_i)/(U_(i+p-r+1)-U_i). Zero knot intervals contribute alpha=0 under the repeated-knot convention. Local support means only p+1 controls affect a parameter value.

## NURBS: homogeneous coordinates
Multiply each control point by its weight and append the weight as a third homogeneous coordinate. Apply de Boor to these weighted triples, then divide the first two coordinates by the third. A rational quadratic quarter-circle with middle weight sqrt(1/2) is an exact validation fixture.

## Validation
Tests cover endpoint interpolation, quadratic Bezier equivalence, a rational quarter-circle midpoint, knot/domain validation and sampling. These functions evaluate curves; they do not fit a curve to noisy observations or perform Kalman/RTS smoothing.
