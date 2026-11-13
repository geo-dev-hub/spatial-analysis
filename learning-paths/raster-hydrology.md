# From an elevation raster to a drainage network

A digital elevation model describes the shape of the land. This path follows the steps that turn those elevations into a picture of where water may travel.

## The route through the subject

1. **Start with the terrain.** Understand raster cells, resolution, alignment, NoData and elevation units. A DEM foundations lesson is planned.
2. **Choose a downhill neighbour.** [D8 flow direction](../algorithms/hydrology/d8-flow-direction.md) explains how each cell selects its steepest downslope neighbour. It includes a tested teaching implementation and an interactive lab. **Available**
3. **Deal with pits and flats.** Learn when depressions are real, when they are artefacts and how conditioning methods change the surface. These lessons are planned.
4. **Count the contributing area.** Flow accumulation uses the direction network to count or weight the cells draining through each location. A lesson is planned.
5. **Trace a catchment.** Watershed delineation connects a pour point to the upstream area that drains to it. A lesson is planned.
6. **Compare flow models.** MFD and D-infinity distribute flow differently from D8. Their assumptions and outputs should be compared on the same DEM.

## Before using a result

Check the DEM source, horizontal and vertical units, cell size, projection, NoData edges and depression treatment. A flow-direction raster is not automatically a verified drainage network.

The path is being built. Only lessons explicitly marked available should be treated as completed material.
