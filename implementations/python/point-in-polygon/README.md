# Point in polygon with Python

This tutorial asks a simple question: given a point and a boundary, is the point inside, outside or exactly on the edge?

It implements the ray-crossing (even–odd) method for one simple polygon ring and reports boundary points separately.

## Set up

Use Python 3.10 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run it

```bash
python point_in_polygon.py
```

Expected output:

```text
(2, 2) inside
(5, 2) outside
(4, 2) boundary
```

## Run the tests

```bash
python -m pytest -q
```

The test suite covers inside, outside, edge, vertex, concavity, a ray passing through a concave vertex, and both open and explicitly closed ring representations.

## Follow the code

1. Start with `PointLocation`: the result has three states, not just True or False.
2. Read `_on_segment`: boundary is checked before counting crossings.
3. Read `locate_point`: each edge is checked once and a crossing toggles the parity.
4. Change the point coordinates and predict the classification before running the tests.

## Step-by-step implementation walkthrough

Read [how the implementation works](implementation-walkthrough.md) for ring normalisation, boundary detection, half-open scanline crossings and parity toggling.

## Important limits

- This is a teaching implementation for a single simple ring.
- It does not support holes, multipolygons or self-intersecting rings.
- It uses exact floating-point comparisons for the boundary test. Real datasets may require a carefully chosen tolerance or robust predicates.
- It uses planar x/y coordinates; it does not transform CRS or interpret longitude/latitude.
- Production systems should use a geometry library with documented topology and boundary semantics.

## Checked environment

- Python 3.13.5
- pytest 9.0.2

The 12 tests passed in the recorded environment. Run them again in your own environment before using the code in a project.
