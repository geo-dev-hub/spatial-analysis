# Source inventory transcription — pages 16–20

> Faithful text extraction from the supplied *Spatial Analysis Algorithms: Complete Compendium*. Original page boundaries are retained below. This is an intake transcription, not a technical verification or editorial rewrite.

<PARSED TEXT FOR PAGE: 16 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Few-shot and zero-shot, meta-learning (prototypical networks, MAML), open-set
      recognition, model merging, task arithmetic, continual learning
      Compression: pruning, quantization-aware training, distillation to small students, on-
      board satellite inference, edge and UAV deployment
      Training systems: mixed precision, gradient checkpointing, FSDP, DeepSpeed, flash
      attention, AdamW, LARS, layer-wise learning-rate decay, EMA teachers
      Tooling: TorchGeo, Terratorch, tiled and sliding-window inference with Gaussian
      blending, vector databases and embedding caches

Downstream tasks

      Segmentation: UNet, DeepLab, Mask2Former, UPerNet, SAM and SAM 2 adaptations
      (RSPrompter, SAMGeo)
      Detection: Oriented R-CNN, RoI Transformer, ReDet, DETR variants, YOLO
      Change detection: Siamese networks, ChangeFormer, BIT, SNUNet
      Mapping tasks: cloud masking, flood and burn-scar mapping, crop type mapping,
      canopy height regression, building and road extraction (D-LinkNet, HRNet,
      RoadTracer), vectorization (PolyWorld, HiSup), field boundaries, monocular height and
      depth
      Super-resolution and generative: SRGAN, diffusion, DiffusionSat, CycleGAN, Pix2Pix,
      VAEs, VQGAN, cloud removal, sensor translation, synthetic data generation
      Open-vocabulary and referring segmentation (SegEarth-OV)
      HD map construction and BEV perception: MapTR, VectorMapNet, BEVFormer
      Visual place recognition and geolocalization: NetVLAD, MixVPR, CosPlace, SALAD,
      PlaNet, StreetCLIP, G3, cross-view matching

Vision-language and agentic GeoAI

      Remote sensing VLMs: GeoChat, EarthGPT, LHRS-Bot, SkyEyeGPT, RSGPT, VHM,
      TEOChat, EarthDial; RemoteSAM, GeoSAM
      Captioning, VQA, visual grounding, reasoning benchmarks, chain-of-thought VLMs,
      reinforcement learning (GRPO-style) for geo-VLMs
      LLM agents: text-to-SQL and text-to-GIS (LLM-Geo, GeoAgent, GeoGPT), PyQGIS
      and GeoPandas code generation, tool-calling, MCP-based agents, GeoRAG, dense
      retrieval over layers and metadata
      Geographic knowledge probing (GeoLLM), LLM geolocation, geocoding with language
      models, toponym resolution, spatial reasoning and mental map prompting, vision-
      language navigation

Location encoders and representation learning




                                                                                      Page 16 of 47

<PARSED TEXT FOR PAGE: 17 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Space2Vec, Sphere2Vec, Theory, Grid, wrap and RBF encoders; spherical harmonics
      and Spherical Fourier Features; SINR for species ranges
      Multi-scale sinusoidal and random Fourier features, hyperbolic (Poincaré)
      embeddings
      Tile2Vec, Place2Vec, Urban2Vec, Geo2Vec, H3 and geohash token embeddings
      Graph embeddings: Node2Vec, DeepWalk, LINE, TransE and RotatE on geographic
      knowledge graphs

Spatiotemporal and Earth-system deep learning

      Graph models: GCN, GAT, GraphSAGE, TGN, spatiotemporal GCNs, GNN-based
      kriging (KCN, IGNNK, SATCN)
      Sequence and field models: ConvLSTM, PredRNN, SimVP, Earthformer, neural ODEs,
      neural fields, implicit neural representations, neural point processes (Neural Hawkes)
      Weather and climate: FourCastNet, Pangu-Weather, GraphCast, GenCast, FuXi,
      FengWu, Aurora, ClimaX, Prithvi WxC, NeuralGCM, NowcastNet, DGMR, MetNet
      Neural operators and physics-informed: FNO, DeepONet, PINNs; diffusion and flow-
      matching downscaling (CorrDiff); world models and Earth-system emulators
      3D and equivariant: spherical CNNs, DeepSphere, icosahedral and HEALPix
      convolutions, equivariant message passing, 3D Gaussian splatting

Spatial ML and hybrid statistics

      Geographically weighted random forest, RFsp, spatial stacking, kriging plus ML
      residuals, spatial KNN, GNNWR, GWNN, deep kriging, deep GP, neural Gaussian
      processes, Spatial Lag Neural Networks, TabPFN on spatial features
      Spatial feature engineering: buffer statistics, distance to features, lag features
      Weak-label methods: positive-unlabeled learning, one-class SVM, noisy-label learning,
      semi-supervised (FixMatch), active learning
      Physics-guided hybrids: LSTM plus process models in hydrology and crop modeling

Losses, augmentation, evaluation

      Losses: Dice, Tversky, focal, Lovász-softmax, class-balanced cross-entropy, boundary
      and distance-transform loss, clDice, Huber, quantile and pinball
      Augmentation: rotation, flip, scale jitter, CutMix, mosaic, copy-paste, spectral jitter,
      band dropout, cloud and shadow simulation, test-time augmentation
      Metrics: OA, F1, IoU and mIoU, Dice, kappa, mAP with rotated IoU, boundary F-score,
      panoptic quality, RMSE, MAE, R², NSE, KGE, CRPS, ECE
      Embedding quality: linear probing, k-NN, retrieval recall@k, clustering NMI
      Benchmarks: GEO-Bench, PANGAEA, Satlas, fMoW, BigEarthNet, EuroSAT




                                                                                           Page 17 of 47

<PARSED TEXT FOR PAGE: 18 / 47>

Spatial Analysis Algorithms: Complete Compendium




Spatial validity, uncertainty and interpretability

      Spatial block cross-validation, leave-location-out, autocorrelation-aware sampling and
      loss
      Domain adaptation (DANN, CORAL), test-time adaptation, covariate shift correction,
      importance weighting, out-of-distribution detection, area of applicability
      Uncertainty: MC dropout, deep ensembles, conformal prediction, evidential deep
      learning, Bayesian neural networks, SWAG, Laplace approximation, temperature
      scaling
      Explainability: SHAP, GeoShapley, LIME, Grad-CAM, integrated gradients, attention
      rollout, TCAV, probing, spatial partial dependence, ALE, counterfactuals
      Fairness: geographic generalization gaps, spatial fairness metrics, coverage audits for
      training data, label scarcity in the Global South
      Federated and privacy-preserving training; scaling laws for Earth observation models


9. Geodesy, cartography, data infrastructure, privacy, text and
semantics
The supporting layer: coordinate math, map making, data handling, and language-based
geography.

Geodesy and coordinate systems

      Projections: Transverse Mercator (Gauss-Krüger), UTM, Lambert conformal, Web
      Mercator, Tobler hyperelliptical, adaptive composite projections
      Datum transformations: Helmert, Molodensky, Bursa-Wolf 7-parameter, NTv2 grids;
      ECEF, ENU and geodetic conversions; antimeridian and pole handling
      Geoid and gravity: EGM2008 evaluation, Stokes integral, spherical harmonic analysis,
      gravity anomaly and terrain correction, IGRF and WMM magnetic models
      Spherical geometry: spherical polygon area, spherical Voronoi and Delaunay, spherical
      wavelets, icosahedral and cubed-sphere grids
      Space geodesy: SLR, DORIS, VLBI, GNSS time series, velocity fields, strain rate, TEC
      maps, tropospheric delay (Saastamoinen, VMF), precise orbit determination, GRACE
      gravity recovery, altimetry crossover adjustment
      Satellite orbits: SGP4/SDP4, TLE processing, ground tracks and swaths, revisit
      analysis, sun-synchronous design, Walker constellations, conjunction analysis
      Astronomical: solar position, sunrise and sunset, tidal prediction, least-squares
      network adjustment

Georeferencing and transformation




                                                                                       Page 18 of 47

<PARSED TEXT FOR PAGE: 19 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Affine, polynomial and rubber-sheeting transforms; thin plate spline rectification; co-
      registration
      Historical map digitization: control point selection, line-following vectorization, map
      text spotting, symbol segmentation, legend parsing, color quantization
      Conflation: road and building matching, shape-based matching (turning function,
      Fourier descriptors, Procrustes, shape context), OSM quality and vandalism
      detection, completeness estimation

Geocoding and record linkage

      Geocoding, reverse geocoding, rooftop and parcel geocoding, address interpolation,
      address parsing (libpostal-style CRFs, transformers)
      String similarity: Levenshtein, Jaro-Winkler, n-gram, Soundex, Metaphone; Fellegi-
      Sunter, blocking, canopy clustering
      POI deduplication, gazetteer fusion, entity resolution at scale, embedding-based
      place matching

Cartography and geovisualization

      Classification: Jenks natural breaks, quantiles, equal interval, bivariate choropleth,
      perceptual color scales
      Generalization: smoothing (Bezier, Gaussian, PAEK), aggregation, displacement,
      exaggeration, building generalization
      Labeling: label placement optimization, collision-free layouts, glyph placement
      Special maps: dot density, cartograms (Dorling, Gastner-Newman), flow maps with
      edge bundling (FDEB), hexbin maps, schematic and metro layout
      Rendering: isosurfaces, streamlines and LIC, ray marching, hillshade variants, vector
      tile styling, tile pyramids, level-of-detail, WebGL and WebGPU pipelines

Data infrastructure and computing

      Formats and catalogs: COG, Zarr, GeoParquet, FlatGeobuf, STAC, Mapbox Vector Tile,
      TopoJSON, WKB and WKT, Google polyline, Draco, spatial deduplication
      Distributed and GPU computing: Sedona, GeoMesa, Dask, Spark, cuSpatial, GPU
      raster algebra, parallel viewshed and flow accumulation, out-of-core and streaming
      raster algorithms
      Pipelines: openEO, xarray, Rasterio, Snakemake, Airflow; process graphs, lineage
      tracking, data versioning
      Numerical methods: finite difference, finite volume, finite element, spectral, semi-
      Lagrangian, multigrid, conjugate gradient, FFT solvers, lattice Boltzmann, level set
      Collision detection: sweep and prune, BVH, spatial hash grids




                                                                                        Page 19 of 47

<PARSED TEXT FOR PAGE: 20 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Procedural terrain: Perlin and simplex noise, fractional Brownian motion, diamond-
      square, Poisson disk sampling, wave function collapse, L-systems, synthetic city
      generation

Quality assurance and validation

      Topology checks, DE-9IM validation rules, temporal consistency checks, automated
      QA/QC, outlier rules
      Benchmark design and geographic bias audits for GeoAI

Location privacy

      Geomasking (random perturbation, donut masking), spatial k-anonymity and cloaking,
      geo-indistinguishability, differential privacy for location data
      Synthetic population and trajectory generation, federated learning on spatial data

Text, social and semantic geography

      Geoparsing, place NER, toponym resolution, spatial relation extraction, qualitative
      spatial reasoning (RCC-8, Allen intervals, cone-based directions), natural-language
      route instructions
      Geographic information retrieval: spatial keyword search, query understanding, map
      search ranking, geographic topic models
      Social sensing: tweet and post geolocation, burst and event detection, VGI validation,
      tourist trajectory mining from photo sharing sites
      Knowledge graphs: GeoSPARQL, spatial RDF, ontology alignment, entity linking,
      GeoQA, ontology-driven reasoning (SWRL)

Indoor, sports and retail analytics

      Indoor: IndoorGML, indoor routing, floor plan reconstruction, indoor SLAM
      Sports: Voronoi pitch control, expected threat, passing networks, player tracking
      Retail: customer flow, indoor heatmaps, dwell-time analysis

Topological, graph and geometric data analysis

      Persistent homology, Mapper, Reeb graphs, Morse-Smale complexes
      Optimal transport (Wasserstein, Sinkhorn, Gromov-Wasserstein), manifold learning
      (t-SNE, UMAP, Isomap)
      Graph signal processing, spectral clustering, graph kernels, random walk with restart,
      HITS, heat kernel diffusion, graph Laplacian smoothing, motif mining

Spatial causal inference

      Spatial difference-in-differences, synthetic control, geographic regression
      discontinuity, spatial instrumental variables



                                                                                     Page 20 of 47
