# Spatial analysis catalogue

This directory is the structured index of the project's knowledge inventory. It includes algorithms, operations, data structures, models, statistics, standards, workflows, systems and applied methods. Full technical explanations belong in canonical records in their relevant directories.

## Coverage

See the [source-to-repository coverage matrix](coverage-matrix.md) for an honest view of what is captured, what has been researched and where work remains. The matrix deliberately does not count a source transcription as verified coverage. See the [source review dashboard](review-dashboard.md) for a dated count of all 694 source-entry rows and their current review labels.

## Intake source

The initial 47-page *Spatial Analysis Algorithms: Complete Compendium* has been imported page-by-page under [source-inventory](../source-inventory/README.md). That is the preserved intake record.

The transcription preserves original page boundaries and extracted wording. It is not an independently verified reference work. The next task is a separate, auditable catalogue pass. A source entry is not automatically an algorithm or a verified canonical record.

## Intake and normalisation rules

For every source entry, preserve:

- original section numbering and headings;
- original category groupings;
- source wording for each listed method, variant, named algorithm and implementation family;
- source page or page range;
- ambiguities, caveats and possible duplicates.

Normalisation is a second pass. Do not silently delete, rename or merge source entries because they appear redundant. Preserve the original source label and record a canonical label or relationship separately. The source explicitly marks some later additions as remembered and requiring verification; keep those entries flagged.

Use the [source-entry verification protocol](verification-protocol.md) to record identity, bibliography, technical claims, implementation and rights as separate dimensions. Do not use one blanket “verified” status.

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

Codes may be extended as the inventory is fully audited. Once assigned to a published record, an ID is stable. See the [record-type taxonomy](record-types.md) before creating or classifying a canonical record.

## Suggested inventory fields

| Field | Meaning |
|---|---|
| `source_section` | Original compendium section |
| `source_heading` | Original category heading |
| `source_label` | Exact source wording |
| `source_page` | Original page |
| `canonical_name` | Normalised name, if established |
| `record_id` | Stable ID, once assigned |
| `kind` | Algorithm, operation, data structure, model, statistic, metric, method, workflow, system, standard, implementation, dataset or application |
| `domain` | Main domain |
| `relationships` | Prerequisites, variants, alternatives and applications |
| `identity_status` | Whether the named item has been resolved |
| `bibliography_status` | Whether citation metadata has been checked |
| `claim_status` | Whether specific technical claims have been checked |
| `implementation_status` | Whether a reproducible implementation exists and has been tested |
| `rights_status` | Whether reuse rights have been checked for the intended use |
| `evidence` | Primary or authoritative evidence and review date |
| `notes` | Ambiguity, duplicate candidate or scope note |

## Item-level section indexes

The [section index](sections/README.md) links to source entries extracted and provisionally classified section by section. [Section 1](sections/01-core-gis.md) is the first completed intake pass; it is not yet a fully verified technical catalogue.

## Canonical records already developed

The repository contains a growing set of scoped canonical records, including geometry algorithms and operations, spatial statistics, raster and hydrology methods, geostatistics, geodesy, decision-support methods and location-science models. Each record should state its own evidence and implementation scope. The existence of a canonical page does not automatically verify every grouped source entry that mentions the same family.

The full source catalogue has not yet been normalised record-by-record. Do not infer completion from the page transcription or the presence of related learning materials alone.
