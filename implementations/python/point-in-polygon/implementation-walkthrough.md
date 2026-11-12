# How the point-in-polygon example works

This implementation classifies a point relative to one simple planar ring. It uses a ray-crossing test and reports boundary points separately.

## 1. Define the result states

The `PointLocation` enum has three values:
- `INSIDE`;
- `OUTSIDE`;
- `BOUNDARY`.

Keeping boundary separate avoids forcing a boundary point into an inside/outside answer before the application has chosen its rule.

## 2. Normalise the ring

The function copies the supplied vertices. If the first vertex is repeated at the end, that duplicate closing coordinate is removed.

It then checks that at least three distinct vertices remain. The function treats the ring as closed even when the first coordinate is not repeated at the end.

This is a simple input contract. It does not validate polygon topology or holes.

## 3. Check the boundary first

Before counting ray crossings, the function checks every edge with `_on_segment()`.

That helper:
1. computes a cross product to test collinearity;
2. checks that the point lies within the edge's x and y ranges.

If the point lies on any segment, the function returns `BOUNDARY` immediately.

The comparison uses exact floating-point equality. That is acceptable for this small teaching example, but not a robust tolerance strategy for arbitrary coordinates.

## 4. Cast a horizontal ray

The algorithm imagines a ray extending rightward from the query point. Every time that ray crosses a ring edge, the inside/outside state toggles.

A point is inside if the ray crosses the boundary an odd number of times. It is outside if the number of crossings is even.

## 5. Avoid counting a shared vertex twice

The condition is:

```python
crosses_scanline = (y1 > y) != (y2 > y)
```

This half-open vertical interval rule means an edge contributes only when its endpoints lie on opposite sides of the query y-coordinate. It avoids counting a vertex twice when the ray passes exactly through it.

## 6. Find the x-coordinate of the crossing

For an edge that crosses the horizontal scanline, the function calculates the x-coordinate where the edge meets the line:

```python
crossing_x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
```

If the crossing lies to the right of the query point, the inside state toggles.

## 7. Return the classification

After every edge has been checked:
- return `INSIDE` if the state is true;
- otherwise return `OUTSIDE`.

Boundary points have already returned from the earlier check.

## 8. Why this is only a teaching implementation

This function assumes one simple ring in a planar coordinate space. It does not handle:
- holes or multipolygons;
- self-intersecting rings;
- robust exact predicates for arbitrary floating-point coordinates;
- CRS transformations;
- prepared geometries or spatial indexes.

For production point-in-polygon work, use a maintained geometry engine such as Shapely/GEOS and choose the boundary predicate that matches the application.

## 9. What the tests cover

The tests check interior, exterior and boundary points; horizontal and vertical edges; vertex contact; reversed ring orientation; implicitly and explicitly closed rings; and invalid rings.

Read the [point-in-polygon lesson](../../../algorithms/geometry/point-in-polygon.md) for the ray-crossing diagram and edge cases.

## Reproduce

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```
