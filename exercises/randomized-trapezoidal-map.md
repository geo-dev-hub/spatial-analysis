# Exercise: trace a randomized trapezoidal-map insertion

This is a paper-and-pencil exercise. It is designed to make the map/search-structure invariant concrete before attempting a full implementation.

## Part A — Build a small decomposition

Draw a bounding rectangle and six non-crossing, non-vertical line segments. Avoid shared endpoints and equal x-coordinates for this first pass.

1. Choose a random insertion order and write it down.
2. Insert the first segment. Draw the vertical walls from its endpoints to the bounding rectangle.
3. Insert the second segment. Identify the trapezoid containing its left endpoint.
4. Trace the segment through every trapezoid it crosses, from left to right.
5. Remove the crossed trapezoids and draw the replacement upper and lower trapezoids.
6. Repeat until all six segments have been inserted.

## Part B — Maintain the search DAG

For each insertion, draw the decisions needed to replace the old leaves:

- x-coordinate comparisons for endpoint walls;
- y-coordinate comparisons for endpoint location;
- segment-side comparisons for the newly inserted segment.

Keep references to unaffected leaves. Explain why a leaf can have more than one incoming edge after a local update.

## Part C — Test point-location queries

Choose at least eight query points:
- two strictly inside different trapezoids;
- one on a vertical wall;
- one on an input segment;
- one at a segment endpoint;
- one at a shared boundary between two faces;
- one outside the bounded subdivision;
- one near a vertex but not on an edge.

For each query, record the search path and the expected face or boundary result. Explain which queries require an explicit boundary convention.

## Part D — Analyse the algorithm

1. Why does a random insertion permutation help expected performance?
2. What is the role of the trapezoid history DAG?
3. Why can an adversarial order produce poor search paths?
4. Which general-position assumptions simplify the construction?
5. Which assumptions are most likely to fail in real GIS linework?
6. Why must the search DAG and trapezoidal map be updated together?

Read the [planar point-location lesson](../algorithms/geometry/point-location.md) before attempting this exercise. Do not claim the exercise is an implementation or a substitute for a tested point-location data structure.
