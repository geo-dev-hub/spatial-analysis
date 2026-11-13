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
- [x] Add line simplification dossiers and tested open-polyline baselines for Douglas–Peucker and Visvalingam–Whyatt.
- [x] Add an offsetting dossier and a tested Shapely/GEOS wrapper, explicitly distinguished from Clipper2.
- [x] Add proximity graph definitions and tested small-input baselines for Gabriel, relative neighbourhood, lune-based beta-skeleton, Yao graph and Euclidean MST.
- [x] Add a planar point-location dossier and a tested static slab locator for pairwise interior-disjoint polygon faces; randomized trapezoidal-map construction remains open.
- [x] Add shortest-path family research and tested Dijkstra, A*, Bellman–Ford and Floyd–Warshall baselines.
- [x] Add coverage-aware polygon simplification through Shapely/GEOS with validity checks and tests.
- [x] Add a native Clipper2 C# offset example with a CI smoke test.
- [x] Extend shortest-path teaching code with bidirectional Dijkstra and directed ALT landmarks.
- [ ] Implement a dedicated snap-rounding noder, efficient Delaunay-based Yao/beta-skeleton constructions, and a true randomized trapezoidal-map locator.
- [x] Add tested edge-based turn-aware and FIFO time-dependent earliest-arrival baselines.
- [ ] Extend network routing with contraction hierarchies, non-FIFO routing, transit algorithms and multimodal transfers.
- [ ] Extend spatial indexing into dynamic trees, octrees, ball/VP trees and space-filling curves.
- [ ] Extend spatial statistics with spatial correlograms, point-pattern analysis and spatial regression.
- [x] Add a first geostatistics lesson comparing IDW and ordinary kriging, with an empirical semivariogram estimator, tests, intern walkthrough and interactive notebook.
- [x] Add a first raster lesson for the Euclidean distance transform, including non-square cell spacing, tests, intern walkthrough and interactive notebook.
- [x] Add a D8 flow-direction lesson with explicit direction codes, rectangular cell spacing, NoData handling, tests, intern walkthrough and interactive notebook.
- [x] Add a Horn 3×3 slope-and-aspect lesson with projected-grid spacing, vertical-unit conversion, downslope aspect convention, strict NoData policy, tests, intern walkthrough and interactive notebook.
- [x] Add a local hillshade lesson derived from slope/aspect, with explicit sun-angle conventions, flat-cell behavior, tests and an extended terrain notebook.\n- [x] Add a topographic wetness index lesson from supplied specific catchment area and slope, with explicit units and flat-slope floor, tests and an extended terrain notebook.
- [x] Add a topographic wetness index lesson with specific-area units, explicit flat-slope floor, tests, intern walkthrough and interactive terrain notebook.
- [x] Add a raster least-cost distance lesson with multi-source Dijkstra, 4/8 connectivity, anisotropic cell spacing, explicit edge costs and corner policy, tests, intern walkthrough and interactive notebook.
- [x] Add a first remote-sensing lesson for NDVI, with explicit NoData/quality-mask handling, tests, intern walkthrough and interactive notebook.
- [x] Add a first location-science lesson for uncapacitated p-median, with an exact small-instance solver, tests, intern walkthrough and interactive notebook.
- [x] Add a first 2SFCA accessibility lesson and binary-catchment implementation with explicit supply/demand and unreachable-pair contracts, tests, intern walkthrough and interactive notebook.
- [x] Add a DBSCAN density-clustering lesson, deterministic border-point policy, tests, intern walkthrough and interactive notebook.
- [x] Add a fixed-bandwidth planar Gaussian KDE point-pattern lesson with explicit intensity units and edge-effect limits, tests, intern walkthrough and interactive notebook.
- [x] Add a descriptive Clark–Evans nearest-neighbour index with a homogeneous Poisson reference, explicit edge-effect limits, tests, intern walkthrough and interactive notebook.
- [x] Add an uncorrected Ripley's K/L point-pattern summary with explicit finite-window limitations, tests, intern walkthrough and interactive notebook.
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
- [x] GitHub Actions workflow configured to test all forty Python implementation packages and execute all thirty-three notebooks. The k-d tree, quadtree and polygon-validity suites are included in the matrix; the quadtree notebook is included in notebook execution.
- [x] Confirm a successful Actions run for all twenty-eight Python implementation suites, the Clipper2 C# smoke test, internal links and all twenty-one notebook executions. A later DBSCAN ambiguous-border regression case is being revalidated in a follow-up run.
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

The repository has item-level intake indexes for all 22 source sections, but intake is not the same as verification. Section 1 now has a substantial geometry, indexing and routing learning set, with explicit open work including a true snap-rounding noder, randomized trapezoidal maps, scalable proximity-graph construction and advanced transit/network routing. Section 2 has Global and Local Moran/Geary/Getis-Ord material, DBSCAN, fixed-bandwidth planar KDE, Clark–Evans and an uncorrected Ripley's K/L summary; edge-corrected inference, point-process models, broader clustering, spatial regression and econometrics remain open. Section 3 has an audited IDW/ordinary-kriging lesson, empirical semivariogram estimator, tests and notebook; model fitting, anisotropy, co-kriging and scalable approximations remain open. Section 4 now has focal raster statistics, Priority-Flood depression filling, a Euclidean distance transform, Horn slope/aspect, local hillshade, topographic wetness index, Euclidean and least-cost distance, D8 flow direction and accumulation, single-outlet watershed delineation, and Strahler/Shreve stream ordering. Depression breaching, flat resolution, D-infinity/MFD, curvature and channel extraction remain open. Section 5 has an NDVI lesson with explicit reflectance and quality-mask caveats. Section 6 has an uncapacitated p-median model and exact small-instance solver; capacity, robust and equity constraints and the wider mobility/transport methods remain open. Sections 7–22 are still primarily indexed source intake, not complete technical chapters.

The branch currently contains forty Python implementation packages, thirty-three executable notebooks and a Clipper2 C# smoke check. The latest completed CI run passed all 40 Python implementation suites, the Clipper2 C# smoke check, internal links and all 33 notebook executions (43/43 jobs). The subsequent topographic-wetness-index additions are in the next validation run. The repository is still a draft: source entries need item-by-item verification, licensing decisions remain open, and many subject areas have not yet received researched learning material.

We will keep working through those gaps before designing the membership tiers, archive packaging or Patreon publishing workflow.
