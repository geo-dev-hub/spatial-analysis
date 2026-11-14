# D8 flow direction: Python example

This small implementation assigns each valid DEM cell to one of its eight downslope neighbours using the ESRI-style direction codes.

## Run it

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Use it

```python
from d8 import flow_direction

dem = [
    [10, 10, 10],
    [10, 10, 8],
    [10, 10, 10],
]
print(flow_direction(dem)[1][1])  # 1: east
```

## Scope

This is a teaching variant. It does not fill depressions, resolve flats, force edge cells outward or reproduce every GIS application's tie rules. It returns 0 where no strictly lower neighbour is available and `None` for NoData cells.

See the [D8 lesson](../../../algorithms/hydrology/d8-flow-direction.md) and [implementation walkthrough](implementation-walkthrough.md).
