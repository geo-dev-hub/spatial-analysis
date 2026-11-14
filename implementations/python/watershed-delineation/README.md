# Single-outlet watershed delineation from a D8 grid

A watershed (contributing area) for a pour point is the set of valid raster cells whose downstream D8 path reaches that outlet.

This teaching implementation takes an existing direction raster and a row/column outlet. It traces the flow network upstream from the outlet. It does not derive flow directions, snap an outlet to a stream, or condition the DEM.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
from watershed_delineation import delineate_watershed

directions = [
    [-1, 4, -1],
    [-1, 1, -1],
    [-1, 64, -1],
]
mask = delineate_watershed(directions, outlet=(1, 1))
~~~

## Contract and limitations

- Direction codes follow the ESRI D8 convention: E=1, SE=2, S=4, SW=8, W=16, NW=32, N=64, NE=128, terminal=0, invalid=-1.
- The outlet must be an in-grid valid cell.
- The returned boolean mask includes the outlet and all valid cells whose directed path reaches it.
- Flow leaving the raster or entering NoData does not contribute to an in-grid outlet.
- The complete valid direction graph must be acyclic; cycles are rejected.
- A cell with code 0 is a terminal cell. If it is not the chosen outlet and has no path to it, it is outside the returned watershed.
- The result depends on the supplied routing grid, DEM conditioning, grid alignment and outlet placement.
- This is a single-outlet D8 delineation, not a hydrodynamic basin model or a multi-flow-direction algorithm.

Read the [canonical lesson](../../../algorithms/raster/watershed-delineation.md) and [intern walkthrough](implementation-walkthrough.md).
