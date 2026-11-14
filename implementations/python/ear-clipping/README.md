# Ear-clipping polygon triangulation

This package turns one simple polygon boundary into non-overlapping triangles. It is a compact implementation for learning how triangulation works—not a replacement for a robust geometry library.

## Run it

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

~~~python
from ear_clipping import triangulate, triangle_area

boundary = [(0, 0), (5, 0), (5, 4), (3, 2), (0, 4)]
triangles = triangulate(boundary)
print(len(triangles))  # 3
print(sum((triangle_area(t) for t in triangles), start=0))
~~~

## What the implementation guarantees

- The input is treated as one closed or open simple ring; a repeated final copy of the first vertex is accepted.
- Clockwise rings are reversed internally so output triangles are counter-clockwise.
- Consecutive duplicate vertices and exactly collinear vertices lying between their neighbours are removed before clipping.
- Orientation and point-in-triangle predicates use Python `Fraction` arithmetic. Decimal inputs are interpreted through their decimal string representation.
- A successful result contains exactly (n-2) triangles for the normalized ring, and their summed area equals the polygon area in the tested cases.
- Self-intersecting rings, zero-area rings and non-finite coordinates are rejected.

## Scope and limitations

This deliberately straightforward version recomputes candidate ears and scans the active vertices for each candidate. Its conservative worst-case bound is O(n^3), so it is intended for small teaching examples. A maintained ear queue with carefully scoped updates can achieve O(n^2); that optimization is a useful next exercise. This package does not support holes, multipolygons, constrained segments, mesh quality optimization, or automatic repair. Large coordinate fractions can also increase arithmetic cost.

A production workflow should use a maintained triangulation library, validate coordinate reference systems and topology, and decide explicitly how holes and constraints are represented. A triangulation is not automatically a constrained Delaunay triangulation and does not promise good-shaped triangles.

## Why the method works

A simple polygon with more than three vertices has an ear: three consecutive vertices whose triangle lies inside the polygon and contains no other polygon vertex. Removing the middle vertex replaces two boundary edges with the triangle's third edge. Repeating this operation leaves one final triangle.

For a normalized ring with (n) vertices, the process clips (n-3) ears and leaves one triangle, giving (n-2) triangles in total. The two-ears theorem guarantees that a simple polygon has an ear at every non-trivial stage; the implementation's checks determine which candidate is safe to remove.

See the [algorithm lesson](../../../algorithms/geometry/ear-clipping.md), [walkthrough](implementation-walkthrough.md), [exercise](../../../exercises/ear-clipping-triangulation.md) and [visual lab](../../../notebooks/ear-clipping-lab.ipynb).
