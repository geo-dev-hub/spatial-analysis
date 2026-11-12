# Source inventory transcription — pages 21–25

> Faithful text extraction from the supplied *Spatial Analysis Algorithms: Complete Compendium*. Original page boundaries are retained below. This is an intake transcription, not a technical verification or editorial rewrite.

<PARSED TEXT FOR PAGE: 21 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Spillover and interference models, propensity scores with spatial confounding,
      staggered DiD on spatial panels, double machine learning with spatial structure


10. Additions: classical, statistical and computational methods
Further methods not listed in sections 1 to 9.

Rasterization, curves and low-level geometry

      Line and polygon rasterization: Bresenham, DDA, Wu's anti-aliased line, scanline
      polygon fill, supercover lines
      Line clipping: Cohen-Sutherland, Liang-Barsky, Cyrus-Beck, Nicholl-Lee-Nicholl
      Line simplification variants: Reumann-Witkam, Lang, Opheim, Zhao-Saalfeld,
      Visvalingam-Whyatt with effective area
      Curves and smoothing: Chaikin corner cutting, Catmull-Rom, B-splines, NURBS, Bezier
      fitting (Schneider), Kalman and RTS smoothers
      Geodesics on meshes: MMP exact geodesics, Chen-Han, fast marching on triangle
      meshes
      Spherical and discrete global grids: ISEA3H, rHEALPix, DGGRID, hierarchical
      triangular mesh (HTM), hexagonal grid operations

Time series and change detection

      Change-point detection: CUSUM, PELT, binary segmentation, BEAST, Bayesian online
      change-point detection
      Trend and seasonality: STL, seasonal-trend decomposition, Prophet, Theil-Sen, Pettitt
      test, ARIMA, Kalman filtering of EO series
      Hidden Markov models and Viterbi decoding for state sequences (map matching, land
      cover trajectories)

Forecast verification and nowcasting skill

      Fractions Skill Score, neighborhood verification, SAL (structure, amplitude, location),
      object-based verification (MODE)
      ETS, POD, FAR, CSI, Brier skill score, ROC and AUC, CRPS decomposition, rank
      histograms
      Optical flow for advection: Lucas-Kanade, Farneback, DIS, variational optical flow

Spatial cross-validation and sampling

      NNDM, kNNDM, buffered leave-one-out, spatial k-fold by clustering, blockCV,
      spatial+temporal leave-out




                                                                                       Page 21 of 47

<PARSED TEXT FOR PAGE: 22 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Adaptive and Bayesian sampling: Bayesian optimization on spatial fields, multi-armed
      bandits for survey design, adaptive cluster sampling, active learning for map
      validation
      Kernel two-sample tests and domain divergence metrics for spatial distribution shift

Geophysical gridding and potential field processing

      Minimum curvature gridding, nearest-neighbor and triangulation gridding, kriging
      versus minimum curvature comparison
      Potential fields: analytic signal, tilt derivative, Euler and Werner deconvolution,
      matched filtering, continuation, vertical and horizontal derivatives
      Airborne EM and magnetotelluric inversion, seismic attribute analysis, receiver
      functions

Urban microclimate and energy

      Radiation and thermal comfort: SOLWEIG, UMEP, ENVI-met, mean radiant
      temperature, UTCI, PET
      Urban wind and CFD: RANS, LES, lattice Boltzmann for street canyons, pedestrian
      wind comfort
      Stormwater and drainage: SWMM, 1D-2D coupled urban flood models, low-impact
      development siting
      Urban building energy modeling: archetype-based simulation, CityBES, shading and
      view-factor computation

Environmental monitoring and MRV

      Deforestation alerts: GLAD, RADD, forest loss detection from SAR and optical fusion
      Carbon accounting: forest carbon stock mapping, REDD+ MRV, soil carbon mapping,
      additionality and leakage analysis
      Methane and gas emissions: matched-filter plume detection, deep plume
      segmentation, integrated mass enhancement (IME), cross-sectional flux, Gaussian
      plume inversion
      Illegal fishing and maritime domain awareness: vessel behavior classification, gap
      detection in AIS, fishing effort mapping from SAR and AIS
      Water quality and harmful algal bloom detection: chlorophyll, turbidity, cyanobacteria
      indices

Population and social data

      Gridded population: top-down dasymetric, bottom-up microcensus, building-based
      disaggregation, settlement-level estimation




                                                                                            Page 22 of 47

<PARSED TEXT FOR PAGE: 23 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Synthetic data for privacy: synthetic microdata, spatial k-anonymity for census,
      differential privacy for aggregates
      Segregation and diversity: Reardon-Firebaugh multigroup indices, spatial exposure
      indices, Shannon and Simpson diversity


11. Additions: GeoAI, GeoFMs and computer vision
Extra GeoFM families, tasks and datasets. Names are representative and not verified
against current releases.

More GeoFM families and pretraining recipes

      Optical and multispectral: Prithvi-EO-2.0, SatMAE++, RingMo, RVSA, SatViT, USat,
      SMARTIES, DeCUR, FoMo, THOR, RoMA, SkySense++
      Multimodal and multi-sensor: OmniSat, MMEarth (pretext tasks from auxiliary
      geographic data), SSL4EO-S12, DOFA-CLIP, Hydra-style multi-head pretraining
      Time-series and temporal: EarthPT, TESSERA, Presto, SITS-Former, pixel-wise
      transformers for satellite image time series
      Mamba and linear-attention variants for hyperspectral and large-scene encoders
      (HyperSIGMA, Samba)
      Pretraining datasets: SSL4EO-S12, MMEarth, Satlas, fMoW, BigEarthNet, SEN12MS,
      Major TOM, GeoPile

Detection, tracking and counting

      Oriented detection: Gliding Vertex, S2A-Net, R3Det, LSKNet, Oriented RepPoints,
      ReDet
      Small-object detection and slicing: SAHI, tile-based inference, multi-scale feature
      fusion
      Video and tracking: SORT, DeepSORT, ByteTrack, satellite video object tracking,
      vehicle counting, crowd density estimation
      Instance, panoptic and keypoint tasks: Mask R-CNN, Mask2Former, panoptic FPN,
      building roof keypoints, centerline and road graph extraction

Vision-language and multimodal additions

      Remote sensing VLMs: SkySenseGPT, GeoPixel, GeoGround, EarthMind, GeoLLaVA-
      style models; image-text corpora such as RS5M
      Pixel-level grounding, change captioning, multi-temporal VQA, visual question
      answering over multispectral and SAR inputs
      Multimodal LLM agents that call segmentation and detection models as tools

Neural combinatorial optimization and RL for spatial problems



                                                                                      Page 23 of 47

<PARSED TEXT FOR PAGE: 24 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Attention models and POMO for TSP and VRP, GNN-based heuristics, learned
      neighborhood search
      Reinforcement learning for traffic signal control (max pressure baselines, DQN, PPO),
      ride-hailing dispatch, spatial crowdsourcing assignment, ambulance relocation
      Learned routing and ETA models: GNN-based travel time, transformer-based route
      recommendation

Generative and probabilistic models for Earth observation

      Diffusion for cloud removal, super-resolution, gap filling, and controllable synthetic
      scene generation
      Flow matching and consistency models for fast generation; latent diffusion in learned
      EO tokenizers
      Probabilistic forecasting heads: mixture density networks, normalizing flows, quantile
      regression networks

Benchmarks and datasets (representative)

      Segmentation and land cover: LoveDA, iSAID, Open-Earth-Map, SpaceNet, FLAIR,
      Sen1Floods11, HLS Burn Scars, So2Sat LCZ42, DynamicEarthNet
      Detection: DOTA, DIOR, xView, FAIR1M
      Multi-task GeoFM evaluation: PANGAEA, GEO-Bench, Copernicus-Bench
      Weather and climate: WeatherBench 2, SEVIR, ClimateBench, ERA5-based training
      sets

Operational GeoAI engineering

      Data curation: tile deduplication, label noise audits, class-balanced geographic
      sampling, region-stratified splits
      MLOps for imagery: dataset versioning, STAC-driven training pipelines, monitoring for
      temporal drift and sensor change
      Human-in-the-loop mapping: active learning loops, interactive segmentation with
      SAM, quality scoring and review queues
      Evaluation under distribution shift: cross-continent splits, seasonal shift tests,
      sensor-swap tests, calibration drift checks


12. Additions: signal processing, GNSS, regional science,
resilience
More methods from adjacent fields that spatial analysts regularly borrow.

Smoothing and semiparametric spatial models




                                                                                           Page 24 of 47

<PARSED TEXT FOR PAGE: 25 / 47>

Spatial Analysis Algorithms: Complete Compendium




      GAM and GAMM with spatial smooths (thin plate, Duchon splines, soap film
      smoothers), Bayesian P-splines
      Penalized spatial regression: geographically weighted LASSO, spatial LASSO, fused
      LASSO on graphs, spatially varying coefficients with regularization
      Intensity estimation: Voronoi and Delaunay-based estimators, STKDE (space-time
      KDE), prospective hotspot mapping
      Palm distributions, nearest neighbor distance distributions, inhomogeneous K and
      pair correlation functions

Matrix and tensor methods for spatial data

      NMF, ICA, MAF (maximum autocorrelation factors), dictionary learning, sparse
      coding, compressive sensing
      Tensor decomposition: CP, Tucker, tensor train; low-rank spatiotemporal completion
      Kalman variants: EKF, UKF, ensemble square-root filters, RTS smoothing, particle
      smoothing

GNSS and geodetic adjustment (more)

      Ambiguity resolution (LAMBDA), cycle slip detection, ionosphere-free and geometry-
      free combinations, PPP-AR
      Multipath mitigation, RAIM and fault detection, Baarda data snooping, least squares
      collocation
      Time transfer, clock modeling, kinematic positioning with INS integration (loosely and
      tightly coupled)

Sensor calibration and image quality

      Vicarious and cross-sensor radiometric calibration, MTF estimation, GIQE and NIIRS
      image quality scoring
      Perceptual hashing and content-based image retrieval for EO archives, near-duplicate
      tile detection
      Lossy and learned compression for imagery (neural codecs), rate-distortion
      evaluation for downstream tasks

SAR and polarimetric deep learning

      Deep despeckling, SAR ship detection, SAR target recognition (ATR), polarimetric
      feature learning
      Cross-modal SAR-optical matching, SAR image registration, interferogram denoising
      networks

Quantitative spatial economics and regional science




                                                                                     Page 25 of 47
