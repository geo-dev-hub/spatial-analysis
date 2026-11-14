# How the polygon validity example works

This is a library-backed workflow example. Shapely delegates geometric validity and repair operations to GEOS; this code demonstrates how to call those operations responsibly and preserve the source geometry.

## 1. Separate inspection from repair

The inspect_polygon function asks Shapely whether a Polygon or MultiPolygon is valid and requests the diagnostic reason. It also records the geometry type, area and component count.

The function does not change the input. Keeping inspection read-only makes it possible to retain the original feature and its source identifier while deciding what to do next.

## 2. Why record the reason?

A Boolean flag says whether the geometry passes the selected validity model. The reason helps direct the next inspection: self-intersection, a hole outside its shell or a collection-level overlap are different data problems.

Diagnostic wording and the reported location can vary with the underlying GEOS version. The tests therefore check a meaningful substring for the bow-tie case rather than treating the full diagnostic string as a permanent API contract.

## 3. Keep repair explicit

repair_polygon_explicitly calls shapely.make_valid. It does not overwrite the original object or claim that the result is the intended geometry.

A self-crossing ring can be interpreted into multiple polygonal pieces. Other repairs can produce GeometryCollections or lower-dimensional remnants. The caller must inspect:
- output geometry type;
- validity;
- component count;
- area;
- lower-dimensional parts;
- whether the result matches the source's intended meaning.

The repair algorithm is a decision with consequences, not a routine cleanup step.

## 4. Test the cases that matter

The tests include:
- a valid polygon;
- a bow-tie ring;
- a hole outside the shell;
- overlapping MultiPolygon components;
- an empty polygon;
- a non-polygon geometry;
- an explicit repair whose output is checked independently.

The test suite does not assert one universal repaired WKT representation. Geometry engines may differ in component ordering or details while satisfying the same validity contract.

## 5. Reproduce

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

Compare the results with the [polygon validity lesson](../../../algorithms/geometry/polygon-validity.md). For overlay, see the [polygon overlay lesson](../../../algorithms/geometry/overlay-operations.md).
