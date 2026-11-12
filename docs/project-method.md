# Project method

## 1. The knowledge lifecycle

Every topic moves through a visible lifecycle:

1. **Intake** — capture the source wording and source location without losing detail.
2. **Triage** — assign a stable ID, identify duplicates and related concepts, and note prerequisite knowledge.
3. **Research** — collect primary and authoritative references; record disagreements and uncertainties.
4. **Dossier** — write the canonical explanation using the dossier template.
5. **Verification** — check mathematics, assumptions, examples, complexity statements and citations.
6. **Implementation** — add a reference implementation or document why one is not appropriate.
7. **Testing** — test normal cases, boundary cases, invalid inputs and numerical edge cases.
8. **Publication** — select suitable public and member-facing derivatives; preserve the canonical record.
9. **Maintenance** — version corrections and update references without erasing publication history.

A topic may be useful before every stage is complete. Status must make its maturity clear.

## 2. Stable identity

Algorithm IDs identify concepts, not newsletter issues or file locations.

Proposed ID form: `SA-<DOMAIN>-<SLUG>`, for example `SA-GEO-INTERSECTION`.

Once assigned, an ID should not change merely because a title, folder or learning path changes. If two records are merged or split, document redirects or relationships rather than silently reusing an ID.

Newsletter editions have their own sequence (for example, Edition 001). A learning path may place records in a different order. These are three distinct things:

- canonical algorithm identity;
- publication sequence;
- learner's chosen sequence.

## 3. Research dossier structure

A complete dossier should address, where applicable:

- concise definition and intuition;
- problem formulation and use cases;
- mathematical foundations;
- inputs, outputs and assumptions;
- algorithm steps and pseudocode;
- correctness or approximation properties;
- time and space complexity, with the model and assumptions stated;
- numerical robustness and precision;
- edge cases and failure modes;
- implementation options and version-specific behaviour;
- worked example;
- tests and reproducibility instructions;
- performance considerations;
- alternatives and trade-offs;
- exercises;
- references and unresolved questions.

Do not fill sections with generic prose when evidence is missing. Mark the gap.

## 4. Relationships and prerequisites

The catalogue should express relationships such as:

- prerequisite / builds on;
- alternative to;
- special case of;
- commonly combined with;
- implemented by;
- used in domain.

Do not force every topic into a single tree. Spatial analysis is a network of concepts with multiple valid learning routes.

## 5. Implementation policy

Prefer a small reference implementation that demonstrates the method and its limitations. Where mature libraries are the practical implementation, explain their role and provide a minimal reproducible usage example rather than reimplementing everything unnecessarily.

Every implementation should identify:

- language and dependency versions;
- input data and licence;
- CRS and units;
- precision/tolerance policy;
- expected output;
- tests and known limitations.

## 6. Manual-first production

The production process will initially be run manually and documented. Automate only steps that have become stable and repeatable. This reduces the risk of encoding a flawed editorial or technical process into automation.

## 7. Quality states

Use these states consistently:

- `captured` — present in the source inventory;
- `triaged` — identity and relationships reviewed;
- `researching` — evidence gathering underway;
- `draft` — dossier exists but is not approved;
- `review` — awaiting technical/editorial review;
- `verified` — claims, references and examples checked to the stated scope;
- `implemented` — reproducible implementation exists;
- `published` — released in one or more channels;
- `needs-update` — known material requires revision.

A status describes the record's state, not its importance.
