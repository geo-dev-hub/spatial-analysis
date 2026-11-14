# Exercise: triangulate a concave polygon

## Goal

Use ear clipping to divide a simple concave polygon into triangles. You will predict candidate ears, run the implementation and verify the result.

## Input

Use this counter-clockwise ring:

~~~python
ring = [(0, 0), (6, 0), (6, 5), (4, 2), (2, 4), (0, 5)]
~~~

## Part 1 — Work by hand

1. Calculate the orientation determinant at each vertex.
2. Mark convex, reflex and collinear vertices.
3. Select one candidate ear.
4. Check whether any other vertex lies inside or on its triangle.
5. Record the triangle and remove its middle vertex.
6. Repeat until only one triangle remains.

Do not assume the first convex vertex is automatically an ear.

## Part 2 — Run the implementation

From the package directory:

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

Then call `triangulate(ring)`. Compare the number of triangles with (n-2), and compare the sum of triangle areas with the polygon area.

## Part 3 — Challenge the assumptions

Try each of these inputs and explain the outcome:

- the same ring in clockwise order;
- a repeated closing vertex;
- a redundant collinear point on an edge;
- a bow-tie ring that crosses itself;
- a polygon with a hole represented as a second ring.

The first three should be handled according to the documented contract. The bow-tie should be rejected. The final case is outside this package's scope: do not concatenate the rings and pretend that this is a valid polygon-with-holes representation.

## Part 4 — Improve it

The current implementation scans all active vertices and is deliberately simple. Design an ear queue that initially classifies candidate vertices, clips one candidate, and rechecks only its two neighbours. Explain how stale queue entries are detected and how you would preserve exact predicates.

## Submission

Provide:
- your hand-worked ear sequence;
- the resulting triangle list;
- an area check;
- one test you added;
- a short note explaining why this is not constrained Delaunay triangulation.
