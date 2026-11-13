# How the Graham scan implementation works

This walkthrough follows the code in `graham_scan.py`. It is written so a new intern can reproduce the implementation and explain why each step is present.

## 1. Normalise and validate the input

`_normalise_points` converts coordinates to floating-point numbers, rejects non-finite values and removes duplicates with a set.

Why remove duplicates? Two identical coordinates do not create a new geometric extreme point. Keeping them would only add repeated candidates to the sort and scan.

This conversion also defines a limitation: ordinary floating-point values are used. The implementation is intended for learning and well-behaved planar coordinates, not exact arithmetic.

## 2. Choose the anchor

```python
anchor = min(pts, key=lambda p: (p[1], p[0]))
```

The point with the smallest y-coordinate is selected. If several points share that y-coordinate, the smallest x-coordinate wins.

This point must be on the convex hull. If another point lay strictly below it, it would have a smaller y-coordinate and would have been selected instead.

## 3. Sort the other points around the anchor

The code uses `atan2(dy, dx)` to obtain a polar angle. It sorts by angle and then by squared distance from the anchor.

The distance tie-break is important. Points on the same ray must be considered from nearest to farthest. The scan can then remove nearer collinear candidates and keep the farthest point on that boundary ray.

A production alternative can compare half-planes and cross products directly rather than computing angles.

## 4. Understand the orientation test

For points (O,A,B), the signed cross product is

$$
(A_x-O_x)(B_y-O_y)-(A_y-O_y)(B_x-O_x).
$$

A positive result is a left turn, a negative result is a right turn, and zero means collinear.

The helper `cross` makes this rule explicit and independently testable.

## 5. Build the hull with a stack

For each sorted point:

1. inspect the last two points currently on the stack;
2. calculate their turn with the candidate;
3. while the turn is clockwise or collinear, remove the stack's last point;
4. append the candidate.

Why remove on `<= 0`? This lesson returns only extreme vertices. A collinear middle point is not a corner and is therefore removed. If an application needs every boundary point, the condition and output policy must change.

## 6. Why the scan is linear after sorting

Each point is appended once. A point can be removed from the stack only after it has been appended, and once removed it is never reinserted.

Therefore the total number of stack pushes and pops is proportional to the number of points. The scan takes (O(n)) time after the (O(n\log n)) sort.

## 7. Reproduce and inspect

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

The tests cover the expected hull, interior points, duplicates, collinear inputs, same-ray sorting, anchor tie-breaking, orientation signs, small inputs and invalid coordinates.

## 8. What the tests do not prove

Passing these tests does not establish robust behaviour for every floating-point input. In particular, nearly collinear points can produce a cross product whose sign is changed by rounding.

For production geometry, use a robust orientation predicate, define the coordinate reference and numeric model, and compare results against an independent implementation on adversarial cases.
