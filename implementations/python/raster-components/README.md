# Raster connected-component labeling

This package labels connected foreground regions in a 2D boolean raster mask using breadth-first search.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Contract

- Foreground is a 2D boolean-like mask.
- Connectivity is either 4-neighbour or 8-neighbour.
- An optional valid mask marks cells included in the analysis; invalid cells are barriers.
- Label zero means background or invalid. Positive labels are assigned in deterministic row-major discovery order.
- The function returns the label raster and a mapping from label to cell count.
- This is a simple BFS baseline; it does not implement run-length/union-find optimizations, distributed labeling or vector polygonization.

Read the [canonical lesson](../../../algorithms/raster/connected-components.md) and [intern walkthrough](implementation-walkthrough.md).
