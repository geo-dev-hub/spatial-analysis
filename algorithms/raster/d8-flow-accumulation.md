# D8 flow accumulation: how much upstream area reaches each cell?

Stable ID: `SA-RASTER-D8-FLOW-ACCUMULATION` · Draft 0.1 · Source compendium section 4, page 7

## The hydrology question

A flow-direction raster says where each cell sends its flow. Flow accumulation answers the next question: how many upstream cells, or how much upstream contribution, reaches each cell?

The [D8 flow-direction lesson](d8-flow-direction.md) assigns each cell to one of its eight neighbours. Given that direction grid, accumulation propagates each cell's contribution downstream.

## The recurrence

Let $w_i$ be the contribution generated at cell $i$. With an unweighted cell-count interpretation, $w_i=1$. The accumulation includes the cell itself:

$$
A_i=w_i+\sum_{j\to i}A_j
$$

The summation includes every immediate upstream cell $j$ whose D8 direction points to $i$. For an unweighted raster, the result is the number of contributing cells including the current cell. If the cell represents a regular projected grid with area $a$, multiplying the count by $a$ gives contributing area under that grid-cell interpretation. For a geographic grid, cell area varies with latitude and should not be treated as constant.

## Why processing order matters

An upstream cell must contribute before its downstream cell is finalised. The D8 graph is a directed graph with at most one outgoing edge per valid cell. If the direction raster is acyclic, a topological ordering exists.

The teaching implementation uses Kahn's algorithm:
1. Count the number of incoming flow edges (indegree) for each cell.
2. Queue valid cells with indegree zero.
3. Remove a queued cell, add its accumulated value to its downstream neighbour and decrement that neighbour's indegree.
4. Queue the neighbour once all its upstream cells have been processed.
5. If not all valid cells were processed, a directed cycle exists and the input is rejected.

This is linear in the number of valid cells:

$$
T(n)=O(n),\qquad S(n)=O(n)
$$

## Boundary and NoData policy

The [Python implementation](../../implementations/python/d8-flow-accumulation/README.md) uses the same ESRI power-of-two D8 codes as the direction lesson. Code 0 is a valid terminal cell; -1 marks invalid/NoData.

A direction that points beyond the raster or into a NoData cell is treated as leaving the valid analysis domain. The accumulation is not propagated into invalid cells. This is a declared boundary convention, not a universal hydrological rule. For a study area, the analyst must decide whether the raster boundary is a true outlet, a clipped portion of a larger basin or a data gap.

## Weighted accumulation

The input can optionally provide a non-negative contribution $w_i$ for each valid cell. This can represent a chosen source quantity such as rainfall excess, but the units and physical meaning must be explicit. The output then sums those contributions, not simply the number of cells.

## Important limitations

- D8 sends all flow from a cell to exactly one neighbour; it does not split flow across multiple directions.
- The implementation does not derive flow directions from elevation.
- It does not fill depressions, resolve flats, breach sinks or enforce hydrological conditioning.
- It does not delineate watershed boundaries or extract a stream network.
- Flow accumulation is not discharge unless the input contribution and time basis support that interpretation.
- A cycle indicates an invalid or unexpected direction graph and raises an error.

## Exercises

1. Predict the accumulation along a one-row grid that drains east.
2. Draw a confluence and calculate the contributing-cell count by hand.
3. Supply nonuniform weights. How does the output differ from cell count?
4. Make a direction point outside the raster. Explain the boundary convention.
5. Create a two-cell loop and explain why no valid topological order exists.
6. Explain why multiplying a count by one constant cell area can be wrong for a geographic-coordinate raster.

## References

- O'Callaghan, J. F. and Mark, D. M. (1984), *The extraction of drainage networks from digital elevation data*, Computer Vision, Graphics, and Image Processing, 28(3), 323–344.
- Jenson, S. K. and Domingue, J. O. (1988), *Extracting topographic structure from digital elevation data for geographic information system analysis*, Photogrammetric Engineering & Remote Sensing, 54(11), 1593–1600.

**Scope:** accumulation on an existing acyclic D8 direction raster; no DEM conditioning, alternative flow-routing model or watershed delineation is included.
