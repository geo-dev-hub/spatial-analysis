# Repository roadmap

This roadmap keeps the work focused on making the public collection genuinely useful before we design the membership experience.

The goal is not to fill folders or publish pages quickly. The goal is a collection that a new reader can enter easily, learn from independently, reproduce and improve with others.

## 1. The reader can find their way

- [x] Public-facing introduction and clear first steps.
- [x] Reader-friendly writing guide.
- [x] Learning paths that allow people to start with a problem rather than a fixed sequence.
- [x] Clear links to algorithms, implementations, exercises, research and benchmarks.
- [x] Contribution guidance and GitHub issue forms.
- [x] Add an automated check for relative links in Markdown files and notebook Markdown cells.
- [ ] Check heading anchors and rendered navigation across the repository.
- [ ] Confirm rights to publish the supplied compendium and its transcription.
- [x] Prepare a licensing decision proposal for original code, documentation, third-party material and contributions.
- [ ] Choose project licences for original code and documentation; agree contributor sign-off.
- [ ] Review navigation on a phone-sized screen and with a screen reader.

## 2. The source compendium is accounted for

- [x] Preserve the 47-page source transcription and original page boundaries.
- [x] Preserve the original 22 section headings and editorial cautions.
- [x] Publish a coverage matrix that distinguishes captured material from researched material.
- [x] Capture and provisionally classify the grouped source entries across all 22 sections; preserve original groupings and labels.
- [x] Mark each grouped entry as captured but not individually verified, and label proposed record types as provisional.
- [ ] Verify names, variants and claims against authoritative sources.
- [x] Record source-page provenance in the item-level section indexes.
- [ ] Map duplicates, variants and cross-domain relationships across the full catalogue.
- [x] Define a primary record-type taxonomy and classification rules.
- [ ] Verify every named method, model, metric, product and implementation; promote provisional types to confirmed primary kinds only when evidence supports them.

## 3. The first learning paths work end to end

- [x] Geometry starter set: point in polygon, segment intersection, polygon intersection and Bentley–Ottmann.
- [x] Runnable Python examples and tests for the four topics.
- [x] Step-by-step implementation walkthroughs for all ten Python examples.
- [x] Complete the geometry foundations path as a coherent four-lesson sequence.
- [x] Add worked examples, runnable examples and a final review exercise connecting the four topics.
- [x] Add four source-derived spatial-statistics lessons and two supplementary companions, with PySAL-based runnable notebooks, conditional permutation explanations and FDR treatment.
- [x] Add live ipywidgets controls to compare Moran's I and Geary's C while changing values and weight style.
- [x] Add an interactive geometry lab for point-in-polygon, segment intersection and polygon overlay.
- [x] Add a learning path connecting global and local autocorrelation methods, including Getis-Ord hotspot analysis.
- [x] Add the first spatial-index foundation: STR-packed R-tree, a tested teaching implementation and interactive notebook.
- [x] Add filter-and-refine spatial join with a Shapely implementation, tests and an interactive notebook.
- [x] Add a spatial weights foundation lesson and notebook covering contiguity, distance bands, kNN, transformations and isolates.
- [x] Add the first deterministic interpolation record: inverse distance weighting, with a tested Python reference implementation, walkthrough and interactive notebook.
- [x] Add the empirical semivariogram foundation, with a tested Matheron estimator, pair-count diagnostics, walkthrough and interactive lab.
- [x] Add ordinary kriging with PyKrige, point/grid tests, a step-by-step walkthrough and an interactive prediction/variance lab.
- [ ] Extend interpolation through natural neighbour, splines, radial basis functions, variograms and kriging.
- [ ] Extend spatial indexing into dynamic trees, quadtrees, nearest-neighbour search, proximity and networks.
- [ ] Extend spatial statistics with spatial correlograms, point-pattern analysis and spatial regression.
- [ ] Add domain paths only when their methods and examples are ready.

## 4. Every lesson uses the right teaching tools

- [x] Mathematical notation standard and rendered display equations.
- [x] Add a live widget lab comparing Global Moran's I and Geary's C with adjustable observations and weights.
- [x] Mermaid diagrams for process and decision logic.
- [x] SVG for precise geometric illustrations.
- [x] Source-figure attribution and licence policy.
- [x] Reuse seven verified Wikimedia Commons figures across lessons: three CC BY-SA 4.0, two CC BY-SA 3.0, one CC0 1.0 and one public-domain figure.
- [x] Add six spatial-statistics notebooks for Global Moran's I, Global Geary's C, Local Moran's I, Local Geary, Global Getis-Ord G and Getis-Ord Gi*.
- [x] Add three further notebooks for STR-packed R-tree, filter-and-refine spatial join and spatial weights.
- [x] Add an interactive IDW lab with a movable target, power control and neighbour selection.
- [x] Add an interactive empirical semivariogram lab with adjustable lag bins and maximum distance.
- [x] Add stable cell IDs to all twelve notebooks and repair missing required code-cell outputs.
- [x] Reuse a verified public-domain R-tree diagram, with creator credit and source rights recorded.
- [ ] Add maps and real datasets where geographic context is essential.
- [ ] Check diagrams, formulas and examples in GitHub's rendered view before release.
- [x] Ensure every reused figure has useful alt text and a caption.

## 5. The examples can be trusted and reproduced

- [x] Versioned dependencies for current Python examples.
- [x] Tests and documented input contracts.
- [x] Add a regression test for a ray passing through a concave vertex in point-in-polygon.
- [x] A benchmark report with its workload and limitations stated.
- [x] GitHub Actions workflow configured to test all eleven Python examples and execute all thirteen notebooks.
- [x] Confirm successful Actions run for all eleven Python test suites, all thirteen notebooks and the internal-link check.
- [ ] Add regression tests whenever a real edge case is discovered.
- [ ] Add representative workloads before drawing broader performance conclusions.
- [ ] Publish data provenance and licence notes for every shared dataset.

## 6. The collection is ready for a wider audience

Before moving to the membership and Patreon work, check that:

- a first-time reader can find a useful starting point without needing personal guidance;
- the geometry foundations path and the first spatial-autocorrelation path provide complete, reproducible sequences;
- the source catalogue has a traceable review process and no invented coverage;
- every published lesson distinguishes established facts, implementation behaviour, experiments and open questions;
- examples and tests are reproducible;
- diagrams and datasets have clear reuse rights;
- contributors can report, improve and extend the work without paying;
- the public collection offers real value on its own.

## Current position

The repository now has item-level intake indexes for all 22 source sections, a complete geometry foundations path with four runnable examples and intern walkthroughs, and a spatial-autocorrelation path with four source-derived methods plus two supplementary companions. It also has two spatial-indexing/query-processing lessons and a spatial-weights foundation. The previous recorded Actions run verified ten notebooks and eight Python example suites, alongside the internal-link check. The IDW and empirical semivariogram implementations and their notebooks have been added to the workflow; the expanded run now covers ten test suites and twelve notebooks and is awaiting confirmation. The source indexes now mark each grouped entry as captured but not individually verified, and proposed record types are explicitly provisional. The catalogue still needs item-by-item verification, duplicate and variant mapping, licensing decisions, and substantial researched learning material across most subject areas.

We will keep working through those gaps before designing the membership tiers, archive packaging or Patreon publishing workflow.
