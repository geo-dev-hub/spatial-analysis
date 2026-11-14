# Single-outlet watershed delineation from a D8 flow grid

Stable ID: `SA-RASTER-WATERSHED-D8` · Draft 0.1 · Source compendium section 4, page 7

## The question

Given a pour point on a drainage network, which raster cells contribute flow to it under the chosen flow-routing model?

A watershed or contributing area is the set of cells whose downstream path reaches the selected outlet. With D8, each valid cell points to at most one neighbour, so the flow network is a directed graph.

## Reverse the network

If cell $u$ flows to cell $v$, write $u\to v$. To delineate the watershed of outlet $o$, traverse the reverse graph from $o$:

$$
W(o)=\{u\mid \text{the directed path from }u\text{ reaches }o\}\cup\{o\}
$$

An implementation can build reverse adjacency lists and perform a depth-first or breadth-first traversal. Every cell is visited at most once, so the traversal is O(n) in the number of valid cells, with O(n) storage.

## Algorithm at a glance\n\n~~~mermaid\nflowchart TD\n  A[Choose valid outlet cell] --> B[Build reverse flow links]\n  B --> C[Push outlet onto traversal stack]\n  C --> D[Visit upstream neighbours]\n  D --> E[Add unseen neighbours to basin]\n  E --> F{Stack empty?}\n  F -- No --> D\n  F -- Yes --> G[Return contributing-area mask]\n~~~\n\n## Direction codes and domain boundaries

The [Python implementation](../../implementations/python/watershed-delineation/README.md) uses ESRI D8 codes: E=1, SE=2, S=4, SW=8, W=16, NW=32, N=64, NE=128, terminal=0 and invalid/NoData=-1.

The outlet must be an in-grid valid cell. A direction that leaves the raster or enters NoData is treated as leaving the valid analysis domain. Cells that drain to another terminal cell are not part of the selected watershed.

The implementation validates the complete direction graph for cycles before returning a mask. A cyclic flow-direction graph has no valid drainage interpretation and is rejected.

## The outlet is a modelling decision

A real pour point may fall between cell centres or on a nearby stream cell. Snapping it to a high-accumulation cell can be useful, but the snapping threshold, search radius and tie policy must be explicit. This teaching baseline deliberately requires the outlet cell to be supplied and does not silently snap.

## Do not confuse the watershed with flood extent

A contributing-area boundary is not an inundation boundary. Flood extent requires additional information such as rainfall/runoff, channel geometry, water levels, hydraulic connectivity and a flood model. A bathtub elevation threshold is not equivalent to hydrodynamic inundation.

## Limitations and exercises

The method does not condition the DEM, fill depressions, resolve flats, derive flow directions, snap outlets or model D-infinity/MFD flow. It assumes an already-prepared D8 direction raster.

1. Trace the watershed of a confluence by hand.
2. Choose a different terminal cell. Which upstream cells leave the original basin?
3. Explain what happens when a flow path leaves the raster.
4. Why should outlet snapping be a separate, documented operation?
5. Explain why this mask is not a flood inundation map.

## References

- Jenson, S. K. and Domingue, J. O. (1988), “Extracting topographic structure from digital elevation data for geographic information system analysis,” *Photogrammetric Engineering & Remote Sensing*, 54(11), 1593–1600. [USGS publication record](https://pubs.usgs.gov/publication/70142175).
- O'Callaghan, J. F. and Mark, D. M. (1984), “The extraction of drainage networks from digital elevation data,” *Computer Vision, Graphics, and Image Processing*, 28(3), 323–344. https://doi.org/10.1016/S0734-189X(84)80011-0.

**Scope:** single-outlet contributing area from an existing acyclic D8 direction raster; no DEM conditioning, outlet snapping or hydraulic flood model is included.
