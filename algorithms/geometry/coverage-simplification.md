# Polygon coverage simplification: preserve shared boundaries

A polygon layer can contain individually valid features and still be an invalid coverage. Adjacent polygons may share boundaries. If each feature is simplified independently, the two copies of a shared edge can move differently, creating gaps or overlaps.

Coverage simplification treats the shared boundary as shared information.

## The coverage contract

A polygon coverage is a collection of polygonal faces whose interiors do not overlap and whose shared boundaries are exactly edge-matched. This is stronger than requiring every polygon to be valid on its own.

Before simplification, establish:
- a consistent coordinate reference system and meaningful tolerance units;
- valid polygon rings and holes;
- no overlapping polygon interiors;
- identical shared-edge geometry in adjacent faces;
- a policy for gaps, outer boundaries and narrow corridors.

## Per-feature versus coverage-aware simplification

~~~mermaid
flowchart TD
  A[Polygon layer] --> B{How are boundaries represented?}
  B -->|Each feature independently| C[Per-feature simplification]
  B -->|Shared edges are coordinated| D[Coverage simplification]
  C --> E[Adjacent edges may diverge]
  D --> F[Shared edges simplified consistently]
  E --> G[Check for gaps and overlaps]
  F --> H[Validate coverage again]
~~~

A per-feature topology-preserving option protects the topology of each input geometry. It does not necessarily preserve the relationships between separate features. A coverage-aware operation is designed for the layer-level shared-edge contract.

## Runnable implementation

The repository example wraps Shapely's `coverage_simplify` operation, backed by GEOS 3.12 or newer. It checks the input coverage, applies simplification and checks the output coverage.

- [Implementation](../../implementations/python/coverage-simplification/README.md)
- [Intern walkthrough](../../implementations/python/coverage-simplification/implementation-walkthrough.md)
- [Tests](../../implementations/python/coverage-simplification/test_coverage_simplification.py)

This is a library-backed teaching implementation, not a new simplification algorithm. It does not repair invalid input or decide whether a tolerance is appropriate for a legal or scientific boundary.

## Snap rounding is a separate problem

Snap rounding is not another name for simplification. It is a precision and noding technique for arrangements of line segments. A snap-rounding noder constructs a consistent arrangement under a declared grid model. It may move coordinates and introduce nodes; its purpose is robust finite-precision topology, not simply reducing vertex count.

See [precision models and snap rounding](precision-models.md) for the distinctions and implementation status.

## Practical investigation

1. Create two adjacent polygons with a shared boundary containing several bends.
2. Simplify each polygon independently and inspect the shared edge.
3. Run coverage-aware simplification on the same inputs.
4. Check coverage validity, total area, component count and shared-edge equality.
5. Repeat with narrow corridors, holes and multiple map scales.
6. Explain why a valid output can still be unsuitable for the intended application.

## References

- [Shapely: coverage_simplify](https://shapely.readthedocs.io/en/stable/reference/shapely.coverage_simplify.html).
- [Shapely: coverage_is_valid](https://shapely.readthedocs.io/en/stable/reference/shapely.coverage_is_valid.html).
- [GEOS C API: coverage simplification](https://libgeos.org/doxygen/geos__c_8h.html).

**Scope:** this record covers coverage-aware simplification through Shapely/GEOS. Shared-arc generalisation, network-constrained simplification and cartographic selection remain separate topics.
