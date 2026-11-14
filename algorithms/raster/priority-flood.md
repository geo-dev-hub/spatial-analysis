# Priority-Flood: filling depressions in a digital elevation model

Stable ID: `SA-RASTER-PRIORITY-FLOOD` · Draft 0.1 · Source compendium section 4, page 7

## Why depression filling exists

A digital elevation model may contain local depressions. Some represent real closed basins; others are artefacts from measurement, interpolation or rasterisation. A strict downslope flow-direction algorithm cannot route water out of a pit unless the surface is conditioned or a different sink policy is used.

Priority-Flood raises cells inside depressions to the lowest spill elevation that connects them to the chosen raster boundary.

## The expansion rule

Seed all valid boundary cells in a min-priority queue. Repeatedly remove the lowest frontier cell and inspect its unvisited neighbours. If a neighbour has original elevation $z$ and the current spill level is $h$, set:

$$
z_{filled}=\max(z,h)
$$

A neighbour below the current frontier is raised to that frontier level; a higher neighbour retains its original elevation. The neighbour is then inserted into the priority queue.

The [Python implementation](../../implementations/python/priority-flood/README.md) uses eight-neighbour connectivity. Valid outer-edge cells and valid cells adjacent to NoData are treated as outlet seeds. It returns both the filled DEM and a fill-depth raster:

$$
d_{fill}=z_{filled}-z_{original}
$$

## Algorithm at a glance\n\n~~~mermaid\nflowchart TD\n  A[Seed valid raster edges and NoData neighbours] --> B[Pop lowest frontier cell]\n  B --> C[Visit each unvisited valid neighbour]\n  C --> D{Neighbour below spill level?}\n  D -- Yes --> E[Raise neighbour to spill level]\n  D -- No --> F[Keep original elevation]\n  E --> G[Push neighbour into min-heap]\n  F --> G\n  G --> H{Heap empty?}\n  H -- No --> B\n  H -- Yes --> I[Return filled DEM and fill depth]\n~~~\n\n## Boundary and NoData policy

NoData is not assigned an elevation. It is an invalid barrier. Valid cells adjacent to NoData are treated as boundary seeds in this teaching implementation. That is a deliberate policy: an internal data gap may not be a real hydrological outlet, and a clipped raster boundary may omit upstream terrain.

A real analysis should decide whether to fill to the raster edge, use a larger hydrologically complete DEM, mask internal gaps, or preserve closed basins.

## Filling is not breaching or flat resolution

- **Filling** raises low cells to a spill elevation.
- **Breaching** cuts a channel through a barrier to connect a depression to an outlet.
- **Flat resolution** assigns a routing structure across equal-elevation areas so flow direction can be determined.

These operations are not interchangeable. This implementation performs filling only. It does not resolve the flats that may remain after filling.

## Complexity and validation

With a binary heap, the implementation is O(n log n) time and O(n) memory for n valid cells. It uses a deterministic neighbour order and returns fill depth so the terrain modification is inspectable.

1. Fill a one-cell pit surrounded by higher cells.
2. Compare the lowest spill elevation with the maximum DEM elevation.
3. Add an internal NoData hole. Which valid cells become outlet seeds?
4. Explain why a clipped raster boundary can produce an incorrect basin.
5. Compare filling with breaching and explain when preserving a real closed basin matters.

## References

- Barnes, R., Lehman, C. and Mulla, D. (2014), *Priority-Flood: An optimal depression-filling and watershed-labeling algorithm for digital elevation models*, Computers & Geosciences, 62, 117–127. https://doi.org/10.1016/j.cageo.2013.04.024
- Wang, L. and Liu, H. (2006), *An efficient method for identifying and filling surface depressions in digital elevation models for hydrologic analysis and modelling*, International Journal of Geographical Information Science, 20(2), 193–213. https://doi.org/10.1080/13658810500433453

**Scope:** heap-based eight-neighbour depression filling with explicit raster/NoData boundary seeds; no breaching or flat resolution is included.
