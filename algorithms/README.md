# Algorithm collection

Each record explains one method or operation, its assumptions, where it is useful, and what can go wrong. The collection is growing from the supplied [source inventory](../source-inventory/README.md); an entry is not treated as verified merely because it appears in that inventory.

## Geometry

- [Point in polygon](geometry/point-in-polygon.md) — classify a point as inside, outside or on a polygon boundary.
- [Polygon intersection](geometry/polygon-intersection.md) — construct the geometry shared by two inputs.
- [Segment intersection](geometry/segment-intersection.md) — determine whether two line segments cross, touch or overlap.
- [Bentley–Ottmann](geometry/bentley-ottmann.md) — find intersecting pairs across a set of segments using a plane sweep.

## Spatial statistics

- [Global Moran's I](statistics/global-morans-i.md) — measure global spatial autocorrelation for a continuous attribute under a stated spatial weights matrix.

## A connected place to start

The [geometry foundations path](../learning-paths/geometry-foundations.md) connects the first four geometry lessons in a practical sequence, from point location to all-segment intersection. Global Moran's I is the first researched record in the spatial-statistics collection; a wider path will follow as related methods are verified.

## How to read a record

Start with the practical question, then follow the explanation into the formal definition, method, guarantees, complexity, numerical issues and references. Where a runnable implementation exists, it is linked from the record.

Records may have different evidence and implementation status. Check the status and version before relying on them.
