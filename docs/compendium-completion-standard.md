# Compendium completion standard

This document defines what it means to develop the supplied *Spatial Analysis Algorithms: Complete Compendium* into a useful, reproducible technical and learning resource. It supplements—not replaces—the preserved [47-page source transcription](../source-inventory/README.md), the [22 section indexes](../catalog/sections/README.md), the [coverage matrix](../catalog/coverage-matrix.md), and the [source-entry verification protocol](../catalog/verification-protocol.md).

## 1. The source compendium remains the master specification

The source transcription is the scope-preserving record. Do not shrink it to match the current repository, silently discard awkward or unfamiliar entries, or substitute the index for the source. Preserve original page, section, wording, cautions and grouped relationships.

The section indexes and coverage matrix are navigation and project-management layers. They are not the compendium itself and do not prove that a method has been researched, explained or implemented.

Every source entry must remain traceable to:
- its original page and section;
- its preserved source wording;
- one or more normalised child records where the source groups distinct methods;
- the canonical lesson, research dossier, implementation or external maintained tool that addresses it;
- an explicit development and review status.

## 2. Develop each entry according to its actual kind

Do not force every entry into a Python algorithm. First classify it using [the record-type taxonomy](../catalog/record-types.md).

| Record kind | Appropriate technical treatment | Executable treatment |
|---|---|---|
| Algorithm | Problem, inputs/outputs, assumptions, derivation, steps, correctness or guarantees, complexity, failure modes and variants | From-scratch teaching implementation where meaningful; tests and comparison baseline |
| Statistical model or estimator | Mathematical model, estimand, assumptions, identification, inference, uncertainty, diagnostics and validation | Numerical example, tests against known or trusted results, sensitivity notebook |
| Metric or index | Definition, units, range, interpretation, invariance, edge cases and misuse | Calculation, hand-checkable fixtures, tests and a worked notebook where useful |
| Data structure or index | Invariants, operations, complexity, memory/update behaviour and workload fit | Data structure, invariant/property tests and workload experiment |
| Software, framework or platform | Purpose, architecture, supported methods, version, dependencies, licence, maturity and reproducibility | Minimal documented integration or reproducible example; do not reimplement the platform |
| Standard, format or data model | Normative source, schema, semantics, coordinate/time conventions, interoperability and version | Parser/validator or interoperability fixture where useful |
| Workflow or applied method | Inputs, stages, decisions, data provenance, spatial/temporal scale, calibration and validation | Reproducible end-to-end case with synthetic or licensed data |
| Research family or unresolved name | Identity investigation, competing interpretations, primary sources and explicit uncertainty | No code until the method is identified and its contract can be stated |

A row that names six different algorithms is not one implementation task. Split it into child records, retain the parent grouping, and track the children separately.

## 3. Canonical lesson standard

A lesson should include the parts relevant to its record kind:

1. **The question:** what problem is being solved and why it matters.
2. **Inputs and outputs:** data model, units, coordinate reference, spatial and temporal scope.
3. **Core idea:** intuitive explanation and a worked example.
4. **Mathematics:** rendered notation, defined symbols, derivation or model definition where appropriate.
5. **Algorithm or workflow:** clear steps, pseudocode or process diagram.
6. **Correctness and limits:** assumptions, guarantees, edge cases, failure modes and what the method does not do.
7. **Complexity and trade-offs:** time, memory, accuracy, scale and alternatives where meaningful.
8. **Practical use:** when to choose it, when not to, and how it relates to adjacent methods.
9. **Evidence:** primary references, official documentation, versioned sources and attribution.
10. **Learning activities:** prediction, tracing, experiments, exercises and further questions where useful.

Not every method needs a long chapter. It does need enough substance for a reader to understand what the method does, how to use it responsibly and how to investigate it further.

## 4. Implementation standard

Every implementation must state which of these it is:

- **Teaching implementation:** transparent, deliberately bounded and designed to expose the algorithm.
- **Reference reproduction:** a documented reproduction of a published method or benchmark.
- **Library integration:** a reproducible wrapper around a maintained specialist implementation.
- **Production-oriented implementation:** designed and tested for operational constraints, with performance and failure behaviour documented.

Do not call a teaching baseline production-ready. Do not claim an algorithm is implemented merely because a package with a similar name is imported.

Where code is appropriate, include:
- explicit input, output, units, coordinate and numerical contracts;
- validation and useful errors;
- deterministic behaviour or documented randomness;
- tests for ordinary, boundary, degenerate, invalid and adversarial cases as relevant;
- differential/property tests or comparison with an authoritative implementation where possible;
- complexity and performance notes;
- dependencies and reproducible setup;
- a step-by-step walkthrough.

For wrappers, state exactly what is delegated to the dependency and what this repository contributes. For a software product or standard, a reproducible integration can be the correct deliverable; a from-scratch clone is not required.

## 5. Notebook standard

A notebook is appropriate when it materially improves understanding, comparison, visual inspection or reproducibility. It should:
- run from a clean environment using documented dependencies;
- use small, reproducible or clearly licensed data;
- explain the experiment and expected observation;
- expose meaningful parameters and intermediate results;
- include interpretation, not just code output;
- avoid relying on hidden local files, manual state or network access unless explicitly documented.

A notebook does not replace the canonical explanation or automated tests. Not every source entry needs a separate notebook: related methods can share a lab if each remains traceable.

## 6. Diagrams, data and reuse

Prefer a clear original diagram or a permitted, accurately attributed source figure when it improves the lesson. Record the exact source, creator, licence, modifications and access date. A citation is not permission to reproduce. Check the rights of code, figures, text, datasets, model weights and notebook assets separately.

Use synthetic data when it makes an experiment reproducible and avoids implying that illustrative data are observations. For real datasets, document provenance, licence, spatial/temporal coverage, resolution and known limitations.

## 7. Independent review dimensions

Track these separately; do not collapse them into one generic completion badge:

- **Identity:** the name refers to the intended method, model, software or standard.
- **Bibliography:** primary or authoritative references and version details are correct.
- **Technical claims:** equations, assumptions, guarantees, complexity and limitations are checked.
- **Implementation/reproduction:** code or integration matches the stated contract and is reproducible.
- **Tests/validation:** meaningful edge cases and comparison evidence exist.
- **Rights:** every reused artefact has a documented basis for use.
- **Learning/publishing:** explanation, notebook, exercises, accessibility and navigation are fit for the intended edition.

A source row is complete only when its child records have the applicable dimensions reviewed. A research-only record can be complete without original code if the record kind does not call for it and the reason is explicit. An implementation is not a substitute for bibliography, technical review or rights review.

## 8. Release gates before Patreon

The compendium is ready to move into the publishing/membership phase only when:

- all 47 source pages and 22 original sections remain preserved and accounted for;
- every source entry has been triaged, ambiguities and grouped families split, and cross-links resolved;
- every in-scope child record has a canonical treatment and an explicit rationale for implementation, integration or research-only status;
- all promised implementations have tests, and all notebooks designated as executable have been run in CI;
- primary references, technical claims, dependencies and reuse rights have been reviewed;
- the coverage matrix, source dashboard, road map and README agree with the actual repository;
- full validation passes on the exact release commit;
- the public learning experience has been checked for navigation, rendering, accessibility and mobile use.

The first public edition can be curated from completed material before every research question is exhausted, but the project must distinguish that edition from completion of the full source compendium. Patreon planning must not redefine or reduce the underlying technical scope.

## 9. Current baseline

The repository currently preserves the 47-page source transcription and indexes all 22 sections. The dated source dashboard records 694 grouped source-entry rows, of which 52 are marked partial and 642 intake-only; zero are fully verified across all review dimensions. Those counts are not a direct percentage of implementation work: grouped rows contain multiple child methods, and substantial existing lessons, code and notebooks are not yet reflected as complete source-entry reviews.

The repository tree currently contains 77 algorithm lesson files, 32 method guides, 187 Python source files, 93 Python test files and 73 notebooks. File counts indicate substantial work already exists; they do not establish that every source entry is covered or that every test/notebook passes at the current head.

Use the [coverage matrix](../catalog/coverage-matrix.md) for the section-level narrative and the [repository roadmap](repository-roadmap.md) for the next work queue. Recalculate all counts from the actual tree and review records before making a release claim.
