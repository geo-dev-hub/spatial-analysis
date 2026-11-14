# Intern walkthrough: merge two convex polygon boundaries

## Learning outcome

By the end, you should be able to explain why the Minkowski sum of two convex polygons can be constructed by merging their boundary-edge directions, and why the merge takes linear time.

## 1. Start with the definition

For point sets (A) and (B),

[
A oplus B = {a+b mid ain A, bin B}.
]

For two convex polygons, the boundary of the sum is assembled from translated copies of the input boundary edges. Their directions are already cyclically ordered because each polygon is convex. We therefore merge two ordered edge sequences instead of sorting a combined list.

## 2. Prepare the rings

The implementation converts coordinates to `Fraction`, removes a repeated closing coordinate and consecutive duplicates, and removes redundant points along straight boundary runs. It then checks orientation and convexity. Clockwise rings are reversed to counter-clockwise order.

The lowest vertex (minimum y, then minimum x) is used as the starting vertex. This gives a consistent start for the cyclic edge sequence.

## 3. Merge directions without angles

Calling `atan2` would introduce floating-point angle values and unnecessary sorting. Instead, each vector is assigned to one of two half-planes. Within a half-plane, the sign of the cross product tells which vector has the smaller polar angle.

For vectors (u) and (v),

[
u 	imes v = u_xv_y-u_yv_x.
]

A positive result means (v) is counter-clockwise from (u) by an angle smaller than (pi). A zero result means the vectors are collinear; the half-plane test distinguishes same-direction from opposite-direction vectors.

When the next edge directions match, both are advanced together and their vectors are added. This avoids creating a redundant vertex on the sum boundary.

## 4. Maintain the boundary point

The first output point is the sum of the two selected starting vertices. Each merged edge vector advances the current output point. Every intermediate point is therefore the endpoint of a boundary edge in the Minkowski sum.

The algorithm processes each input edge once. It does not compare every vertex pair. The total number of merge steps is at most (m+n), giving (O(m+n)) time after input validation.

## 5. Validate the result

The tests cover rectangles, clockwise input, commutativity (up to cyclic starting position), exact fractional coordinates, parallel edges, redundant collinear points, invalid inputs and optional closing coordinates.

The rectangle exercise is especially useful: a (4	imes2) rectangle plus a (1	imes1) rectangle produces a (5	imes3) rectangle. Check that result both by the edge merge and by reasoning about all pairwise point sums.

## 6. Know when to stop

This implementation intentionally stops at convex polygons. A non-convex Minkowski sum can have more complicated boundary structure and may contain holes. Convex decomposition requires a union of pairwise convex sums; convolution methods require arrangement construction and winding-number classification. Do not silently feed a concave ring to this function.

## Further reading

- Ron Wein, [CGAL 2D Minkowski Sums](https://doc.cgal.org/Manual/latest/doc_html/cgal_manual/Minkowski_sum_2/Chapter_main.html), especially the convex edge-merge and non-convex decomposition/convolution sections.
