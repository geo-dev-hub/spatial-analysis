# D8 flow accumulation

Flow accumulation counts or sums the upstream contribution reaching each raster cell under an existing D8 flow-direction grid. This package does not derive flow directions from elevations.

By default each valid cell contributes one unit, so the output is the number of upstream cells **including the cell itself**. Optional non-negative weights allow a different contribution per cell, such as rainfall excess or an explicitly chosen source quantity.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
import numpy as np
from d8_flow_accumulation import d8_flow_accumulation

# Each row flows east; the final cell is a sink.
directions = np.array([[1, 1, 0]])
print(d8_flow_accumulation(directions))
# [[1. 2. 3.]]
~~~

## Direction convention

Codes follow the ESRI power-of-two D8 convention used by the companion [D8 flow-direction lesson](../../../algorithms/raster/d8-flow-direction.md): E=1, SE=2, S=4, SW=8, W=16, NW=32, N=64, NE=128. Code 0 is a valid terminal cell; -1 marks invalid/NoData.

## Contract and limits

- Input is a 2D integer direction grid containing only -1, 0, 1, 2, 4, 8, 16, 32, 64 or 128.
- The accumulation at a cell includes its own contribution.
- A direction that exits the raster or points into an invalid cell is treated as flow leaving the valid domain; it is not propagated into NoData.
- Invalid cells have output NaN and contribute nothing.
- A cycle in the flow graph raises ValueError rather than returning a partial accumulation.
- The routine detects cycles and accumulates in O(n) time and O(n) auxiliary memory for n valid cells.
- It assumes the supplied D8 graph is the intended flow network. It does not fill depressions, resolve flats, enforce hydrological conditioning or calculate a watershed boundary.

Read the [canonical lesson](../../../algorithms/raster/d8-flow-accumulation.md) and [intern walkthrough](implementation-walkthrough.md).
