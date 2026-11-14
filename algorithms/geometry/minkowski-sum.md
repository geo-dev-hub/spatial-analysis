# Minkowski sums: combine shapes by adding every pair of points

A Minkowski sum combines two geometric sets by adding their points. It appears in robot motion planning, collision detection, toolpath generation, offsets and configuration-space reasoning.

For sets (A,B\subseteq\mathbb{R}^2), the Minkowski sum is

[
A\oplus B=\{a+b\mid a\in A,\ b\in B\}.
]

If (B) is a disc of radius (r), the sum expands (A) outward by distance (r) (a dilation/offset). If (B) is a reflected robot footprint, the sum helps turn collision checking for a moving robot into point-location against a configuration-space obstacle.

## The geometric intuition

Imagine sliding shape (B) so that one of its points is placed at every point of (A). The Minkowski sum is the region swept out by all those placements. It is not generally the same as the union of two shapes, and it is not the same as adding their bounding boxes.

## Convex polygons: merge the edge directions

For two convex polygons (P) and (Q), the boundary of (P\oplus Q) can be built by merging their edge vectors in angular order. Start at the sum of suitable lowest vertices, then walk around both boundaries. When the next edge directions differ, advance along the polygon with the next direction; when they are parallel and point the same way, add both vectors.

If (P) has (m) edges and (Q) has (n), the merge takes (O(m+n)) time after the vertices have been placed in consistent counter-clockwise order and a suitable start vertex selected.

This is closely related to merging two sorted sequences. The sort key is edge direction around the circle, not the raw x-coordinate.

## Non-convex polygons: two broad strategies

### Convex decomposition

Partition each input polygon into convex pieces (P_1,\ldots,P_k) and (Q_1,\ldots,Q_\ell). Compute each convex pair sum

[
S_{ij}=P_i\oplus Q_j
]

and union the results:

[
P\oplus Q=\bigcup_{i=1}^{k}\bigcup_{j=1}^{\ell} S_{ij}.
]

This reuses the efficient convex-polygon routine, but the number and shape of the pieces matter. A decomposition with many pieces can create many pairwise sums and a large union problem. The best decomposition can depend on both input polygons and the downstream operation; minimum piece count is not necessarily the best performance objective.

### Boundary convolution

A second approach constructs a set of translated boundary segments called the polygon convolution. Its cycles may self-intersect and are not necessarily the final boundary. An arrangement is built, and winding-number information identifies the cells belonging to the Minkowski sum.

This method can produce a smaller intermediate arrangement than the pairwise decomposition strategy on many inputs. It is more involved than the convex merge and requires robust arrangement construction and face classification.

CGAL documents both decomposition and full/reduced convolution routines, including support for polygons with holes in its 2D Minkowski-sum package.

## Configuration-space obstacle

Let (R) be a robot footprint relative to its reference point, and let (O) be an obstacle. The forbidden reference-point positions are

[
C_{obs}=O\oplus(-R),
]

where (-R=\{-r\mid r\in R\}) is the reflection of the robot around its reference point. The reference point can move without collision when it remains outside the configuration-space obstacle (subject to the chosen contact policy).

This transformation is powerful because a finite-size moving object becomes a point moving among expanded obstacles. It also shows why the robot's reference point and footprint orientation must be defined carefully.

## Offsets are a special case

For a region (P) and a disc (D_r) of radius (r),

[
P\oplus D_r
]

is the outward offset (dilation). An inward offset is not obtained by simply changing (r) to a negative number in ordinary set addition; it is an erosion/inset operation with different topology and collapse behaviour. Narrow corridors can disappear, components can split, and holes can grow or vanish.

For polygonal approximations of a disc, the result is an approximation whose error depends on the chosen number of sides and orientation. Exact circular arcs require a geometry representation capable of storing them.

## Validate the result

- Verify that the input coordinate systems and units agree. Minkowski addition has no useful meaning when one input is in degrees and the other in metres.
- Preserve winding and hole semantics.
- Test known convex examples against the edge-vector merge.
- Check symmetry: (A\oplus B=B\oplus A).
- Check translation: ((A+t)\oplus B=(A\oplus B)+t).
- Check point identity: (A\oplus\{(0,0)\}=A).
- For configuration space, verify the robot reflection and reference-point convention.
- Inspect topology changes and precision effects in non-convex outputs.

These are useful invariants, but a matching area or bounding box is not proof of an exact boundary.

## Decision guide

| Inputs and objective | Suitable route |
|---|---|
| Two convex polygons | Angular merge of edge vectors |
| Non-convex polygons, existing convex partition | Pairwise convex sums followed by union |
| Non-convex polygons with complex topology | Robust convolution/arrangement implementation |
| Polygon plus disc | Dedicated offset/dilation operation |
| Robot and obstacles | Configuration-space construction using a reflected footprint |

## Follow the learning sequence

- [Convex decomposition](convex-decomposition.md) explains why the partition affects the pairwise-sum approach.
- [Polygon offsetting](offsetting.md) covers practical offset operations and precision issues.
- [Minkowski sum exercise](../../exercises/minkowski-sum.md) works through convex sums and configuration-space reasoning.

## Further reading

- [CGAL 2D Minkowski Sums manual](https://doc.cgal.org/6.1.1/Minkowski_sum_2/index.html) describes convex sums, decomposition and convolution strategies, plus offsets.
- Baram, A., Fogel, E., Halperin, D., Hemmer, M. and Morr, S. (2018), [*Exact Minkowski Sums of Polygons with Holes*](https://doi.org/10.1016/j.comgeo.2018.06.005), *Computational Geometry* 73, 46–56.
- Agarwal, P. K., Flato, E. and Halperin, D. (2002), [*Polygon decomposition for efficient construction of Minkowski sums*](https://doi.org/10.1016/S0925-7721(01)00041-4), *Computational Geometry: Theory and Applications* 21(1–2), 39–61.
- Mount, D. M., [Computational Geometry lecture notes](https://jeffe.cs.illinois.edu/teaching/compgeom/refs/Mount.pdf), section on configuration-space obstacles and convex Minkowski sums.
