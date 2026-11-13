# Point location: which face contains this coordinate?

Point-in-polygon asks whether a point lies inside one polygon. Planar point location is broader: given a planar subdivision, determine which face contains a query point.

A subdivision may contain many vertices, edges and faces. The challenge is to answer repeated queries without scanning every edge each time.

## The query model

Let a planar subdivision be formed by non-crossing segments that partition a region into faces. A point-location data structure preprocesses that subdivision and answers: which face contains query point q=(x,y)?

The data structure must define what happens when q lies exactly on an edge or vertex. A production API should return a boundary classification or documented tie-breaking result rather than silently assigning the point to an arbitrary face.

## Slab method

The slab method draws vertical decomposition lines through the x-coordinates of subdivision vertices. These event lines divide the plane into vertical slabs. Within the open interior of a slab, the vertical order of non-crossing edges is fixed.

A query conceptually proceeds as follows:
1. binary-search x-event coordinates to identify the slab;
2. evaluate edges crossing that slab at query x;
3. binary-search their y-order to find the interval containing query y;
4. return the face label associated with that interval;
5. handle event lines and boundary points under an explicit convention.

With a straightforward static representation, preprocessing and storage can be O(n²), because many edges can cross many slabs. A query can be O(log n) with indexed slab and interval structures. More sophisticated representations reduce space or improve construction costs; the exact bound depends on the model and data structure.

The slab approach is intuitive, but a naïve implementation that sorts all crossing edges for every query is not a preprocessed point-location data structure.

## Trapezoidal maps

A trapezoidal decomposition extends each segment endpoint vertically until it meets another segment or a bounding box. The resulting cells are trapezoids, with degeneracies handled by the model. A search structure stores decisions based on x-coordinates, y-coordinates and segment comparisons.

Randomized incremental construction inserts segments in random order and updates the trapezoidal map and its search structure. Seidel's 1991 paper gives an influential randomized construction and expected bounds for trapezoidal decomposition and point location. Later work studies stronger worst-case query and storage guarantees.

~~~mermaid
flowchart TD
    A[Planar subdivision] --> B[Preprocess]
    B --> C[Slab decomposition]
    B --> D[Randomized trapezoidal map]
    C --> E[Search by x then y]
    D --> F[Search DAG]
    E --> G[Containing face]
    F --> G
    G --> H[Boundary and degeneracy policy]
~~~

## What must be specified

- Are segments pairwise interior-disjoint?
- Are vertical segments allowed?
- Are endpoints shared?
- Is the subdivision bounded or does it include an unbounded face?
- How are collinear or coincident edges represented?
- What is the boundary-query result?
- Is the structure static or does it support updates?
- Are expected or worst-case bounds required?

Trapezoidal-map analysis does not automatically apply to arbitrary intersecting line segments without first defining a planar subdivision and handling intersections.

## Do not confuse these problems

| Problem | Query | Typical method |
|---|---|---|
| Point in polygon | Is q inside one ring? | Ray casting, winding number |
| Point location | Which subdivision face contains q? | Slab structures, trapezoidal map |
| Nearest-neighbour search | Which stored point is closest to q? | k-d tree, R-tree variants |
| Spatial containment query | Which indexed geometries contain q? | Spatial index plus exact predicate |

An R-tree can help find candidate polygons, but candidate filtering is not the same as a planar point-location structure with a face search guarantee.

## Implementation status

A tested [static slab point locator](../../implementations/python/point-location/README.md) now covers a deliberately restricted model: valid, pairwise interior-disjoint polygon faces with linear rings. It stores edge crossing groups per x-slab and uses binary search for interior-slab queries. Event-line queries use an explicit boundary-aware fallback. This is not a randomized trapezoidal map and does not claim Seidel's expected bounds; the advanced structure remains a separate implementation target.

## Try it

Draw a planar subdivision with at least six faces. Add a vertical decomposition through every vertex x-coordinate. Choose query points strictly inside each face, on a vertical decomposition line, on a non-vertical edge, on a vertex and outside the bounded subdivision.

For each point, state the expected face or boundary result. Explain why a data structure must preserve edge order within each open slab. Then run the [interactive point-location lab](../../notebooks/point-location-lab.ipynb) to inspect the event lines, crossing groups and hole handling.

## References

- Seidel, R. (1991), [A simple and fast incremental randomized algorithm for computing trapezoidal decompositions and for triangulating polygons](https://doi.org/10.1016/0925-7721(91)90012-4), Computational Geometry, 1, 51–64.
- Hemmer, M., Kleinbort, M. and Halperin, D. (2016), [Optimal randomized incremental construction for guaranteed logarithmic planar point location](https://doi.org/10.1016/j.comgeo.2016.07.006), Computational Geometry, 58, 110–123.

**Scope:** this record introduces static planar point location and the two source-listed structures. Dynamic point location and a complete trapezoidal-map implementation remain open.
