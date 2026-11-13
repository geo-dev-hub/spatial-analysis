# Intern walkthrough: fixed-grid precision

## Step 1 — State the precision model

A grid size is expressed in coordinate units. The example uses a planar
coordinate system and a grid of 0.1 units. A longitude/latitude grid is not a
uniform ground-distance model.

## Step 2 — Reduce coordinate precision

`reduce_precision` wraps Shapely's `set_precision`. The selected mode controls
how collapsed components are handled. The default `valid_output` mode returns
valid output and removes collapsed components.

## Step 3 — Compute a fixed-grid overlay

`fixed_precision_intersection` calls GEOS intersection with an explicit
`grid_size`. This differs from separately rounding coordinates and then
assuming every later operation will use the same precision model.

## Step 4 — Inspect changes

Compare geometry type, validity, area, length, component count and coordinate
movement. Include narrow corridors and near-coincident edges.

## Step 5 — Do not rename the operation

The wrapper does not implement a full snap-rounding noder. Snap rounding is an
arrangement-level algorithm with a defined noding procedure. This package
teaches fixed-grid precision operations and makes their limits explicit.
