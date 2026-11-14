# Discrete global grids: ISEA3H, rHEALPix, DGGRID and HTM

A discrete global grid system (DGGS) partitions the Earth or another global surface into cells that have identifiers and can be refined into finer resolutions. It is more than a projected grid: a DGGS defines a global spatial reference framework, cell geometry, hierarchy and addressing rules.

DGGSs can support global aggregation, data-cube indexing, multi-resolution storage and spatial queries. They do not automatically make all cells identical, all neighbour relationships trivial or every analysis faster. Those properties depend on the particular grid design and implementation.

## 1. What a DGGS must specify

A usable grid system needs explicit answers to several questions:

- **Reference surface:** sphere, ellipsoid or another model?
- **Partition:** triangles, quadrilaterals, hexagons, diamonds or mixed cell shapes?
- **Projection or construction:** how is the surface partition generated and related to coordinates?
- **Hierarchy:** how does one resolution refine another?
- **Addressing:** how are cells assigned unique, stable identifiers?
- **Neighbourhood:** how are adjacent cells found, including across base-face boundaries?
- **Measurements:** are cell areas equal, approximately equal or variable?
- **Operations:** how are points, lines, polygons and raster samples assigned, aggregated and queried?

A grid can be hierarchical without being equal-area. A cell shape can look regular in a planar projection while having varying ground area. A cell identifier is meaningful only together with its grid definition, resolution and version.

## 2. ISEA3H: icosahedral Snyder equal-area aperture-3 hexagons

ISEA3H combines three design choices:

1. an icosahedron-based global construction;
2. the Icosahedral Snyder Equal Area (ISEA) projection;
3. an aperture-3 hierarchical hexagonal partition.

The area of a typical hexagonal cell is refined by a factor of three between successive resolutions. The spherical topology requires twelve pentagonal cells at each resolution: a sphere cannot be tiled entirely by hexagons with ordinary three-cell vertices. In the OGC ISEA3H definition, each of those twelve pentagonal zones has 5/6 the area of a hexagonal zone at the same level. Therefore, do not describe every cell in the grid as exactly equal area.

**Why it is useful:** global equal-area-style aggregation, hierarchical indexing and a mostly hexagonal neighbourhood structure can be attractive for global statistical analysis and data cubes.

**What to check:** pentagon handling, cell identifiers, resolution semantics, edge-neighbour traversal, the precise ISEA orientation and the target implementation's treatment of the twelve exceptional cells.

## 3. rHEALPix: rearranged HEALPix

rHEALPix is based on the HEALPix family and rearranges the projected layout into a cube-like arrangement. Its projected cells are arranged in aligned square grids, which can make indexing, display and raster-like processing convenient.

The rHEALPix DGGS uses a hierarchical refinement scheme with aperture 9. Its cell geometry includes distinct polar and equatorial forms in the projected representation; do not assume every projected cell is a visually identical square. Its design aims to preserve equal-area properties on the reference surface, while the projection is not conformal and does not preserve local shape.

The rHEALPix literature also describes cell identifiers that support topological operations directly, without converting every operation back through conventional geographic coordinates. That is a useful property, but it depends on implementing the specified identifier scheme and topology correctly.

**Why it is useful:** equal-area global analysis, nested cells, and a square-oriented projected layout that can be convenient for Earth-observation data cubes.

**What to check:** reference ellipsoid/sphere handling, polar-cell conventions, cell identifier version, neighbour operations, and interoperability with the raster/data-cube system.

## 4. HTM: Hierarchical Triangular Mesh

HTM recursively subdivides the sphere into spherical triangles, often called *trixels*. The base sphere is divided into eight spherical triangles, and each triangle is recursively split into four children. A path through the hierarchy yields a cell identifier.

At depth d greater than zero, the standard eight-root quad-tree subdivision has

$$
N(d)=8\times4^{d-1}
$$

triangles at that depth. The hierarchy supports region covering and multi-resolution spatial lookup. HTM is particularly well known in astronomical catalogues, where cone searches and spherical-region queries are common.

HTM is an indexing tessellation, not a guarantee of equal-area cells. Its spherical triangles have similar but not identical shapes and sizes. A query usually covers a region with a set of trixels at a chosen depth, then applies an exact geometric predicate to remove false positives.

**Why it is useful:** hierarchical indexing of points on the celestial sphere or Earth, especially region searches and database candidate filtering.

**What to check:** depth and identifier convention, boundary inclusion, conservative region covering, spherical predicate precision, and the distinction between candidate retrieval and exact final geometry tests.

## 5. DGGRID: software for constructing and working with DGGSs

DGGRID is software for generating and working with discrete global grids. It is not itself one unique cell geometry or one unique DGGS. Depending on the selected grid definition, the software can construct different global grid families and resolutions.

This distinction matters when comparing a named grid such as ISEA3H or rHEALPix with a software package such as DGGRID. A software engine can support multiple grid definitions, while each grid definition has its own geometry, hierarchy and cell-addressing contract.

Before adopting DGGRID in a workflow, verify the exact grid type and version, supported operations, identifier semantics, file outputs, neighbour/traversal support and how the tool handles points or geometries on cell boundaries.

## 6. Compare by analytical requirement

| Requirement | ISEA3H | rHEALPix | HTM |
|---|---|---|---|
| Primary cell geometry | Mostly hexagons plus pentagons | Cube-based hierarchical projected cells | Spherical triangles |
| Hierarchy | Aperture 3 | Aperture 9 | Quad-tree subdivision |
| Area behaviour | Equal-area design with 12 smaller pentagonal zones | Equal-area design on stated reference surface | Not inherently equal-area |
| Typical strength | Global aggregation and hexagonal neighbourhoods | Equal-area grid with square-oriented projected layout | Hierarchical spherical indexing and region search |
| Important caveat | Pentagon exceptions and identifier scheme | Polar/equatorial geometry and identifier operations | Similar, not identical, trixel areas and exact-predicate filtering |

DGGRID belongs in a separate software/tooling column in a real implementation comparison. Do not compare it as though it were a competing cell tessellation.

## 7. Cell identifiers are not geometry

A cell ID is a compact address within a particular grid system. It is not a universal coordinate. Store enough metadata to interpret it:

- DGGS name and definition/version;
- resolution or hierarchy depth;
- identifier scheme/version;
- reference surface and coordinate datum;
- any orientation or configuration parameters.

Do not mix identifiers from different DGGSs, or treat an identifier as stable across changed grid definitions without a compatibility guarantee.

A common spatial query pipeline is:

~~~mermaid
flowchart TD
    A[Input point or query geometry] --> B[Transform to DGGS reference surface]
    B --> C[Cover with cells at chosen resolution]
    C --> D[Retrieve candidate cell IDs]
    D --> E[Fetch associated records]
    E --> F[Exact geometry or distance predicate]
    F --> G[Aggregate or return results]
~~~

Cell covering is often a candidate-generation stage. For a polygon query, cells intersecting the polygon may be included conservatively; the final geometry predicate determines exact membership. This prevents a cell-covering approximation from silently becoming the analytical truth.

## 8. Choosing a resolution

A finer resolution increases the number of cells and the potential storage, indexing and processing cost. It can reduce spatial aggregation error, but it does not recover information absent from the input data.

A useful first estimate for a target equal-area cell area A on a reference surface with area S is

$$
N\approx\frac{S}{A}.
$$

This estimates the number of cells, not the exact count for every DGGS. Base cells, pentagonal exceptions, refinement rules and the definition of the reference surface affect actual counts.

Choose resolution from the analytical question, source-data precision, expected query scale, privacy requirements and operational budget. Avoid choosing the finest available resolution by default.

## 9. Validation checklist

1. Confirm the named DGGS definition and software version.
2. Check that every test point receives exactly one valid cell ID under the declared boundary rule.
3. Test points on cell edges, vertices, poles and base-polyhedron seams.
4. Check parent/child relationships across several resolutions.
5. Verify neighbour traversal across face boundaries, not only within one face.
6. Measure cell areas on the actual reference surface and inspect exceptional cells.
7. Test polygon covering for false negatives; a conservative cover must not omit intersected cells.
8. Compare candidate queries with exact spherical or ellipsoidal geometry predicates.
9. Round-trip identifiers to cell geometry and back where the implementation promises that property.
10. Record the effect of resolution on cell count, storage, query latency and aggregation error.

## Further reading

- Open Geospatial Consortium, [OGC API – Discrete Global Grid Systems, Part 1: Core](https://docs.ogc.org/is/21-038r1/21-038r1.html), including the ISEA3H DGGRS definition and cell-zone semantics.
- Sahr, K., White, D. and Kimerling, A. J. (2003), “Geodesic Discrete Global Grid Systems,” *Cartography and Geographic Information Science*, 30(2), 121–134. [Article record and paper](https://www.discreteglobalgrids.org/wp-content/uploads/2016/01/gdggs03.pdf).
- Gibb, R. G. (2016), “The rHEALPix Discrete Global Grid System,” *IOP Conference Series: Earth and Environmental Science*, 34, 012012. [DOI 10.1088/1755-1315/34/1/012012](https://doi.org/10.1088/1755-1315/34/1/012012).
- Gibb, R., Raichev, A. and Speth, M., “The rHEALPix Discrete Global Grid System,” [author-hosted paper](https://datastore.landcareresearch.co.nz/dataset/f0c488fe-ab25-4737-9d20-eb7777806a41/resource/f6e5726d-07be-460f-89be-bf1c84310972/download/gibbrhealpixdggs.pdf), for construction, cell identifiers and topology.
- Szalay, A. S., Gray, J., Fekete, G., Kunszt, P. Z., Kukol, P. Z. and Thakar, A. (2005), “Indexing the Sphere with the Hierarchical Triangular Mesh,” Microsoft Research Technical Report MSR-TR-2005-123. [Research record](https://www.microsoft.com/en-us/research/publication/indexing-the-sphere-with-the-hierarchical-triangular-mesh/).
- Kmoch, A., Matsibora, V., Vasilyev, I. and Uuemaa, E. (2022), “Applied open-source Discrete Global Grid Systems,” *AGILE GIScience Series*, 3, 41. [DOI 10.5194/agile-giss-3-41-2022](https://doi.org/10.5194/agile-giss-3-41-2022), comparing open-source DGGS software APIs.

## Scope

This is a system-selection and data-contract guide. It does not implement ISEA3H, rHEALPix, HTM or DGGRID. A practical follow-up should benchmark one named grid implementation against the intended data model and query workload rather than treating DGGS as a single interchangeable technology.
