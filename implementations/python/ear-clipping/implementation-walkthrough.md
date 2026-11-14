# Intern walkthrough: build an ear-clipping triangulator

## 1. Start with the polygon, not the code

A polygon ring is an ordered list of vertices. Each vertex has a previous and next neighbour. At a candidate middle vertex (b), the points (a,b,c) form a possible ear when:

1. the corner at (b) is convex;
2. the triangle (abc) lies inside the polygon;
3. no other active polygon vertex lies inside or on that triangle.

Clipping the ear stores triangle (abc) and removes (b) from the active boundary.

## 2. Make orientation independent of floating-point angles

The signed orientation determinant is

[
\operatorname{orient}(a,b,c) =
(b_x-a_x)(c_y-a_y)-(b_y-a_y)(c_x-a_x).
]

A positive result means counter-clockwise, a negative result clockwise, and zero collinear. We do not calculate angles or slopes. Converting decimal coordinate strings to rational numbers makes the sign test exact for the supplied decimal values.

## 3. Normalize and validate

The implementation removes a repeated closing coordinate, consecutive duplicates and redundant collinear points between their neighbours. It then checks for intersections between non-adjacent edges. This is deliberately quadratic and keeps the topology contract visible.

Do not silently repair a self-crossing ring. The meaning of its interior depends on a fill rule and a repair policy; this package rejects it.

## 4. Clip one ear at a time

For each active vertex, inspect its predecessor and successor. A non-positive orientation is not a convex ear for the counter-clockwise ring. Next, test every other active vertex against the candidate triangle. Boundary points also block clipping so that a vertex on a candidate diagonal is not skipped.

Once an ear is accepted, append its triangle and remove its middle vertex. Only the two neighbours can have changed ear status, but this simple implementation recomputes candidates in the next pass rather than maintaining an ear queue. This makes the control flow easier to follow while preserving the (O(n^2)) bound.

## 5. Check the result

For a simple polygon with (n) normalized vertices:

- expect (n-2) triangles;
- expect every output triangle to have positive orientation;
- compare the sum of triangle areas with the polygon area;
- test both clockwise and counter-clockwise input;
- test concavity, collinearity, duplicates and invalid topology.

Area equality is a useful invariant, not a complete proof that triangles do not overlap. The ear condition and simple-polygon precondition supply the topological argument.

## 6. Reproduce the tests

From this directory run `python -m pytest -q`. Read each test as a claim about the contract, not merely as a line of code to make green. Then modify the concave example and predict which ear will be clipped first.

## 7. Know when to stop using this implementation

The package deliberately excludes holes, constrained triangulation, quality refinement and large datasets. A real GIS pipeline should use a mature implementation and retain its validity checks, precision model and documented handling of holes. Never label this output “Delaunay” unless a separate constrained-Delaunay procedure has actually been run.
