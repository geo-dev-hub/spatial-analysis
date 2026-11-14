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
- [x] Add a conservative source-entry review label to every entry row across all 22 section indexes; a linked canonical record is marked partial, not verified.
- [ ] Confirm the primary kind and record identity, bibliography, technical-claim and rights status separately for every source entry.

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
- [x] Add line simplification dossiers and tested open-polyline baselines for Douglas–Peucker and Visvalingam–Whyatt.
- [x] Add an offsetting dossier and a tested Shapely/GEOS wrapper, explicitly distinguished from Clipper2.
- [x] Add proximity graph definitions and tested small-input baselines for Gabriel, relative neighbourhood, lune-based beta-skeleton, Yao graph and Euclidean MST.
- [x] Add a planar point-location dossier, tested static slab locator for pairwise interior-disjoint polygon faces, intern implementation contract and interactive lab; randomized trapezoidal-map construction remains open.
- [x] Add shortest-path family research and tested Dijkstra, A*, Bellman–Ford and Floyd–Warshall baselines.
- [x] Add coverage-aware polygon simplification through Shapely/GEOS with validity checks and tests.
- [x] Add a native Clipper2 C# offset example with a CI smoke test.
- [x] Extend shortest-path teaching code with bidirectional Dijkstra and directed ALT landmarks.
- [x] Add a dedicated exact-arithmetic hot-pixel snap-rounding teaching noder, tests, walkthrough, exercise and visual lab. Its pairwise discovery and hot-pixel scan are intentionally not output-sensitive.
- [ ] Implement efficient Delaunay-based Yao/beta-skeleton constructions and a true randomized trapezoidal-map locator.
- [x] Add tested edge-based turn-aware and FIFO time-dependent earliest-arrival baselines.
- [ ] Extend network routing with contraction hierarchies, non-FIFO routing, transit algorithms and multimodal transfers.
- [ ] Extend spatial indexing into dynamic trees, octrees, ball/VP trees and space-filling curves.
- [ ] Extend spatial statistics with spatial correlograms, point-pattern analysis and spatial regression.
- [x] Add a spatial cross-validation lesson and tested grid-block/buffered-fold baseline with an intern walkthrough; keep block-size selection and deployment-specific design as explicit research decisions.
- [x] Add a masked-autoencoding method lesson and tested NumPy patch masking/restoration baseline with an intern walkthrough; do not present it as a trained foundation model.
- [x] Add a seven-parameter Helmert Position Vector lesson and tested geocentric XYZ implementation, including a published IOGP example and inverse-transform tests.
- [x] Add an affine georeferencing lesson and tested least-squares control-point fit, including rank checks, residual diagnostics and pixel-coordinate convention notes.
- [x] Add a first geostatistics lesson comparing IDW and ordinary kriging, with an empirical semivariogram estimator, tests, intern walkthrough and interactive notebook.
- [x] Add a first raster lesson for the Euclidean distance transform, including non-square cell spacing, tests, intern walkthrough and interactive notebook.
- [x] Add a D8 flow-direction lesson with explicit direction codes, rectangular cell spacing, NoData handling, tests, intern walkthrough and interactive notebook.
- [x] Add a Horn 3×3 slope-and-aspect lesson with projected-grid spacing, vertical-unit conversion, downslope aspect convention, strict NoData policy, tests, intern walkthrough and interactive notebook.
- [x] Add a local hillshade lesson derived from slope/aspect, with explicit sun-angle conventions, flat-cell behavior, tests and an extended terrain notebook.
- [x] Add a topographic wetness index lesson from supplied specific catchment area and slope, with explicit units and flat-slope floor, tests and an extended terrain notebook.
- [x] Add a raster least-cost distance lesson with multi-source Dijkstra, 4/8 connectivity, anisotropic cell spacing, explicit edge costs and corner policy, tests, intern walkthrough and interactive notebook.
- [x] Add a first remote-sensing lesson for NDVI, with explicit NoData/quality-mask handling, tests, intern walkthrough and interactive notebook.
- [x] Add a first location-science lesson for uncapacitated p-median, with an exact small-instance solver, tests, intern walkthrough and interactive notebook.
- [x] Add a MEXCLP expected-coverage lesson, exact small-instance placement solver, independent-busy-fraction tests, intern walkthrough, exercise and interactive sensitivity lab; distinguish it from deterministic backup coverage and hypercube queueing.
- [x] Add a weighted linear combination decision-rule lesson, tested NumPy aggregation baseline, explicit factor/constraint and NoData contracts, sensitivity guidance, intern walkthrough and interactive suitability lab.
- [x] Add a first 2SFCA accessibility lesson and binary-catchment implementation with explicit supply/demand and unreachable-pair contracts, tests, intern walkthrough and interactive notebook.
- [x] Add a DBSCAN density-clustering lesson, deterministic border-point policy, tests, intern walkthrough and interactive notebook.
- [x] Add a fixed-bandwidth planar Gaussian KDE point-pattern lesson with explicit intensity units and edge-effect limits, tests, intern walkthrough and interactive notebook.
- [x] Add a descriptive Clark–Evans nearest-neighbour index with a homogeneous Poisson reference, explicit edge-effect limits, tests, intern walkthrough and interactive notebook.
- [x] Add uncorrected and rectangular-window translation-corrected Ripley's K/L summaries, then extend them with conditional-CSR simulation envelopes and a global studentised maximum-deviation test, tests, intern walkthrough, exercise and interactive notebook.
- [ ] Continue the source-derived coverage in sections 2–6: point patterns, variogram fitting and uncertainty, terrain/hydrology, sensor processing, location models and transport analysis.
- [ ] Add domain paths only when their methods and examples are ready.

## 4. Every lesson uses the right teaching tools

- [x] Mathematical notation standard and rendered display equations.
- [x] Add a live widget lab comparing Global Moran's I and Geary's C with adjustable observations and weights.
- [x] Mermaid diagrams for process and decision logic.
- [x] SVG for precise geometric illustrations.
- [x] Source-figure attribution and licence policy.
- [x] Reuse seven verified Wikimedia Commons figures across lessons: three CC BY-SA 4.0, two CC BY-SA 3.0, one CC0 1.0 and one public-domain figure.
- [x] Add six spatial-statistics notebooks for Global Moran's I, Global Geary's C, Local Moran's I, Local Geary, Global Getis-Ord G and Getis-Ord Gi*; add DBSCAN as a separate density-clustering lab.
- [x] Add three further notebooks for STR-packed R-tree, filter-and-refine spatial join and spatial weights.
- [x] Add interactive notebooks for empirical geostatistical interpolation, raster distance transforms, focal raster statistics, Priority-Flood depression filling, D8 flow direction, D8 flow accumulation, single-outlet watershed delineation, Strahler/Shreve stream order, point-pattern KDE, Clark–Evans and Ripley's K/L, NDVI, p-median facility location and 2SFCA accessibility.
- [x] Add stable cell IDs to all ten notebooks and repair missing required code-cell outputs.
- [x] Reuse a verified public-domain R-tree diagram, with creator credit and source rights recorded.
- [x] Add a visual polygon-overlay notebook showing operation outputs, lower-dimensional contacts, holes, multipart results and precision-grid experiments.
- [x] Add a Graham scan convex-hull lesson, tested dependency-free implementation, intern walkthrough and visual notebook.
- [x] Add a Voronoi/Delaunay duality lesson, validated SciPy/Qhull wrapper, equidistance and empty-circumcircle tests, intern walkthrough and visual notebook.
- [ ] Add maps and real datasets where geographic context is essential.
- [ ] Check diagrams, formulas and examples in GitHub's rendered view before release.
- [x] Ensure every reused figure has useful alt text and a caption.

## 5. The examples can be trusted and reproduced

- [x] Versioned dependencies for current Python examples.
- [x] Tests and documented input contracts.
- [x] Add a regression test for a ray passing through a concave vertex in point-in-polygon.
- [x] A benchmark report with its workload and limitations stated.
- [x] GitHub Actions workflow configured to test all seventy-eight Python implementation packages and execute all sixty-six notebooks. The k-d tree, quadtree and polygon-validity suites are included in the matrix; the quadtree and point-location labs are included in notebook execution.
- [x] Confirm successful full-head Actions run `43563534022` on commit `2a340035372f45eb43e16770e6f41f2d6b78f70d`: all 81 workflow jobs passed, including 78 Python package suites, 66 notebook executions, internal-link checks and Clipper2 checks.
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

The repository has item-level intake indexes for all 22 source sections, but intake is not the same as verification. Section 1 now has a substantial geometry, indexing and routing learning set, with explicit open work including randomized trapezoidal maps, scalable proximity-graph construction and advanced transit/network routing. A scoped exact-arithmetic hot-pixel snap-rounding noder is now implemented with tests, walkthrough, exercise and visual lab; production-scale output-sensitive algorithms remain open. Proximity-graph research now distinguishes Delaunay-based RNG/beta-skeleton filtering from the separate O(n log n) Yao construction; scalable implementations remain open. Section 2 has Global and Local Moran/Geary/Getis-Ord material, DBSCAN, fixed-bandwidth planar KDE, Clark–Evans and uncorrected plus rectangular-window translation-corrected Ripley's K/L summaries. Ripley's K/L also has conditional homogeneous-CSR simulation envelopes and a global studentised maximum-deviation test; isotropic/border corrections, inhomogeneous point-process models, broader clustering, spatial regression and econometrics remain open. Section 3 has a combined IDW/ordinary-kriging lesson, a standalone IDW package and lesson, empirical semivariogram summaries, tests and notebooks; model fitting, anisotropy, co-kriging and scalable approximations remain open. Section 4 now has focal raster statistics, Priority-Flood depression filling, a Euclidean distance transform, Horn slope/aspect, local hillshade, topographic wetness index, nearest/bilinear resampling, zonal statistics, connected-component labeling, Euclidean and least-cost distance, D8 flow direction and accumulation, single-outlet watershed delineation, and Strahler/Shreve stream ordering. Depression breaching, flat resolution, D-infinity/MFD, curvature and channel extraction remain open. Section 5 has an NDVI lesson with explicit reflectance and quality-mask caveats. Section 6 now distinguishes uncapacitated and capacitated p-median, p-center, set covering, maximal covering, deterministic backup coverage, MEXCLP expected coverage, M/M/c queueing, accessibility-equity diagnostics, equity-constrained maximal covering and binary plus distance-decay 2SFCA. The capacitated p-median has an exact tiny-instance assignment solver for indivisible demand and deterministic scalar capacities. The first backup-coverage, MEXCLP and M/M/c implementations are exact small-instance or closed-form teaching baselines with tests, intern walkthroughs, exercises and notebooks; they do not replace stochastic reliability, adjusted MEXCLP, hypercube queueing, split-demand or robust capacity models. The wider mobility and transport methods remain open. Section 7 now has six researched decision-support lessons with tested numerical baselines: weighted linear combination; AHP pairwise weighting; Boolean/fuzzy overlay; ordered weighted averaging; TOPSIS; and weights of evidence. A scoped ELECTRE I-style relation builder now calculates weighted concordance, range-normalised discordance and the pairwise outranking relation, with tests, walkthrough, exercise and visual lab. Kernel extraction and a complete ELECTRE choice procedure remain open; the wider domain models remain open. Section 8 now has its first scoped contrastive-learning lesson; the model catalogue and remaining pretraining, architecture, adaptation, downstream and agentic topics remain open. Section 9 now has coordinate-transformation, Helmert and affine-georeferencing lessons plus a spatial-data-formats guide; cartography, infrastructure and privacy methods remain open. Section 21 now has an exact orientation predicate lesson, rational-reference implementation, near-degenerate tests and visual notebook; adaptive precision and robust constructions remain open. Section 22 now has a researched Euclidean stationary covariance foundation with five-model NumPy baseline, plus a valid scalar isotropic covariance construction on the two-sphere using non-negative Legendre coefficients. Both have tests, intern walkthroughs, exercises and visual notebooks. A third Section 22 lesson now adds graph-spectral covariance from non-negative Laplacian spectral variances, with a tested NumPy baseline and visual lab; this is not a directed flow or generic shortest-path model. Geometry-specific stationary network covariance, inference engines, basis expansions, broader spherical statistics and asset-monitoring methods remain open. A Gneiting-class nonseparable covariance baseline now has a Euclidean space-time lesson, NumPy implementation, tests, intern walkthrough, exercise and lab notebook. Section 20 now has a triple-collocation lesson, tested implementation, exercise and visual notebook, plus a researched marine heatwave event-detection lesson, tested single-series baseline and visual notebook; thermal/microwave retrieval, product merging, seasonal climatology construction and gridded feature tracking remain open. Sections 10–22 still need their own researched and verified technical material.

The latest Section 6 additions include accessibility-equity diagnostics, equity-constrained maximal covering, deterministic backup coverage, MEXCLP expected coverage and M/M/c queueing. The configured validation inventory is 78 Python package suites and 66 executable notebooks, plus internal-link and Clipper2 checks. Full-head run [43563534022](https://github.com/geo-dev-hub/spatial-analysis/actions/runs/43563534022) passed all 81 jobs on commit `2a340035372f45eb43e16770e6f41f2d6b78f70d`. The Section 2 bibliography corrections and contributor-guidance update are included in this validated head. The Matheron (1963) source citation, narrower interpolation scope description and geostatistics README/walkthrough rendering correction are included in this validated head. Section 4–5 D8, stream-order and NDVI source corrections are included in this validated head. Selected spectral-index citations for SAVI, EVI, NDWI and MNDWI are included in this validated head. Direct links to existing canonical records and conservative partial-status labels have been added to Sections 2–6 and passed full-head validation. Further links for existing records in Sections 7–10 and 20–22, plus a more precise bibliography-only partial status, are being validated separately. A green run validates configured checks, not source accuracy, rights clearance or publication readiness. The repository remains a draft: source entries still require item-by-item research, licensing decisions remain open, and many subject areas have not yet received researched learning material.

We will keep working through those gaps before designing the membership tiers, archive packaging or Patreon publishing workflow.


## 4. Continuation work recorded on 14 November 2026

- [x] Complete the ELECTRE I-style choice stage for small decision sets: exact kernel enumeration, multiple/no-kernel reporting, tests, intern walkthrough, exercise and visual lab. The relation builder's range-normalised discordance convention remains explicitly scoped.
- [x] Add a geodetic → ECEF → local ENU learning package with an explicit WGS 84 default, ellipsoidal-height contract, inverse rotation, published EPSG:9836 reference test, walkthrough, exercise and visual lab.
- [x] Extend Ripley's K/L from pair-count summaries to rectangular-window translation correction and conditional homogeneous-CSR simulation. Add pointwise quantile bands and a separate global studentised maximum-deviation Monte Carlo test, with caveats, tests, walkthrough, exercise and updated notebook.
- [x] Add the new Python package and notebook to CI rather than leaving them as unexecuted examples.
- [x] Review full-head Actions run `43563534022` on commit `2a340035372f45eb43e16770e6f41f2d6b78f70d`; the Section 2 citation corrections and contributor-guide update passed in this full-head validation; the Section 3 source and scope corrections passed in this full-head validation; the README and walkthrough formatting correction passed in this full-head validation; the Section 4–5 D8, stream-order and NDVI corrections passed in this full-head validation; the selected SAVI, EVI, NDWI and MNDWI references passed in this full-head validation; source-index linkage for Sections 2–6 passed in this full-head validation; further linkage in Sections 7–10 and 20–22 requires its own run.
- [ ] Continue the source verification and implementation passes across the remaining entries in Sections 1–22. In particular, randomized trapezoidal-map construction, efficient Yao/beta-skeleton methods, inhomogeneous point-process models, advanced routing, dynamic geodetic reference frames, and the majority of domain-specific Section 7–22 methods remain open.
- [ ] Complete a full rendered-content review, licence decision and contributor workflow review before declaring the compendium ready for public membership distribution.


## 5. Location science continuation

- [x] Add maximal covering location as a distinct model from p-median and 2SFCA, with an at-most-p budget, explicit service threshold, weighted coverage objective, deterministic tie-breaking, exact small-instance enumeration, tests, intern walkthrough, exercise and visual lab.
- [x] Add the new package and notebook to the Python CI matrix and execution list.
- [x] Add capacitated p-median with a separate capacity-load input, deterministic exact tiny-instance enumeration, infeasibility handling, tests, intern walkthrough, exercise and visual lab.
- [ ] Extend location science with stochastic/robust capacity, adjusted MEXCLP variants and hypercube queueing; distinguish these from the current deterministic and equal-busy-probability teaching baselines.


- [x] Add discrete p-center as a distinct minimax facility-location model, with exact small-instance enumeration, assignment output, tests, intern walkthrough, exercise and visual lab.
- [x] Add p-center and maximal covering to the CI matrix and notebook execution list.
- [x] Add set covering, capacitated location and distance-decay accessibility as separate, explicitly scoped models.
- [x] Add equity-aware accessibility diagnostics and group-constrained maximal covering with explicit group floors, separate population/objective weights and documented limitations.
- [x] Add deterministic backup coverage (r-covering) and a separate M/M/c queueing model, each with tests, walkthroughs, exercises and notebooks.


- [x] Integrate the standalone inverse-distance-weighting lesson, package, SVG explanation, learning path and notebook from the base branch; add the package and notebook to CI.


- [x] Add location set covering as the minimum-cardinality model for reaching every demand point within a service threshold, with infeasibility reporting, exact small-instance enumeration, tests, intern walkthrough, exercise and visual lab.
- [x] Add set covering to the CI package matrix and notebook execution list.
- [x] Add capacitated p-median and distance-decay 2SFCA with tests, walkthroughs, exercises and visual labs.
- [x] Complete the first scoped backup-coverage, queueing and equity-aware location-science packages; see the dedicated continuation records below.
- [ ] Extend location science with stochastic/robust capacity, adjusted MEXCLP variants and hypercube queueing.


## 6. Repository integrity gate — 14 November 2026

The current GitHub state has been checked directly rather than inferred from earlier session notes.

- Pull request: [#1 — Continue the spatial analysis compendium](https://github.com/geo-dev-hub/spatial-analysis/pull/1).
- State: open, draft and unmerged.
- Branch: `compendium/section-01-geometry-continuation`; base: `main`.
- Current comparison: **diverged; 129 commits behind at the last comparison** the base; GitHub reports the comparison as diverged and the pull request as not mergeable.
- Merge base: `e7a3600f8b2dd6cbede1486935b69b64cc01fcb7`.
- The branch contains a large body of work, but the divergence must be reconciled deliberately. Do not force-push, merge, or rebase blindly.
- The configured validation inventory is **78 Python package suites and 66 notebook executions**, with internal-link and Clipper2 checks. Full-head run [43563534022](https://github.com/geo-dev-hub/spatial-analysis/actions/runs/43563534022) completed successfully on `2a340035372f45eb43e16770e6f41f2d6b78f70d`, with all 81 jobs passing. Section 2 bibliography and contributor-guide changes are included in this validated head; the Section 3 source and scope corrections passed in this full-head validation; the README and walkthrough formatting correction passed in this full-head validation; the Section 4–5 D8, stream-order and NDVI corrections passed in this full-head validation; the selected SAVI, EVI, NDWI and MNDWI references passed in this full-head validation; source-index linkage for Sections 2–6 passed in this full-head validation; further linkage in Sections 7–10 and 20–22 requires its own run. This validates the configured checks on that commit; it does not establish source accuracy, rights clearance or publication readiness.
- The Section 6 continuation now includes accessibility distribution diagnostics, group-constrained maximal covering, deterministic r-covering, MEXCLP expected availability and M/M/c queueing. These are explicitly scoped teaching models, not a claim that the full location-science, stochastic reliability or fairness literature is complete.

### Release blockers

1. Reconcile the branch with the current base and inspect conflicts without discarding either side's work.
2. Run the complete validation matrix on the reconciled head and resolve every failure.
3. Verify source entries and claims against authoritative references across all 22 sections; source transcription and indexing are not verification.
4. Decide publication rights for the supplied 47-page compendium and its transcription.
5. Select and apply code/documentation licences, with contributor sign-off.
6. Review rendered navigation, heading anchors, mobile presentation, accessibility, diagrams, formulas and notebook outputs.
7. Complete the contributor workflow and public-facing documentation review.

**Patreon remains out of scope until these GitHub release gates are satisfied.** The purpose of this gate is to prevent a large, technically promising draft from being mistaken for a finished, validated and publishable compendium.


## 7. Backup-coverage learning package — 14 November 2026

Added a deterministic r-covering extension to the location-science path.

- Canonical lesson: `algorithms/optimization/backup-coverage.md`.
- Implementation: `implementations/python/backup-coverage/`, with exact subset enumeration, input validation, per-demand facility counts and deterministic tie-breaking.
- Tests: `test_backup_coverage.py`, including the distinction between distinct selected facilities and duplicate reachability.
- Learning materials: intern walkthrough, exercise and executable notebook.
- Integrated into the Section 6 catalogue, algorithm index, coverage matrix, location-science learning path and CI workflow.
- Validation inventory is now **78 Python package suites and 66 notebook executions**.

The solver is intentionally scoped as deterministic redundancy screening. It does not estimate outage probabilities, correlated failures, spare capacity or queueing. The full-head GitHub Actions run `43563534022` passed the backup-coverage package suite and all notebook executions on commit `2a340035372f45eb43e16770e6f41f2d6b78f70d`.


## 8. Service queueing learning package — 14 November 2026

Added a separate M/M/c service-operations model to the Section 6 learning path.

- Canonical lesson: `algorithms/optimization/mmc-queue.md`.
- Implementation: `implementations/python/mmc-queue/`, with Erlang-C waiting probability, expected queue/system lengths and times, utilisation, and an explicit stability check.
- Tests: M/M/1 closed-form agreement, additional-server response, Little's law, near-capacity behaviour and invalid/unstable inputs.
- Learning materials: intern walkthrough, exercise and executable notebook.
- Integrated into the algorithm index, Section 6 catalogue, coverage matrix, location-science path and CI workflow.
- Validation inventory is now **78 Python package suites and 66 notebook executions**.

The package is a stationary M/M/c teaching model, not a time-varying simulation. The full-head GitHub Actions run `43563534022` passed the M/M/c package suite and all notebook executions on commit `2a340035372f45eb43e16770e6f41f2d6b78f70d`.

## Section 6 reference corrections — 14 November 2026

- Corrected the Radke and Mu (2000) 2SFCA precursor citation to *Geographic Information Sciences*, 6(2), 105–112, DOI `10.1080/10824000009480538`.
- Corrected the Luo and Wang (2003) 2SFCA citation to *Environment and Planning B: Planning and Design*, 30(6), 865–884, DOI `10.1068/b29120`.
- Added the Luo and Qi (2009) E2SFCA erratum reference and clarified that the notebook's zonal weights are illustrative, analyst-supplied values.
- Corrected the Church and ReVelle location-model references in the equity-constrained covering lesson: the 1974 MCLP paper and the distinct 1976 theoretical-links paper now have their own correct metadata and DOI.
- The source-entry verification protocol and row-level review labels now distinguish intake, partial canonical coverage and actual evidence review. These corrections do not imply that all Section 6 source entries are verified.

## Section 1–2 bibliography audit — 14 November 2026

- Confirmed selected Section 1 source metadata for Graham (1972), Fortune (1987), Aurenhammer (1991), Bentley and Ottmann (1979), and Boissonnat and Preparata (2000); the relevant index now records the publisher/authoritative identifiers.
- Confirmed selected Section 2 source metadata for Moran (1950), Geary (1954), Getis and Ord (1992), Anselin (1995), and Ripley (1976, 1977). Corrected Ripley's 1977 page range from 172–212 to 172–192 and added the DOI; added the 1976 DOI.
- These are selected bibliographic checks, not a complete verification of all source entries or statistical assumptions in Sections 1–2.

## Section 3 bibliography audit — 14 November 2026

- Added the verified Matheron (1963) “Principles of geostatistics” reference to the interpolation lesson: *Economic Geology*, 58(8), 1246–1266, DOI `10.2113/gsecongeo.58.8.1246`.
- Replaced the phrase “first audited interpolation lesson” with a narrower scope description. A foundational citation and tested teaching solver do not imply that the whole kriging family or every Section 3 source entry has been audited.

## Geostatistics rendering correction — 14 November 2026

- The README and intern walkthrough contained literal `\\n` text in prose and a formula block rather than actual line breaks. The correction restores paragraph boundaries and the semivariogram equation as a normal display-math block. Full-head run `43563534022` passed all 81 jobs after this correction.
- This was a presentation/documentation fix; the numerical implementation and notebook were not changed.

## Section 4–5 bibliography checks — 14 November 2026

- Added DOI and publisher/USGS record links for the foundational D8 and watershed references: O'Callaghan and Mark (1984), and Jenson and Domingue (1988).
- Added DOI links for the foundational stream-order sources: Strahler (1957) and Shreve (1966).
- Expanded the NDVI source citation to include the five named authors, report period, NASA report number and NASA NTRS record. Changed “first audited spectral index” to the narrower “first scoped and tested spectral-index lesson.”
- These are selected bibliographic checks, not a complete review of all Section 4–5 methods, source entries or remote-sensing preprocessing claims.

## Selected spectral-index bibliography — 14 November 2026

- Added publisher-verified references for Huete's SAVI (1988), the MODIS vegetation-index performance paper by Huete et al. (2002), McFeeters' NDWI (1996), Xu's MNDWI (2006), and Huete et al.'s global vegetation-index comparison (1997) to the Section 5 index.
- These records help identify the named index families; they do not constitute lessons or validate every band choice, sensor-specific implementation, atmospheric correction or product workflow.

## Source-index linkage refinement — 14 November 2026

- Added direct links from grouped source-entry rows to existing canonical records for Ripley's K, IDW, ordinary kriging, variogram work, D8 routing/accumulation, watershed delineation, stream ordering, NDVI, facility-location models, M/M/c queueing, 2SFCA and accessibility equity.
- Changed the corresponding row summaries from “Not checked” to “Partial — related record exists; source-entry review pending.” The labels remain conservative: a linked record covers only part of a grouped source entry and does not verify the entire family.

## Source-index linkage validation — 14 November 2026

- Full-head run `43563534022` passed all 81 jobs after adding row-level links for existing canonical lessons in Sections 2–6. These links support a conservative “Partial” status, not full source-entry verification.
- The next pass extends those direct links to the existing records in Sections 7–10 and 20–22 and distinguishes a partially checked bibliography from a linked canonical lesson.
