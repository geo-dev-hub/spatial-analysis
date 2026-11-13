# Polygon offsetting example

This package wraps Shapely/GEOS buffer operations for valid planar Polygon and MultiPolygon inputs. It exposes distance, join style, miter limit and round-arc resolution.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
from shapely.geometry import Polygon
from offsetting import offset_polygon

parcel = Polygon([(0, 0), (20, 0), (20, 10), (0, 10)])
expanded = offset_polygon(parcel, 2, join_style="round")
contracted = offset_polygon(parcel, -1, join_style="mitre")
print(expanded.area, contracted.area)
~~~

Coordinates must use a planar CRS appropriate to the intended distance. A positive distance expands polygon exteriors; a negative distance contracts them. Holes change in the opposite direction.

## Important distinction

This is not a Python binding to Clipper2. It demonstrates GEOS buffer semantics. Clipper2 has its own integer-path, join, end-type, miter-limit and output-tree contracts. See the algorithm dossier before comparing results.
