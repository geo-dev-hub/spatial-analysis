# Repository roadmap

This roadmap keeps the work focused on making the public collection genuinely useful before we design the membership experience.

The goal is not to fill folders or publish pages quickly. The goal is a collection that a new reader can enter easily, learn from independently, reproduce and improve with others.

## 1. The reader can find their way

- [x] Public-facing introduction and clear first steps.
- [x] Reader-friendly writing guide.
- [x] Learning paths that allow people to start with a problem rather than a fixed sequence.
- [x] Clear links to algorithms, implementations, exercises, research and benchmarks.
- [x] Contribution guidance and GitHub issue forms.
- [ ] Check every internal link and anchor across the repository.
- [ ] Confirm rights to publish the supplied compendium and its transcription.
- [ ] Choose project licences for original code and documentation; agree contributor sign-off.
- [ ] Review navigation on a phone-sized screen and with a screen reader.

## 2. The source compendium is accounted for

- [x] Preserve the 47-page source transcription and original page boundaries.
- [x] Preserve the original 22 section headings and editorial cautions.
- [x] Publish a coverage matrix that distinguishes captured material from researched material.
- [x] Extract and classify the source entries across all 22 sections; preserve original groupings and labels.
- [ ] Verify names, variants and claims against authoritative sources.
- [x] Record source-page provenance in the item-level section indexes.
- [ ] Map duplicates, variants and cross-domain relationships across the full catalogue.
- [ ] Keep algorithms distinct from operations, models, data structures, systems, metrics, standards and workflows.

## 3. The first learning paths work end to end

- [x] Geometry starter set: point in polygon, segment intersection, polygon intersection and Bentley–Ottmann.
- [x] Runnable Python examples and tests for the four topics.
- [x] Step-by-step Bentley–Ottmann implementation walkthrough.
- [ ] Complete and review the first geometry learning path as a coherent sequence.
- [ ] Add worked examples and exercises that connect the four topics.
- [x] Add the first researched spatial-statistics lesson: Global Moran's I, with a tested dense reference implementation.
- [ ] Build the next foundations in spatial indexing, proximity, joins and networks.
- [ ] Extend spatial statistics with Geary's C, local indicators and spatial regression.
- [ ] Add domain paths only when their methods and examples are ready.

## 4. Every lesson uses the right teaching tools

- [x] Mathematical notation standard and rendered display equations.
- [x] Mermaid diagrams for process and decision logic.
- [x] SVG for precise geometric illustrations.
- [x] Source-figure attribution and licence policy.
- [x] Two verified CC BY-SA 4.0 diagrams linked into relevant lessons.
- [x] Add an interactive notebook for Global Moran's I; add others where changing inputs materially improves understanding.
- [ ] Add maps and real datasets where geographic context is essential.
- [ ] Check diagrams, formulas and examples in GitHub's rendered view before release.
- [ ] Ensure every figure has useful alt text and a caption.

## 5. The examples can be trusted and reproduced

- [x] Versioned dependencies for current Python examples.
- [x] Tests and documented input contracts.
- [x] A benchmark report with its workload and limitations stated.
- [x] GitHub Actions workflow configured to test all five Python examples and execute the learning notebook.
- [ ] Confirm successful Actions runs and repair any failures.
- [ ] Add regression tests whenever a real edge case is discovered.
- [ ] Add representative workloads before drawing broader performance conclusions.
- [ ] Publish data provenance and licence notes for every shared dataset.

## 6. The collection is ready for a wider audience

Before moving to the membership and Patreon work, check that:

- a first-time reader can find a useful starting point without needing personal guidance;
- the first learning path has a complete, tested sequence;
- the source catalogue has a traceable review process and no invented coverage;
- every published lesson distinguishes established facts, implementation behaviour, experiments and open questions;
- examples and tests are reproducible;
- diagrams and datasets have clear reuse rights;
- contributors can report, improve and extend the work without paying;
- the public collection offers real value on its own.

## Current position

The repository has its source intake, reader-facing foundations, contribution process, visual and mathematical standards, and a first set of runnable computational-geometry examples. The work is still early: the 22-section source catalogue has not been audited item by item, and most subject areas do not yet have researched learning material.

We will keep working through those gaps before designing the membership tiers, archive packaging or Patreon publishing workflow.
