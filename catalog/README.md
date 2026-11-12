# Algorithm catalogue

This directory is the index of the project's knowledge inventory. It is not the place for full technical explanations; those belong in canonical records under `algorithms/`.

## Intake rule

The initial 47-page *Spatial Analysis Algorithms: Complete Compendium* is the source inventory. Intake must preserve:

- original section numbering and headings;
- original category groupings;
- each listed method, variant, named algorithm and implementation family;
- source page or page range where it can be established;
- ambiguities and apparent duplicates as review notes.

Normalisation is a second pass. Do not silently delete, rename or merge source entries because they appear redundant. Preserve the source label and record a canonical label or relationship separately.

## Stable IDs

Proposed format: `SA-<DOMAIN>-<SLUG>`.

Initial domain codes (provisional):

- `GEO` — geometry and vector operations;
- `IDX` — indexing and query processing;
- `NET` — networks and routing;
- `STA` — spatial statistics and geostatistics;
- `RAS` — raster and image analysis;
- `RS` — remote sensing and Earth observation;
- `3D` — 3D, terrain and point clouds;
- `SIM` — simulation and modelling;
- `AI` — machine learning and GeoAI;
- `DB` — spatial databases and distributed systems;
- `APP` — applied/domain methods;
- `CART` — cartography and visualisation.

Codes may be extended as the inventory is fully ingested. Once a record is published, its ID is stable.

## Suggested inventory fields

| Field | Meaning |
|---|---|
| `source_section` | Original compendium section |
| `source_heading` | Original category heading |
| `source_label` | Exact source wording |
| `canonical_name` | Normalised name, if established |
| `algorithm_id` | Stable ID, once assigned |
| `kind` | Algorithm, operation, data structure, model, method, system or implementation |
| `domain` | Main domain |
| `relationships` | Prerequisites, variants, alternatives and applications |
| `status` | Lifecycle state from project method |
| `notes` | Ambiguity, duplicate candidate or scope note |

## First intake batch

The first compendium section is **Core GIS: geometry, indexing, proximity, networks, routing**. Its vector/computational geometry subsection includes overlay operations, hulls and tessellations, point location, segment intersection, polygon clipping, simplification, triangulation/decomposition, distance/extent methods, proximity graphs, visibility and Boolean geometry.

This is an intake description, not a completed record-by-record import. The detailed source inventory will be committed in its own file after page-by-page extraction and checking.
