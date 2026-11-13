# Implementation walkthrough: Graham scan

## 1. What are we trying to find?

Given a finite set of planar points, find the smallest convex polygon that contains them. Imagine stretching a rubber band around the outside of the point set: the band traces the convex hull.

The hull contains the extreme points. Points strictly inside it do not affect its boundary.

## 2. Choose a pivot

The implementation chooses the point with the lowest y-coordinate; ties are broken by the lowest x-coordinate. This pivot is guaranteed to be a hull vertex.

Every other point is then ordered by its direction from the pivot, counter-clockwise from the positive x-axis.

## 3. Why orientation tells us what to remove

For three points O, A and B, the signed cross product is:

$$
\operatorname{cross}(O,A,B)
=(A_x-O_x)(B_y-O_y)-(A_y-O_y)(B_x-O_x)
$$

- Positive: the turn from OA to OB is counter-clockwise.
- Negative: the turn is clockwise.
- Zero: the points are collinear.

As the scan follows points in polar order, a clockwise turn means the previous candidate cannot remain on the convex boundary. A collinear turn is also removed under this implementation's policy, so only extreme vertices remain.

## 4. Scan with a stack

For each point in sorted order:

1. Look at the last two points currently on the stack.
2. Calculate the orientation of those two points and the new candidate.
3. While the turn is clockwise or collinear, remove the middle stack point.
4. Push the new candidate.
5. Continue until all candidates have been processed.

The stack always stores the current boundary chain. A point removed from it is no longer needed to describe the convex hull.

## 5. Handle points on the same ray

Several points can share the same polar direction from the pivot. Only the farthest one can be an extreme hull vertex. The implementation orders equal-direction points by squared distance and keeps the farthest candidate.

This avoids a common failure mode where points on one ray create unnecessary collinear vertices or confuse the scan.

## 6. Follow the code

1. Convert coordinates to finite floats and remove duplicates.
2. Return immediately for zero or one unique point.
3. Select the lowest-then-leftmost pivot.
4. Sort the remaining points using a cross-product comparator.
5. Collapse multiple points on the same ray to the farthest point.
6. Build the hull with a stack, removing non-left turns.
7. Return the counter-clockwise extreme vertices.

## 7. Reproduce the tests

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

The tests cover a square, interior points, collinear edge points, an all-collinear set, duplicates, empty and tiny inputs, orientation, pivot choice and non-finite coordinates.

## 8. Numerical caution

This example uses floating-point orientation predicates. When points are nearly collinear, rounding can change the sign of the cross product. Exact/adaptive predicates are important when a wrong orientation could corrupt a critical geometry workflow.

Do not interpret the teaching implementation as a robust geometry kernel. Record coordinate scale, units and numeric assumptions in real projects.
