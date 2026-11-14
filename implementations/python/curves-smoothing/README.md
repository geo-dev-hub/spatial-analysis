# Curve construction and fitting

The package includes Chaikin corner cutting, Catmull–Rom interpolation, Bezier evaluation by de Casteljau, B-spline/NURBS evaluation by de Boor, and Schneider's recursive piecewise-cubic Bezier fitting algorithm.

The Schneider fitter accepts an ordered sequence of planar samples and a maximum squared-error tolerance. It uses chord-length parameterisation, least-squares tangent handle lengths, optional Newton–Raphson reparameterisation and recursive splitting at the maximum-error sample. The output is a connected chain of cubic Bezier segments. This is curve fitting, not line simplification.

Run python -m pytest -q. NumPy is required for the separate Kalman/RTS smoother; the curve-fitting implementation itself uses the standard library.
