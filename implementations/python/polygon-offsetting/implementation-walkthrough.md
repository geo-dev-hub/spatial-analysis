# Intern walkthrough: polygon offsetting

## Objective

Expose a narrow, explicit wrapper around GEOS buffer operations. Do not implement offset geometry from raw normals in this exercise; robust offsetting must handle self-intersections, joins, collapsed parts and polygon hierarchy.

## Step 1 — Define the input contract

Only valid Polygon and MultiPolygon inputs are accepted. The geometry must already be expressed in a suitable planar coordinate system. The distance uses the coordinate units.

## Step 2 — Make corner behaviour explicit

The wrapper accepts round, mitre and bevel join styles. The miter limit bounds sharp-corner extension. The number of quadrant segments controls round-arc approximation.

## Step 3 — Understand collapse

A negative buffer can remove narrow parts or collapse a polygon entirely. Empty output is a valid possible result, not an automatic exception.

## Step 4 — Run tests

The tests check positive and negative offsets, collapse, join-style output, invalid inputs and parameter validation.

## Step 5 — Compare libraries carefully

The repository source names Clipper. This example uses GEOS through Shapely and does not claim to reproduce Clipper2's output. A Clipper2-specific example needs a pinned binding or native-language implementation and its own tests.
