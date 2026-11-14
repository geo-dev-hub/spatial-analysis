# Curve construction teaching implementations

This package includes Chaikin corner cutting, Catmull–Rom interpolation, arbitrary-degree Bezier evaluation by de Casteljau, and B-spline/NURBS evaluation by de Boor's algorithm.

B-spline/NURBS inputs are planar control points, degree, nondecreasing knot vector and parameter in the closed spline domain. The knot vector length is control_count + degree + 1. NURBS weights must be finite and non-zero. Sampling functions include both domain endpoints.

Run python -m pytest -q from this directory. The package does not yet implement Schneider's Bezier curve fitting or Kalman/RTS trajectory smoothing. Curve construction and statistical trajectory estimation are different tasks.
