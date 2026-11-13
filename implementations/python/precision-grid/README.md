# Fixed-grid precision operations

This package exposes two Shapely/GEOS operations with an explicit grid size:
coordinate precision reduction and fixed-precision intersection.

## Run

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Example

```python
from shapely.geometry import LineString
from precision_grid import reduce_precision, fixed_precision_intersection

a = LineString([(0.04, 0.04), (1.04, 1.04)])
b = LineString([(0.04, 1.04), (1.04, 0.04)])
print(reduce_precision(a, 0.1))
print(fixed_precision_intersection(a, b, 0.1))
```

## Important distinction

These are fixed-grid operations provided by GEOS. Coordinate precision reduction
is not a complete snap-rounding implementation. The package does not implement
hot-pixel construction, a snap-rounding noder or arrangement-level correctness
proofs. See the [precision models dossier](../../../algorithms/geometry/precision-models.md).

Grid size uses input coordinate units. Choose and record a suitable CRS, grid
spacing, collapse mode and expected treatment of short segments and polygons.
