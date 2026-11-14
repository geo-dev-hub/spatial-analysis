# Raster cost distance with multi-source Dijkstra

Stable ID: SA-RASTER-COST-DISTANCE · Draft 0.1 · Source compendium section 4, page 6

## The question

Euclidean distance measures straight-line separation. Least-cost distance asks a different question: what is the minimum accumulated cost of moving through a spatially varying surface?

A cost raster assigns each valid cell a non-negative cost per unit distance. High-cost cells are harder to cross; NoData cells are barriers. The answer depends on how the raster is converted into a graph and how edge costs are integrated.

## Raster graph and edge weights

Each valid cell is a node. Four-neighbour or eight-neighbour connectivity defines possible moves. For adjacent cells u and v, this teaching implementation uses:

$$w(u,v)=\frac{c(u)+c(v)}{2}\ell(u,v)$$

where c is cost per horizontal distance unit and ℓ is the physical step length. For diagonal moves on a rectangular grid:

$$\ell_{diag}=\sqrt{\Delta x^2+\Delta y^2}$$

This is a trapezoidal/mean-endpoint approximation to integrating friction along a cell-to-cell segment. Other GIS implementations may use different edge integration conventions.

## Multi-source Dijkstra

Given source set S, the accumulated least cost to cell v is:

$$D(v)=\min_{s\in S}\min_{P:s\leadsto v}\sum_{(u,w)\in P}w(u,w)$$

Dijkstra's algorithm maintains tentative distances in a min-priority queue and repeatedly relaxes edges. Non-negative edge weights are required.

The [Python implementation](../../implementations/python/cost-distance/README.md) supports multiple sources, 4/8 connectivity, rectangular cell spacing and an explicit diagonal corner-cutting rule. It returns infinity for valid cells unreachable from all sources and NaN for NoData.

## What the result means

The output is accumulated cost, not automatically distance or travel time. If c is seconds per metre, the accumulated value has seconds as units. If c is a dimensionless friction multiplier, the output is a weighted distance-like quantity. The cost surface's construction, units and provenance are part of the model.

## Corner and boundary rules

When diagonal movement is enabled, the implementation can prohibit a diagonal move if either adjacent orthogonal cell is blocked. This prevents squeezing through a corner where two barriers touch. Raster boundary cells have no neighbours beyond the grid; they do not wrap around.

## Limitations

- This is a discrete raster graph, not a continuous fast-marching or Eikonal solver.
- The method does not create the cost surface, choose sources, or infer barriers.
- It does not calculate a least-cost path geometry; it calculates accumulated cost.
- It does not implement anisotropic movement, directional turn penalties or a physical travel-time model.
- Results depend on cell resolution, connectivity, cell spacing and edge-cost convention.

## Exercises

1. On a uniform unit-cost grid, compare 4-neighbour and 8-neighbour distances.
2. Increase the cost of a column. Does the cheapest route detour?
3. Introduce a NoData barrier and identify unreachable cells.
4. Compare diagonal corner-cutting policies.
5. Explain why a cost-distance raster is not automatically a travel-time raster.
6. Compare this graph method with fast marching and an Eikonal solver.

## References

- Dijkstra, E. W. (1959), *A note on two problems in connexion with graphs*, Numerische Mathematik, 1, 269–271.
- Tobler, W. (1993), *Three presentations on geographical analysis and modeling*, NCGIA Technical Report 93-1.

**Scope:** multi-source Dijkstra on a regular raster graph with symmetric mean-endpoint edge costs; no continuous Eikonal solver or path geometry.
