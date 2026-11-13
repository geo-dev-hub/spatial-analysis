# Raster terrain and hydrology foundations: from elevation to contributing area

**Status:** First audited terrain and drainage methods now have tested teaching implementations: Horn slope/aspect, local hillshade, topographic wetness index, D8 direction and accumulation, single-outlet watershed delineation, stream ordering, depression filling, Euclidean distance and raster least-cost distance. Terrain conditioning, channel extraction and alternative flow-routing methods remain open.

## The workflow

A raster terrain workflow has distinct stages. Do not collapse them into a single black-box operation:

1. Inspect the DEM, its coordinate system, vertical units, cell dimensions, alignment and NoData mask.
2. Decide how to handle depressions, flats and boundary cells. A raw DEM may contain both real closed basins and artefacts.
3. Derive local terrain derivatives such as slope and aspect.
4. Derive a flow-direction raster using a declared routing model.
5. Accumulate upstream contributions.
6. Extract a channel network or delineate a watershed only after specifying thresholds and an outlet.

## Before flow direction: condition the DEM

Read [Priority-Flood depression filling](../algorithms/raster/priority-flood.md) and run the [Priority-Flood notebook](../notebooks/priority-flood-lab.ipynb). It raises depressions to their lowest spill level and returns a separate fill-depth layer. The example uses valid raster-edge and NoData-adjacent cells as outlets. Filling is not breaching, and it does not resolve the flats that may remain.

### The stages fit together

~~~mermaid
flowchart TD
  A[Original DEM] --> B[Condition depressions]
  B --> C[Calculate slope and aspect]
  C --> D[Derive D8 flow directions]
  D --> E[Accumulate upstream contributions]
  E --> J[Convert accumulation to specific catchment area]
  C --> K[Calculate topographic wetness index]
  J --> K
  E --> F[Choose a channel-initiation rule]
  F --> G[Build a stream mask]
  G --> H[Calculate stream order]
  D --> I[Select a pour point]
  I --> J[Delineate contributing area]
~~~

The diagram shows dependencies, not a single mandatory software command. Stream thresholds, pour points and conditioning policies are analytical choices.

## 1. Derive terrain slope and aspect

Read [Horn slope and aspect](../algorithms/raster/slope-aspect.md) and run the [slope/aspect notebook](../notebooks/slope-aspect-lab.ipynb). The method estimates local derivatives; D8 routing makes a separate discrete choice of one downstream raster neighbour. The Horn baseline requires a regular projected grid, explicit horizontal spacing and a vertical-unit conversion factor. The same lab derives local hillshade from a selected sun azimuth and altitude; this is illumination, not shadow casting.

## 2. Understand D8 direction

Read [D8 flow direction](../algorithms/raster/d8-flow-direction.md) and run the [direction notebook](../notebooks/d8-flow-direction-lab.ipynb). It chooses the steepest positive slope among eight neighbours, with rectangular cell spacing.

The teaching baseline does not resolve flats or fill depressions. A code of zero can therefore indicate a pit or a flat cell, not necessarily a real hydrological outlet.

## 3. Understand accumulation

Read [D8 flow accumulation](../algorithms/raster/d8-flow-accumulation.md) and run the [accumulation notebook](../notebooks/d8-flow-accumulation-lab.ipynb). It propagates cell counts or supplied weights through an existing D8 direction graph in topological order.

Accumulation includes the cell itself. It is not discharge unless the input contributions and time basis justify that interpretation.

## 4. Calculate a topographic wetness index

Read [Topographic wetness index](../algorithms/raster/topographic-wetness-index.md). It combines supplied specific catchment area and slope. The area input must already be converted to specific catchment area in metres; raw flow-accumulation counts are not interchangeable. A positive slope floor handles flat cells and must be reported.

## 5. Delineate a contributing area

Read [Single-outlet watershed delineation](../algorithms/raster/watershed-delineation.md) and run the [watershed notebook](../notebooks/watershed-delineation-lab.ipynb). It traces upstream cells whose D8 paths reach a selected outlet. The outlet cell is explicit; automatic snapping is deliberately not hidden inside the operation.

## 6. Describe the channel network

Read [Stream ordering](../algorithms/raster/stream-order.md) and run the [stream-order notebook](../notebooks/stream-order-lab.ipynb). It compares Strahler order, which increases only when equal highest-order tributaries meet, with Shreve magnitude, which sums headwater contributions. The stream mask is an explicit input; channel extraction and threshold selection are separate modelling decisions.

## 7. Compare routing assumptions

D8 sends all flow from a cell to one neighbour. D-infinity estimates a continuous direction and distributes flow across adjacent downslope cells. Multiple-flow-direction methods distribute flow among several downslope neighbours according to their gradients.

These methods produce different contributing-area patterns. They are not just different encodings of the same answer.

## 8. Compare Euclidean and least-cost distance

Read [Raster cost distance](../algorithms/raster/cost-distance.md) and run the [cost-distance notebook](../notebooks/cost-distance-lab.ipynb). The method converts a cost surface into a weighted 4/8-neighbour graph and applies multi-source Dijkstra. Its output is accumulated cost under an explicit edge-integration rule, not automatically travel time. This differs from the [Euclidean distance transform](../algorithms/raster/euclidean-distance-transform.md), which measures straight-line distance to a target.

## 9. Choose a raster resampling method

Read [Raster resampling](../algorithms/raster/resampling.md) and run the [resampling notebook](../notebooks/raster-resampling-lab.ipynb). Nearest neighbour preserves class labels; bilinear interpolation estimates continuous values from four neighbours. The teaching example changes array shape over a fixed extent and is not a CRS-aware warp.

## Exercises

1. Create a simple plane and predict the Horn slope, aspect and D8 directions.
2. Make a pit and a flat. Explain why the baseline does not resolve either automatically.
3. Draw a confluence and calculate accumulation by hand.
4. Supply weighted contributions and state their units.
5. Explain how a clipped raster boundary differs from a true basin outlet.
6. Compare Euclidean distance and least-cost distance on a surface with a high-cost barrier.
7. Describe why geographic-coordinate cell areas and distances vary spatially.

## What remains

The wider source section also includes broader local, zonal and global raster algebra, weighted focal filters, sink breaching, flat resolution, D-infinity, multiple-flow direction, channel extraction, curvature and multiscale terrain metrics, additional stream-network metrics, basin delineation, HAND, rainfall-runoff models and hydrodynamic methods. Each needs its own assumptions, validation and reproducible example.
