# Implementation walkthrough: polygon overlay

## 1. Separate the mathematical operation from the engine

Set theory defines what should be retained:

$$
A\cap B,\quad A\cup B,\quad A\setminus B,\quad
A\triangle B=(A\setminus B)\cup(B\setminus A)
$$

Those definitions do not specify how to node edges, resolve near-coincident intersections, assemble rings or represent lower-dimensional results. Shapely exposes these operations and delegates construction to GEOS.

## 2. Validate before overlay

The wrapper accepts non-empty Polygon and MultiPolygon inputs only. It checks validity before calling the engine. This avoids silently changing invalid geometry during an operation.

Repair is a separate decision. Use the polygon-validity workflow to inspect the reason, create a repaired candidate explicitly, inspect its new geometry type and dimension, and decide whether the changed geometry is acceptable.

## 3. Choose the operation

| Operation | Meaning | What remains |
|---|---|---|
| Intersection | A and B | shared part |
| Union | A or B | both exclusive parts plus shared |
| Difference | A but not B | A-only |
| Symmetric difference | in A or B, not both | A-only plus B-only |

The order of difference matters: A minus B is not generally equal to B minus A.

## 4. Do not assume the output is a polygon

An edge-touch intersection can be a LineString. A point-touch intersection can be a Point. Disjoint polygon intersection is empty. A union of separated polygons can be a MultiPolygon. A difference can create interior rings.

The describe_result helper records actual geometry type, emptiness, validity, area, length and component count. Inspect the result before passing it into the next workflow stage.

## 5. Understand the area identities

For valid finite planar polygon sets under ordinary area semantics:

$$
\operatorname{area}(A\cup B)+\operatorname{area}(A\cap B)
=\operatorname{area}(A)+\operatorname{area}(B)
$$

$$
\operatorname{area}(A\setminus B)+\operatorname{area}(A\cap B)
=\operatorname{area}(A)
$$

$$
\operatorname{area}(A\triangle B)
=\operatorname{area}(A)+\operatorname{area}(B)
-2\operatorname{area}(A\cap B)
$$

These are useful checks, not proofs of topological correctness. A wrong boundary can still enclose the same area.

## 6. Precision is a modelling choice

A null grid uses floating precision. A positive grid size requests a fixed precision grid for the operation. The value is in input coordinate units. It can move vertices, merge nearby boundaries or collapse narrow features.

Never select a grid merely because it makes a topology exception disappear. Choose it from positional accuracy and the smallest meaningful feature, record it, and test representative geometries.

## 7. Reproduce the suite

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
python overlay_demo.py
~~~

Change one relationship at a time: overlap, containment, disjointness, edge touch, point touch, holes, multiple parts and precision grid.

## 8. Know what this package does not teach

It does not implement noding, planar arrangements, edge labelling or ring construction. Those are geometry-engine internals. It teaches responsible use of a maintained engine, an explicit input contract, output inspection and useful invariants.

For implementation internals, follow the GEOS OverlayNG and JTS OverlayNG references in the algorithm lesson. Record the Shapely and GEOS versions in reproducible work.
