# Intern walkthrough: single-outlet watershed delineation

## 1. Define the outlet

A pour point is a specific raster cell. The result is not determined by a point coordinate alone: the coordinate must be mapped to a cell, and the cell's location relative to the drainage network matters. This baseline accepts an explicit row/column cell and does not perform snapping.

## 2. Reverse the flow graph

Each valid D8 cell points to at most one downstream neighbour. To find every cell that reaches the outlet, build the reverse adjacency: for each downstream cell, store the upstream cells that point to it.

Starting at the outlet, traverse those reverse links. Every visited cell has a downstream path to the selected outlet.

## 3. Validate the direction graph

A directed cycle is incompatible with a drainage network. The implementation applies Kahn's topological procedure to the complete valid graph before returning a watershed. This prevents a malformed loop elsewhere in the raster from being silently ignored.

## 4. Interpret the mask

The returned boolean raster includes the outlet. Other terminal cells and cells draining beyond the raster or into NoData are excluded unless their flow path reaches the selected outlet.

This is a contributing-area mask under the supplied direction model. It is not a flood extent, a physically simulated inundation area or a guarantee of hydrological connectivity in the real landscape.

## 5. Limitations and validation

The method assumes a valid, conditioned D8 direction grid. Depression filling, flat resolution, outlet snapping, stream burning, raster alignment and NoData policy must be handled and documented upstream.

Tests cover a confluence, a separate sink, NoData/domain exits, invalid outlets, unsupported codes and cycle detection. They test the graph operation, not the quality of the DEM or the suitability of the selected outlet.
