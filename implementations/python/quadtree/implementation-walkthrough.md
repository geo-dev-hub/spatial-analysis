# How the point-region quadtree is implemented

This walkthrough follows quadtree.py. The goal is to define a precise spatial contract, preserve every input point and prove that window queries agree with a brute-force answer.

## 1. Define the data model

This implementation indexes points in two-dimensional Cartesian coordinates. It does not index lines or polygons, and it is not a region quadtree for raster compression.

Each stored entry contains an original input ID and a coordinate pair. The ID is stable: it is the point's position in the input sequence, or the position assigned when inserted later.

The root extent is fixed at construction and expressed as (min_x, min_y, max_x, max_y).

## 2. Make the boundary policy explicit

The root extent is closed on all four sides. A point on the minimum or maximum x or y coordinate is valid. A point outside the root is rejected.

At each split, the midpoint is calculated on both axes. The implementation assigns ties consistently:
- x less than midpoint: west;
- x greater than or equal to midpoint: east;
- y less than midpoint: south;
- y greater than or equal to midpoint: north.

Therefore, a point on both split lines goes northeast. It is stored in one child only.

Child bounds overlap on split lines for query pruning. This is intentional: a query touching a split line must visit any child that could contain a matching point. Unique insertion assignment and inclusive query pruning are separate concerns.

## 3. Use a bucket leaf

A leaf stores up to capacity entries before it is split. When the next insertion exceeds that threshold, the node creates four children and redistributes its entries.

The children are ordered southwest, southeast, northwest and northeast. The quadrant function determines the destination.

## 4. Prevent infinite subdivision

Two coincident points can never be separated by spatial subdivision. Floating-point coordinates can also become indistinguishable at very small cell widths.

The implementation uses two safeguards:
- max_depth limits recursion;
- subdivision stops if a midpoint rounds to one of the cell's endpoints.

At either stopping condition, a leaf may contain more entries than its nominal capacity. This is correct: capacity is a preferred split threshold, not permission to lose records or recurse forever.

## 5. Query with subtree pruning

A rectangular query visits a node only if the node's cell intersects the query window. If there is no intersection, the entire subtree can be skipped.

At a leaf, the implementation tests each stored point against the query rectangle using inclusive comparisons. The returned IDs are sorted into original insertion order so callers receive stable results independent of tree traversal order.

The exact query condition is:

$$
x_{min} \leq x \leq x_{max}
\quad\text{and}\quad
y_{min} \leq y \leq y_{max}
$$

## 6. Validate against a simple oracle

The tests implement the same rectangle predicate as a direct scan over the original point list. Deterministic random datasets and windows are compared against that oracle.

The test suite also includes:
- split-line and outer-boundary points;
- coincident points that reach the depth limit;
- zero-depth trees;
- invalid extents and windows;
- points outside the root;
- clustered points and thin windows;
- a floating-point case where subdivision midpoints collapse.

A tree query that is faster but misses one boundary point is not correct. Differential testing makes this failure visible.

## 7. Understand what this implementation does not prove

This is a clear reference implementation, not a performance claim. It uses Python objects and recursive calls, and it sorts result IDs after traversal. It has no deletion, automatic root expansion, bulk-loading strategy, geometry support or global geographic metric.

For longitude/latitude data, the quadtree still partitions numeric coordinate space. Its cells do not have equal ground area or uniform physical dimensions. Choose a suitable projected CRS for local planar work, or a global indexing approach designed for the intended geographic model.

## 8. Reproduce

From this directory:

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

Then compare the implementation with the [conceptual quadtree lesson](../../../algorithms/indexing/quadtree.md) and complete the [spatial indexing exercises](../../../exercises/spatial-indexing-quadtrees-kdtree.md).
