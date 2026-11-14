# Polygon validity: when is a boundary a valid area?

A polygon can look perfectly reasonable on a map and still be invalid as a geometric object. A ring may cross itself, a hole may sit outside its shell, or two components may overlap. These are not merely cosmetic problems: they can make area, containment and overlay operations ambiguous or cause software to reject an operation.

This lesson separates the **meaning of a valid polygon** from the software procedures used to test or repair one.

## The practical question

Before calculating an intersection, union, area or containment relationship, how do we know that the input represents the area we think it represents?

Consider a polygon whose boundary crosses itself like a bow tie. Which of the two lobes is the interior? The answer depends on a fill rule or interpretation that may not be part of the input contract. A geometry engine should not silently guess what the author intended.

## The geometric model

A polygon is commonly represented by one exterior boundary (the shell) and zero or more interior boundaries (holes). A ring is a closed sequence of line segments. In a planar straight-line model, the segments join end-to-end and the final segment returns to the first coordinate.

For a valid polygon under the Simple Features model, the important ideas are:

- each ring is a simple closed curve: it does not cross itself;
- the shell defines the exterior boundary of the area;
- each hole lies within the shell;
- holes do not overlap one another or cross the shell;
- the polygon interior remains connected under the model's validity rules.

A MultiPolygon adds another layer: its polygon components must satisfy the collection's non-overlap and boundary-touching rules. Do not assume that a collection of individually valid polygons is automatically a valid MultiPolygon.

The exact formal rules belong to the selected geometry standard and implementation. Record that choice rather than treating “valid” as a universal informal label.

## A useful mental model

Think of validity as a set of structural promises:

1. **A boundary can be followed.** Its ring structure is coherent.
2. **Inside and outside are unambiguous.** The ring does not cross itself.
3. **Holes mean holes.** They are contained in the shell and do not conflict.
4. **Components agree.** Multi-part geometry does not create forbidden overlaps.
5. **The coordinate model is explicit.** The validity test is performed in a stated planar or other geometry model.

## What a validity check does

A validity checker examines the geometry against the rules of its geometry model. It may return a Boolean result, a reason, or a location associated with the failure.

A useful diagnostic workflow is:

```text
Read geometry
    |
Check type and coordinate structure
    |
Run validity test
    |
    +-- valid --> record result and continue
    |
    +-- invalid --> capture reason and location
                     |
                inspect source and intended meaning
                     |
             choose an explicit repair or reject
```

A validity check is not a repair algorithm. A repair operation may split, collapse, remove or reinterpret parts of the input. The output can have a different geometry type or dimension. Preserve the original and document the repair policy.

## Common failure cases

| Case | Why it matters | What to inspect |
|---|---|---|
| Self-crossing ring | Interior may be ambiguous | Crossing segments and fill interpretation |
| Hole outside shell | Ring roles contradict the polygon model | Shell and hole containment |
| Hole crosses shell | Boundaries are not properly nested | Intersection locations |
| Overlapping holes | Interior definition is inconsistent | Hole-to-hole relationships |
| Duplicate or collapsed edges | Can create zero-length or degenerate pieces | Coordinate precision and repeated vertices |
| Nearly coincident boundaries | Floating-point calculations may disagree about topology | Precision model and snapping policy |
| Overlapping MultiPolygon components | Collection-level topology may be invalid | Component intersections and shared boundaries |

Do not “fix” all cases by deleting repeated coordinates or snapping everything to a coarse grid. Those choices can change the represented area.

## Validity and precision

Coordinates are finite machine numbers, while geometric predicates often depend on exact sign decisions. A tiny rounding difference can change whether two segments cross, touch or miss each other.

A robust workflow records:

- the coordinate reference system and units;
- whether the geometry is planar, projected or spherical;
- the precision model used by the operation;
- any grid size or snapping tolerance;
- whether repair was applied and which algorithm performed it.

Precision reduction is a modelling decision, not a harmless formatting step. A grid that is too coarse can collapse narrow corridors, holes or small polygons.

## Implementation example

With Shapely, inspect validity and its explanation before deciding what to do:

```python
import shapely
from shapely import Polygon

candidate = Polygon([
    (0, 0), (4, 4), (0, 4), (4, 0), (0, 0)
])

print(shapely.is_valid(candidate))
print(shapely.is_valid_reason(candidate))
```

This is an implementation demonstration, not a definition of validity independent of the underlying geometry model. Pin the Shapely and GEOS versions in a reproducible project and record the returned diagnostic.

Do not automatically pass invalid input into a repair function and assume the result preserves the author's intention. Inspect the output type, area, components and boundaries.

## A disciplined repair workflow

1. Preserve the original geometry and its source identifier.
2. Record the validity result and diagnostic.
3. Inspect the offending coordinates in the correct CRS and units.
4. Determine whether the problem is a data error, a precision issue or an intentional representation that needs a different model.
5. Select a repair method only after deciding what the geometry is supposed to mean.
6. Compare before-and-after geometry type, area, component count and boundary.
7. Store the repair method, parameters, software version and result.
8. Keep unresolved cases out of analyses that require valid input.

## What this lesson does not claim

- A geometry being valid does not mean it is geographically correct.
- A validity checker cannot infer the intended boundary from an invalid ring.
- A repaired geometry is not necessarily equivalent to the source.
- Planar validity does not by itself resolve antimeridian, polar or geodesic modelling issues.
- A successful validity test does not guarantee every later overlay will be numerically robust.

## Try it

Create four polygons: a simple shell, a shell with a valid hole, a bow-tie ring and a polygon with a hole outside its shell.

For each one:

1. predict whether it should be valid under the Simple Features polygon model;
2. run the validity checker;
3. record the diagnostic;
4. repair only the invalid cases;
5. compare geometry type and area before and after repair.

Explain why the repaired result is a modelling decision rather than proof that the original geometry had one uniquely correct interpretation.

## Runnable example

The repository includes a [Shapely-backed validity inspection and explicit repair example](../../implementations/python/polygon-validity/README.md), with a [step-by-step walkthrough](../../implementations/python/polygon-validity/implementation-walkthrough.md). The example preserves the original geometry, reports the validity reason and makes repair a separate user decision. Its tests cover invalid rings, holes, overlapping MultiPolygon components and repair outputs.

## References

- [OGC Simple Feature Access — Part 1: Common Architecture](https://www.ogc.org/standards/sfa/). The standard defines the common geometry model and validity concepts; consult the normative document version used by the project.
- [GEOS documentation](https://libgeos.org/). GEOS is the geometry engine used by several open-source geospatial libraries; check the version-specific API documentation for validity and repair behaviour.
- [Shapely documentation](https://shapely.readthedocs.io/). Use the documentation matching the pinned Shapely version for the exact diagnostic and repair API.

**Evidence state:** foundational geometry model linked to the OGC standard; implementation behaviour must be checked against the pinned GEOS/Shapely versions before this record is marked verified.
