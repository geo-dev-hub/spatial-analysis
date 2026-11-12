# Point in polygon: is this point inside the shape?

- **Stable ID:** `SA-GEO-POINT-IN-POLYGON`
- **Domain:** Computational geometry / point location
- **Status:** research draft with tested teaching implementation
- **Version:** 0.1
- **Source inventory location:** Compendium, section 1, “Core GIS: geometry, indexing, proximity, networks, routing”, page 1; listed as point-in-polygon (ray casting, winding number)
- **Related records:** polygon intersection, segment intersection, point location, polygon validity, spatial indexing
- **Prerequisites:** Cartesian coordinates, line segments, polygon rings

## 1. Start here

You have a point on a map and a boundary around an area. Is the point inside that area?

That question appears in everyday spatial work: which service zone contains this address? Is a school inside a planning boundary? Does a GPS position fall within a park, parcel or flood extent?

The task sounds simple, but there is an important detail: a point can be inside, outside, or exactly on the boundary. A reliable method needs to make that distinction deliberately.

## 2. The problem

Given a point (p) and a polygon (P), determine the location of (p) relative to (P).

For a simple polygon, a useful result model is:

- **inside** — the point lies in the polygon's interior;
- **outside** — the point lies in the exterior;
- **boundary** — the point lies on an edge or vertex.

Some software predicates combine or exclude boundary cases differently. For example, a strict containment predicate and a coverage predicate answer different questions. Never assume that the word “inside” has identical boundary semantics across APIs.

## 3. The simple idea: count crossings

Imagine drawing a horizontal ray from the point to the right. Each time the ray crosses a polygon edge, you switch your answer: outside becomes inside, and inside becomes outside.

- An even number of crossings means outside.
- An odd number of crossings means inside.

This is the **even–odd rule**, also called ray crossing or the crossing-number method. The hard part is deciding exactly what counts as a crossing when the ray meets a vertex or runs along an edge. A consistent half-open edge convention prevents a shared vertex from being counted twice.

A second important approach uses the **winding number**: how many times, and in which direction, the polygon boundary winds around the test point. Under the nonzero winding rule, a nonzero winding number indicates the point is inside. The even–odd and winding-number approaches are closely related, but they can define the interior of self-intersecting rings differently.

### See the crossing idea

![A point-in-polygon illustration showing a query point and polygon boundary](https://upload.wikimedia.org/wikipedia/commons/2/2d/Point_in_polygon_problem.svg)

*Figure 1. “Point in polygon problem,” by Adam Majewski, Wikimedia Commons. Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The figure is reproduced unchanged; the licence requires attribution and share-alike for adaptations. [Source and licence record](https://commons.wikimedia.org/wiki/File:Point_in_polygon_problem.svg).*

## 4. Formal foundations

Let the polygon boundary be a closed sequence of vertices (v_0, v_1, \ldots, v_{n-1}), with the final edge connecting (v_{n-1}) to (v_0). A point-location algorithm examines the relationship between (p) and these boundary edges.

For ray crossing, let (c(p,P)) be the number of valid intersections between a ray from (p) and the polygon boundary. Under the even–odd rule:

[
p \text{ is inside } P \iff c(p,P) \bmod 2 = 1
]

The boundary test must be performed separately if the desired output distinguishes boundary from interior and exterior.

For the winding-number approach, the oriented angle changes around the test point are accumulated and divided by (2\pi). The resulting integer captures the net number of turns around the point. The nonzero rule classifies nonzero winding as interior.

## 5. Ray-crossing method

For a simple ring:

1. Remove a repeated closing vertex if the input representation includes one; treat the ring as implicitly closed.
2. Check whether the point lies on any edge. If so, return boundary.
3. Initialise the crossing parity as outside.
4. Visit each edge, including the closing edge.
5. Consider only edges whose vertical range straddles the point's y-coordinate, using a half-open comparison so vertices are not double-counted.
6. Compute where the edge crosses the horizontal line through the point.
7. If that crossing lies to the right of the point, toggle the parity.
8. Return inside for odd parity and outside for even parity.

This is the teaching implementation's method. It uses direct floating-point comparisons and is intentionally limited to one simple ring.

## 6. Correctness and guarantees

For a simple, non-self-intersecting closed ring, the parity of ray crossings gives the inside/outside classification when edge and vertex cases are handled consistently. The boundary is classified separately by the teaching implementation.

For self-intersecting rings, “the interior” is not uniquely determined until a fill rule is chosen. Even–odd and nonzero winding rules can produce different classifications. A dossier or software API must state which rule it uses.

## 7. Complexity

The teaching implementation checks every edge once. For a ring with $n$ edges:

- **Time:** $O(n)$.
- **Additional space:** $O(n)$ in this implementation because it materialises the vertex sequence; the edge scan itself requires $O(1)$ additional working space.

If many points are tested against the same polygon, preprocessing or spatial indexing can reduce the work per query. That is a different algorithmic setting and should be benchmarked separately.

## 8. Numerical and geometric considerations

- **Boundary tolerance:** exact floating-point equality is not a general-purpose robust boundary policy. A tolerance must be tied to coordinate units, data accuracy and the intended application.
- **Vertex crossings:** use a consistent half-open rule; naïvely counting every edge endpoint can double-count vertices.
- **Horizontal edges:** a horizontal edge does not straddle the ray's y-coordinate under the half-open test, but it still needs to be considered by the separate boundary test.
- **Self-intersections:** specify even–odd or nonzero winding semantics.
- **Holes and multiple rings:** define whether the polygon representation uses shell/hole roles or a fill rule across rings. The teaching code here handles one ring only.
- **CRS:** point-in-polygon is a planar topological test in this example. Transform geographic data into a suitable planar coordinate system when the surrounding workflow requires planar geometry operations; be explicit about the CRS.
- **Invalid rings:** repeated, collapsed or self-crossing edges may violate the simple-ring assumptions.

## 9. Edge cases and failure modes

| Case | Expected behaviour | Test or evidence |
|---|---|---|
| Point well inside | Inside | Unit test |
| Point well outside | Outside | Unit test |
| Point on an edge | Boundary | Unit test |
| Point on a vertex | Boundary | Unit test |
| Concave polygon | Correct parity classification | Unit test |
| Explicitly closed ring | Same classification as implicitly closed ring | Unit test |
| Horizontal edge | No false parity toggle; boundary still detected | Test boundary case |
| Ray through a vertex | Count consistently under half-open convention | Requires dedicated adversarial fixtures |
| Self-intersecting ring | Depends on selected fill rule | Not supported by teaching implementation |
| Polygon with holes | Depends on ring structure and fill rule | Not supported by teaching implementation |

## 10. Try it

Use the square with corners (0,0), (4,0), (4,4), (0,4). Test points (2,2), (5,2) and (4,2). Before running the code, decide which should be inside, outside and boundary.

Then try a concave polygon. A point can be inside its bounding box and still be outside the polygon.

## 11. Implementations

| Library / implementation | Relevant API / method | Notes |
|---|---|---|
| Shapely | `contains`, `covers`, `contains_xy`, `intersects` | Distinct predicates have distinct boundary semantics; consult the specific API documentation |
| GEOS / JTS | Point-in-area and point-location operations | Library behaviour should be recorded with the exact version |
| Teaching implementation | Ray crossing in Python | One simple ring; boundary returned separately; exact float comparisons |

The [Python ray-crossing tutorial](../../implementations/python/point-in-polygon/README.md) contains the code and tests. It is a transparent educational implementation, not a replacement for robust production geometry libraries.

## 12. How we check the answer

The reference implementation has tests for interior, exterior, edge and vertex cases, concavity, explicit ring closure and invalid ring size. The tests are useful examples, not an exhaustive proof of robustness for arbitrary floating-point coordinates.

## 13. Applications

- Assign a GPS point to an administrative or service area.
- Check whether an address falls within a catchment, parcel or hazard zone.
- Select observations inside a study boundary.
- Support point-in-polygon spatial joins and geofencing.
- Test whether a location belongs to a protected area or planning zone.

## 14. Have a go

1. Move the test point around a square and record when the answer changes.
2. Put the point exactly on each edge and vertex.
3. Replace the square with a concave polygon. Find a point inside the bounding box but outside the polygon.
4. Add a hole and decide how your data model represents it.
5. Draw a self-intersecting ring. Compare the even–odd and nonzero winding interpretations.
6. Explain why a boundary-aware classification is different from a simple Boolean result.

## 15. References

1. Hormann, K. and Agathos, A. (2001). “The Point in Polygon Problem for Arbitrary Polygons.” *Computational Geometry*, 20(3), 131–144. DOI: https://doi.org/10.1016/S0925-7721(01)00012-8. The paper discusses even–odd/ray-crossing and winding-number approaches, including special cases.
2. W. Randolph Franklin, “PNPOLY — Point Inclusion in Polygon Test”: https://wrfranklin.org/Research/Short_Notes/pnpoly.html. A compact ray-crossing implementation with a discussion of vertex handling.
3. Shapely 2.1.2 predicate reference: https://shapely.readthedocs.io/en/2.1.2/predicates.html. Consult individual predicate definitions for boundary semantics.
4. User-supplied *Spatial Analysis Algorithms: Complete Compendium*, section 1, page 1. See [source inventory](../../source-inventory/README.md).

## 16. What remains uncertain

- Which exact boundary policy should each production example adopt?
- Which integer or robust-predicate implementation should be studied next for near-boundary coordinates?
- How should the collection compare shell/hole models with even–odd and nonzero fill rules without conflating them?
- Which spatial-index preprocessing methods should be compared for repeated queries against one polygon?

## Change history

| Version | Date | Change | Author / contributor |
|---|---|---|---|
| 0.1 | 2026-11-13 | Initial research draft with tested teaching implementation | Project draft |
