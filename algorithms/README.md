# Algorithm collection

Each record explains one method or operation, its assumptions, where it is useful, and what can go wrong. The collection is growing from the supplied [source inventory](../source-inventory/README.md); an entry is not treated as verified merely because it appears in that inventory.

## Geometry

- [Point in polygon](geometry/point-in-polygon.md) — classify a point as inside, outside or on a polygon boundary.
- [Polygon intersection](geometry/polygon-intersection.md) — construct the geometry shared by two inputs.
- [Convex hull](geometry/convex-hull.md) — find the smallest convex set containing a finite planar point set, with a Graham scan implementation.
- [Voronoi and Delaunay](geometry/voronoi-delaunay.md) — understand nearest-site regions, their Delaunay dual, Fortune's sweep and tessellation degeneracies.
- [Segment intersection](geometry/segment-intersection.md) — determine whether two line segments cross, touch or overlap.
- [Bentley–Ottmann](geometry/bentley-ottmann.md) — find intersecting pairs across a set of segments using a plane sweep.
- [Polygon validity](geometry/polygon-validity.md) — check whether rings, shells, holes and multi-part geometries satisfy the chosen geometry model; includes a tested Shapely inspection and explicit-repair workflow.
- [Polygon clipping](geometry/polygon-clipping.md) — compare clipping algorithm families, choose an appropriate tool and study a tested convex Sutherland–Hodgman teaching implementation.
- [Polygon overlay operations](geometry/overlay-operations.md) — understand intersection, union, difference, symmetric difference and precision, with a tested Shapely/GEOS package and visual notebook.
- [Line simplification](geometry/simplification.md) — compare Douglas–Peucker maximum-deviation and Visvalingam–Whyatt effective-area generalisation, with tested baselines.
- [Polygon offsetting](geometry/offsetting.md) — distinguish geometric offsets from clipping and compare join, cap and precision behaviour.
- [Proximity graphs](geometry/proximity-graphs.md) — compare Gabriel, relative-neighbourhood and Euclidean minimum-spanning graphs.
- [Planar point location](geometry/point-location.md) — understand slab decompositions and randomized trapezoidal maps.

## Networks and routing

- [Shortest paths](networks/shortest-paths.md) — understand graph cost models and shortest-path families, with tested Dijkstra and A* baselines.

## Spatial indexing

- [STR-packed R-tree](indexing/str-packed-rtree.md) — organise geometry bounding boxes into a packed hierarchy so queries can skip groups that cannot match.
- [Quadtree](indexing/quadtree.md) — recursively partition a two-dimensional space; this record focuses on bucket point-region trees and distinguishes them from region and other variants.
- [k-d tree nearest-neighbour search](indexing/kd-tree-nearest-neighbour.md) — partition point data along coordinate axes and prune branches using distance lower bounds.
- [Choosing a spatial index](indexing/choosing-spatial-index.md) — match R-trees, point-region quadtrees and k-d trees to the data model, query, update pattern and coordinate metric.

## Methods and analytical foundations

Not every spatial method is a standalone algorithm. See the [methods collection](../methods/README.md) for foundational objects and modelling choices, beginning with the spatial weights matrix.

## Query processing

- [Filter-and-refine spatial join](query-processing/filter-refine-spatial-join.md) — use a spatial index to find candidate geometry pairs, then apply the exact spatial predicate.

## Spatial statistics

- [Global Moran's I](statistics/global-morans-i.md) — measure global spatial autocorrelation by comparing deviations from the mean across neighbouring units.
- [Geary's C](statistics/gearys-c.md) — measure global spatial autocorrelation through squared differences between neighbouring values.
- [Local Moran's I](statistics/local-morans-i.md) — locate local clusters of similar values and spatial outliers, with conditional permutation inference.
- [Local Geary](statistics/local-geary.md) *(supplementary)* — measure local similarity and dissimilarity directly between a unit and its neighbours.
- [Getis-Ord Gi*](statistics/getis-ord-gi-star.md) — identify local concentrations of high values (hotspots) and low values (coldspots).

### Supplementary companion method

- [Global Getis-Ord G](statistics/global-getis-ord-g.md) — a supplementary global concentration statistic added to explain the source-listed local Gi* method; it is not a separate entry in the original compendium.

## A connected place to start

The [geometry foundations path](../learning-paths/geometry-foundations.md) connects the first four geometry lessons and continues into validity, clipping and overlay. The [spatial indexing path](../learning-paths/spatial-indexing.md) connects the packed R-tree, spatial joins, quadtree and k-d tree, with a new selection guide to help match an index to a workload. The [spatial autocorrelation path](../learning-paths/global-spatial-autocorrelation.md) connects global and local Moran, Geary and Getis-Ord methods, with six interactive notebooks. The [spatial indexing path](../learning-paths/spatial-indexing.md) starts with bounding boxes and the STR-packed R-tree.

## How to read a record

Start with the practical question, then follow the explanation into the formal definition, method, guarantees, complexity, numerical issues and references. Where a runnable implementation exists, it is linked from the record.

Records may have different evidence and implementation status. Check the status and version before relying on them.
