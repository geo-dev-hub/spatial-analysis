# Record types and classification

The source compendium covers much more than algorithms. It includes computational operations, data structures, statistical models, measures, standards, software, workflows and applied techniques. The catalogue must preserve that breadth instead of forcing every entry into the same category.

A **source entry** is an item as it appears in the supplied compendium. A **canonical record** is a separately researched, identified and maintained page in this repository. One source entry may lead to several related records; several source entries may also describe variants of one underlying concept. Keep those relationships explicit.

## Choose one primary kind

| Kind | What the record describes | Examples |
|---|---|---|
| algorithm | A defined procedure with steps that transforms inputs into outputs | Point-in-polygon ray crossing; Bentley–Ottmann |
| operation | A named computational action or result, which may have several algorithms or implementations | Polygon intersection; buffer; union |
| data_structure | A way of organising data for storage, access or computation | R-tree; spatial weights graph; quadtree |
| model | A formal representation of a process, relationship or uncertainty | Gaussian process; spatial lag model; cellular automaton |
| statistic | A quantity calculated from observations with a statistical interpretation | Global Moran's I; Geary's C; Ripley's K |
| metric | A measure used to describe or compare quality, error, similarity or performance | RMSE; intersection-over-union; runtime |
| method | A broader analytical technique or family that may combine models and algorithms | Kriging; kernel density estimation; network analysis |
| workflow | An ordered multi-stage process or pipeline | Photogrammetry pipeline; remote-sensing classification workflow |
| system | An integrated software, service or infrastructure arrangement | Spatial data infrastructure; geospatial database platform |
| standard | A published specification, format, protocol or agreed convention | GeoJSON; OGC API Features; GTFS |
| implementation | A particular software package, library, class, API or concrete realisation of a method | GEOS OverlayNG; Shapely; a PostGIS function |
| dataset | A named collection of observations, features, imagery or other data product | A satellite scene collection; a published building-footprint dataset |
| application | A domain-specific analytical use or solution pattern | Transit accessibility analysis; flood exposure assessment |

Choose the kind that best describes the subject of the record itself, not every kind of thing it depends on. Use related-record links and tags for secondary relationships.

## How to decide

Ask these questions in order:

1. Is the subject a published specification or agreed format? Use **standard**.
2. Is it a named data collection or data product? Use **dataset**.
3. Is it a particular software package, class or API? Use **implementation**.
4. Is it an integrated platform or infrastructure? Use **system**.
5. Is it a multi-stage sequence of tasks? Use **workflow**.
6. Is it a data organisation or index? Use **data_structure**.
7. Is it a formal representation of a process or relationship? Use **model**.
8. Is it a calculated inferential or descriptive quantity? Use **statistic**.
9. Is it a measure of error, quality or performance? Use **metric**.
10. Is it a named computational action? Use **operation**.
11. Is it a reproducible procedure with explicit steps? Use **algorithm**.
12. Is it a wider analytical technique or domain solution? Use **method** or **application**, choosing the one that best captures the record's purpose.

These questions guide classification; they are not a reason to split one concept into unnecessary pages.

## Important distinctions

### Algorithm versus operation

An operation describes *what result is requested*. An algorithm describes *how a procedure obtains that result*. Polygon intersection is an operation; plane-sweep overlay, arrangement construction and a library's overlay engine are ways to compute it.

### Algorithm versus implementation

An algorithm is the method, not the package. A Shapely or GEOS implementation can change while the mathematical task remains the same. Record implementation versions and behaviour separately from the method's general guarantees.

### Statistic versus model

A statistic is calculated from data. A model specifies a structure or assumptions that may explain, predict or generate data. A statistic can be used to assess a model, but the two are not interchangeable.

### Data structure versus system

An R-tree is a data structure. A spatial database that stores geometries and uses indexes is a system. The system may use the data structure without being the same thing.

### Method versus workflow

A method describes an analytical approach. A workflow specifies an ordered sequence of operations and methods, including data preparation and validation.

## Examples from this repository

| Subject | Primary kind | Related records |
|---|---|---|
| Point in polygon | algorithm | Polygon model; boundary convention; implementation |
| Polygon intersection | operation | Overlay algorithms; precision model; GEOS and Shapely implementations |
| Bentley–Ottmann | algorithm | Segment intersection; event queue; sweep-line status structure |
| STR-packed R-tree | data_structure | STR bulk-loading algorithm; bounding-box query; implementation and benchmark |
| Global Moran's I | statistic | Spatial weights; spatial lag; permutation inference |
| Spatial weights matrix | data_structure | Contiguity, distance-band and k-nearest-neighbour construction |
| GeoJSON | standard | Geometry model; software implementations |
| Transit accessibility analysis | application | Network model; routing algorithm; impedance and access metrics |

## Catalogue fields

Each canonical record should preserve enough information to trace it back to the intake source:

- **record_id:** stable repository identifier;
- **canonical_name:** preferred name after verification;
- **kind:** one primary type from this guide;
- **source_label:** exact wording from the original source;
- **source_section** and **source_page:** original provenance;
- **aliases** and **variants:** alternate names, not silently merged;
- **related_records:** prerequisites, components, alternatives and implementations;
- **verification_status:** what has actually been checked;
- **implementation_status:** whether a reproducible implementation exists and has been tested.

Do not assign a canonical name, type or ID merely because an item appears in the source inventory. If its identity is uncertain, keep it captured and flag the question for research.

## Keep the source and the catalogue separate

The original 22 section indexes preserve the supplied compendium's structure. They should not be rewritten to make the repository taxonomy look tidy. Classification belongs in the normalised catalogue layer, with the original source label and section retained.

When a source entry is ambiguous, preserve it and record the ambiguity. When two entries appear related, create a relationship note first; merge them only after the evidence supports that decision.
