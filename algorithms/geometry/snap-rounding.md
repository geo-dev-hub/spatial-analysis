# Snap rounding: make an intersecting arrangement work on a fixed grid

- **Stable ID:** SA-GEO-SNAP-ROUNDING
- **Domain:** Computational geometry / robust geometric computation
- **Status:** research-backed lesson with an exact-arithmetic teaching noder
- **Version:** 0.1
- **Source inventory location:** Compendium, section 1, “Core GIS: geometry, indexing, proximity, networks, routing”, page 1; listed under simplification and generalisation
- **Related records:** segment intersection, Bentley–Ottmann, precision models, polygon overlay, robust predicates, planar arrangements
- **Prerequisites:** line segments, segment intersection, rational arithmetic, coordinate grids

## 1. The problem: rounding vertices is not enough

A geometry engine may need coordinates on a fixed precision grid. This can happen when data comes from different sources, when overlay operations produce extremely close vertices, or when a file format or downstream system requires a defined coordinate precision.

A tempting shortcut is to round every input coordinate independently. That can change the geometry's relationships. Two segments that met before rounding may no longer meet afterwards; two segments that were separate may become coincident; a narrow gap may collapse.

Snap rounding addresses a more specific problem. It starts with the arrangement of the input segments, identifies arrangement vertices (input endpoints and segment intersections), maps those vertices to grid locations, and reroutes segments through the grid cells associated with those vertices.

The cells associated with arrangement vertices are called **hot pixels**.

## 2. What is a hot pixel?

Imagine a square grid whose cell centres have integer coordinates. A hot pixel is a grid cell whose centre is the grid point selected for an arrangement vertex.

The geometric sequence is:

1. Find a vertex in the original segment arrangement.
2. Identify the pixel containing that vertex.
3. Mark that pixel as hot.
4. For every original segment that intersects a hot pixel, route the snapped segment through that pixel's centre.

This means a segment can acquire a new vertex even if that point was not an endpoint in the input. The new vertex is introduced so that the rounded arrangement records the influence of the original arrangement vertex.

flowchart TD
    A["Input segments at original precision"] --> B["Find endpoints and segment intersections"]
    B --> C["Map arrangement vertices to grid cells"]
    C --> D["Mark those cells as hot pixels"]
    D --> E["Find every segment that intersects a hot pixel"]
    E --> F["Order hot-pixel centres along each segment"]
    F --> G["Build snapped polylines and noded edges"]

## 3. The geometric model

Let the grid spacing be \(g>0\). Transform a coordinate \((x,y)\) into grid units:

\[
(x',y')=\left(\frac{x}{g},\frac{y}{g}\right).
\]

The grid centres now have integer coordinates. A hot pixel centred at integer point \((i,j)\) is represented in this teaching implementation by the closed square:

\[
[i-\tfrac12,i+\tfrac12]\times[j-\tfrac12,j+\tfrac12].
\]

For a point \(p=(x',y')\), the hot-pixel centre is selected by rounding each coordinate to its nearest integer. Ties are not left to a language default: this implementation sends exact half-grid ties toward positive infinity.

The segment is rerouted through the centres of all hot pixels it intersects. The output is therefore a polyline whose vertices lie on the precision grid.

## 4. Why the order of operations matters

The essential sequence is not “round the coordinates and then check what happened”. It is:

1. Compute the original arrangement vertices.
2. Determine which grid cells those vertices activate.
3. Find every input segment affected by those hot pixels.
4. Route those segments through the corresponding pixel centres.

The original intersection coordinates must be available before snapping. Otherwise, an intersection that falls between grid points can disappear before the algorithm has a chance to create its hot pixel.

For a pair of non-parallel segments \(p+tr\) and \(q+us\), the intersection parameters can be calculated with cross products:

\[
t=\frac{(q-p)\times s}{r\times s},
\qquad
u=\frac{(q-p)\times r}{r\times s}.
\]

When \(0\leq t\leq1\) and \(0\leq u\leq1\), the segments meet. Exact rational arithmetic keeps the constructed intersection exact until the grid-mapping step.

Collinear overlaps need separate handling: their shared endpoints are arrangement vertices too. Endpoint contacts must also be included.

## 5. A worked example

Consider two segments:

\[
s_1:(0,0)\rightarrow(2,2)
\]

\[
s_2:(0,2)\rightarrow(2,0).
\]

Their exact intersection is \((1,1)\), which is already a grid centre when \(g=1\). The pixel centred at \((1,1)\) is hot. Both segments intersect that hot pixel, so both snapped polylines pass through the same centre.

Now consider a crossing at a fractional coordinate. The intersection is still computed exactly first; only then is it assigned to its hot pixel. The hot-pixel centre becomes a shared node in the snapped output.

## 6. Implementation in this repository

The accompanying [Python teaching package](../../implementations/python/snap-rounding-noder/README.md) uses:

- Python's arbitrary-precision integers and fractions.Fraction for exact arithmetic;
- pairwise segment comparisons to discover arrangement vertices;
- an exact Liang–Barsky interval clip to test segment/hot-pixel intersection;
- a documented nearest-grid tie rule;
- source-segment identifiers on the resulting noded edges.

The implementation is deliberately small enough to inspect. It accepts zero-length segments as point-like inputs and records their hot pixel.

## 7. Complexity and production algorithms

The teaching implementation is intentionally not output-sensitive. For \(n\) input segments and \(H\) distinct hot pixels, it performs pairwise segment comparisons and scans the hot-pixel set for each segment. Its broad cost is:

\[
O(n^2+nH),
\]

excluding the bit complexity of exact rational arithmetic.

Research algorithms improve the segment/pixel search and can achieve output-sensitive or intersection-sensitive bounds. Hershberger's 2006 paper develops improved output-sensitive snap-rounding algorithms. De Berg, Halperin and Overmars describe an intersection-sensitive approach. These are not the algorithms implemented in this package.

## 8. Important variants and guarantees

“Snap rounding” is not one interchangeable implementation recipe.

- **Classical snap rounding** routes segments through hot pixels associated with arrangement vertices.
- **Iterated snap rounding** adds a separation condition so a vertex is not arbitrarily close to a non-incident edge. This improves robustness in one respect, while its approximation behaviour must also be considered.
- **Iterated snap rounding with bounded drift** addresses the risk that repeated rerouting can move the approximation too far from the original geometry.
- **Snap rounding with restore** is another variant aimed at robust geometric datasets and topological structure.

The choice depends on the application's requirements. A method that improves separation may change approximation error; a method that preserves a particular topological property may not minimise geometric displacement.

## 9. What this package does not claim

The included implementation is a transparent teaching baseline, not a production noder. It does not implement the indexed segment/pixel intersection machinery or the proven performance bounds of the research algorithms. Its closed-pixel convention can include both adjacent pixels when a segment lies exactly on a pixel boundary; equal projected positions use a deterministic lexicographic order.

The package therefore does not claim a complete proof of topology preservation for every degenerate arrangement. Do not treat its output as interchangeable with JTS, GEOS, CGAL or another precision-reduction implementation. Compare the actual precision model, boundary policy, noding contract and guarantees before choosing a production tool.

## 10. Where to go next

- Revisit [segment intersection](segment-intersection.md) to understand the exact predicates used to find arrangement vertices.
- Read [Bentley–Ottmann](bentley-ottmann.md) for a sweep-line approach to reporting many intersections.
- Compare [precision models](precision-models.md) with snap rounding: fixed-grid coordinate reduction is not the same operation as noding an arrangement.
- Study [polygon overlay](overlay-operations.md) to see why robust noding matters before polygon operations.
- Complete the [snap-rounding exercise](../../exercises/snap-rounding-noder.md) and run the visual lab.

## References

- Hobby, J. D. (1999). Practical segment intersection with finite precision output. *Computational Geometry*, 13(4), 199–214. https://doi.org/10.1016/S0925-7721(99)00021-8
- Hershberger, J. (2006). Improved output-sensitive snap rounding. *Proceedings of the Twenty-Second Annual Symposium on Computational Geometry*, 357–366. https://doi.org/10.1145/1137856.1137909
- Halperin, D., & Packer, E. (2002). Iterated snap rounding. *Computational Geometry*, 23(2), 209–225. https://doi.org/10.1016/S0925-7721(01)00064-5
- de Berg, M., Halperin, D., & Overmars, M. (2007). An intersection-sensitive algorithm for snap rounding. *Computational Geometry*, 36(3), 159–165. https://doi.org/10.1016/j.comgeo.2006.03.002
- Belussi, A., Migliorini, S., Negri, M., & Pelagatti, G. (2016). Snap rounding with restore: An algorithm for producing robust geometric datasets. *ACM Transactions on Spatial Algorithms and Systems*, 2(1), Article 1. https://doi.org/10.1145/2811256
- Bhattacharya, B. K., & Sember, J. (2007). Efficient snap rounding with integer arithmetic. *Proceedings of the Canadian Conference on Computational Geometry*. https://cccg.ca/proceedings/2007/07a1.pdf
