# Straight skeleton: shrink a polygon with parallel wavefronts

A straight skeleton is a graph formed by tracing the vertices of a polygon as its edges move inward, each along a line parallel to itself. The wavefront shrinks and changes topology until it disappears. The paths traced by moving wavefront vertices form the straight skeleton.

Unlike the medial axis, the straight skeleton is not defined by Euclidean distance to the boundary. Its geometry comes from a propagation process.

## The wavefront model

Imagine every edge of a simple polygon moving inward at unit speed while remaining parallel to its original supporting line. At each instant, the moving edges form one or more polygonal wavefronts. A wavefront vertex is the intersection of two moving lines, so it travels along the angle bisector of the corresponding edge directions.

The straight skeleton is the union of those vertex trajectories over time.

## Two fundamental events

- **Edge event:** a wavefront edge shrinks to zero length and disappears.
- **Split event:** a reflex wavefront vertex reaches a non-incident wavefront edge, splitting a wavefront component.

Degenerate inputs can produce simultaneous or more complicated events. An implementation must process event ordering and topology changes consistently; a simple animation is not a robust algorithm.

~~~mermaid
flowchart TD
    A[Initialize inward-moving edge wavefronts] --> B[Compute candidate event times]
    B --> C[Process earliest valid event]
    C --> D[Update wavefront topology and vertex trajectories]
    D --> E{Any wavefront remains?}
    E -- Yes --> B
    E -- No --> F[Collect vertex traces as the straight skeleton]
~~~

## What it is useful for

- Mitered polygon offsets and insets.
- Roof construction and extrusion.
- Surface reconstruction and shape modeling.
- Partitioning a polygon into regions associated with its boundary edges.
- Generating structured paths through a polygon.

A straight skeleton can be interpreted as a roof structure in three dimensions: the wavefront time becomes height, and the moving edges sweep out roof facets.

## Straight skeleton versus medial axis

Both structures partition a polygon and are related to angle bisectors, but their definitions differ.

| Property | Medial axis | Straight skeleton |
|---|---|---|
| Definition | Points with multiple closest boundary points | Traces of vertices in a moving parallel-edge wavefront |
| Metric | Euclidean distance | Supporting-line wavefront propagation |
| Edges | May include parabolic arcs | Straight line segments |
| Non-convex polygons | Reflects true boundary clearance | Can deviate from the centre of the region near reflex vertices |
| Typical use | Maximal discs, local width, clearance | Mitered offsets, roofs, polygon partitioning |

For convex polygons, the straight skeleton and medial axis coincide. For general non-convex polygons, they do not. A straight-skeleton bisector may not lie at the Euclidean centre of the polygon.

## Algorithms and implementation scope

A practical construction needs a priority queue of candidate events, a representation of the current wavefront, and robust updates when edges collapse or vertices split other wavefront components. Stale events must be detected because a candidate event can become invalid after an earlier event changes the local topology.

The unrestricted problem is considerably more involved than drawing angle bisectors at polygon vertices. Research includes algorithms based on motorcycle graphs and event structures, as well as specialized algorithms for monotone or orthogonal polygons. Do not transfer a complexity bound from a restricted input family to arbitrary simple polygons.

CGAL provides a 2D straight-skeleton package with polygon offsetting and extrusion operations. Its documentation describes the relationship among straight skeletons, medial axes and Voronoi diagrams, and makes the supported input and kernel assumptions explicit.

## Validation questions

- Does every skeleton arc begin at an input vertex or a valid event node?
- Are edge and split events processed in nondecreasing time?
- Does each wavefront remain a valid collection of polygonal cycles after an event?
- Do the resulting faces partition the input region?
- Are holes and multiple components supported by the selected implementation?
- Are weighted edge speeds being used? If so, the geometry and event behaviour may differ from the unweighted case.

## Follow the learning sequence

- [Medial axis](medial-axis.md) defines the metric skeleton through maximal inscribed discs.
- [Polygon offsetting](offsetting.md) explains practical offsets and precision effects.
- [Straight-skeleton exercise](../../exercises/straight-skeleton.md) asks you to classify events and distinguish wavefront time from Euclidean distance.

## Further reading

- Aichholzer, O., Aurenhammer, F., Alberts, D. and Gärtner, B. (1995), *A novel type of skeleton for polygons*, Journal of Universal Computer Science.
- Held, M. and Huber, S. (2012), *Topology-oriented construction of straight skeletons*, Computer-Aided Design.
- [CGAL 5.6.2 Straight Skeleton and Polygon Offsetting manual](https://doc.cgal.org/5.6.2/Straight_skeleton_2/index.html).
- [Straight skeletons and motorcycle graphs](https://www.sthu.org/research/straightskeleton/), a research overview with construction background.
