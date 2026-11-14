# Medial axis: find the centres of maximal interior discs

The medial axis describes the interior structure of a shape. It is the set of points that have more than one closest point on the shape's boundary. Equivalently, it is the set of centres of maximal discs contained in the region: a disc is maximal when no larger disc inside the region contains it.

For a region (P) with boundary \(\partial P\), one definition is

[
MA(P)=\{x\in P:\text{there are at least two distinct closest points to }x\text{ on }\partial P\}.
]

The nearest boundary points are the *contact points* of the maximal disc centred at (x).

## Why it matters

The medial axis is useful for shape description, width measurement, skeleton-based generalization, clearance analysis, image analysis, mesh generation and identifying narrow passages. It reduces a two-dimensional region to a lower-dimensional structure while retaining information about the region's local thickness.

## Connection to Voronoi diagrams

A polygon boundary is not just a set of vertices. Its edges and vertices are boundary features. A Voronoi diagram of those features partitions the plane according to the nearest feature. The medial axis is the part of this feature Voronoi diagram that lies inside the polygon, with the precise feature and degeneracy conventions handled by the construction.

The resulting edges are not always straight. For a polygonal boundary, the bisector between two line segments can be a line or a parabolic arc, depending on which features are closest. This is why a general polygon medial axis should not be represented as a straight-line graph without approximation or loss of exactness.

## What the structure tells you

- A point on the axis has at least two closest boundary contact points.
- The radius of its maximal disc is the distance to those contacts.
- Branches often meet at locations where a maximal disc touches three or more boundary features.
- The axis reveals narrow corridors and local width changes.
- Small boundary perturbations can create large changes in the detailed axis.

The last point is important: the medial axis is sensitive to small boundary features. A noisy polygon can produce many short branches. Pruning or smoothing may be useful, but those operations change the representation and must be documented.

## Construction strategies

For polygonal domains, one exact route is to construct a Voronoi diagram of the boundary segments and vertices, then extract the interior portion that satisfies the medial-axis definition. Specialized algorithms can exploit polygon structure. The literature includes an (O(n\log n)) construction and a later linear-time result for the relevant polygonal setting; simple implementations are often quadratic.

Raster skeletonization is a different problem. Thinning a binary image produces a pixel skeleton whose result depends on grid connectivity, resolution and thinning rules. It should not be described as an exact continuous medial axis.

## Medial axis versus straight skeleton

The medial axis is metric: its points are equidistant from multiple boundary features under Euclidean distance. The straight skeleton is defined by a wavefront in which polygon edges move inward while remaining parallel to themselves. For convex polygons the structures coincide, but for general non-convex polygons they differ.

The straight skeleton consists of straight segments. The medial axis can contain parabolic arcs. The straight skeleton is often convenient for mitered offsets and roof-like constructions; the medial axis is the appropriate structure when maximal inscribed discs and Euclidean clearance are the goal.

## Practical cautions

1. Specify whether the input is a simple polygon, polygon with holes, or a more general region.
2. Preserve the boundary-feature model: segment interiors and vertices both matter.
3. Use the intended metric. A Euclidean medial axis is not automatically meaningful in a projected coordinate system with unsuitable distortion.
4. Expect short branches from small notches and digitization noise.
5. If pruning branches, record the threshold and the effect on width or clearance measurements.
6. Do not confuse a medial axis with a centreline obtained by visual digitization or raster thinning.

## Follow the learning sequence

- [Voronoi and Delaunay](voronoi-delaunay.md) introduces nearest-site partitions and the dual graph.
- [Straight skeleton](straight-skeleton.md) contrasts a wavefront-based polygon skeleton with the metric medial axis.
- [Medial-axis exercise](../../exercises/medial-axis.md) asks you to reason about contact points, local width and boundary noise.

## Further reading

- Lee, D.-T. (1982), *Medial axis transformation of a planar shape*, IEEE Transactions on Pattern Analysis and Machine Intelligence 4(4), 363–369.
- Choi, S.-W., Lee, H.-P. and others (1999), work on linear-time medial-axis construction for polygonal domains; consult the original publication before relying on a specific variant's assumptions.
- O'Rourke, J. and Tóth, C. D. (2017), [Handbook chapter on medial axis](https://www.csun.edu/~ctoth/Handbook/chap54.pdf), for the relation to Voronoi diagrams and applications.
