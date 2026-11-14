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
- [Polygon coverage simplification](geometry/coverage-simplification.md) — preserve shared boundaries when simplifying an edge-matched polygon coverage.
- [Precision models and snap rounding](geometry/precision-models.md) — distinguish coordinate precision reduction, fixed-grid overlay and snap-rounding noding.
- [Snap rounding noder](geometry/snap-rounding.md) — understand hot pixels, exact arrangement vertices and fixed-grid rerouting, with a tested teaching baseline.
- [Polygon offsetting](geometry/offsetting.md) — distinguish geometric offsets from clipping and compare join, cap and precision behaviour.
- [Proximity graphs](geometry/proximity-graphs.md) — compare Gabriel, relative-neighbourhood and Euclidean minimum-spanning graphs.
- [Planar point location](geometry/point-location.md) — understand slab decompositions and randomized trapezoidal maps, with a tested restricted static slab locator.

## Optimization and location science

- [The p-median problem](optimization/p-median.md) — choose a fixed number of candidate facilities to minimise weighted assignment cost.
- [Capacitated p-median](optimization/capacitated-p-median.md) — minimise assignment cost while respecting finite facility capacities and indivisible demand.
- [Accessibility equity diagnostics](optimization/accessibility-equity.md) — inspect population-weighted accessibility distributions, lower-tail outcomes and group gaps without treating one metric as a fairness verdict.
- [Equity-constrained maximal covering](optimization/equity-constrained-covering.md) — maximise covered demand while enforcing explicit minimum coverage shares for caller-defined groups.
- [Two-step floating catchment area](optimization/two-step-fca.md) — estimate potential service accessibility by combining provider supply and population demand within travel catchments.

## Remote sensing

- [Normalised Difference Vegetation Index (NDVI)](remote-sensing/ndvi.md) — calculate a red/NIR spectral contrast while preserving invalid pixels and preprocessing caveats.

## Raster operations

- [Euclidean distance transform](raster/euclidean-distance-transform.md) — calculate centre-to-centre distance from every grid cell to the nearest target cell.
- [Focal raster statistics](raster/focal-statistics.md) — calculate NoData-aware square-window means efficiently using integral images.
- [Priority-Flood](raster/priority-flood.md) — fill DEM depressions to their lowest spill elevation and inspect the fill-depth surface.
- [D8 flow direction](raster/d8-flow-direction.md) — assign each DEM cell to its steepest downslope neighbour.
- [D8 flow accumulation](raster/d8-flow-accumulation.md) — propagate upstream cell counts or weighted contributions through an existing D8 direction grid.
- [Watershed delineation](raster/watershed-delineation.md) — trace the contributing area of a selected outlet through a D8 flow network.
- [Stream ordering](raster/stream-order.md) — compare Strahler order and Shreve magnitude on a connected D8 channel network.

## Geostatistics

- [Spatial interpolation](geostatistics/interpolation.md) — compare inverse-distance weighting with ordinary kriging, a variogram model and conditional prediction variance.

## Networks and routing

- [Shortest paths](networks/shortest-paths.md) — understand graph cost models and shortest-path families, with tested Dijkstra, A*, bidirectional Dijkstra and ALT baselines.
- [Turn-aware and time-dependent routing](networks/turn-aware-time-dependent-routing.md) — model prohibited turns, turn penalties and FIFO travel-time functions, with tested edge-based and earliest-arrival examples.

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

- [Ripley's K and L](statistics/ripley-k.md) — compare uncorrected pair-count summaries with the homogeneous Poisson reference across distance scales.
- [Clark–Evans nearest-neighbour index](statistics/clark-evans.md) — compare observed mean nearest-neighbour spacing with a homogeneous Poisson reference.
- [Kernel density estimation for point patterns](statistics/point-pattern-kde.md) — estimate a fixed-bandwidth planar Gaussian intensity surface and understand bandwidth and edge effects.


- [DBSCAN](statistics/dbscan.md) — identify density-connected clusters and noise in planar point data.


- [Global Moran's I](statistics/global-morans-i.md) — measure global spatial autocorrelation by comparing deviations from the mean across neighbouring units.
- [Geary's C](statistics/gearys-c.md) — measure global spatial autocorrelation through squared differences between neighbouring values.
- [Local Moran's I](statistics/local-morans-i.md) — locate local clusters of similar values and spatial outliers, with conditional permutation inference.
- [Local Geary](statistics/local-geary.md) *(supplementary)* — measure local similarity and dissimilarity directly between a unit and its neighbours.
- [Getis-Ord Gi*](statistics/getis-ord-gi-star.md) — identify local concentrations of high values (hotspots) and low values (coldspots).

### Supplementary companion method

- [Global Getis-Ord G](statistics/global-getis-ord-g.md) — a supplementary global concentration statistic added to explain the source-listed local Gi* method; it is not a separate entry in the original compendium.

## Raster and terrain analysis

- [Focal raster statistics](raster/focal-statistics.md) — calculate NoData-aware neighbourhood summaries.
- [Priority-Flood](raster/priority-flood.md) — fill DEM depressions to their lowest spill elevation.
- [Euclidean distance transform](raster/euclidean-distance-transform.md) — calculate centre-to-centre distance on a regular raster grid.
- [D8 flow direction](raster/d8-flow-direction.md) — assign each cell to its steepest downslope neighbour.
- [D8 flow accumulation](raster/d8-flow-accumulation.md) — propagate upstream contributions through a D8 grid.
- [Watershed delineation](raster/watershed-delineation.md) — trace cells draining to a selected outlet.
- [Stream ordering](raster/stream-order.md) — compare Strahler order and Shreve magnitude.
- [Terrain slope and aspect](raster/slope-aspect.md) — estimate local derivatives with Horn's 3×3 operator.
- [Local hillshade](raster/hillshade.md) — derive normalized illumination from slope, aspect and a declared sun position.
- [Topographic wetness index](raster/topographic-wetness-index.md) — combine specific catchment area and slope into a relative terrain index.
- [Raster resampling](raster/resampling.md) — compare nearest-neighbour and bilinear interpolation, including NoData policies.
- [Zonal statistics](raster/zonal-statistics.md) — summarize aligned raster values by integer zone labels.
- [Connected-component labeling](raster/connected-components.md) — identify connected foreground regions under 4/8-neighbour rules.
- [Raster cost distance](raster/cost-distance.md) — calculate multi-source least accumulated cost through a weighted raster graph.

## Geodesy and coordinate systems

- [Coordinate transformation and CRS axis order](geodesy/crs-transformation.md) — transform point coordinates with explicit longitude/latitude and x/y conventions.

## GeoAI

- [Contrastive representation learning with NT-Xent](geoai/contrastive-info-nce.md) — derive a self-supervised objective and examine geospatial positive-pair design.

## A connected place to start

The [geometry foundations path](../learning-paths/geometry-foundations.md) connects the first four geometry lessons and continues into validity, clipping and overlay. The [Core GIS continuation path](../learning-paths/core-gis-continuation.md) adds simplification, offsetting, proximity graphs and point location; [network routing foundations](../learning-paths/network-routing-foundations.md) connects graph models with shortest-path methods. The [spatial indexing path](../learning-paths/spatial-indexing.md) connects the packed R-tree, spatial joins, quadtree and k-d tree, with a new selection guide to help match an index to a workload. The [spatial autocorrelation path](../learning-paths/global-spatial-autocorrelation.md) connects global and local Moran, Geary and Getis-Ord methods, with six interactive notebooks. The [spatial indexing path](../learning-paths/spatial-indexing.md) starts with bounding boxes and the STR-packed R-tree.

## How to read a record

Start with the practical question, then follow the explanation into the formal definition, method, guarantees, complexity, numerical issues and references. Where a runnable implementation exists, it is linked from the record.

Records may have different evidence and implementation status. Check the status and version before relying on them.

- [Ear clipping](geometry/ear-clipping.md) — triangulate one simple polygon ring, with a tested exact-predicate teaching baseline.

- [Convex decomposition](geometry/convex-decomposition.md) — compare triangulation-based merging, optimal partitioning and approximate convex decomposition.

- [Minkowski sums](geometry/minkowski-sum.md) — combine geometric sets through pointwise addition and apply the result to offsets and collision planning.

- [Medial axis](geometry/medial-axis.md) — represent a region through centres of maximal inscribed discs.
- [Straight skeleton](geometry/straight-skeleton.md) — construct the polygon skeleton from inward parallel wavefronts.

- [Convex Minkowski-sum implementation](../implementations/python/minkowski-convex/README.md) — a tested linear-time edge merge for convex rings.

- [Convex decomposition implementation](../implementations/python/convex-decomposition/README.md) — a tested greedy triangulate-and-merge teaching baseline.

- [Delaunay-filtered proximity graphs](../implementations/python/proximity-graphs/README.md) — compare sparse candidate filtering with all-pairs reference methods.


### Geodesy

- [Geodetic, ECEF and local ENU coordinates](geodesy/ecef-enu.md) — move between ellipsoidal longitude/latitude/height, Earth-centred Cartesian coordinates and a local East-North-Up frame.

- [Maximal covering location](optimization/maximal-covering.md) — choose at most p facilities to maximize demand reached within a defined service threshold.

- [Discrete p-center](optimization/p-center.md) — minimize the maximum nearest-facility cost when exactly p candidate sites must open.

- [Inverse distance weighting](interpolation/inverse-distance-weighting.md) — estimate values at unsampled locations with normalized inverse-distance weights and explicit neighbourhood choices.

- [Location set covering](optimization/set-covering.md) — minimize the number of facilities needed to reach every demand location within a service threshold.
