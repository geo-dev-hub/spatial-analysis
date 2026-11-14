# Polygon overlay operations with Shapely

This package demonstrates four Boolean operations on valid polygonal inputs. Shapely delegates geometric construction to GEOS; this package is not a from-scratch overlay engine.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
python overlay_demo.py
~~~

## Contract

- Inputs must be non-empty, valid Polygon or MultiPolygon geometries.
- Both geometries must use the same planar coordinate space and compatible units.
- Operations: intersection, union, difference (A minus B), and symmetric difference.
- Output type and dimension are inspected, not guessed. An intersection may be a polygon, line, point, geometry collection or empty depending on topology and engine semantics.
- Holes and multipart polygon inputs are supported by Shapely/GEOS.
- Invalid input is rejected, not silently repaired.
- A null precision grid uses floating precision. A non-negative grid size requests precision reduction for the operation, in coordinate units; it can move coordinates or collapse small features.
- This is planar computation. Project geographic coordinates before interpreting area or distance in ground units.

## Example

~~~python
from shapely import Polygon
from polygon_overlay import overlay

a = Polygon([(0, 0), (4, 0), (4, 3), (0, 3)])
b = Polygon([(2, -1), (5, -1), (5, 2), (2, 2)])
for operation in ("intersection", "union", "difference", "symmetric_difference"):
    result = overlay(a, b, operation)
    print(operation, result.geom_type, result.area)
~~~

Expected areas: intersection 4, union 17, difference 8, symmetric difference 13 square coordinate units.

## What the tests teach

The suite checks area identities, disjoint multipart union, empty intersection, containment creating a hole, edge-only and point-only contact, polygon holes, MultiPolygon input, invalid-input rejection, unsupported geometry rejection, invalid precision grids and result reporting.

## Read next

- [Overlay algorithm lesson](../../../algorithms/geometry/overlay-operations.md)
- [Implementation walkthrough](implementation-walkthrough.md)
- [Polygon validity workflow](../polygon-validity/README.md)
- [Convex polygon clipping](../polygon-clipping/README.md)
