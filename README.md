# Spatial Analysis

A growing, structured knowledge and implementation project for spatial analysis algorithms.

The project connects four things:

1. **Algorithm knowledge** — what a method does, why it works, its assumptions, limitations and computational cost.
2. **Reproducible implementations** — code, test cases, examples, benchmarks and comparisons.
3. **Learning journeys** — structured routes through the material, without forcing every learner to follow one sequence.
4. **Research and publishing** — a continuously maintained body of work that can support public articles, weekly editions, premium learning materials and collaborative research.

This repository is the public, version-controlled technical foundation. It is not intended to be a chronological newsletter archive or a dump of unreviewed AI-generated notes.

## Project principles

- Preserve the source inventory before reorganising it.
- Give each knowledge item a stable identifier independent of newsletter issue numbers.
- Separate publication chronology from learning order.
- Make claims traceable to sources and distinguish established methods from implementation choices.
- Prefer small, testable, reproducible examples over unsupported claims.
- Record assumptions, coordinate reference systems, units, tolerances and edge cases.
- Keep the public contribution surface open; paid products may add depth, guidance and convenience without making basic participation pay-to-contribute.
- Use AI as a research and drafting assistant, not as an unquestioned authority.

## Repository map

| Path | Purpose |
|---|---|
| `source-inventory/` | Preserved page-by-page intake of the original compendium |
| `catalog/` | Normalised inventory, taxonomy and stable algorithm records |
| `algorithms/` | Canonical algorithm dossiers |
| `implementations/` | Reproducible implementations and examples |
| `benchmarks/` | Performance experiments and comparison protocols |
| `exercises/` | Public learning exercises and selected solutions |
| `learning-paths/` | Curated sequences through the catalogue |
| `research/` | Research notes, evidence and open questions |
| `templates/` | Reusable dossier, experiment and issue templates |
| `docs/` | Methodology, contribution and editorial standards |

Some directories will be populated as material is reviewed. An empty directory is not evidence that a topic has been completed or deliberately excluded.

## Start here

- [Project method](docs/project-method.md)
- [Research and evidence standard](docs/research-standard.md)
- [Contribution guide](CONTRIBUTING.md)
- [Algorithm dossier template](templates/algorithm-dossier.md)
- [Source inventory](source-inventory/README.md)
- [Catalogue guide](catalog/README.md)
- [Learning paths](learning-paths/README.md)
- [Publishing and access model](docs/publishing-model.md)

## Source inventory

The initial scope is based on the supplied *Spatial Analysis Algorithms: Complete Compendium* (47 pages, 12 November 2026). Its extracted text has now been imported page-by-page under `source-inventory/`. The intake transcription preserves the original page order; it is not a claim that every named method has been verified.

The compendium spans foundational GIS and computational geometry through spatial databases, statistics, remote sensing, networks, simulation, GeoAI and applied domains. Its own caveats are retained. In particular, entries marked by the source as remembered or requiring verification must not be cited as established facts until checked.

## First canonical dossier

[Polygon intersection](algorithms/geometry/polygon-intersection.md) is the first research draft. It distinguishes the Boolean predicate from the geometry-producing overlay operation and documents the broad OverlayNG pipeline, precision concerns and an initial test matrix. It is not yet implementation-verified.

## Status

**Stage:** Repository foundation and 47-page source intake imported; first algorithm dossier drafted. Next: audit the source inventory into structured catalogue entries, then implement and test the first dossier.

This project is evolving. See the commit history for changes and decisions.
