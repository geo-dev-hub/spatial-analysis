# Source inventory transcription — pages 26–30

> Faithful text extraction from the supplied *Spatial Analysis Algorithms: Complete Compendium*. Original page boundaries are retained below. This is an intake transcription, not a technical verification or editorial rewrite.

`<PARSED TEXT FOR PAGE: 26 / 47>`

Spatial Analysis Algorithms: Complete Compendium




      Garin-Lowry and Lowry models, input-output and spatial CGE models, quantitative
      spatial equilibrium (Rosen-Roback style)
      Gravity trade models (PPML estimation), market access, spatial price equilibrium
      Regional convergence analysis, spatial Markov chains, LISA transitions, spatial
      dynamics of income distributions

Network resilience and infrastructure risk

      Critical node and edge detection, percolation on road networks, cascading failure
      models
      Interdependent infrastructure modeling, vulnerability and fragility curves, HAZUS-
      style loss estimation
      Reliability analysis for networks (Monte Carlo, minimal cut sets), post-disaster
      restoration scheduling

Computational geometry for districting and partitioning

      Power diagrams, centroidal Voronoi tessellation (Lloyd's algorithm), capacity-
      constrained Voronoi, semi-discrete optimal transport
      Balanced partitioning with compactness constraints, graph partitioning for equal-
      population districts

Climate analysis and attribution

      Teleconnection indices, regime detection, pattern scaling, ensemble weighting of
      CMIP models
      Extreme event attribution, detection and attribution, return level estimation with
      covariates
      Multivariate bias correction (MBCn), spatial coherence-preserving downscaling
      (Schaake shuffle, ECC)

Terrain traversability and off-road mobility

      Traversability estimation from LiDAR and imagery, rover path planning, slope and
      roughness cost maps
      Soil-vehicle interaction models, swarm and multi-robot coverage planning


13. Additions: GeoFM workflows, urban and mobility foundation
models, geo-LLMs
More of the GeoAI stack, from how foundation models are used day to day to models for
cities, movement and language. Model names are representative and from memory, so
verify before citing.




                                                                                         Page 26 of 47

`<PARSED TEXT FOR PAGE: 27 / 47>`

Spatial Analysis Algorithms: Complete Compendium




Using GeoFMs: embedding-based workflows

      Similarity search and few-shot mapping: query-by-example over embedding indexes,
      prototype-based land cover from a handful of labels
      Linear and k-NN probes on annual embedding fields; unsupervised clustering of
      embeddings for land cover discovery
      Change detection by embedding differencing, anomaly detection in embedding
      space, temporal trajectory analysis of embeddings
      Retrieval at scale: approximate nearest neighbor search (HNSW, IVF-PQ) with spatial
      and temporal metadata filters
      Evaluation protocols: frozen versus full fine-tune, label-efficiency curves, cross-
      sensor transfer, resolution generalization, spectral generalization, cross-region splits

Physics-informed and simulation-based GeoAI

      Hybrid radiative transfer plus deep learning: PROSAIL and SCOPE-driven pretraining,
      neural network inversion, Gaussian process emulators of RTMs
      Simulation-based inference and amortized Bayesian inference for retrieval problems
      Physics-guided losses and constraints: mass conservation, energy balance,
      monotonicity constraints in hydrology and climate emulators
      Differentiable simulators and differentiable hydrology (differentiable parameter
      learning)

Multimodal inputs beyond imagery

      LiDAR, GEDI and ICESat-2 fused with optical and SAR; street view; POIs; building
      footprints; road graphs; soundscapes
      Mobility and social data as modalities: CDR, GPS traces, check-ins, transit smart card
      data
      Text and knowledge graph conditioning for place understanding, geographic
      hierarchies as inductive bias

Urban and spatiotemporal foundation models

      Urban vision-language: UrbanCLIP, UrbanVLP, region embedding models, street-view
      and satellite fusion for socioeconomic prediction
      Spatiotemporal and traffic foundation models: UniST, UrbanGPT, OpenCity, UrbanDiT,
      STFM-style universal forecasters
      Trajectory foundation models: TrajFM, UniTraj, trajectory tokenizers, mobility LLMs for
      next-location and mode prediction
      General time-series foundation models applied to spatial sensors: TimesFM, Chronos,
      Moirai, Lag-Llama, with spatial adapters




                                                                                        Page 27 of 47

`<PARSED TEXT FOR PAGE: 28 / 47>`

Spatial Analysis Algorithms: Complete Compendium




      Hypergraph and heterogeneous graph neural networks for urban knowledge graphs,
      region and POI embeddings (HGI, ReMVC)

Geospatial LLMs and agents

      Domain LLMs: GeoGalactica, K2, GeoGPT, GeoLLM, map-aware instruction-tuned
      models
      Map understanding: map VQA, map reading, georeferenced map OCR, chart and
      cartographic style question answering
      Tool-use evaluation: GeoLLM-Engine, GeoBenchX, GIS Copilot-style agents, spatial
      reasoning benchmarks (SpatialEval, GeoQA)
      Pipelines: natural language to spatial SQL, to PyQGIS, to GeoPandas or GDAL, with
      validation, execution sandboxes and self-repair loops
      Retrieval and grounding: GeoRAG over STAC catalogs, metadata-aware retrieval, OSM
      tag reasoning, gazetteer-augmented generation

Data-centric GeoAI

      Label refinement from coarse land cover and OSM, noisy-label correction, confident
      learning for segmentation
      Synthetic data: physically based rendering, procedural cities, domain randomization,
      diffusion-generated training tiles
      Dataset distillation and core-set selection for imagery, geographic diversity sampling,
      long-tail class handling
      Annotation tooling: SAM-assisted labeling, superpixel scribbles, interactive
      segmentation, consensus labeling across annotators

Scaling and efficiency

      Neural scaling laws for EO pretraining (data, parameters, compute), compute-optimal
      budgets, data pruning
      Efficient attention: windowed, linear, state-space, FlashAttention; resolution-adaptive
      patching; token dropping
      Mixed-resolution inference: coarse-to-fine cascades, region-of-interest zoom,
      gigapixel streaming


14. Additions: databases, graphics, morphology, hazards,
inventory, cartographic math
Further algorithm families, many from computer science and applied fields.

Spatial database and distributed systems internals




                                                                                      Page 28 of 47

`<PARSED TEXT FOR PAGE: 29 / 47>`

Spatial Analysis Algorithms: Complete Compendium




      R-tree node split heuristics (linear, quadratic, R*), bulk loading (Nearest-X, Hilbert
      packing, STR, OMT), buffer trees, LSM-based spatial indexes
      PostgreSQL index types for spatial data: GiST, SP-GiST, BRIN; time-partitioned spatial
      tables
      Distributed spatial joins: broadcast joins, quadtree and KDB-tree partitioning, skew
      handling, Z-order partitioning, DITA and Simba-style trajectory engines
      Streaming spatial analytics: continuous range queries, sliding-window geofencing,
      incremental kNN maintenance

3D graphics algorithms used in geospatial analysis

      Ray-triangle intersection (Moller-Trumbore), BVH construction with surface area
      heuristic, kd-tree ray traversal
      Frustum and occlusion culling, level-of-detail selection, shadow mapping and shadow
      volumes for city shadow analysis
      Photon mapping and radiosity for urban radiation, sky-view and sunlight-hours
      computation on 3D city models
      IFC to CityGML conversion, scan-to-BIM, point cloud to BIM, BIM-GIS integration, 3D
      utility network mapping

Mathematical morphology and image structure

      Erosion, dilation, opening, closing, hit-or-miss, geodesic reconstruction, granulometry
      Component trees: max-tree, min-tree, alpha-tree, attribute filters, area and shape
      openings
      Thinning and skeletonization (Zhang-Suen), Moore neighbor and Suzuki contour
      tracing, two-pass connected components
      Interactive segmentation: GrabCut, random walker, seeded region growing
      Morphological spatial pattern analysis (MSPA) for habitat structure

Accessibility and public health catchments

      Floating catchment variants: E2SFCA, 3SFCA, M2SFCA, G2SFCA, KD2SFCA
      Travel-time decay functions (Gaussian, power, kernel density), multimodal
      accessibility, spatial mismatch indices
      Disease mapping extensions: Leroux CAR, Knorr-Held space-time interaction models,
      age standardization, Poisson-gamma models
      Cluster tests for case data: Cuzick-Edwards, Whittemore, spatial scan with covariates

Mass movement and volcanic runout

      Rockfall trajectory simulation (CRSP, Rockyfor3D), debris flow runout (RAMMS,
      r.avaflow), energy cone and energy line models



                                                                                         Page 29 of 47

`<PARSED TEXT FOR PAGE: 30 / 47>`

Spatial Analysis Algorithms: Complete Compendium




      Pyroclastic flow and lahar models (TITAN2D, LaharZ), lava flow models (MAGFLOW,
      probabilistic path models)
      Tsunami inundation and runup coupling, coastal landslide hazard

Precision agriculture and forest inventory

      Management zone delineation (fuzzy c-means, MZA), variable-rate prescriptions,
      yield monitor data cleaning, on-farm experiment analysis with spatially varying
      coefficients
      UAV plant counting, weed mapping, row detection, stand emergence and canopy
      cover from imagery
      Forest inventory: area-based approach with LiDAR, individual tree approach, k-NN
      and gradient nearest neighbor imputation, stand delineation, volume and basal area
      models, small-area estimation for inventory

Cartographic mathematics

      Projection families: Robinson, Winkel Tripel, Equal Earth, Natural Earth, Goode
      homolosine, Dymaxion, azimuthal and conic equidistant
      Distortion analysis: Tissot indicatrix computation, areal and angular distortion indices,
      projection selection algorithms
      Contiguous cartograms by rubber sheet and diffusion, tile grid maps via Hungarian
      assignment, Voronoi treemaps, hexagon maps
      Perceptual color: CIELAB and CIECAM interpolation, ColorBrewer rules, viridis-style
      perceptual uniformity, color-blind safe palette generation

Geovisualization and interaction

      Origin-destination maps (Wood and Dykes layout), Sankey flows, space-time cube,
      small multiples, brushing and linking
      Uncertainty visualization: bivariate and value-suppressing palettes, ensemble maps,
      hypothetical outcome plots
      Animation and temporal generalization, data-driven scrollytelling, level-of-detail
      streaming

Linguistic, political and social geography

      Dialect mapping, isogloss detection, spatial lexical variation analysis
      Ecological inference (King's EI, Goodman regression), spatial voting models, partisan
      bias metrics (efficiency gap, mean-median, declination)
      Gerrymandering detection via ensemble simulation, packing and cracking diagnostics




                                                                                        Page 30 of 47
