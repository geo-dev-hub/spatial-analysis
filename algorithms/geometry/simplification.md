# Line simplification: Douglas–Peucker and Visvalingam–Whyatt

A digitised line often contains more vertices than are needed for a particular map scale, display resolution or analysis. Simplification reduces that representation while trying to preserve the features that matter.

The key question is not simply how many vertices can we remove? It is what geometric error and cartographic change are acceptable for this use?

## Douglas–Peucker: maximum deviation

Douglas–Peucker (also called Ramer–Douglas–Peucker) starts with the endpoints of a line. It finds the interior vertex furthest from the segment joining those endpoints.

- If the maximum distance is no greater than tolerance ε, replace the chain with the endpoint segment.
- Otherwise retain the furthest vertex and recursively simplify the two subchains.

For a point P and segment AB, use distance to the finite segment, not the infinite supporting line:

~~~text
v = B - A
t = clamp(dot(P - A, v) / dot(v, v), 0, 1)
Q = A + t v
distance = ||P - Q||
~~~

This matters when the perpendicular projection falls beyond an endpoint. The tolerance has the same units as the coordinates. A tolerance of 10 means 10 metres only when coordinates use a suitable metre-based CRS. Applying it directly to longitude/latitude degrees is usually not a meaningful ground-distance rule.

## Visvalingam–Whyatt: effective area

Visvalingam–Whyatt assigns each interior vertex the area of the triangle formed by it and its current neighbours. The vertex with the smallest effective area is removed first; neighbouring triangles are then recomputed.

For consecutive vertices A, B, C:

$$
A_{triangle}=\frac{1}{2}|(B-A)\times(C-A)|
$$

The algorithm produces an importance ordering. A threshold is an area, with squared coordinate units—not a distance tolerance.

A common implementation uses a priority queue and linked predecessor/successor relationships. To make the importance sequence monotonic, the effective area assigned at removal is at least the previous removal area's value.

The 1993 Visvalingam–Whyatt paper describes the effective-area approach and compares it with Douglas–Peucker. The methods express different notions of importance; equal numeric thresholds are not comparable.

## Compare the models

~~~mermaid
flowchart TD
    A[Original ordered vertices] --> B{Choose importance model}
    B --> C[Douglas–Peucker]
    B --> D[Visvalingam–Whyatt]
    C --> E[Keep points beyond maximum deviation]
    D --> F[Remove smallest effective-area points]
    E --> G[Simplified line]
    F --> G
    G --> H[Check shape, topology and application error]
~~~

## What these algorithms do not guarantee

- A small local deviation does not guarantee that a road network remains connected.
- Simplifying each polygon independently can create gaps and overlaps between shared boundaries.
- A distance tolerance does not define a cartographic scale by itself.
- A visually plausible output is not necessarily suitable for measurement or legal boundaries.
- Neither basic line algorithm automatically preserves topology across a layer.

For polygon coverages, use a topology-aware generalisation workflow. For example, simplify shared arcs once and reuse them for adjacent polygons, or use a library operation explicitly designed to preserve topology. Validate the resulting coverage after processing.

## Snap rounding is different

Snap rounding is a precision/topology technique that maps coordinates and segment intersections to a declared grid under a specific noding model. It is not a synonym for Douglas–Peucker or Visvalingam simplification. It can change geometry to make a finite-precision arrangement consistent; it should not be sold as a vertex-reduction algorithm.

## Implementation and reproducibility

The teaching package implements Douglas–Peucker and Visvalingam–Whyatt for open 2D polylines. It preserves endpoints and documents tolerance units. It does not implement topology-preserving polygon simplification or snap rounding.

- [Runnable implementation](../../implementations/python/line-simplification/README.md)
- [Step-by-step walkthrough](../../implementations/python/line-simplification/implementation-walkthrough.md)
- [Tests](../../implementations/python/line-simplification/test_simplification.py)

## Try it

Use a detailed river centreline and simplify it with both methods. Compare retained vertex count, maximum perpendicular deviation, total line length, Hausdorff distance and visual shape at two map scales.

Then simplify the two polygons on either side of a shared boundary independently. Inspect whether a gap or overlap appears. Explain why preserving one line's shape is not the same as preserving a polygon coverage.

## References

- Douglas, D. H. and Peucker, T. K. (1973), [Algorithms for the reduction of the number of points required to represent a digitized line or its caricature](https://doi.org/10.3138/FM57-6770-U75U-7727), Cartographica, 10(2), 112–122.
- Visvalingam, M. and Whyatt, J. D. (1993), [Line generalisation by repeated elimination of points](https://doi.org/10.1179/000870493786962263), The Cartographic Journal, 30(1), 46–51.
- [ArcGIS Pro: How Simplify Line works](https://pro.arcgis.com/en/pro-app/3.4/tool-reference/cartography/how-simplify-line-works.htm).
- [UCGIS GIS&T Body of Knowledge: Point, Line, and Area Generalization](https://gistbok-ltb.ucgis.org/current/concept/DM-06-085).

**Scope:** this record covers open-line simplification. Polygon topology preservation, Wang–Müller, weighted effective area, simplification hierarchies and snap rounding require separate records.


## Additional algorithms in the teaching package

The package now also includes two separately named simplifiers:

- **Reumann–Witkam:** a moving-strip method. The implementation documents its infinite-strip distance, restart and endpoint conventions; these details must be matched when comparing with another software implementation.
- **Lang:** a look-ahead method. At each retained anchor it tests candidate endpoints within a configured number of vertices and chooses the furthest candidate for which all intervening points remain within the distance tolerance of the finite baseline segment.

These methods have different decision rules from Douglas–Peucker and Visvalingam–Whyatt. Lang's look-ahead is a vertex count, not a map distance. The package remains limited to open planar lines and does not preserve topology across coverages.

- [Runnable implementations and tests](../../implementations/python/line-simplification/README.md)
- [Four-algorithm walkthrough](../../implementations/python/line-simplification/implementation-walkthrough.md)
- [Simplification comparison lab](../../notebooks/line-simplification-lab.ipynb)


## Reumann–Witkam, Lang and Opheim

These extended-local algorithms should not be merged into one generic simplifier.

- **Reumann–Witkam** moves a strip in the direction of the initial tangent and retains the last point in each strip section.
- **Lang** uses a fixed look-ahead count and checks the distance of intermediate points to a candidate baseline segment.
- **Opheim** adds minimum and maximum distance constraints to a corridor search. The implementation in this repository explicitly defines a strip half-width and Euclidean min/max radii; it is a bounded teaching variant, not a reproduction of the road-network-specific improved Opheim method.

The Opheim method is described in the cartographic generalisation literature as a constrained search region based on the Reumann–Witkam corridor with minimum and maximum distance constraints. See Clayton's NOAA review and the later road-network study by Guo et al. The latter's improved Opheim variant adds semantic critical-point and topology handling; those additions are not part of this implementation.

- [Opheim implementation and tests](../../implementations/python/line-simplification/README.md)
