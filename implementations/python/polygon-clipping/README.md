# Sutherland–Hodgman clipping for convex polygons

A dependency-free teaching implementation of polygon intersection.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Input and output contract

- Both inputs must be simple, non-degenerate **convex** polygon rings.
- Coordinates must use one planar coordinate system and consistent units.
- Clockwise and counter-clockwise inputs are accepted; output is counter-clockwise.
- The intersection is represented by one polygon ring.
- Point-only and shared-edge-only contacts return an empty list: this API models area output, not point or line intersections.
- Holes, MultiPolygons, self-intersections, geodesic coordinates and general concave overlay are outside scope.
- Epsilon is scale-dependent; it is not a CRS transformation or universal precision setting.

Both inputs are required to be convex so the result is connected and representable by one ring. The validation is intentional: it prevents a narrow teaching API from silently claiming general overlay support.

## Example

~~~python
from polygon_clipping import clip_convex_polygon

parcel = [(0, 0), (6, 0), (6, 4), (0, 4)]
project_area = [(2, -1), (5, -1), (5, 5), (2, 5)]
print(clip_convex_polygon(parcel, project_area))
~~~

Expected ring: (2, 0), (5, 0), (5, 4), (2, 4).

## Read next

- [Algorithm lesson](../../../algorithms/geometry/polygon-clipping.md)
- [Implementation walkthrough](implementation-walkthrough.md)
- [General overlay lesson](../../../algorithms/geometry/overlay-operations.md)
