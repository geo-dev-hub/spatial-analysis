# Geometry methods

- [Point in polygon](point-in-polygon.md)
- [Polygon intersection](polygon-intersection.md)
- [Segment intersection](segment-intersection.md)
- [Bentley–Ottmann](bentley-ottmann.md)
- [Line simplification](simplification.md)
- [Polygon coverage simplification](coverage-simplification.md)
- [Precision models and snap rounding](precision-models.md)
- [Snap rounding noder](snap-rounding.md)
- [Polygon offsetting](offsetting.md)
- [Proximity graphs](proximity-graphs.md)
- [Planar point location](point-location.md)

These records are part of the broader [algorithm collection](../README.md). The source inventory identifies the methods to investigate; each record documents its own scope, assumptions and evidence.

- [Ear clipping](ear-clipping.md) — triangulate a simple polygon ring by repeatedly removing an interior ear.

- [Convex decomposition](convex-decomposition.md) — partition a polygon into convex pieces, and distinguish exact from approximate objectives.

- [Minkowski sums](minkowski-sum.md) — combine sets by vector addition; connect convex edge merging, convolution and configuration-space obstacles.

- [Medial axis](medial-axis.md) — locate centres of maximal interior discs through boundary-feature distance.
- [Straight skeleton](straight-skeleton.md) — trace wavefront vertices as polygon edges move inward in parallel.

- [Convex Minkowski-sum implementation](../../implementations/python/minkowski-convex/README.md) — exact rational edge merge, tests and intern walkthrough.

- [Convex decomposition implementation](../../implementations/python/convex-decomposition/README.md) — exact-predicate greedy triangle merging, tests and walkthrough.

- [Delaunay-filtered proximity graphs](../../implementations/python/proximity-graphs/README.md) — sparse candidate filtering for Gabriel and RNG, with documented degeneracy limits.
