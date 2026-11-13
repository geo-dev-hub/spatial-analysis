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
- [x] Extract and classify the source entries across all 22 sections; preserve original groupings and labels.
- [ ] Verify names, variants and claims against authoritative sources.
- [x] Record source-page provenance in the item-level section indexes.
- [ ] Map duplicates, variants and cross-domain relationships across the full catalogue.
- [x] Define a primary record-type taxonomy and classification rules.
- [ ] Apply a primary kind and verification status to every source entry across all 22 sections.

## 3. The first learning paths work end to end

- [x] Geometry starter set: point in polygon, segment intersection, polygon intersection and Bentley–Ottmann.
- [x] Runnable Python examples and tests for the four topics.
- [x] Step-by-step implementation walkthroughs for all eight Python examples.
- [x] Complete the geometry foundations path as a coherent four-lesson sequence.
- [x] Add worked examples, runnable examples and a final review exercise connecting the four topics.
- [x] Add four source-derived spatial-statistics lessons and two supplementary companions, with PySAL-based runnable notebooks, conditional permutation explanations and FDR treatment.
- [x] Add live ipywidgets controls to compare Moran's I and Geary's C while changing values and weight style.
- [x] Add an interactive geometry lab for point-in-polygon, segment intersection and polygon overlay.
- [x] Add a learning path connecting global and local autocorrelation methods, including Getis-Ord hotspot analysis.
- [x] Add the first spatial-index foundation: STR-packed R-tree, a tested teaching implementation and interactive notebook.
- [x] Add filter-and-refine spatial join with a Shapely implementation, tests and an interactive notebook.
- [x] Add a spatial weights foundation lesson and notebook covering contiguity, distance bands, kNN, transformations and isolates.
- [x] Add a spatial index selection guide that compares the R-tree, quadtree and k-d tree by data model, query, update pattern, coordinate metric and validation workload.
- [x] Review the polygon-clipping and overlay-operation lessons; add scoped runnable examples, edge-case tests and intern walkthroughs.
- [x] Add a Shapely-backed polygon-validity inspection and explicit-repair example with tests and an intern walkthrough. This demonstrates the API workflow, not a from-scratch validity algorithm.
- [x] Add a static 2D k-d tree teaching implementation, deterministic tie handling, brute-force differential tests and an intern walkthrough.
- [x] Add a bucket point-region quadtree with explicit split-boundary, root-extent and duplicate-coordinate rules, brute-force differential tests, an intern walkthrough and an executable notebook. The implementation remains a scoped teaching index, not a production geospatial index.
- [ ] Extend spatial indexing into dynamic trees, octrees, ball/VP trees, space-filling curves, advanced nearest-neighbour queries, proximity and networks.
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
- [x] Add stable cell IDs to all ten notebooks and repair missing required code-cell outputs.
- [x] Reuse a verified public-domain R-tree diagram, with creator credit and source rights recorded.
- [x] Add a visual polygon-overlay notebook showing operation outputs, lower-dimensional contacts, holes, multipart results and precision-grid experiments.
- [ ] Add maps and real datasets where geographic context is essential.
- [ ] Check diagrams, formulas and examples in GitHub's rendered view before release.
- [x] Ensure every reused figure has useful alt text and a caption.

## 5. The examples can be trusted and reproduced

- [x] Versioned dependencies for current Python examples.
- [x] Tests and documented input contracts.
- [x] Add a regression test for a ray passing through a concave vertex in point-in-polygon.
- [x] A benchmark report with its workload and limitations stated.
- [x] GitHub Actions workflow configured to test all thirteen Python examples and execute all twelve notebooks. The k-d tree, quadtree and polygon-validity suites are included in the matrix; the quadtree notebook is included in notebook execution.
- [x] Confirm a previous successful Actions run for the eight established Python test suites, all ten notebooks and the internal-link check. The new k-d tree suite has been added to CI but has not yet been observed passing.
- [x] Add regression tests for polygon validity, clipping, overlay topology and precision-grid input contracts.
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

The repository now has item-level intake indexes for all 22 source sections, a complete geometry foundations path with four runnable examples and intern walkthroughs, and a spatial-autocorrelation path with four source-derived methods plus two supplementary companions. The indexing material now includes an STR-packed R-tree, filter-and-refine spatial join, a static 2D k-d tree and a bucket point-region quadtree, connected by a workload-oriented index selection guide. A Shapely-backed polygon-validity inspection and explicit-repair example has also been added. The k-d tree and quadtree each have Python teaching implementations, brute-force differential tests and intern walkthroughs; the quadtree also has an executable notebook. The k-d tree's first CI run exposed an incorrect split-axis coordinate in its pruning bound. The implementation has been corrected, a dedicated regression test added, and the corrected algorithm independently checked against a brute-force oracle over the regression case and 600 deterministic random queries. The quadtree test suite passed in CI and the internal-link check passed. The run was cancelled before all notebook checks completed; a clean full run for the latest head is still required. The polygon-validity lesson now has a tested Shapely-backed workflow; convex polygon clipping has a dependency-free Sutherland–Hodgman teaching implementation; and polygon overlay has a tested Shapely/GEOS package covering four operations, topology edge cases and precision-grid controls. A visual overlay notebook is included in CI. These are teaching packages with explicit limits, not a from-scratch GEOS replacement. The quadtree is specifically a point-region tree for point-window queries, not a region quadtree or general geometry index. The work is still early: the source catalogue has not been audited item by item, licensing decisions remain open, and most subject areas do not yet have researched learning material.

We will keep working through those gaps before designing the membership tiers, archive packaging or Patreon publishing workflow.
