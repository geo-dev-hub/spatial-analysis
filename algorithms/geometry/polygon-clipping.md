# Polygon clipping: keeping the part inside a boundary

Polygon clipping answers a familiar question: given a shape and a clipping region, which part of the shape remains inside that region?

It is easy to confuse polygon clipping with every kind of polygon overlay. They are related, but the problem assumptions and output requirements differ. The right algorithm depends on the shape of the clipping window, whether the subject may be concave or self-intersecting, whether disconnected output is possible, and which Boolean operation is required.

## The practical question

Imagine a parcel boundary extending beyond a project area. We want the part of the parcel inside the project boundary. That is an intersection:

[
P_{\mathrm{out}} = P_{\mathrm{subject}} \cap P_{\mathrm{clip}}
]

The result may be empty, one polygon, or multiple polygon components. A clipping routine that assumes a single connected output may not represent every valid case.

## The first distinction: what is the clipping region?

A polygon is convex when the line segment between any two points in its interior stays inside it. A concave polygon has an inward indentation.

This matters because some classic algorithms clip against a sequence of half-planes. A convex clipping polygon can be represented as the intersection of the inside half-plane of each edge. A general concave clipping region cannot be treated as one such intersection.

## Sutherland–Hodgman

Sutherland–Hodgman processes the subject polygon against the clipping polygon one edge at a time. Each clipping edge defines an inside half-plane. The output vertex list from one stage becomes the input to the next.

For each subject edge from (S) to (E), classify the endpoints relative to the current clipping boundary:

| Start (S) | End (E) | Output |
|---|---|---|
| inside | inside | (E) |
| inside | outside | intersection |
| outside | inside | intersection, then (E) |
| outside | outside | nothing |

The algorithm is elegant because each stage is local and can be implemented as a pipeline. Its classical use assumes a convex clipping window. Do not present it as a general solution for arbitrary polygon–polygon Boolean overlay.

### Boundary intersection

For a subject segment (S + t(E-S)) and a clipping line, the crossing parameter (t) can be found by solving the line equation. A robust implementation must still define how points exactly on the clipping boundary are classified and how parallel or coincident edges are handled.

## Other algorithm families

The source compendium lists several families. They should not be treated as interchangeable names for one method.

| Method | Useful distinction | Important qualification |
|---|---|---|
| Sutherland–Hodgman | Repeated half-plane clipping; clear for convex clipping windows | Not a general arbitrary polygon Boolean engine |
| Weiler–Atherton | Traverses subject and clip boundaries through intersection events | Requires careful handling of topology and degeneracies |
| Vatti | General polygon clipping framework supporting broad polygon configurations and Boolean operations | Implementation details and fill rules matter |
| Greiner–Hormann | Linked-list approach for clipping arbitrary 2D polygons | Degenerate and coincident cases require explicit treatment |
| Liang–Barsky | Parametric line clipping, especially useful for rectangular windows | It is line clipping, not a general polygon overlay algorithm |

The comparison is not a universal performance ranking. A method's suitability depends on its input contract and the exact output required.

## A conceptual event-based workflow

General polygon clipping often needs more than classifying vertices. It must locate boundary intersections, insert them into the boundary representations, classify entry and exit events, and traverse the boundaries to construct the result.

```text
Validate and prepare both boundaries
             |
Find boundary intersections
             |
Insert intersection events in order
             |
Classify entry / exit / coincident cases
             |
Traverse the appropriate boundary arcs
             |
Assemble result rings and components
             |
Validate output and preserve provenance
```

This is a conceptual outline, not pseudocode for every clipping family. Vatti, Weiler–Atherton and Greiner–Hormann have different data structures and event rules.

## The difficult cases

A convincing demonstration should include more than two overlapping rectangles.

- **No intersection:** one polygon is outside the other.
- **Containment:** one polygon lies entirely inside the other.
- **Multiple components:** the intersection is disconnected.
- **Vertex touch:** boundaries meet at one point.
- **Shared edge:** boundaries coincide over a segment.
- **Collinear overlap:** edge ordering and event classification become delicate.
- **Holes:** output rings need correct shell/hole roles.
- **Self-intersection:** the fill rule and input contract must be explicit.
- **Near-coincidence:** floating-point rounding can change topology.

A lesson that omits these cases may teach the happy path while leaving the most important implementation questions hidden.

## Clipping is not always overlay

In graphics, clipping may be a rendering operation against a view window. In GIS, polygon overlay usually means constructing a topologically meaningful geometry for intersection, union, difference or symmetric difference.

A rectangular viewport clip and a cadastral parcel overlay may use related geometry machinery, but their requirements are not identical. GIS output may need holes, multiple components, consistent topology, a declared precision model and valid geometry semantics.

## Practical implementation

For production geospatial work, use a maintained geometry engine unless implementing the algorithm itself is the learning objective. Shapely exposes intersection and other overlay operations through GEOS; this is a library-backed operation, not a from-scratch Sutherland–Hodgman or Vatti implementation.

```python
from shapely import Polygon

subject = Polygon([
    (0, 0), (6, 0), (6, 4), (0, 4)
])
window = Polygon([
    (2, -1), (5, -1), (5, 5), (2, 5)
])

clipped = subject.intersection(window)
print(clipped.wkt)
```

Record the input validity, CRS, units, precision policy, Shapely version and GEOS version when turning this into a reproducible example.

## Try it

Draw a concave subject polygon and clip it against a convex rectangle. Then reverse the roles: use a concave clipping region.

Before running code, predict:

1. whether the result is empty, connected or disconnected;
2. which vertices are retained;
3. where new vertices are introduced;
4. whether a single vertex sequence can represent the result without ambiguity.

Compare the predictions with a library overlay result. Explain why the second case needs a more general algorithmic contract than the first.

## References

- Sutherland, I. E. and Hodgman, G. W. (1974), [“Reentrant polygon clipping”](https://doi.org/10.1145/360767.360802), Communications of the ACM.
- Greiner, G. and Hormann, K. (1998), [“Efficient clipping of arbitrary polygons”](https://doi.org/10.1145/274363.274364), ACM Transactions on Graphics.
- [A Brief Survey of Clipping and Intersection Algorithms](https://doi.org/10.15388/23-INFOR508), a review of polygon clipping and intersection families.
- [GEOS OverlayNG documentation](https://libgeos.org/doxygen/classgeos_1_1operation_1_1overlayng_1_1OverlayNG.html), for modern geometry overlay semantics and precision behaviour.

**Evidence state:** the convex-window scope of Sutherland–Hodgman and the arbitrary-polygon scope of Greiner–Hormann are supported by the cited primary literature. Vatti's exact guarantees and degenerate-case behaviour require a dedicated review of the original paper and the chosen implementation before a comparative claim is published.
