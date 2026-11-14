# Point-region quadtree: Python teaching implementation

This directory contains a bucket point-region (PR) quadtree for 2D point data and inclusive rectangular window queries.

## Run it

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

Example:

~~~python
from quadtree import PointRegionQuadtree

stops = [(1, 2), (4, 5), (8, 7), (9, 1)]
index = PointRegionQuadtree(
    extent=(0, 0, 10, 10), points=stops, capacity=2, max_depth=12
)
print(index.query((3, 3, 10, 8)))
print(index.query_points((3, 3, 10, 8)))
~~~

The query returns original zero-based point IDs in input order. The insert method returns the ID assigned to a newly inserted point. The query_points method returns matching coordinates.

## Explicit spatial rules

- Root extent is (min_x, min_y, max_x, max_y) and must have positive width and height.
- The root boundary is closed: points on any outer edge are accepted.
- Points outside the root extent are rejected; the root does not expand automatically.
- A vertical midpoint tie goes east; a horizontal midpoint tie goes north. A point on both goes northeast.
- Child cells use closed bounds for query pruning. Their bounds overlap along split lines, but insertion assigns each point to exactly one child.
- Window predicates are inclusive on all four sides.
- Leaves split when their entry count exceeds capacity, unless max_depth has been reached or floating-point midpoints can no longer subdivide the cell.
- Coincident points may remain together in an over-capacity leaf at the stopping limit.
- This is a static-root teaching structure with insertion support. It does not implement deletion, root expansion, geometry indexing or raster-region compression.

## Validation

The test suite checks boundary and midpoint behaviour, duplicate points, stopping depth, invalid and out-of-extent inputs, narrow windows, clustered data and deterministic random queries. Every query test compares results with a brute-force inclusive rectangle scan.

## Read next

- [Conceptual quadtree lesson](../../../algorithms/indexing/quadtree.md)
- [Step-by-step implementation walkthrough](implementation-walkthrough.md)
- [Spatial-indexing learning path](../../../learning-paths/spatial-indexing.md)
