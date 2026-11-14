# DBSCAN clustering for planar point data

DBSCAN groups points that form density-connected regions. It uses two parameters: a neighbourhood radius eps and a minimum number of points min_samples. Noise points receive label -1.

This implementation uses an explicit pairwise Euclidean distance calculation. It is a transparent O(n²) teaching baseline, not a spatially indexed large-data implementation.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
from dbscan import dbscan

points = [(0, 0), (0.1, 0), (0, 0.1), (5, 5), (5.1, 5)]
labels = dbscan(points, eps=0.2, min_samples=2)
print(labels)
~~~

## Contract and limits

- Input coordinates are planar 2D values in one projected CRS.
- eps uses the same coordinate units as the input.
- min_samples includes the point itself.
- Labels are assigned deterministically by input order. A border point reachable from two clusters is assigned to the first cluster expanded.
- The distance calculation is Euclidean and O(n²) in time and memory.
- This is not HDBSCAN or OPTICS and does not estimate a variable-density hierarchy.
- Standardise or otherwise justify coordinate units and parameter values; do not select eps solely because a plot looks attractive.

Read the [canonical lesson](../../../algorithms/statistics/dbscan.md) and [intern walkthrough](implementation-walkthrough.md).
