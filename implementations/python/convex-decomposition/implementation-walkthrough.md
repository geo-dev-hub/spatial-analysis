# Intern walkthrough: turn a triangulation into convex pieces

## 1. Why decompose?

Some operations are easier on convex pieces than on a concave polygon. Convex decomposition is used in collision detection, motion planning, rendering and geometric algorithms. The goal is to partition the interior without gaps or overlaps so each piece is convex.

## 2. Triangulate first

The implementation calls the repository's ear-clipping routine. A simple polygon with (n) vertices becomes (n-2) triangles. Each triangle is convex, so this is a valid starting partition, but it may contain more pieces than necessary.

## 3. Find a merge candidate

Two pieces are adjacent when they share an edge in opposite directions. The shared edge is internal to their union. Remove it and trace the remaining boundary of both pieces to obtain a candidate polygon.

## 4. Test convexity exactly

At each candidate vertex, compute the orientation of the incoming and outgoing edges. A negative turn is reflex, so the merge is rejected. Zero turns are allowed and redundant straight-through vertices are removed.

No floating-point angle is needed. The sign of the cross product is enough:

[
operatorname{orient}(a,b,c)
=(b_x-a_x)(c_y-a_y)-(b_y-a_y)(c_x-a_x).
]

## 5. Repeat, then check conservation

The baseline scans piece pairs and merges the first admissible pair, repeating until no merge remains. It finally checks that the sum of the exact piece areas equals the input polygon area.

This is deliberately simple rather than asymptotically optimized. It demonstrates the geometry behind triangulate-and-merge while keeping the complexity and guarantees honest.

## 6. What the result does not mean

A locally irreducible greedy partition is not necessarily a minimum-cardinality partition. The implementation does not claim the Hertel–Mehlhorn approximation guarantee. It also does not handle holes, invalid rings or Steiner-point variants.

## Further reading

- CGAL, [2D Polygon Partitioning](https://doc.cgal.org/latest/Partition_2/index.html), for triangulation-based Hertel–Mehlhorn, Greene and related partitioning methods.
- Chazelle and Dobkin, [Decomposing a polygon into its convex parts](https://doi.org/10.1016/0020-0190(85)90044-7), for foundational convex partitioning work.
