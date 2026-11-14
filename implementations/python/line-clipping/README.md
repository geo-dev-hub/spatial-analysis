# Line clipping — Python teaching implementation

Implements Cohen–Sutherland and Liang–Barsky clipping against an axis-aligned rectangle, plus Cyrus–Beck clipping against a convex polygon. All functions return clipped endpoint pairs or `None` when the segment is rejected.

Run tests with `python -m pytest -q` from this directory. Runtime code uses only the standard library; pytest is the test runner.

Inputs are planar Cartesian coordinates in consistent units. This package clips a segment, not a polygon boundary or arbitrary geometry collection. Cyrus–Beck requires a simple convex ring and accepts clockwise or counter-clockwise vertex order. Degenerate windows, non-finite coordinates and malformed bounds are rejected. Floating-point arithmetic is used; this is not an exact-predicate geometry kernel.
