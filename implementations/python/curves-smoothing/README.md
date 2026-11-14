# Curve construction teaching implementations

This package provides three bounded, transparent curve algorithms:

- Chaikin corner cutting for open polylines and closed rings.
- Centripetal Catmull–Rom interpolation for open control-point sequences, with uniform and chordal parameterisation available through the alpha parameter.
- Arbitrary-degree Bezier evaluation using de Casteljau's algorithm.

Run `python -m pytest -q` from this directory. Runtime code uses only the Python standard library.

The package does **not** implement B-spline or NURBS evaluation/fitting, Schneider's cubic Bezier curve fitting, Kalman filtering or Rauch–Tung–Striebel smoothing. Those are different mathematical problems and require separate contracts and tests. The algorithms here are curve construction/geometry examples, not trajectory denoising or statistically optimal smoothing.
