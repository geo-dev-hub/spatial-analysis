# Offsetting: parallel boundaries, buffers and toolpath geometry

Offsetting constructs a curve or boundary at a specified distance from an input curve. It appears in cartography, CAD, manufacturing, road design, safety zones and computational geometry.

The source inventory says “Offsetting (Clipper)”. That label combines two different things: a geometric operation (offsetting) and a software library family (Clipper). This dossier keeps them separate.

## The geometric idea

For a planar line, an offset at distance d is a parallel curve displaced along a chosen normal direction. For a polygon, a positive offset commonly expands the exterior boundary and contracts holes; a negative offset contracts the exterior and expands holes.

For a closed polygon, the operation is related to a Minkowski sum or difference with a disk of radius |d|, with implementation details depending on the chosen join approximation and geometry model.

Offsetting is not identical to polygon clipping. Clipping constructs Boolean results from input boundaries; offsetting constructs a distance-based envelope around a path or area.

## Join styles change the result

At a corner, the offset edges need to be connected.

| Join | Behaviour | Typical effect |
|---|---|---|
| Miter | Extend adjacent offset edges to their intersection | Sharp corners; acute angles can create long spikes |
| Square | Truncate the corner with a squared join | Bounded, angular corner |
| Bevel | Cut the corner with a straight segment | Simple chamfer |
| Round | Approximate a circular arc around the original vertex | Rounded corner |

For miter joins, a miter limit prevents extreme spikes. The limit is commonly expressed as a ratio relative to the offset distance. Round joins also depend on arc tolerance or approximation resolution.

Open paths have end-cap choices as well: butt, square and round. These are not the same as polygon joins.

## Conceptual pipeline

~~~mermaid
flowchart TD
    A[Input path or polygon] --> B[Validate ring orientation and geometry]
    B --> C[Construct edge normals at offset distance]
    C --> D[Resolve convex and concave joins]
    D --> E[Apply miter limit or arc approximation]
    E --> F[Resolve self-intersections and collapsed parts]
    F --> G[Return offset paths or polygon tree]
    G --> H[Validate output and inspect components]
~~~

This is a conceptual pipeline. Robust libraries include more detailed logic for joins, path orientation, self-intersections, holes, precision and output hierarchy.

## Clipper is a library, not one offset algorithm

Clipper2 provides polygon clipping and offsetting functionality. Its offset API exposes join types (miter, square, bevel and round), end types, miter limits and arc tolerance. Positive and negative offsets of closed paths affect outer contours and holes in opposite directions. Correct path orientation and output interpretation matter.

Do not confuse Clipper's offsetting API with the Sutherland–Hodgman polygon-clipping algorithm. They solve different problems.

## Distance and coordinate units

An offset distance is expressed in the coordinate units supplied to the library. If geometry is in longitude and latitude, a planar offset of 100 is not a 100-metre ground buffer. Project to a suitable local metric CRS or use an explicitly geodesic method when the application requires ground distances over a large or high-latitude area.

## Degeneracies and failure modes

- Narrow corridors can collapse under a negative offset.
- Concave corners can produce complex local geometry.
- Acute convex corners can produce large miter spikes.
- Small holes can disappear during contraction.
- Self-intersections can appear in naïve offset constructions.
- Round joins approximate arcs with segments.
- A result may be empty or contain multiple components.
- Repeated offsets are not generally equivalent to one offset by the sum if intermediate cleanup or discretisation changes the geometry.

## Runnable example

The companion implementation demonstrates a polygon buffer using Shapely/GEOS and makes the join style explicit. This is a reproducible Python teaching route; it is not a binding to Clipper2. The Clipper2 API is documented separately in the references.

- [Implementation and environment](../../implementations/python/polygon-offsetting/README.md)
- [Intern walkthrough](../../implementations/python/polygon-offsetting/implementation-walkthrough.md)
- [Tests](../../implementations/python/polygon-offsetting/test_offsetting.py)

## Try it

Offset a concave polygon by positive and negative distances. Repeat with round, bevel and miter joins. Record input and output area, polygon components, hole count, validity, coordinate units and CRS, miter limit and arc resolution.

Find a narrow corridor that disappears under inward offset. Explain why that is a meaningful geometric result rather than necessarily a software bug.

## References

- [Clipper2 documentation: JoinType](https://www.angusj.com/clipper2/Docs/Units/Clipper/Types/JoinType.htm).
- [Clipper2 documentation: ClipperOffset](https://www.angusj.com/clipper2/Docs/Units/Clipper/Classes/ClipperOffset/ClipperOffset.htm).
- [Clipper2 documentation: EndType](https://www.angusj.com/clipper2/Docs/Units/Clipper/Types/EndType.htm).
- [Shapely buffer reference](https://shapely.readthedocs.io/en/stable/reference/shapely.buffer.html).

**Scope:** the teaching implementation uses Shapely/GEOS. Clipper2-specific integer-path semantics, polygon-tree output and version-specific behaviour must be tested separately before being claimed as implemented.
