# How the polygon-intersection example works

This example deliberately uses Shapely rather than reimplementing a production polygon overlay engine. Shapely delegates the geometric operation to GEOS. The purpose here is to make the API contract and the important decisions visible.

## 1. Import the geometry API

`intersection_demo.py` imports Shapely and its `Polygon` type. The function accepts two planar Shapely geometries and returns their point-set intersection.

The return type is not forced to Polygon. Depending on the inputs, an intersection can be a polygon, line, point, collection or empty geometry.

## 2. Reject missing inputs

The function checks for `None` before calling the geometry engine. A missing geometry is a data problem, not an empty intersection.

This keeps two different situations separate:
- no geometry was supplied;
- two valid geometries were supplied but do not overlap.

## 3. Reject invalid geometries

The example checks `is_valid` for both inputs. It does not silently repair invalid polygons.

Geometry repair is a separate operation with its own choices. A repair can change the geometry, so it should be explicit and recorded.

## 4. Call the overlay operation

The central line is:

```python
return shapely.intersection(first, second, grid_size=grid_size)
```

This calls the GEOS-backed intersection operation. The optional `grid_size` controls precision snapping for the operation. It is not a universal fix for invalid topology, and choosing a grid size changes the precision model.

## 5. Build the worked example

The example creates two axis-aligned boxes:
- the first covers coordinates from 0 to 4 in both dimensions;
- the second overlaps part of the first.

It calls the same public function used by the tests and returns the two inputs and the shared geometry.

## 6. Inspect the result

The command-line example prints:
- the Shapely version;
- the input geometries as WKT;
- the intersection as WKT;
- the resulting geometry type;
- the result area.

Inspecting the geometry type is important. An intersection operation returns the actual set-theoretic result, not necessarily a polygon.

## 7. What the tests check

The tests cover overlapping polygons, disjoint polygons, edge-only contact, point-only contact, invalid geometry, missing inputs and the optional precision grid.

They verify the behaviour of the wrapper and the geometry engine. They do not reimplement or independently prove the full GEOS overlay algorithm.

## 8. What this example does not do

- It does not choose or transform a CRS.
- It does not repair invalid geometries.
- It does not implement overlay noding or topology graphs.
- It does not guarantee that a chosen precision grid is appropriate.
- It does not turn a geometry intersection into a spatial join.

Read the [polygon intersection lesson](../../../algorithms/geometry/polygon-intersection.md) for the conceptual overlay pipeline, then run the [interactive geometry notebook](../../../notebooks/README.md) as additional examples are added.

## Reproduce

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```
