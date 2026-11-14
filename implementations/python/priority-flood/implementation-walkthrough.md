# Intern walkthrough: Priority-Flood depression filling

## 1. Why condition a DEM?

A flow-direction algorithm needs a rule for depressions and flats. A DEM may contain pits caused by measurement noise, interpolation or genuine closed basins. If every pit is left untouched, a strict downslope method can terminate flow there.

Priority-Flood raises depressions to their lowest spill level. It does not decide whether every depression is an error; that is a modelling decision.

## 2. Seed the valid boundary

The algorithm begins with all valid outer-edge cells and all valid cells adjacent to NoData. These cells define where the raster can drain out under this implementation's boundary policy.

NoData is not treated as a low elevation. It is an invalid barrier, and its valid neighbours become boundary seeds. This policy must be reconsidered for clipped rasters and internal data gaps.

## 3. Expand from the lowest frontier

A min-heap stores the current lowest frontier elevation. The algorithm repeatedly removes the lowest cell and visits each unvisited valid neighbour.

For a neighbour with original elevation $z$, and current spill level $h$, the filled elevation is:

$$
z_{filled}=\max(z,h)
$$

If the neighbour is lower than the frontier, it is raised to the frontier level. Otherwise it keeps its original elevation. It is then added to the heap.

## 4. Return both elevation and fill depth

The fill depth is:

$$
d_{fill}=z_{filled}-z_{original}
$$

Keeping this layer matters: a filled DEM alone hides where and by how much the terrain was changed.

## 5. Complexity and limits

Each valid cell enters the heap once and each of its eight neighbours is examined a bounded number of times. Heap operations give O(n log n) time and O(n) memory.

This implementation fills depressions. It does not breach barriers, distinguish real closed basins from artefacts, resolve flats or guarantee that a subsequent flow-direction algorithm has a unique downhill path across a filled plateau.

## 6. Validate the result

Inspect the fill-depth raster, compare known sinks and outlets, and test the boundary policy. Do not use a filled DEM without preserving the original surface and recording the conditioning operation.
