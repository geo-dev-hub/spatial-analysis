# Do two line segments meet?

This example takes two line segments with integer-coordinate endpoints and classifies their intersection as no intersection, one shared point, or a shared segment.

It handles proper crossings, endpoint contacts, collinear touches and collinear overlaps.

## Run it

Use Python 3.10 or newer. The example code has no third-party runtime dependency.

```bash
python segment_intersection.py
```

## Run the tests

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

The 11 tests cover orientation, proper crossings, a rational-valued crossing, endpoint contact, collinear overlap and touch, disjoint and parallel segments, vertical segments, reversed endpoint order and degenerate input.

## Why exact arithmetic here?

The orientation test asks whether a third point lies to the left of, right of, or exactly on a directed line. Its answer is the sign of a determinant. With integer coordinates, Python's integer arithmetic evaluates this determinant exactly. The constructed crossing coordinate may be fractional, so it is represented as a rational number rather than rounded to a float.

This is a deliberately narrow contract. Real GIS data commonly uses floating-point coordinates, and robust predicates for those inputs require more care. See Shewchuk's work on adaptive-precision geometric predicates.

## Step-by-step implementation walkthrough

Read [how the implementation works](implementation-walkthrough.md) for orientation tests, collinear overlap, endpoint contact and exact rational crossings.

## What this does not do

This function intersects **one pair** of segments. It is not Bentley–Ottmann, does not find all intersections in a set, and does not provide a sweep-line data structure. The next level up is an all-segment problem with an output-sensitive algorithm.
