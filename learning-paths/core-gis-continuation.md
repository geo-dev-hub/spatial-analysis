# Core GIS continuation: shape, proximity and location

This path follows the first geometry foundations sequence. It moves from individual boundaries and intersections into generalisation, offset geometry, proximity relationships and planar subdivisions.

You can follow the sequence or jump to the problem you need to solve.

## 1. Reduce line complexity without losing the shape

[Line simplification](../algorithms/geometry/simplification.md)

Compare Douglas–Peucker and Visvalingam–Whyatt. Work through the [implementation](../implementations/python/line-simplification/README.md), then inspect the differences in the [Core GIS lab](../notebooks/core-gis-algorithms-lab.ipynb). For adjacent polygon faces, continue with [coverage-aware simplification](../algorithms/geometry/coverage-simplification.md) and its [tested implementation](../implementations/python/coverage-simplification/README.md).

## 2. Move a boundary by a distance

[Polygon offsetting](../algorithms/geometry/offsetting.md)

Understand joins, end caps, miter limits, inward collapse and CRS units. Run the [GEOS-backed example](../implementations/python/polygon-offsetting/README.md), then compare it with the [native Clipper2 C# example](../implementations/clipper2-csharp/README.md).

## 3. Turn points into a spatial graph

[Proximity graphs](../algorithms/geometry/proximity-graphs.md)

Compare Gabriel, relative neighbourhood and Euclidean minimum spanning graphs. Run the [small-input implementations](../implementations/python/proximity-graphs/README.md) and examine the strict open-region tie convention.

## 4. Choose a precision model

[Precision models and snap rounding](../algorithms/geometry/precision-models.md)

Compare coordinate precision reduction, fixed-grid overlay and full snap-rounding noding. Run the [tested fixed-grid operations](../implementations/python/precision-grid/README.md), then explain which guarantees are—and are not—provided.

## 5. Locate a point in a subdivision

[Planar point location](../algorithms/geometry/point-location.md)

Move beyond point-in-polygon. Learn how slab decompositions and randomized trapezoidal maps answer repeated face-location queries. Run the [static slab locator](../implementations/python/point-location/README.md), then compare its restricted subdivision contract with the more general randomized trapezoidal-map literature.

## 6. Find a least-cost route through a graph

[Shortest paths](../algorithms/networks/shortest-paths.md)

Start with Dijkstra and A*, then run the tested [bidirectional Dijkstra and ALT landmark implementations](../implementations/python/shortest-paths/README.md). Compare the roles of contraction hierarchies and customizable route planning.

## Practice

Complete the [Core GIS continuation exercises](../exercises/core-gis-continuation.md). Record the coordinate model, units, assumptions, expected results and edge cases before running code.

## What this path does not claim

The path now includes tested coverage-aware simplification and fixed-grid precision wrappers, a native Clipper2 offset example, bidirectional Dijkstra, directed ALT, Yen's k-shortest loopless paths, edge-based turn restrictions and FIFO time-dependent earliest-arrival search. A dedicated snap-rounding noder, efficient Delaunay-based Yao/beta-skeleton construction, randomized trapezoidal-map locator, contraction hierarchies, non-FIFO routing and transit routing remain open.
