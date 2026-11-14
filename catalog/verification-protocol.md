# Source-entry verification protocol

This protocol separates preservation, identification, technical verification and publication rights. A source transcription is evidence of what the supplied compendium said; it is not evidence that the named method exists under that name, that its description is correct, or that its material may be redistributed.

## Keep two records distinct

- A **source entry** records one item or grouped label from the 47-page intake source. Preserve its exact wording, section, category and page.
- A **canonical record** is a separately researched page with a defined scope, preferred name, evidence and related records. One source entry may lead to several canonical records; several entries may refer to one concept or variant.

Do not silently replace the source label with a canonical name. Keep both.

## Verification dimensions

Do not compress all checks into one unqualified `verified` flag. Record these dimensions separately.

Each section index also has a concise **source-entry review status**. Use `Not checked — intake only` when no independent review is recorded, and `Partial — related record exists; source-entry review pending` when a linked canonical record covers only part of the grouped entry. These are summary labels, not substitutes for the separate verification dimensions below.

| Dimension | Status values | What the status means |
|---|---|---|
| Capture | `captured`, `capture_incomplete` | The source wording and page provenance have been preserved, or a transcription gap remains |
| Identity | `not_checked`, `in_progress`, `confirmed`, `ambiguous`, `not_found` | The named entity or method has been resolved to an authoritative identity |
| Bibliography | `not_checked`, `in_progress`, `confirmed`, `corrected`, `not_applicable` | Author, title, venue, year, volume, pages and DOI/URL have been checked |
| Technical claims | `not_checked`, `in_progress`, `partially_checked`, `checked`, `disputed`, `not_applicable` | The specific mathematical, algorithmic or empirical claims have been compared with primary evidence |
| Implementation | `not_started`, `planned`, `tested_teaching_baseline`, `reproduced`, `not_applicable` | Code status is described precisely; passing unit tests alone does not prove a method's literature claims |
| Rights | `not_checked`, `in_progress`, `permitted`, `permission_required`, `link_only`, `not_applicable` | Rights to reproduce text, figures, code, data or model artefacts have been checked for the intended use |
| Canonicalisation | `not_started`, `candidate`, `created`, `merged_with_evidence`, `retained_as_source_only` | The decision about a separate canonical record is explicit |

A record may be identity-confirmed while its technical claims remain unchecked. Rights are independent of technical correctness. A method may be correctly described but still not be reproducible from the available data or software.

## Minimum evidence for each check

### Identity

Prefer the original paper, standards body, official project, author-maintained documentation or institutional publication record. Record the exact title and stable identifier. Search snippets and unsourced secondary lists are discovery aids, not final evidence.

### Bibliography

Check the publisher or authoritative bibliographic record. Verify every field rather than copying a citation from another bibliography. Resolve DOI redirects and compare the destination title with the cited work. Record corrections explicitly; do not silently preserve a plausible but wrong DOI.

### Technical claims

State the claim being checked. Compare definitions, assumptions, equations, guarantees and limitations with the primary source. For statistical methods, record the estimand, sampling model, null hypothesis, spatial weights, edge correction and inferential procedure where relevant. For optimisation models, record decision variables, objective, constraints and units. For algorithms, distinguish worst-case guarantees from empirical performance and distinguish a problem definition from one solution method.

### Implementation and reproduction

Identify the exact software version, input contract, coordinate or unit assumptions, numerical tolerances and known limitations. A small exact solver may be a valuable teaching oracle without being a scalable production solver. Tests validate the stated contract; they do not automatically establish fidelity to every published variant.

### Rights

Check the exact asset or dataset, not merely the host website or paper. Record creator, source, licence and version, required attribution, modifications and date checked. If redistribution rights are unclear, link to the original rather than copying it. The supplied compendium and its transcription require a separate ownership and permission decision.

## Recommended entry record

For each source entry, retain:

- stable source-entry ID;
- original section, heading and page;
- exact source label;
- provisional and then confirmed primary kind;
- identity and bibliography status;
- technical-claim status and the exact claims checked;
- implementation/reproduction status;
- rights status for any reused artefact;
- evidence URLs or DOIs, access date and concise evidence notes;
- candidate canonical-record links, aliases, variants and duplicate relationships;
- reviewer and last-reviewed date.

For grouped labels, do not assign one status to a whole family if its members have different identities or evidence. Split the group into child entries while retaining the original grouped label as the parent intake record.

## Review order

1. Preserve the intake text and source-page provenance.
2. Split ambiguous grouped labels into reviewable child entries where necessary.
3. Resolve identity and canonical spelling.
4. Verify bibliographic metadata.
5. Check the technical claims relevant to the planned lesson.
6. Decide canonical scope and relationships.
7. Check implementation/reproduction claims.
8. Check redistribution rights independently.
9. Update the section index, coverage matrix and canonical record together.

## Publication rule

Use wording that matches the evidence. “Captured” means transcribed. “Identity confirmed” means the item has been resolved. “Bibliography confirmed” means its citation metadata is accurate. “Technical claims checked” means the named claims were compared with evidence. Never call a whole source entry or section simply “verified” when only one of these dimensions has been checked.
