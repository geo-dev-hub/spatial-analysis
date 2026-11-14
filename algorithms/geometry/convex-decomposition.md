# Convex decomposition: partition a polygon into simpler pieces

A concave polygon can make later geometric operations harder. Convex decomposition partitions its interior into convex polygons, so each piece has a simpler shape while the pieces together preserve the original region.

This is a *partition*: pieces should cover the input without gaps or interior overlap. It is not the same as taking a convex hull, which fills every concavity and changes the represented area.

## Why decompose?

Convex pieces are useful in collision detection, motion planning, configuration-space construction, computational geometry, constrained optimization and some mesh workflows. The right decomposition depends on what the next operation needs:

- **Few pieces:** reduce the number of downstream pairwise operations.
- **No new vertices:** preserve the input boundary's vertex set.
- **Small or well-shaped pieces:** control numerical conditioning or workload.
- **Approximate convexity:** ignore tiny boundary notches when the application permits a tolerance.
- **Holes:** preserve interior rings and their topology explicitly.

These objectives can conflict. A decomposition with the fewest pieces is not automatically the fastest or most useful decomposition for a downstream operation.

## Convexity test

For a consistently counter-clockwise simple ring, a vertex is reflex when its local orientation is negative:

[
\operatorname{orient}(a,b,c)=
(b_x-a_x)(c_y-a_y)-(b_y-a_y)(c_x-a_x)<0.
]

A polygon is convex when it has no reflex vertices (after applying the chosen policy for collinear boundary points). A candidate diagonal is valid only if it lies inside the polygon and splits it into valid subpolygons. Do not infer validity from endpoint visibility alone without checking intersections and interior placement.

## Main approaches

### 1. Triangulate, then merge

First triangulate the polygon. Then consider internal diagonals and remove a diagonal whenever merging its two incident regions leaves a convex polygon. The result is a convex partition.

This is the core intuition behind the Hertel–Mehlhorn approximation: start from a triangulation and discard unnecessary diagonals. It is a useful baseline because triangulation already gives a complete partition into convex cells (triangles), and each accepted merge reduces the number of pieces.

The result is not guaranteed to use the minimum possible number of pieces. The approximation guarantee depends on the precise algorithm and assumptions; the Hertel–Mehlhorn method is commonly presented as producing at most four times the optimal number of convex pieces. CGAL documents its implementation as a linear-time post-process of a supplied triangulation, with the triangulation cost handled separately.

### 2. Dynamic programming for an optimal partition

For simple polygons, exact minimum-piece decompositions can be computed with dynamic programming under a specified model. The result depends on whether Steiner points (new vertices inserted inside the polygon or on its boundary) are allowed and whether the objective is the number of pieces, the number/length of diagonals, or another cost.

CGAL documents Greene's optimal partitioning algorithm with (O(n^4)) worst-case time and (O(n^3)) space. This is a concrete library implementation, not a universal bound for every optimal-decomposition formulation.

### 3. Sweep-line approximations

Greene also described an approximation route based on first partitioning a polygon into monotone pieces and then refining those pieces into convex regions. CGAL documents its sweep-line approximation as (O(n\log n)) time and (O(n)) space. The quality and guarantees should be read against the exact variant and input assumptions.

### 4. Approximate convex decomposition

Some applications do not need mathematically convex pieces. They need pieces whose concavities are smaller than a chosen tolerance. Lien and Amato's method repeatedly resolves significant notches and produces a hierarchy of increasingly convex pieces. This can reduce the number of parts and ignore small geometric detail, but it changes the contract: the output is *approximately convex*, not an exact convex partition.

## A safe workflow

~~~mermaid
flowchart TD
    A[Validate polygon and ring structure] --> B{Holes present?}
    B -- Yes --> C[Choose a holes-aware method]
    B -- No --> D[Choose exact or approximate objective]
    C --> E[Select a library and preserve topology]
    D --> F{Need a minimum piece count?}
    F -- Yes --> G[Use a specified optimal method]
    F -- No --> H[Triangulate, then remove safe diagonals]
    G --> I[Validate partition]
    H --> I
    E --> I
    I --> J[Check coverage, overlap, convexity and area]
~~~

## How to validate a decomposition

For input region (P) and output pieces (C_1,\ldots,C_k), check:

1. **Coverage:** (P=\bigcup_i C_i).
2. **No interior overlap:** (\operatorname{interior}(C_i)\cap\operatorname{interior}(C_j)=\varnothing) for (i\ne j).
3. **Convexity:** every output piece satisfies the selected convexity predicate.
4. **Boundary agreement:** internal edges occur in matching pairs; the union boundary matches the input boundary.
5. **Area:** (A(P)=\sum_i A(C_i)), subject to the precision model and topology.
6. **Topology:** holes, disconnected components and ring orientation are handled explicitly.

Area agreement alone is not enough: overlapping pieces can have the same total area as the input if gaps and overlaps cancel. Validate the union and pairwise interiors as well.

## Complexity and problem boundaries

Do not write “convex decomposition is NP-hard” without specifying the problem variant. For simple polygons, important exact polynomial-time algorithms are known; some models allow Steiner points and some forbid them. With holes, several minimum-decomposition formulations become NP-hard. Approximate convex decomposition is a different objective again.

The input model matters too: one simple ring, a polygon with holes, a polygonal set with multiple components, and a possibly self-intersecting path are not interchangeable inputs.

## Follow the learning sequence

- [Ear clipping](ear-clipping.md) explains how a simple polygon can first be triangulated.
- [Ear-clipping implementation](../../implementations/python/ear-clipping/README.md) is a transparent teaching baseline; it does not yet implement the Hertel–Mehlhorn merge pass.
- [Convex decomposition exercise](../../exercises/convex-decomposition.md) asks you to derive and validate a partition.
- [Minkowski sums](minkowski-sum.md) shows why the choice of convex decomposition affects downstream geometry operations.

## Further reading

- Hertel, S. and Mehlhorn, K. (1983), *Fast triangulation of simple polygons*, in the context of approximation algorithms for convex partitioning. The edge-removal idea is described in the computational-geometry literature and implemented by CGAL.
- Greene, D. H. (1983), *The decomposition of polygons into convex parts*, in *Computational Geometry*. CGAL documents optimal and sweep-line approximation variants.
- Lien, J.-M. and Amato, N. M. (2004), [*Approximate Convex Decomposition of Polygons*](https://doi.org/10.1145/997817.997823), SoCG, 17–26.
- Agarwal, P. K., Flato, E. and Halperin, D. (2002), [*Polygon decomposition for efficient construction of Minkowski sums*](https://doi.org/10.1016/S0925-7721(01)00041-4), *Computational Geometry: Theory and Applications* 21(1–2), 39–61.
- [CGAL 2D Polygon Partitioning manual](https://doc.cgal.org/6.1.1/Partition_2/index.html) documents the exact and approximate routines and their implementation-specific bounds.
