# Exercise: add shapes, then reason about collision

## Goal

Calculate a convex Minkowski sum by merging edge directions, then use the same definition to reason about a moving robot.

## Part 1 — Calculate a sum

Let (P) be the rectangle with vertices ((0,0),(4,0),(4,2),(0,2)), and let (Q) be the rectangle with vertices ((0,0),(1,0),(1,1),(0,1)), both counter-clockwise.

1. Write the directed edge vectors of each polygon in boundary order.
2. Merge the edge directions around the circle.
3. Starting at the sum of the two lower-left vertices, accumulate the merged edge vectors.
4. Write the resulting boundary vertices.
5. Check that the result is a rectangle of the expected dimensions.

## Part 2 — Test the algebra

Explain why each identity follows from the definition:

- (A\oplus B=B\oplus A);
- ((A+t)\oplus B=(A\oplus B)+t);
- (A\oplus\{(0,0)\}=A).

Then explain why these identities are useful as tests for an implementation.

## Part 3 — Configuration-space obstacle

A robot is a rectangle centred on its reference point, with half-width 1 and half-height 0.5. An obstacle is an axis-aligned rectangle from ((5,4)) to ((8,7)).

1. Reflect the robot footprint about the origin.
2. Compute the configuration-space obstacle (O\oplus(-R)).
3. State which robot reference-point positions are forbidden.
4. Explain what changes if the robot reference point is at a corner rather than its centre.

## Part 4 — Pick the algorithm

For each case, choose the most appropriate route and explain why:

- two convex polygons with 100 and 200 edges;
- two concave polygons for which convex partitions are already available;
- two polygons with holes and complicated topology;
- a polygon expanded by a circular clearance radius.

Use the lesson references to distinguish the convex edge merge, decomposition approach, convolution approach and dedicated offset routines.

## Part 5 — Precision and topology

List at least four failure modes that can affect a practical GIS implementation. Include coordinate units, ring orientation, narrow corridors, holes and precision collapse in your discussion.

## Submission

Provide your edge-vector table, resulting polygon, configuration-space sketch, algorithm choices and validation identities.


## Part 4 — Run and inspect the teaching implementation

Run the [convex Minkowski-sum package](../implementations/python/minkowski-convex/README.md) and its [visual lab](../notebooks/minkowski-convex-lab.ipynb).

1. Confirm that the rectangle example returns the vertices of a 5-by-3 rectangle.
2. Reverse one input ring and explain why the result is unchanged.
3. Use a pair of convex polygons with parallel edges. Identify where the merge advances both edge lists in one step.
4. Try a concave polygon and explain why the implementation rejects it.
5. Compare the exact rational output with a geometry library. If the library returns a different starting vertex, compare the cyclic boundary rather than raw list order.

**Submission:** a short trace table with the two current edge vectors, the cross-product comparison, the chosen step, and the accumulated output vertex for each merge iteration.
