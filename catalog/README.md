# Algorithm catalogue

This directory is the structured index of the project's knowledge inventory. It is not the place for full technical explanations; those belong in canonical records under `algorithms/`.

## Coverage

See the [source-to-repository coverage matrix](coverage-matrix.md) for an honest view of what is captured, what has been researched and where work remains. The matrix deliberately does not count a source transcription as verified coverage.

## Intake source

The initial 47-page *Spatial Analysis Algorithms: Complete Compendium* has been imported page-by-page under [source-inventory](../source-inventory/README.md). That is the preserved intake record.

The transcription preserves original page boundaries and extracted wording. It is not an independently verified reference work. The next task is a separate, auditable catalogue pass.

## Intake and normalisation rules

For every source entry, preserve:

- original section numbering and headings;
- original category groupings;
- source wording for each listed method, variant, named algorithm and implementation family;
- source page or page range;
- ambiguities, caveats and possible duplicates.

Normalisation is a second pass. Do not silently delete, rename or merge source entries because they appear redundant. Preserve the original source label and record a canonical label or relationship separately. The source explicitly marks some later additions as remembered and requiring verification; keep those entries flagged.

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

Codes may be extended as the inventory is fully audited. Once assigned to a published record, an ID is stable.

## Suggested inventory fields

| Field | Meaning |
|---|---|
| `source_section` | Original compendium section |
| `source_heading` | Original category heading |
| `source_label` | Exact source wording |
| `source_page` | Original page |
| `canonical_name` | Normalised name, if established |
| `algorithm_id` | Stable ID, once assigned |
| `kind` | Algorithm, operation, data structure, model, method, system, metric or implementation |
| `domain` | Main domain |
| `relationships` | Prerequisites, variants, alternatives and applications |
| `verification_status` | Whether the item has been independently checked |
| `notes` | Ambiguity, duplicate candidate or scope note |

## First audited record

The first canonical draft is [Polygon intersection](../algorithms/geometry/polygon-intersection.md), sourced from section 1, page 1. Its ID is `SA-GEO-POLYGON-INTERSECTION`.

The full source catalogue has not yet been normalised record-by-record. Do not infer completion from the page transcription alone.
