# D8 flow direction on a raster DEM

The D8 method assigns each valid raster cell to the steepest downslope neighbour among its eight adjacent cells. Direction codes follow the ESRI power-of-two convention:

| Direction | Code |
|---|---:|
| East | 1 |
| South-east | 2 |
| South | 4 |
| South-west | 8 |
| West | 16 |
| North-west | 32 |
| North | 64 |
| North-east | 128 |

The implementation uses strict downslope movement. A valid cell with no lower valid neighbour is coded 0 (sink/flat); an invalid or NoData cell is coded -1.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
import numpy as np
from d8_flow import d8_flow_direction

dem = np.array([[9, 8, 7], [8, 7, 6], [7, 6, 5]], dtype=float)
directions = d8_flow_direction(dem, cell_size=(10, 20))
~~~

## Contract and limits

- The DEM is a two-dimensional elevation grid.
- Cell size is supplied as (row spacing, column spacing), in horizontal map units; elevations must use compatible vertical units.
- The selected neighbour maximises elevation drop divided by centre-to-centre distance.
- Ties follow the documented direction iteration order.
- Flat areas and pits are not resolved or breached; they receive code 0 if no strictly lower neighbour exists.
- Invalid cells receive -1 and are not considered as neighbours.
- This is D8 flow direction only. It does not calculate flow accumulation, stream networks, watershed boundaries or depression filling.
- The algorithm is sensitive to grid resolution, DEM noise and the selected treatment of flats and sinks.

Read the [canonical lesson](../../../algorithms/raster/d8-flow-direction.md) and [intern walkthrough](implementation-walkthrough.md).
