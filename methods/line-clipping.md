# Line clipping: Cohen–Sutherland, Liang–Barsky and Cyrus–Beck

Line clipping keeps the part of a finite line segment inside a specified region. It is a geometric operation that changes endpoints or rejects the segment; it is not the same as drawing a complete line and masking pixels afterwards.

## 1. Define the problem

Let the closed, axis-aligned rectangle be

$$
W=[x_{min},x_{max}]\times[y_{min},y_{max}].
$$

A segment from A to B has the parametric form

$$
P(t)=A+t(B-A),\qquad 0\leq t\leq1.
$$

Clipping finds the interval of parameter values for which P(t) lies inside W. The result is empty or a segment between the two limiting parameter values. This lesson treats the window as closed, so edge and corner touches are retained. An implementation must state its own boundary policy.

## 2. Cohen–Sutherland: classify before intersecting

Cohen–Sutherland assigns each endpoint a four-bit outcode indicating whether it lies left, right, below or above the rectangle. A point on a boundary is inside for that boundary test.

For endpoint codes cA and cB:

- If (cA OR cB) equals zero, both endpoints are inside: accept.
- If (cA AND cB) is nonzero, both endpoints are outside on at least one common side: reject.
- Otherwise, the segment may cross the window. Intersect an outside endpoint with a relevant boundary, replace it, recompute its code and repeat.

The bit tests provide trivial acceptance and rejection, not a complete decision for every crossing case.

### Outcode regions

~~~text
        TOP
   1001 | 1000 | 1010
  -------+------+-------
   LEFT  | 0000 | RIGHT
  0001   |      | 0010
  -------+------+-------
   0101 | 0100 | 0110
       BOTTOM
~~~

The bit labels are illustrative. Implementations must define one consistent bit ordering. The four bits encode half-plane membership, not a unique one-of-nine region identifier.

**Strength:** cheap bitwise trivial tests and a clear algorithm trace.

**Limitations:** crossing cases may require repeated intersection calculations. Floating-point implementations need a defined tolerance and termination policy.

## 3. Liang–Barsky: intersect parameter intervals

Substitute the parametric segment into the four rectangle inequalities. Write each constraint as pᵢt ≤ qᵢ, using the conventional left, right, bottom, top ordering:

$$
p=(-\Delta x,\Delta x,-\Delta y,\Delta y),
$$

$$
q=(x_0-x_{min},x_{max}-x_0,y_0-y_{min},y_{max}-y_0).
$$

Start with [t0,t1]=[0,1]. For each boundary:

- If pᵢ=0 and qᵢ<0, the segment is parallel to and outside that boundary: reject.
- If pᵢ<0, update the entering bound: t0=max(t0,qᵢ/pᵢ).
- If pᵢ>0, update the leaving bound: t1=min(t1,qᵢ/pᵢ).
- Reject as soon as t0>t1.

Otherwise the clipped endpoints are P(t0) and P(t1). Parallel boundaries must be handled explicitly; never divide by zero. Use a documented numeric policy rather than silently expanding the window.

## 4. Cyrus–Beck: convex clipping regions

For a convex polygon or polyhedron, each boundary defines a half-space. Let the inside of boundary i satisfy

$$
n_i\cdot(P(t)-F_i)\leq0,
$$

where nᵢ is an outward normal and Fᵢ is a point on that boundary. Substitution gives a linear constraint in t. Intersect all constraints with [0,1], updating entering and leaving values as in Liang–Barsky.

Cyrus–Beck is a parametric convex-clipping method. It is not a general solution for concave clipping regions: a concave region can retain multiple disjoint intervals, whereas intersection with convex half-spaces produces at most one segment interval.

## 5. Choose the method

| Method | Region | Main idea | Good fit |
|---|---|---|---|
| Cohen–Sutherland | Axis-aligned rectangle | Endpoint outcodes and trivial tests | Teaching and cheap early rejection |
| Liang–Barsky | Axis-aligned rectangle | Intersect a segment parameter interval | Compact rectangular clipping |
| Cyrus–Beck | Convex polygon/polyhedron | Intersect half-space constraints | General convex clipping windows |

Nicholl–Lee–Nicholl is another rectangular line-clipping method that uses endpoint-region classification to reduce intersection work. It is useful for literature comparison, but not essential to a first robust implementation.

## 6. Worked example

Clip A=(-2,1) to B=(6,5) against [0,4] × [0,3].

$$
P(t)=(-2,1)+t(8,4).
$$

The x constraints require 0≤-2+8t≤4, hence 1/4≤t≤3/4. The y constraints require 0≤1+4t≤3, hence -1/4≤t≤1/2. Intersecting these with [0,1] gives:

$$
t\in[1/4,1/2].
$$

The clipped segment runs from (0,2) to (2,3); the latter endpoint lies on the top boundary.

## 7. Numerical and GIS considerations

- **Coordinate units:** segment and window must use the same coordinate space. A longitude/latitude rectangle is not a metric buffer.
- **Boundary precision:** exact equality is fragile with floating-point coordinates. State whether the operation is exact, tolerance-based or precision-grid based.
- **Degenerate segments:** A=B is a point; test it against the window explicitly.
- **Degenerate windows:** zero width or height may be meaningful for a line/point query, or invalid for an application. Define the contract.
- **Topology:** clipping every edge of a polygon independently does not construct the clipped polygon. New boundary segments must be connected in order; use a polygon-clipping algorithm for polygon output.
- **Antimeridian:** geographic extents crossing the antimeridian or approaching a pole need deliberate splitting or transformation.

## 8. Test plan

Test wholly inside and outside segments; crossings of all four boundaries; parallel-inside and parallel-outside cases; corner touches; edge-coincident segments; zero-length segments; reversed endpoints; and very large and very small coordinate magnitudes.

For a robust implementation, compare generated small cases against an independent geometry library while retaining hand-constructed boundary tests. A reference library should not be the only test oracle.

## Further reading

- Matthes, J. and Drakopoulos, V. (2022), “Line Clipping in 2D: Overview, Techniques and Algorithms,” *Journal of Imaging*, 8(10), 286. [Open-access article](https://doi.org/10.3390/jimaging8100286). The survey distinguishes encoding, parametric and midpoint-subdivision approaches.
- Stanford CS 248, Marc Levoy, [Rasterization algorithms and scan conversion notes](https://www.graphics.stanford.edu/courses/cs248-08/scan/scan1.html).
- The [polygon-clipping lesson](../algorithms/geometry/polygon-clipping.md) explains why segment clipping alone is insufficient for polygon output.

## Scope

This is a method comparison and derivation, not a production clipping library. The named methods are described, but no new implementation is claimed. A future package must specify boundary inclusion, numeric precision, degenerate inputs and differential tests.


## Nicholl–Lee–Nicholl clipping

Nicholl–Lee–Nicholl is a 2D line-segment algorithm for axis-aligned rectangular clipping windows. It partitions the endpoint plane using rays from the first endpoint to window corners. The first endpoint is mapped by symmetry into one of three canonical regions: inside, left, or top-left. Slope-region tests then identify the relevant boundary or boundary pair directly, reducing repeated clipping iterations.

The Python implementation includes canonical-region transformations, side selection, boundary intersection and explicit handling for vertical and boundary-outward segments. It is tested differentially against Liang–Barsky on hand-selected and randomized cases. It does not clip arbitrary convex polygons; Cyrus–Beck remains the convex-window method in this package.

- [Implementation](../implementations/python/line-clipping/line_clipping.py)
- [Tests](../implementations/python/line-clipping/test_line_clipping.py)
- [Intern walkthrough](../implementations/python/line-clipping/implementation-walkthrough.md)
- Primary reference: Nicholl, Lee & Nicholl (1987), “An efficient new algorithm for 2-D line clipping: Its development and analysis,” SIGGRAPH '87, DOI: 10.1145/37401.37432.
- Supporting walkthrough: Brown University computer graphics notes, [Nicholl–Lee–Nicholl clipping](https://cs.brown.edu/media/filer_public/88/9c/889c4b64-6979-4d31-a4fe-3904a681b978/dasilva.pdf).
