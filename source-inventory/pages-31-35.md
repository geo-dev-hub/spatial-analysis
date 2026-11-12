# Source inventory transcription — pages 31–35

> Faithful text extraction from the supplied *Spatial Analysis Algorithms: Complete Compendium*. Original page boundaries are retained below. This is an intake transcription, not a technical verification or editorial rewrite.

<PARSED TEXT FOR PAGE: 31 / 47>

Spatial Analysis Algorithms: Complete Compendium




15. Additions: vision backbones, registration, vector extraction,
hydrology ML
Model and method names are representative and from memory, so verify before citing.

Vision backbones, promptable and open-vocabulary tools

      Backbones: SegFormer, HRNet, Mask DINO, Video Swin, TimeSformer, ViViT,
      VideoMAE for satellite image time series, Perceiver IO, MLP-Mixer, ConvMixer
      Promptable segmentation: SAM variants (SAM-HQ, MobileSAM, EfficientSAM),
      Grounded-SAM, CLIPSeg
      Open-vocabulary detection and grounding: Grounding DINO, OWL-ViT, Florence-2,
      remote sensing adaptations (LAE-DINO, OpenRSD)
      Monocular depth and height estimation: Depth Anything-style models adapted to
      overhead imagery

Hyperspectral deep learning

      Classification: 3D-CNN, HybridSN, SSRN, SpectralFormer, spectral-spatial
      transformers, graph convolution on superpixels
      Unmixing autoencoders: EndNet, DAEN, uDAS-style models; physically constrained
      unmixing networks
      Denoising and super-resolution: low-rank and tensor-based denoising, HSI-DeNet,
      hyperspectral-multispectral fusion networks
      Complex-valued CNNs for polarimetric SAR, PolSAR classification networks

Point cloud deep learning, registration and building reconstruction

      Self-supervised and large backbones: Point-BERT, Point-MAE, PointMLP, PointNeXt,
      SPVCNN, Cylinder3D, Point Transformer V3, Sonata
      Aerial LiDAR segmentation benchmarks: DALES, SensatUrban, Toronto-3D
      Registration: point-to-plane ICP, generalized ICP, NDT, colored ICP, FPFH with
      RANSAC, TEASER++, deep registration (DCP, PointNetLK, GeoTransformer)
      Building reconstruction: PolyFit, City3D, 2.5D dual contouring, roof plane
      segmentation (RANSAC, region growing), LoD2 generation, implicit surfaces
      (DeepSDF, occupancy networks)

Image matching and multimodal registration

      Classical features: SIFT, ORB, AKAZE; phase correlation, ECC, mutual information
      registration
      Learned matching: SuperPoint with SuperGlue or LightGlue, LoFTR, DKM, RoMa,
      multimodal matchers (MINIMA)
      Optical-SAR matching: RIFT, HOPC, CFOG, OS-SIFT, deep cross-modal descriptors


                                                                                       Page 31 of 47

<PARSED TEXT FOR PAGE: 32 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Dense optical flow and sub-pixel displacement: COSI-Corr-style correlation, deep
      flow for glacier and landslide motion

Road, building and polygon extraction

      Road graph extraction: Sat2Graph, RNGDet, iCurb, RoadTracer, lane graph inference
      Polygon and frame-field methods: PolyRNN, Pix2Poly, frame field learning, HiSup,
      P2PFormer
      Evaluation: APLS, TOPO, junction F1, boundary IoU, polygon similarity and vertex-
      based metrics
      Map inference from GPS traces: kernel density methods, trace merging, clustering-
      based, incremental, deep map generation (DeepMG, kharita)

Bayesian spatial clustering and partition models

      Potts-model priors, Voronoi tessellation priors, product partition models, spatial
      Dirichlet process mixtures
      Bayesian cluster detection (BaySTDetect), spatially varying finite mixtures,
      reversible-jump MCMC for change in partition
      Bayesian spatial change-point models and boundary detection

Hydrology machine learning

      Streamflow LSTMs, CAMELS-based training, regional models for ungauged basins,
      transformer and graph-based flood forecasting
      Differentiable hydrology: HBV-style differentiable models, differentiable parameter
      learning, neural ODEs for catchments
      Operational flood forecasting pipelines, hybrid process-ML models, data assimilation
      with learned correctors
      Ocean surrogates and ocean forecasting models, learned wave and surge emulators

Image geolocation

      Cell classification over S2 or H3 cells with hierarchical heads, contrastive image-
      location training, retrieval plus refinement (PIGEON, G3, StreetCLIP)
      Evaluation with distance-threshold accuracy, geographic bias audits, adversarial
      robustness and privacy risk analysis

Onboard and edge intelligence

      Onboard cloud screening (CloudScout-style), low-power CNN accelerators for
      satellites, event-triggered downlink
      Model update strategies for in-orbit inference, quantized models for UAV payloads

Renewable energy forecasting



                                                                                       Page 32 of 47

<PARSED TEXT FOR PAGE: 33 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Solar nowcasting from satellite imagery and sky cameras, irradiance forecasting, PV
      power estimation
      Wind power forecasting with graph neural networks, spatiotemporal ensembles,
      probabilistic forecasting for grid operations


16. Additions: flows, regions, deformation, marine, biodiversity,
humanitarian
More applied methods across fields not yet covered in depth.

Spatial interaction models (advanced)

      Entropy-maximizing models (Wilson), production, attraction and doubly constrained
      forms, Poisson and negative binomial gravity models
      Competing destinations, intervening opportunities variants, spatial autocorrelation in
      flows (Griffith eigenvector filtering, LeSage-Pace origin-destination models)
      Flow clustering and flow mapping: flow-based community detection, flow KDE, OD
      flow hotspot detection

Functional regions and urban boundaries

      Functional region delineation from flows: Intramax, CURDS, Louvain and Leiden on
      flow networks, commuting zone definition
      Urban boundary delineation: city clustering algorithm (CCA), DBSCAN on building
      density, percolation-based clustering, natural cities via head/tail breaks
      Home and work location inference from traces, activity space delineation, co-location
      and contact pattern extraction

Classification schemes and aggregation

      Head/tail breaks, maximum breaks, geometric interval, standard deviation, box plot,
      pretty breaks, Dalenius-Hodges, optimal 1D k-means (ckmeans)
      Zone design and aggregation: AMOEBA, automated zoning procedures, scale-effect
      analysis, variance by aggregation level

Cost surfaces and movement through terrain

      Anisotropic cost surfaces (Tobler hiking function, Naismith, Langmuir), path distance
      with vertical factors, backlink rasters
      Least-cost corridors, cost-weighted distance with turning penalties, energy-
      expenditure models for walking and loaded travel

SAR geometry, InSAR time series and crustal deformation




                                                                                      Page 33 of 47

<PARSED TEXT FOR PAGE: 34 / 47>

Spatial Analysis Algorithms: Complete Compendium




      SAR geometry: radiometric terrain correction (RTC), geocoding, multilooking,
      calibration, enhanced spectral diversity (ESD) coregistration
      Phase corrections: atmospheric phase screen estimation, GACOS and ERA5-based
      tropospheric correction, orbital ramp removal, DEM error correction
      Time-series InSAR workflows: SBAS variants, NSBAS, MintPy-style and LiCSBAS-style
      pipelines, GNSS-InSAR integration for 3D velocity decomposition
      Source modeling: Okada dislocation, Mogi source, finite fault slip inversion, elastic and
      viscoelastic deformation models

Marine and fisheries spatial analysis

      CPUE standardization (GAM and spatiotemporal models such as VAST-style vector
      autoregressive models), spatial stock assessment, fishing effort allocation
      Larval dispersal and ocean connectivity: Lagrangian tools (Parcels, OpenDrift),
      connectivity matrices, marine protected area network design
      Marine spatial planning with Marxan and Zonation, benthic habitat mapping from
      multibeam backscatter

Biodiversity assessment and conservation planning

      IUCN range metrics: extent of occurrence (convex hull, alpha hull), area of occupancy,
      range fragmentation indices
      Essential biodiversity variables, protected area gap analysis, key biodiversity area
      delineation, species richness and endemism indices (weighted endemism,
      phylogenetic diversity)
      Wildlife crime and anti-poaching: green security games, learned patrol planning, risk
      maps from patrol data

Climate analogs, velocity and refugia

      Climate analogs and novel climates (Mahalanobis distance based), climate velocity,
      climate-change refugia, bioclimatic envelope shifts
      Land degradation analysis: RESTREND, NPP residual methods, desertification
      indicators, soil salinity mapping

Humanitarian, food security and conflict

      Relief facility location, humanitarian logistics routing, displacement camp mapping,
      tent and structure counting from imagery
      Food security: IPC-style analysis, FEWS NET-style outlooks, livelihood zone
      delineation, market integration and price transmission models
      Conflict analysis: ACLED-style event analysis, conflict diffusion models, forecasting
      systems such as ViEWS, spatial event clustering and early warning indicators




                                                                                        Page 34 of 47

<PARSED TEXT FOR PAGE: 35 / 47>

Spatial Analysis Algorithms: Complete Compendium




17. Additions: geometry II, scalable computation, design, siting,
implementations
More algorithm families, plus a short map of where common ones are implemented.

Computational geometry II

      Voronoi variants: weighted (additively and multiplicatively weighted, Apollonius),
      order-k, farthest-point, line-segment Voronoi
      Triangulation variants: regular triangulation, alpha complexes, 3D Delaunay
      refinement and tetrahedralization (TetGen-style)
      Polygon decomposition: Seidel and Chazelle triangulation, monotone partition, Hertel-
      Mehlhorn, optimal convex partition
      Boolean operations: Martinez-Rueda polygon clipping, 3D mesh Booleans; watchman
      route problem
      Approximate geometry: geometric hashing, BBD-trees for approximate nearest
      neighbor, coresets for k-means
      Mesh processing: Laplacian and Taubin smoothing, remeshing, mesh repair, ball
      pivoting, half-edge, winged-edge and quad-edge data structures

Scalable computation for spatial statistics

      Log-determinant approximation: Chebyshev, Monte Carlo trace estimators, Lanczos,
      Pace-Barry, sparse Cholesky
      Gaussian Markov random field sampling, conjugate gradient solvers, Kronecker-
      structured covariances, circulant embedding with FFT on regular grids
      Sparse GP methods: inducing points, SVGP, Nystrom, structured kernel interpolation
      (KISS-GP), random Fourier features, hierarchical matrices, fast multipole
      Variogram estimation: Matheron, Cressie-Hawkins and Genton robust estimators,
      REML, composite likelihood, cross-validation-based fitting

Fast density and sketching

      Fast KDE: binned KDE with FFT, dual-tree KDE, random Fourier feature KDE,
      quantized and grid-based DBSCAN
      Streaming sketches for grids and tiles: HyperLogLog for distinct counts, count-min
      sketch, Bloom filters for tile existence, reservoir sampling for spatial streams

Optimal sampling and experimental design

      Space-filling designs: maximin, coffee-house, spatial coverage design (k-means
      based), Latin hypercube




                                                                                         Page 35 of 47
