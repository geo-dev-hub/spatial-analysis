# Implementation walkthrough: Sutherland–Hodgman clipping

This walkthrough is for a learner who has not seen the repository or algorithm before. Keep the tests open as you read.

## 1. State the problem

We have a subject polygon and a convex clipping polygon. We want the part of the subject inside every edge half-plane of the clip polygon.

For a convex clip polygon C, its interior is the intersection of the inward half-planes of its edges:

$$
C = \bigcap_{i=1}^{m} H_i
$$

We can therefore clip repeatedly: edge 1, then edge 2, and so on. Each pass consumes a vertex ring and emits a new ring.

## 2. The orientation test

For directed clip edge a to b, evaluate:

$$
s(a,b,p)=(b_x-a_x)(p_y-a_y)-(b_y-a_y)(p_x-a_x)
$$

A positive value places p to the left of the edge; a negative value places it to the right; zero means it lies on the supporting line. For a counter-clockwise clip ring, the interior is to the left of every edge. The implementation normalizes both rings to counter-clockwise orientation first.

## 3. The four transitions

For each subject segment from S to E:

| Start | End | Emit |
|---|---|---|
| inside | inside | E |
| inside | outside | crossing point |
| outside | inside | crossing point, then E |
| outside | outside | nothing |

The order matters: emitted vertices must follow the polygon boundary. The next clip-edge pass consumes that output sequence.

## 4. Compute a crossing

Parameterize the segment:

$$
P(t)=S+t(E-S),\qquad 0\leq t\leq1
$$

The signed side value changes linearly along the segment. If endpoint values are d_S and d_E, the crossing occurs at:

$$
t=\frac{d_S}{d_S-d_E}
$$

Substitute t into P(t) to obtain the intersection with the infinite line containing the clip edge.

## 5. Follow the code

1. signed_area calculates ring orientation using the shoelace formula.
2. _validate removes a repeated closing coordinate, rejects duplicate vertices and zero-area rings, checks consistent turns, and normalizes orientation.
3. _cross evaluates a point's signed side relative to a directed edge.
4. _intersection calculates the segment-line crossing.
5. _deduplicate removes consecutive points numerically indistinguishable under the chosen epsilon.
6. clip_convex_polygon repeats the four-transition pass for every clip edge.

Do not remove input validation just to make a concave example run. That would weaken the contract without solving the disconnected-output problem.

## 6. Why the scope is narrow

A concave subject clipped by a convex window can produce disconnected pieces, while this implementation returns one vertex ring. Holes, multiple components, coincident boundaries and self-intersections require a richer output and topology model.

This implementation therefore requires **both** inputs to be convex. Their intersection is then convex and connected, and one ring is sufficient. For general GIS overlay, use a maintained geometry engine such as GEOS through Shapely, and document its version and precision behaviour.

## 7. Reproduce and validate

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

Tests cover overlap, orientation, containment, disjoint inputs, edge-only contact, point-only contact, concave-input rejection, zero-area rejection and invalid epsilon.

## 8. Experiments

- Reverse each input ring; the result area should remain unchanged.
- Move the clip polygon until it is disjoint; the result should become empty.
- Move it until it shares one edge; this API still returns empty because the intersection has zero area.
- Replace one input with a concave ring; the function should reject it.
- Compare valid convex cases with Shapely's polygon intersection.

## 9. Record in a real project

Record CRS, units, coordinate scale, epsilon, input validity, source identifiers, algorithm version and output validation. A tolerance sensible for metre coordinates may be inappropriate for longitude/latitude or millimetre-scale engineering data.
