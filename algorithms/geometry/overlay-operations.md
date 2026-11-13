# Polygon overlay: intersection, union and difference

Overlay operations combine two geometries according to a spatial relationship. They are among the most useful GIS operations—and among the easiest to misuse when geometry validity, precision and output dimensions are ignored.

## Four questions, four operations

Let $A$ and $B$ be two geometries in the same coordinate space.

**Intersection** keeps what belongs to both:

$$
A \cap B
$$

**Union** keeps what belongs to either:

$$
A \cup B
$$

**Difference** keeps what belongs to the first geometry but not the second:

$$
A \setminus B
$$

**Symmetric difference** keeps what belongs to one geometry but not both:

$$
(A \setminus B) \cup (B \setminus A)
$$

These are set-theoretic definitions. They do not by themselves specify how a computer should construct a valid output geometry.

## What the result can look like

An overlay result is not guaranteed to be one polygon.

- Two polygons may intersect in several disconnected pieces.
- Touching polygons may produce line or point components depending on the operation and result semantics.
- A difference may create holes.
- A union may merge components or preserve separate components.
- Mixed-dimensional inputs can produce outputs containing more than one geometry dimension, subject to the engine's semantics.

Do not infer output type from the input type alone. Inspect the actual result and state whether lower-dimensional components are retained.

## How overlay engines construct results

A common conceptual strategy is:

1. identify candidate boundary segments that can interact;
2. compute segment intersections and node the linework at those points;
3. build a planar arrangement or topology graph;
4. classify directed edges according to their location relative to each input;
5. select the edges that bound the requested set operation;
6. assemble rings and components;
7. validate the result under the chosen geometry model.

This is a conceptual description, not a claim that every geometry engine uses one identical internal implementation. OverlayNG, for example, is a specific implementation with explicit precision-model and noding choices.

## Why noding matters

A planar line arrangement is properly noded when every intersection is represented as a vertex in the linework. If an intersection is missed or computed inconsistently, the topology graph may be wrong.

The segment-intersection and Bentley–Ottmann lessons explain how intersections can be detected. Overlay adds the further task of using those events to construct the boundaries of a set-theoretic result.

## Precision and robustness

The sign of an orientation or intersection test can change when floating-point arithmetic rounds a value near zero. A tiny numerical discrepancy may change whether segments cross, touch or miss each other.

GEOS OverlayNG documents different strategies for floating and fixed precision. Fixed precision uses snap-rounding noding; floating precision may still encounter topology exceptions. The robust overlay path uses a sequence of increasingly robust strategies. These are implementation details, not a guarantee that every malformed input can be repaired or that every chosen precision is appropriate.

A precision grid changes coordinates. Choose it in the context of the data's units and the smallest meaningful feature. Never copy a tolerance from an unrelated dataset.

## Reproducible example with Shapely

```python
from shapely import Polygon

a = Polygon([(0, 0), (4, 0), (4, 3), (0, 3)])
b = Polygon([(2, -1), (5, -1), (5, 2), (2, 2)])

print("intersection:", a.intersection(b).area)
print("union:", a.union(b).area)
print("difference:", a.difference(b).area)
print("symmetric difference:", a.symmetric_difference(b).area)
```

For this example, the expected areas are:

- intersection: 4 square units;
- union: 17 square units;
- difference (A \setminus B): (8);
- symmetric difference: 13 square units;

These values provide a simple arithmetic check, not a complete geometry validation. Add assertions for the output geometry, component count and validity in the implementation suite.

## Invariants worth checking

For valid planar polygon inputs with ordinary area semantics, useful checks include:

$$
\operatorname{area}(A \cup B) +
\operatorname{area}(A \cap B)
=
\operatorname{area}(A) + \operatorname{area}(B)
$$

and

$$
\operatorname{area}(A \setminus B) +
\operatorname{area}(A \cap B)
=
\operatorname{area}(A)
$$

These identities are useful tests for area, but they are not sufficient to prove that the output geometry is topologically correct. Different incorrect geometries can have the same area.

## Input and output contract

Before using overlay in an analytical workflow, state:

- geometry types and dimensions accepted;
- whether inputs must be valid;
- coordinate reference system and units;
- planar versus geodesic interpretation;
- precision model and any grid size;
- behaviour for empty geometries and mixed dimensions;
- whether lower-dimensional topology collapses are included;
- how geometry collections and multiple components are handled;
- software and geometry-engine versions.

The OGC Simple Feature Access standard provides the common geometry model. A library's overlay documentation defines the behaviour of that particular implementation.

## Try it

Use two overlapping polygons and calculate all four operations.

Then change one input at a time:

1. make the polygons disjoint;
2. make one polygon contain the other;
3. make their boundaries touch at one point;
4. make them share an edge;
5. introduce a hole;
6. introduce a narrow sliver or near-coincident edge.

For every case, record the geometry type, component count, area, validity and any exception. Explain which changes are consequences of set theory and which depend on the engine's precision and output rules.

## References

- [OGC Simple Feature Access — Part 1: Common Architecture](https://www.ogc.org/standards/sfa/).
- [GEOS OverlayNG class reference](https://libgeos.org/doxygen/classgeos_1_1operation_1_1overlayng_1_1OverlayNG.html), including the four overlay operations and precision model behaviour.
- [JTS OverlayNGRobust API](https://locationtech.github.io/jts/javadoc/org/locationtech/jts/operation/overlayng/OverlayNGRobust.html), describing the sequence of noding strategies used for robust overlay.
- [Shapely documentation](https://shapely.readthedocs.io/), for the Python API and version-specific behaviour.

**Evidence state:** set-theoretic operation definitions and GEOS precision behaviour are grounded in the cited references. The worked example is a hand-checkable planar rectangle case. Broader robustness claims must remain scoped to the documented GEOS/JTS version.
