# Polygon validity: inspect first, repair only by decision

This example uses Shapely 2.1.2 to inspect Polygon and MultiPolygon validity and to demonstrate an explicit repair call. It does not implement the Simple Features validity algorithm itself.

## Run it

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

Example:

~~~python
from shapely import Polygon
from polygon_validity import inspect_polygon, repair_polygon_explicitly

source = Polygon([(0, 0), (4, 4), (0, 4), (4, 0), (0, 0)])
print(inspect_polygon(source))

repaired = repair_polygon_explicitly(source)
print(inspect_polygon(repaired))
~~~

## Important contract

- Input must be a Shapely Polygon or MultiPolygon.
- Inspection does not modify the input.
- The report includes geometry type, validity, reason, area and component count.
- Repair is a separate, explicit call using Shapely's make_valid operation.
- A repair result may be a MultiPolygon or GeometryCollection and may include lower-dimensional components.
- The example does not infer what the source author intended or promise that the repaired geometry preserves that intent.
- Coordinates are treated in the planar model used by Shapely. This example does not transform a CRS or apply a precision grid.

## Validation

Tests cover a valid polygon, a bow-tie self-intersection, a hole outside its shell, overlapping MultiPolygon components, explicit repair, empty polygons and rejected non-polygon input.

The tests assert validity outcomes and stable contract properties. They do not hard-code every diagnostic string or assume all GEOS versions return identical repair component ordering.

## Read next

- [Polygon validity lesson](../../../algorithms/geometry/polygon-validity.md)
- [Implementation walkthrough](implementation-walkthrough.md)
- [Polygon overlay lesson](../../../algorithms/geometry/overlay-operations.md)
