# Indexed spatial join with Shapely

This example joins two geometry collections using Shapely 2.x's STRtree. The tree is built over the right-hand collection, and each left-hand geometry is queried against it.

The function returns pairs of original input indices:

`(left_index, right_index)`

## Run it

```bash
python -m pip install -r requirements.txt
python - <<'PY'
from shapely import box
from shapely.geometry import Point
from spatial_join import spatial_join

points = [Point(0.5, 0.5), Point(3, 3)]
areas = [box(0, 0, 1, 1), box(2, 2, 4, 4)]

print(spatial_join(points, areas, predicate="within"))
PY
```

Expected output:

```text
[(0, 0), (1, 1)]
```

## Run the tests

```bash
python -m pytest -q
```

The ten tests cover point-in-polygon joins, boundary behaviour, one-to-many matches, predicate direction, empty geometries, polygons with holes and comparison against a brute-force join.

## How the indexed join works

1. Build an STRtree over the right-hand geometries.
2. Query it with the left-hand geometries.
3. Use bounding boxes to discard pairs that cannot match.
4. Apply the exact predicate to the remaining candidates.
5. Return the original left and right indices.

Shapely performs the bounding-box filtering and exact predicate refinement when a predicate is passed to `STRtree.query()`.

## Predicate direction matters

Shapely evaluates the predicate as:

`predicate(input_geometry, tree_geometry)`

The left-hand input geometries are the first argument. The right-hand geometries stored in the tree are the second argument.

For points on polygons:
- `within` tests point-within-polygon;
- `intersects` also includes points on the polygon boundary;
- `contains` would test the reverse direction if the input and tree roles were swapped.

## Limits

- This example uses Shapely 2.x, whose STRtree query returns integer index pairs.
- It returns index pairs, not a GeoDataFrame or joined attribute table.
- The caller is responsible for keeping geometries and their associated records in the same order.
- The example performs a planar 2D operation. CRS, units and geometry validity still matter.
- For large datasets, benchmark the actual workload and compare the index selectivity with a brute-force baseline.

Continue with the [filter-and-refine spatial join lesson](../../../algorithms/query-processing/filter-refine-spatial-join.md), the [STR-packed R-tree lesson](../../../algorithms/indexing/str-packed-rtree.md) and the [interactive notebook](../../../notebooks/filter-refine-spatial-join-lab.ipynb).
