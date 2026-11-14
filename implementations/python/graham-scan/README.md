# Graham scan: Python example

This teaching implementation computes the extreme vertices of the convex hull of a finite set of planar points.

## Run it

From this directory:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Use it

```python
from graham_scan import graham_scan

points = [(0, 0), (2, 0), (3, 1), (2, 2), (0, 2), (1, 1)]
print(graham_scan(points))
# [(0.0, 0.0), (2.0, 0.0), (3.0, 1.0), (2.0, 2.0), (0.0, 2.0)]
```

## Output contract

- Vertices are returned in counter-clockwise order.
- The first vertex is not repeated at the end.
- Duplicate input points are removed.
- Collinear points between extreme endpoints are omitted.
- Empty input returns an empty list; a fully collinear input returns its two endpoints.

## Scope and limitations

This is a learning implementation, not a robust production geometry engine. It uses `atan2` for sorting and ordinary floating-point arithmetic for orientation. Nearly collinear values can be misclassified due to rounding. Use robust predicates and a documented coordinate model for precision-critical work.

See the [Graham scan lesson](../../../algorithms/geometry/graham-scan.md) and [step-by-step walkthrough](implementation-walkthrough.md).
