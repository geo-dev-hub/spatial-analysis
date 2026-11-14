# Graham scan: build the convex hull of a point set

This is a small, dependency-free teaching implementation of the Graham scan for finite 2D points.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
python graham_scan.py
~~~

## What the algorithm returns

The convex hull is the smallest convex set containing all input points. This implementation returns its extreme vertices in counter-clockwise order, without repeating the first point at the end.

- Duplicate input coordinates are removed.
- Interior points are excluded.
- Collinear points along hull edges are omitted; only extreme endpoints remain.
- Empty input returns an empty list.
- One or two unique points are returned directly.
- Non-finite coordinates are rejected.

## Example

~~~python
from graham_scan import convex_hull

points = [(0, 0), (2, 0), (2, 2), (0, 2), (1, 1)]
print(convex_hull(points))
~~~

Expected output:

~~~text
[(0.0, 0.0), (2.0, 0.0), (2.0, 2.0), (0.0, 2.0)]
~~~

## Important numerical limit

The implementation uses ordinary floating-point cross products for orientation and polar ordering. It is suitable for learning and ordinary well-scaled examples, not adversarial near-collinear data or high-assurance computational geometry. Robust production systems may use exact or adaptive-precision predicates.

## Complexity

The polar-ordering phase sorts the points in O(n log n). The scan processes each sorted point a constant number of times, so the overall expected algorithmic bound is O(n log n) for the comparison sort.

## Read next

- [Convex hull lesson](../../../algorithms/geometry/convex-hull.md)
- [Implementation walkthrough](implementation-walkthrough.md)
- [Visual convex hull lab](../../../notebooks/convex-hull-lab.ipynb)
