# Core GIS continuation: shape, proximity and location

This path follows the first geometry foundations sequence. It moves from individual boundaries and intersections into generalisation, offset geometry, proximity relationships and planar subdivisions.

You can follow the sequence or jump to the problem you need to solve.

## 1. Reduce line complexity without losing the shape

[Line simplification](../algorithms/geometry/simplification.md)

Compare Douglas–Peucker and Visvalingam–Whyatt. Work through the [implementation](../implementations/python/line-simplification/README.md), then inspect the differences in the [Core GIS lab](../notebooks/core-gis-algorithms-lab.ipynb).

## 2. Move a boundary by a distance

[Polygon offsetting](../algorithms/geometry/offsetting.md)

Understand joins, end caps, miter limits, inward collapse and CRS units. Run the [GEOS-backed example](../implementations/python/polygon-offsetting/README.md). It is deliberately not presented as a Clipper2 binding.

## 3. Turn points into a spatial graph

[Proximity graphs](../algorithms/geometry/proximity-graphs.md)

Compare Gabriel, relative neighbourhood and Euclidean minimum spanning graphs. Run the [small-input implementations](../implementations/python/proximity-graphs/README.md) and examine the strict open-region tie convention.

## 4. Locate a point in a subdivision

[Planar point location](../algorithms/geometry/point-location.md)

Move beyond point-in-polygon. Learn how slab decompositions and randomized trapezoidal maps answer repeated face-location queries. The dossier is research-ready, but the complete data structure is not yet implemented.

## 5. Find a least-cost route through a graph

[Shortest paths](../algorithms/networks/shortest-paths.md)

Start with Dijkstra and A*, then compare the roles of ALT, contraction hierarchies and customizable route planning. Run the [tested Python baseline](../implementations/python/shortest-paths/README.md).

## Practice

Complete the [Core GIS continuation exercises](../exercises/core-gis-continuation.md). Record the coordinate model, units, assumptions, expected results and edge cases before running code.

## What this path does not claim

The path does not yet provide production implementations of topology-preserving polygon simplification, snap rounding, Clipper2 offsets, Yao/beta-skeleton graphs, trapezoidal-map point location, ALT, contraction hierarchies, turn-aware routing or time-dependent routing. These remain explicit follow-up work rather than hidden gaps.
