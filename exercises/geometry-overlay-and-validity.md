# Geometry exercises: validity, clipping and overlay

These exercises extend the [geometry foundations path](../learning-paths/geometry-foundations.md). They assume familiarity with point-in-polygon, segment intersection and polygon intersection.

## Exercise 1 — Diagnose before repairing

Create:
- a valid polygon with one hole;
- a bow-tie self-crossing ring;
- a polygon whose hole lies outside its shell;
- a MultiPolygon with overlapping components.

For each input, predict validity, run the checker, and record its diagnostic. Repair only after stating what you believe the intended area is.

**Submit:** input construction, validity output, repair output, before/after geometry type and area, and a short explanation of why repair is not neutral.

**Hint:** test polygon validity and collection validity separately.

## Exercise 2 — Clipping algorithm selection

Choose an algorithm family for each task:

1. clip a concave subject polygon against a convex rectangular window;
2. intersect two arbitrary concave polygons;
3. clip a line segment against a rectangular viewport;
4. perform a GIS parcel overlay where holes and disconnected components must be preserved.

Explain the input assumptions that make your choice appropriate. Do not select a method based only on its name.

**Submit:** a decision table with task, method, assumptions, expected output structure and at least one limitation.

## Exercise 3 — Overlay identities

Construct two overlapping polygons (A) and (B). Calculate intersection, union, difference and symmetric difference.

Check:

[
\operatorname{area}(A \cup B) +
\operatorname{area}(A \cap B)
=
\operatorname{area}(A) + \operatorname{area}(B)
]

and

[
\operatorname{area}(A \setminus B) +
\operatorname{area}(A \cap B)
=
\operatorname{area}(A)
]

Then explain why passing these area checks does not prove that the result boundaries are correct.

## Exercise 4 — Precision experiment

Create two polygons with nearly coincident edges. Run overlay under the default floating precision model and under at least one explicitly chosen fixed precision grid.

Record:
- coordinate units and scale;
- grid size;
- output type and area;
- validity;
- any exception;
- what geometric detail was lost or preserved.

Do not choose a grid merely because it makes an exception disappear. Justify it in the context of the data.

## Exercise 5 — Build a regression suite

Write tests for:
- disjoint polygons;
- containment;
- shared edge;
- point touch;
- hole preservation;
- disconnected intersection;
- invalid input;
- near-coincident boundaries.

Use both expected geometry properties and a reference implementation. State which properties your tests do not establish.

## Review checklist

- [ ] Did I distinguish validity from geographic correctness?
- [ ] Did I distinguish clipping from general overlay?
- [ ] Did I state the algorithm's input assumptions?
- [ ] Did I check output geometry type and component count?
- [ ] Did I record CRS, units, precision and software versions?
- [ ] Did I test more than the happy path?
- [ ] Did I preserve the original geometry when repairing?
