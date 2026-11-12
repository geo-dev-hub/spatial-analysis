# Algorithm collection

Each record explains one method or operation, its assumptions, where it is useful, and what can go wrong. The collection is growing from the supplied [source inventory](../source-inventory/README.md); an entry is not treated as verified merely because it appears in that inventory.

## Geometry

- [Point in polygon](geometry/point-in-polygon.md) — classify a point as inside, outside or on a polygon boundary.
- [Polygon intersection](geometry/polygon-intersection.md) — construct the geometry shared by two inputs.
- [Segment intersection](geometry/segment-intersection.md) — determine whether two line segments cross, touch or overlap.
- [Bentley–Ottmann](geometry/bentley-ottmann.md) — find intersecting pairs across a set of segments using a plane sweep.

## Spatial indexing

- [STR-packed R-tree](indexing/str-packed-rtree.md) — organise geometry bounding boxes into a packed hierarchy so queries can skip groups that cannot match.

## Spatial statistics

- [Global Moran's I](statistics/global-morans-i.md) — measure global spatial autocorrelation by comparing deviations from the mean across neighbouring units.
- [Geary's C](statistics/gearys-c.md) — measure global spatial autocorrelation through squared differences between neighbouring values.
- [Local Moran's I](statistics/local-morans-i.md) — locate local clusters of similar values and spatial outliers, with conditional permutation inference.
- [Local Geary](statistics/local-geary.md) — measure local similarity and dissimilarity directly between a unit and its neighbours.
- [Getis-Ord Gi*](statistics/getis-ord-gi-star.md) — identify local concentrations of high values (hotspots) and low values (coldspots).

### Supplementary companion method

- [Global Getis-Ord G](statistics/global-getis-ord-g.md) — a supplementary global concentration statistic added to explain the source-listed local Gi* method; it is not a separate entry in the original compendium.

## A connected place to start

The [geometry foundations path](../learning-paths/geometry-foundations.md) connects the first four geometry lessons in a practical sequence, from point location to all-segment intersection. The [spatial autocorrelation path](../learning-paths/global-spatial-autocorrelation.md) connects global and local Moran, Geary and Getis-Ord methods, with six interactive notebooks. The [spatial indexing path](../learning-paths/spatial-indexing.md) starts with bounding boxes and the STR-packed R-tree.

## How to read a record

Start with the practical question, then follow the explanation into the formal definition, method, guarantees, complexity, numerical issues and references. Where a runnable implementation exists, it is linked from the record.

Records may have different evidence and implementation status. Check the status and version before relying on them.
