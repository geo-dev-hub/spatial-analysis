# How the segment-intersection example works

This implementation finds the intersection of two closed line segments with integer-coordinate endpoints. It handles proper crossings, endpoint contact, collinear touches and collinear overlap.

It uses integer orientation tests and exact rational coordinates so the example can avoid floating-point rounding in its core decisions.

## 1. Make the result explicit

The `Intersection` dataclass stores:
- a kind: `none`, `point` or `overlap`;
- the geometry associated with that kind.

A single intersection point is represented with `Fraction` coordinates. An overlap is represented by its two integer endpoints.

## 2. Use orientation to compare three points

`orientation(a, b, c)` calculates the signed 2D determinant:

```python
determinant = (
    (b[0] - a[0]) * (c[1] - a[1])
    - (b[1] - a[1]) * (c[0] - a[0])
)
```

Its sign tells us whether the turn from A to B to C is counter-clockwise, clockwise or collinear.

Because the inputs are integers and Python integers have arbitrary precision, the sign test is exact for these coordinates.

## 3. Check whether a point lies on a segment

`_on_segment()` combines two conditions:
- the point is collinear with the segment;
- its x and y coordinates lie between the endpoints.

This catches endpoint contact and collinear overlap cases.

## 4. Handle collinear segments separately

If all four orientation tests are zero, the two supporting lines are collinear.

The implementation sorts each pair of endpoints lexicographically, then finds:
- the later start point;
- the earlier end point.

If the start is after the end, there is no overlap. If they are equal, the segments touch at one point. If the start is before the end, the shared geometry is a segment.

This works because lexicographic order is monotonic along a non-degenerate collinear segment.

## 5. Handle endpoint contact

Before testing for a proper crossing, the function checks whether any endpoint lies on the other segment.

This is necessary because a segment can touch another at an endpoint without having a strict orientation sign change.

If a contact is found, it returns that exact integer point as a pair of `Fraction` values.

## 6. Handle a proper crossing

A proper crossing occurs when:
- C and D lie on opposite sides of AB;
- A and B lie on opposite sides of CD.

The code checks this with:

```python
if o1 * o2 < 0 and o3 * o4 < 0:
```

For this case, the supporting lines are not parallel. `_line_intersection()` calculates the line parameter using integer determinants and converts it to a `Fraction`.

The resulting coordinates remain exact, even when the intersection is not an integer point.

## 7. Reject zero-length segments

A segment with identical endpoints is rejected explicitly. That keeps the function's contract simple: every input is a proper segment with two distinct endpoints.

A more general geometry engine might treat a zero-length segment as a point, but this teaching implementation does not.

## 8. What the tests cover

The tests include proper crossings, parallel segments, collinear disjoint segments, endpoint touches, collinear overlap, vertical and horizontal segments, negative coordinates, fractional intersections and zero-length input.

They are designed to exercise the different branches in the algorithm, not only the typical crossing case.

## 9. What this example does not do

This is a pairwise segment test. It does not find all intersections among a large collection of segments. For that problem, continue to the [Bentley–Ottmann sweep-line lesson](../../../algorithms/geometry/bentley-ottmann.md).

Read the [segment-intersection lesson](../../../algorithms/geometry/segment-intersection.md) for the orientation diagram and mathematical explanation.

## Reproduce

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```
