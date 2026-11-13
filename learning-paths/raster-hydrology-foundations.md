# Raster hydrology foundations: from elevation to contributing area

**Status:** D8 flow direction, accumulation and single-outlet watershed delineation now have tested teaching implementations; terrain conditioning, stream extraction and alternative flow-routing methods remain open.

## The workflow

A basic raster drainage workflow has several distinct stages. Do not collapse them into a single black-box operation:

1. Inspect the DEM, its coordinate system, vertical units, cell dimensions, alignment and NoData mask.
2. Decide how to handle depressions, flats and boundary cells. A raw DEM may contain both real closed basins and artefacts.
3. Derive a flow-direction raster using a declared routing model.
4. Accumulate upstream contributions.
5. Extract a channel network or delineate a watershed only after specifying the relevant thresholds and outlet.

## 1. Understand D8 direction

Read [D8 flow direction](../algorithms/raster/d8-flow-direction.md) and run the [direction notebook](../notebooks/d8-flow-direction-lab.ipynb). It chooses the steepest positive slope among eight neighbours, with rectangular cell spacing.

The teaching baseline does not resolve flats or fill depressions. A code of zero can therefore indicate a pit or a flat cell, not necessarily a real hydrological outlet.

## 2. Understand accumulation

Read [D8 flow accumulation](../algorithms/raster/d8-flow-accumulation.md) and run the [accumulation notebook](../notebooks/d8-flow-accumulation-lab.ipynb). It propagates cell counts or supplied weights through an existing D8 direction graph in topological order.

Accumulation includes the cell itself. It is not discharge unless the input contributions and time basis justify that interpretation.

## 3. Delineate a contributing area

Read [Single-outlet watershed delineation](../algorithms/raster/watershed-delineation.md) and run the [watershed notebook](../notebooks/watershed-delineation-lab.ipynb). It traces upstream cells whose D8 paths reach a selected outlet. The outlet cell is explicit; automatic snapping is deliberately not hidden inside the operation.

## 4. Describe the channel network

Read [Stream ordering](../algorithms/raster/stream-order.md) and run the [stream-order notebook](../notebooks/stream-order-lab.ipynb). It compares Strahler order, which increases only when equal highest-order tributaries meet, with Shreve magnitude, which sums headwater contributions. The stream mask is an explicit input; channel extraction and threshold selection are separate modelling decisions.

## 5. Compare routing assumptions

D8 sends all flow from a cell to one neighbour. D-infinity estimates a continuous direction and distributes flow across adjacent downslope cells. Multiple-flow-direction methods distribute flow among several downslope neighbours according to their gradients.

These methods produce different contributing-area patterns. They are not just different encodings of the same answer.

## Exercises

1. Create a simple plane and predict the D8 directions.
2. Make a pit and a flat. Explain why the baseline leaves both unresolved.
3. Draw a confluence and calculate accumulation by hand.
4. Supply weighted contributions and state their units.
5. Explain how a clipped raster boundary differs from a true basin outlet.
6. Describe why geographic-coordinate cell areas vary spatially.

## What remains

The wider source section includes priority-flood depression filling, sink breaching, D-infinity, multiple-flow direction, flow accumulation, stream ordering, watershed and basin delineation, HAND, topographic wetness, rainfall-runoff models and hydrodynamic methods. Each needs its own assumptions, validation and reproducible example.
