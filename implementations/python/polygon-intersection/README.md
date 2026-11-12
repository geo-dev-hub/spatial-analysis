# Polygon intersection with Python

This is the first runnable example in the Spatial Analysis collection. It uses Shapely to calculate the shared part of two polygons.

## What you will see

Two rectangles overlap. The example returns the rectangle covered by both and calculates its area. Then the tests check what happens when shapes are disjoint, contained, touch along an edge, touch at one point, or contain a hole.

## Set up

Use Python 3.10 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the example

```bash
python intersection_demo.py
```

Expected key output:

```text
Result type: Polygon
Area: 4.0
```

The coordinates are simple Cartesian units, not longitude and latitude. The example is for learning geometry operations, not for measuring real-world area.

## Run the tests

```bash
python -m pytest -q
```

The test suite checks nine behaviours, including lower-dimensional results and explicit rejection of invalid input geometry.

## Read the code in this order

1. Open `intersection_demo.py`. Notice that `polygon_intersection` delegates the overlay operation to Shapely.
2. Run the example and inspect the WKT output.
3. Open `test_intersection_demo.py`. Each test isolates one spatial relationship.
4. Change the coordinates and predict the result before running the code again.

## Important limits

- Shapely performs planar geometry operations. Choose an appropriate projected coordinate reference system before interpreting distances or areas as real-world measurements.
- This example rejects invalid polygons. It does not silently repair them, because repair can change the geometry.
- `grid_size` is optional. Do not choose a snapping grid without understanding the coordinate units, data scale and positional accuracy.
- Shapely delegates geometry operations to GEOS. This example demonstrates the library API; it does not reimplement the internal overlay algorithm.

## Environment used for the checked example

- Python 3.13.5
- Shapely 2.1.2
- pytest 9.0.2

The code and tests were run in this environment. Re-run the tests in your own environment before relying on the result in production.
