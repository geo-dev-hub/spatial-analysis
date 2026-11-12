# What the collection covers

This matrix connects the original compendium to the work published in this repository. It is deliberately conservative: a topic is not marked researched or implemented just because its name appears in the source transcription.

**Status key**

- **Captured** — the source text is preserved in the page transcription.
- **Mapped** — the original section is indexed and its scope is visible.
- **In progress** — at least one canonical record or implementation exists, but the section is not comprehensively covered.
- **Not started** — no reviewed canonical coverage has been published yet.

| Section | Original source topic | Intake | Current project coverage | Next useful work |
|---:|---|---|---|---|
| 1 | Core GIS: geometry, indexing, proximity, networks, routing | Captured | **In progress.** Point in polygon, segment intersection, polygon intersection and Bentley–Ottmann have records; Python examples exist for all four. | Continue geometry and topology; then indexing, proximity, joins and network/routing methods. |
| 2 | Spatial statistics: autocorrelation, point patterns, clustering, regression, econometrics | Captured | Not started | Build a foundation path from spatial weights and autocorrelation through point patterns and spatial regression. |
| 3 | Geostatistics, interpolation, uncertainty, spatiotemporal models | Captured | Not started | Begin with distance-based interpolation, variograms and ordinary kriging; make uncertainty visible in examples. |
| 4 | Raster, terrain, hydrology, geomorphology | Captured | Not started | Establish raster data models, neighbourhood operations, terrain derivatives and flow routing. |
| 5 | Remote sensing, SAR, LiDAR, photogrammetry | Captured | Not started | Separate sensor physics, preprocessing, feature extraction and derived products. |
| 6 | Optimization, location science, mobility, transport | Captured | Not started | Connect network algorithms to facility location, routing, accessibility and transport modelling. |
| 7 | Domain modeling: environment, hazards, ecology, health, urban, energy, ocean | Captured | Not started | Organise by domain question and identify the shared methods used across applications. |
| 8 | GeoAI and geospatial foundation models (GeoFMs) | Captured | Not started | Separate model families, tasks, data requirements, evaluation and deployment workflows. |
| 9 | Geodesy, cartography, data infrastructure, privacy, text and semantics | Captured | Not started | Create distinct foundations for reference systems, visual communication, data systems and responsible use. |
| 10 | Additions: classical, statistical and computational methods | Captured | Not started | Audit every named item against primary sources and classify its kind before creating records. |
| 11 | Additions: GeoAI, GeoFMs and computer vision | Captured | Not started | Verify remembered names and distinguish established models from representative examples. |
| 12 | Additions: signal processing, GNSS, regional science, resilience | Captured | Not started | Review adjacent-field methods and document their spatial assumptions. |
| 13 | Additions: GeoFM workflows, urban and mobility foundation models, geo-LLMs | Captured | Not started | Verify model names, papers, dates, datasets and claimed capabilities. |
| 14 | Additions: databases, graphics, morphology, hazards, inventory, cartographic math | Captured | Not started | Split broad groups into data structures, algorithms, metrics and applied workflows. |
| 15 | Additions: vision backbones, registration, vector extraction, hydrology ML | Captured | Not started | Verify each model family and compare it with classical baselines. |
| 16 | Additions: flows, regions, deformation, marine, biodiversity, humanitarian | Captured | Not started | Create cross-domain records with explicit input, scale and validation requirements. |
| 17 | Additions: geometry II, scalable computation, design, siting, implementations | Captured | Not started | Continue geometry coverage and identify methods whose main contribution is system design or implementation. |
| 18 | Additions: moving objects, routing, transit, water and ice, emissions, data-quality statistics | Captured | Not started | Verify the remembered additions; prioritise movement, transit and time-dependent network methods. |
| 19 | Additions: African applications, addressing, finance, telecom, seismology, pitfalls | Captured | Not started | Ground regional examples in published data and local evidence; avoid treating one city or country as representative of a continent. |
| 20 | Additions: indices, microwave and thermal retrieval, event tracking, information theory, surveys | Captured | Not started | Verify terminology and separate measurement indices from retrieval algorithms and survey designs. |
| 21 | Additions: neural fields, climate ML, accounting, robust geometry, semantic maps, integrity | Captured | Not started | Verify recent research claims and distinguish mature methods from emerging proposals. |
| 22 | Additions: inference engines, covariance, spherical statistics, asset mapping, monitoring | Captured | Not started | Verify every named method and map its relationship to existing records. |

## What this tells us

The repository has a useful first set of geometry examples, but it does not yet cover the breadth of the 47-page source. The next stage is not to create hundreds of shallow pages. It is to audit the source section by section, identify the right record type, verify names and references, and build connected explanations with examples.

Sections 11, 13, 15, 18, 19, 20, 21 and 22 carry explicit source warnings about remembered or representative additions. Section 12 also includes methods drawn from adjacent fields. Keep those warnings attached to the relevant intake material until each entry has been checked.

See the [original section map](source-sections.md) and [page-by-page source transcription](../source-inventory/README.md).
