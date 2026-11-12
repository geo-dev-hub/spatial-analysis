# Source inventory transcription — pages 11–15

> Faithful text extraction from the supplied *Spatial Analysis Algorithms: Complete Compendium*. Original page boundaries are retained below. This is an intake transcription, not a technical verification or editorial rewrite.

<PARSED TEXT FOR PAGE: 11 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Activity-based and simulation: MATSim, SUMO, ActivitySim, UrbanSim, car-following
      (IDM, Gipps)
      O-D estimation from counts, GTFS processing, transit accessibility, crash hotspot and
      empirical Bayes screening
      Traffic forecasting: DCRNN, STGCN, Graph WaveNet, ASTGCN, GMAN, PDFormer,
      STID

Human mobility and trajectories

      Trajectory processing: stop and stay-point detection, compression (SQUISH, STTrace,
      opening window, TD-TR), imputation, route recovery
      Similarity and clustering: dynamic time warping, LCSS, Fréchet, TRACLUS, T-DBSCAN,
      trajectory similarity search
      Patterns: flock, convoy, swarm; transport mode detection; activity inference
      Mobility models: exploration and preferential return, Lévy flights, continuous-time
      random walks; metrics (radius of gyration, entropy, predictability)
      Next-location prediction: Markov, DeepMove, LSTPM, GETNext, STAN, Flashback; POI
      recommendation
      Time geography: space-time prisms, potential path areas, activity spaces
      Movement ecology: MCP, KDE, LoCoH, Brownian bridge, step selection, resource
      selection functions
      Mobile phone CDR analysis, footfall estimation, segregation from mobility

Positioning, navigation, robotics

      Haversine, Vincenty and Karney geodesics, great-circle and rhumb lines
      GNSS: RTK, PPP, Kalman and particle filters, dead reckoning, trilateration, Wi-Fi and
      Bluetooth fingerprinting, UWB, Wi-Fi RTT, magnetic fingerprinting, pedestrian dead
      reckoning
      SLAM: EKF-SLAM, FastSLAM, GraphSLAM, ORB-SLAM, LOAM, LIO-SAM; visual
      odometry, loop closure, pose graph optimization
      Planning: RRT and RRT*, PRM, D* Lite, hybrid A*, Dubins and Reeds-Shepp curves,
      potential fields, coverage path planning, navigation meshes, social force crowd
      models
      Maritime and aviation: weather routing (isochrone method), CPA/TCPA collision
      avoidance, AIS trajectory prediction and anomaly analysis, UAV mission planning, 3D
      path planning




                                                                                       Page 11 of 47

<PARSED TEXT FOR PAGE: 12 / 47>

Spatial Analysis Algorithms: Complete Compendium




7. Domain modeling: environment, hazards, ecology, health,
urban, energy, ocean
Applied spatial methods organized by field.

Land change and simulation

      Cellular automata (SLEUTH, ANN-CA, logistic-CA, Markov-CA), CLUE-S, FLUS, PLUS,
      Dinamica EGO, Land Change Modeler
      Agent-based models, Markov chain land-use change, Monte Carlo spatial simulation
      Schelling segregation, Sugarscape, percolation, diffusion-limited aggregation, sandpile
      and forest fire models, spatial game theory
      Spatial random graphs, preferential attachment with distance decay, small-world and
      scale-free networks

Multi-criteria and decision support

      Weighted and Boolean overlay, AHP, fuzzy overlay, TOPSIS, ELECTRE, ordered
      weighted averaging, weights of evidence
      Spatial decision support, participatory GIS, scenario analysis, InVEST ecosystem
      services
      Indices: social vulnerability (SoVI), multi-hazard and compound-risk, environmental
      justice, landscape connectivity (IIC, PC)

Ecology and conservation

      Species distribution: MaxEnt, BIOCLIM, habitat suitability, joint SDMs, occupancy, N-
      mixture, spatial capture-recapture, distance sampling
      Connectivity: Circuitscape, Omniscape, Conefor, least-cost corridors, dispersal
      kernels, metapopulation models
      Landscape metrics (FRAGSTATS): patch density, edge density, contagion; alpha and
      beta diversity; species-area relationships
      Landscape genetics: isolation by distance and resistance, spatial PCA, Geneland,
      TESS, wombling, allele frequency autocorrelation

Agriculture and forestry

      Crop models: DSSAT, APSIM, WOFOST, AquaCrop; yield estimation (SCYM, regression,
      deep learning)
      Crop calendar, phenology extraction (TIMESAT, Savitzky-Golay), field boundary
      delineation, irrigation detection, crop rotation mapping
      Forest disturbance, biomass estimation, allometric equations, species classification
      from hyperspectral and LiDAR
      Growing degree days, drought indices (SPI, SPEI, VCI, PDSI), crop stress detection


                                                                                     Page 12 of 47

<PARSED TEXT FOR PAGE: 13 / 47>

Spatial Analysis Algorithms: Complete Compendium




Weather, climate, air quality

      Weather radar: clutter filtering, attenuation correction, Z-R, hydrometeor
      classification, TITAN, SCIT, TREC, pySTEPS, optical-flow nowcasting
      Rainfall retrieval: IMERG, PERSIANN, CMORPH; radar-gauge merging
      Climate: Köppen, ETCCDI indices, reanalysis (ERA5) processing, bias correction, local
      climate zones, urban heat island
      Air quality: land-use regression, AERMOD, CALPUFF, CMAQ, WRF-Chem, GEOS-
      Chem, AOD-based PM2.5 estimation, low-cost sensor fusion, noise mapping (ISO 9613,
      CNOSSOS)
      Dispersion: Gaussian plume, Lagrangian (HYSPLIT), volcanic ash dispersion

Hazards and risk

      Seismic: probabilistic seismic hazard analysis, ground motion prediction equations,
      ETAS, Coulomb stress, PAGER loss estimation, tsunami propagation
      Fire: Rothermel, FARSITE, elliptical spread, fire risk indices
      Damage and exposure: xBD-style building damage classification, catastrophe loss
      models, exposure aggregation
      Evacuation: contraflow, capacity-constrained routing, crowd simulation, shelter
      location
      Near-repeat analysis, risk terrain modeling, STAC (crime)

Health and epidemiology

      Disease mapping: BYM, standardized ratios, empirical Bayes
      Epidemic models: SIR on networks, reaction-diffusion, metapopulation, gravity-based
      importation, mobility-driven forecasting
      Vector-borne risk: MaxEnt, mechanistic temperature models; contact tracing graphs;
      spatial survival analysis
      Exposure: personal exposure from trajectories, environmental justice analysis

Urban and socioeconomic

      Nighttime lights (VIIRS harmonization), poverty and wealth mapping, urban extent
      (GHSL, WSF), impervious surface mapping, informal settlement detection
      Building height and footprint estimation, footprint regularization, orthogonalization,
      urban morphometrics, walkability
      Land use inference from POIs (topic models, Place2Vec), functional zone discovery
      Urban economics: Alonso-Muth-Mills, von Thünen, Hotelling, central place theory,
      rank-size, location quotient, shift-share, agglomeration, land value capitalization




                                                                                       Page 13 of 47

<PARSED TEXT FOR PAGE: 14 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Urban scaling laws, urban digital twins, CityGML and CityJSON processing, rooftop
      solar potential
      Cadastre: parcel subdivision, COGO, traverse computation, survey network
      adjustment, topological validation

Energy and infrastructure

      Wind: WAsP, Jensen and Park wake models; solar: NREL SPA, Ineichen, Perez, REST2,
      PV yield; hydropower potential
      Least-cost transmission corridors, pipeline routing, electrification planning, minigrid
      sizing, capacity expansion
      Radio propagation: Okumura-Hata, COST-231, ITM/Longley-Rice, ray tracing

Ocean, cryosphere and marine

      Wave models (WAVEWATCH III, SWAN), storm surge (ADCIRC), tidal harmonic
      analysis (T_TIDE, UTide), ocean drift and Lagrangian particle tracking
      Oil spill and ship detection (SAR), AIS anomaly analysis
      Mangrove and coral mapping, glacier and sea ice analysis

Geoscience, mining and planetary

      Seismic tomography, full waveform inversion, migration; gravity and magnetic
      inversion, Euler deconvolution, reduction to pole, upward and downward continuation
      ERT, GPR processing, implicit geological modeling (RBF), 3D geostatistics, stochastic
      reservoir modeling, history matching
      Mining: block models, grade-tonnage, pit optimization (Lerchs-Grossmann,
      pseudoflow), mine scheduling, mineral prospectivity, geochemical anomaly detection
      (U-statistic, concentration-area)
      Planetary: crater detection and counting, photoclinometry, shape from shading,
      mineral mapping, landing site hazard detection
      Archaeology: predictive modeling, site catchment, cumulative visibility, Tobler's hiking
      function, cost surfaces

Cross-disciplinary spatial methods

      Spatial transcriptomics (SpatialDE, cell neighborhood analysis), histopathology point
      patterns, materials grain boundary analysis
      Astronomy: two-point correlation, friends-of-friends, HEALPix cross-matching;
      microscopy particle tracking and Voronoi analysis




                                                                                       Page 14 of 47

<PARSED TEXT FOR PAGE: 15 / 47>

Spatial Analysis Algorithms: Complete Compendium




8. GeoAI and geospatial foundation models (GeoFMs)
The deep learning layer: pretraining, architectures, adaptation, evaluation and
deployment. Model names are representative examples, not an exhaustive or verified
catalog.

Pretraining objectives

      Masked autoencoding: MAE, SatMAE (temporal and spectral grouping), Scale-MAE
      (GSD-aware encoding), SelectiveMAE, S2MAE, SpectralGPT (3D masking)
      Contrastive and self-distillation: SimCLR, MoCo, DINO, DINOv2, DINOv3, iBOT, BYOL,
      Barlow Twins, VICReg, SeCo, SSL4EO, CROMA, JEPA-style latent prediction
      Image-text and image-location alignment: RemoteCLIP, GeoRSCLIP, SkyCLIP, SatCLIP,
      GeoCLIP, CSP
      Multi-sensor and cross-modal masking: Galileo, DOFA, SkySense, Copernicus-FM,
      TerraMind, AnySat, Panopticon
      Embedding fields: AlphaEarth Foundations, Clay, TESSERA; pixel-timeseries models:
      Presto, Galileo, TiMo
      Supervised and multi-task pretraining: SatlasPretrain, MTP, GFM-style continual
      pretraining, distillation
      Weak supervision from land cover maps, OSM and geotagged text; deduplicated and
      stratified global tile sampling

Architectures and encodings

      Backbones: ViT, Swin, hierarchical ViT, ConvNeXt, Mamba and state-space models
      (RS-Mamba, Samba), Perceiver-style encoders, mixture-of-experts
      Prithvi-EO temporal ViT with 3D patch embeddings; U-TAE, L-TAE, PSE-TAE temporal
      attention
      Channel and spectral handling: ChannelViT, hypernetwork-generated weights
      (DOFA), wavelength conditioning (FiLM, cross-attention), spectral-band tokens
      Positional encodings: 2D sin-cos, learned, RoPE, ALiBi, relative; GSD-aware; day-of-
      year and date embeddings
      Decoders and heads: UNet-style, UPerNet, ViTDet feature pyramids, linear and MLP
      probes
      Token handling for large scenes: windowed attention, token merging, token pruning,
      dynamic resolution, register tokens

Adaptation and efficiency

      LoRA, adapters (GeoAdapter), prompt tuning, visual prompt tuning, in-context
      learning, PEFT




                                                                                      Page 15 of 47
