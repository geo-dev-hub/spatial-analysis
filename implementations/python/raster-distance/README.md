# Euclidean raster distance transform

This package computes the centre-to-centre Euclidean distance from every raster cell to the nearest target cell, using SciPy's exact Euclidean distance transform.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
import numpy as np
from raster_distance import distance_to_targets

targets = np.zeros((5, 5), dtype=bool)
targets[2, 2] = True
distance = distance_to_targets(targets, cell_size=(10, 20))
print(distance[2, 3])  # 20 map units
~~~

## Grid contract

- The input is a two-dimensional mask; True marks target cells.
- Cell spacing is `(row_spacing, column_spacing)` in map units.
- Distances are measured between cell centres, not to cell edges.
- At least one target cell is required.
- The output has the same shape and uses floating-point map units.
- The operation is Euclidean and ignores barriers, cost surfaces and connectivity. It is not a least-cost path.
- NoData handling must be designed by the caller. Invalid cells are not automatically excluded from distance measurement.
- This wrapper delegates to SciPy; it does not reimplement the Felzenszwalb–Huttenlocher algorithm.

Read the [canonical lesson](../../../algorithms/raster/euclidean-distance-transform.md) and [intern walkthrough](implementation-walkthrough.md).
