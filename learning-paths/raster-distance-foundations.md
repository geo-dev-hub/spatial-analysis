# Raster distance: how far is each cell from a target?

**Status:** First raster distance and flow-direction lessons published; the broader raster, terrain and hydrology path is still being developed.

## The question

You have a raster grid and one or more target cells. You want to know how far every other cell is from the nearest target. This is useful for proximity screening, environmental analysis and image processing.

## Before you begin

You should be comfortable with:
- rows and columns in a two-dimensional array;
- the Pythagorean distance formula;
- the difference between array indices and map coordinates;
- cell size and coordinate reference systems.

## Follow the path

### 1. Mark the target cells

Read [Euclidean distance transform](../algorithms/raster/euclidean-distance-transform.md). True cells represent targets. The transform calculates the shortest straight-line distance between cell centres.

### 2. Account for cell dimensions

Run the [interactive raster lab](../notebooks/raster-distance-transform-lab.ipynb). Compare square cells with a grid whose row and column spacing differ. Predict the diagonal distance before running the code.

### 3. Distinguish distance from travel cost

Euclidean distance ignores barriers and movement costs. A least-cost path answers a different question and needs a cost surface and a movement neighbourhood.

### 4. Decide how NoData should behave

The teaching wrapper does not infer NoData semantics. Decide whether invalid cells should be ignored, masked or treated as barriers before interpreting a real raster.

## 5. Follow terrain downhill with D8

Read [D8 flow direction](../algorithms/raster/d8-flow-direction.md) and run the [interactive lab](../notebooks/d8-flow-direction-lab.ipynb). The method chooses the steepest downslope neighbour among eight adjacent cells. Pay attention to cell dimensions, sinks, flats and NoData. This baseline does not perform depression filling or flow accumulation.

## Exercises

1. Calculate the distance to a target for a cell two rows and three columns away.
2. Repeat with rectangular cell dimensions.
3. Add a second target and explain which one determines the output at a given cell.
4. Explain why a road network or a river channel cannot be represented by this Euclidean transform alone.
5. Write down the CRS, cell size, target definition and NoData policy for a real analysis.
6. Predict the D8 direction for a cell with a diagonal neighbour that has a larger elevation drop but a smaller slope.
7. Explain why a pit needs a separate depression-filling or breaching policy.

## What comes next

The wider source section includes local/focal/zonal map algebra, connected components, cost-distance, least-cost paths, slope and aspect, terrain indices, visibility, depression filling, flow accumulation, watershed delineation and hydrological models, flood analysis and coastal methods. Each needs its own assumptions, tests and learning materials.
