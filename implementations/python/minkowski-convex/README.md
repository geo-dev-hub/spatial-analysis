# Convex polygon Minkowski sum

A small, exact-arithmetic implementation of the linear-time edge-merge algorithm for the Minkowski sum of two convex polygons.

## Run it

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

The module is `minkowski_sum.py`. Call `minkowski_sum(P, Q)` with each polygon as an iterable of 2D coordinate pairs. It returns counter-clockwise vertices as `fractions.Fraction` values, without repeating the first vertex at the end.

## Contract

- Each input is one non-degenerate, simple, convex polygon ring.
- Either clockwise or counter-clockwise input is accepted.
- A repeated closing vertex, repeated consecutive vertices and redundant collinear boundary vertices are cleaned.
- Coordinates are represented as exact rational values.
- Holes, non-convex polygons, multipolygons, curved boundaries and GIS topology repair are not supported.

The edge merge uses polar half-plane and cross-product comparisons; it does not call `atan2` or sort all edges. For polygons with (m) and (n) vertices, the merge is (O(m+n)).

This is a transparent teaching implementation, not a replacement for a robust polygon-Boolean library. For non-convex input, use a documented decomposition or convolution implementation such as CGAL's 2D Minkowski Sum package.
