# Source inventory transcription — pages 36–40

> Faithful text extraction from the supplied *Spatial Analysis Algorithms: Complete Compendium*. Original page boundaries are retained below. This is an intake transcription, not a technical verification or editorial rewrite.

<PARSED TEXT FOR PAGE: 36 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Model-based design: kriging variance minimization, Bayesian optimal design,
      sequential and adaptive designs, mutual information sensor selection (submodular
      greedy)
      Robotic sampling: adaptive sampling with AUVs and drones, informative path planning

3D formats and level-of-detail

      Point cloud storage: LAZ compression, COPC, Entwine EPT, Potree octrees
      City and terrain streaming: OGC 3D Tiles with screen-space-error refinement, I3S,
      quantized-mesh terrain, CityGML levels of detail (LoD0 to LoD3)
      Data models: Simple Features, arc-node topology, TIN model, TopoJSON, GeoSPARQL

Competitive location and matching

      Competitive facility location: Huff-based, Stackelberg and Nash formulations, Voronoi
      games
      Stable matching (Gale-Shapley), auction algorithms, school choice and spatial
      assignment with preferences

EV charging and refueling siting

      Flow-capturing location model (FCLM), flow-refueling location model (FRLM),
      charging demand estimation from trajectories
      Charging coverage with queuing, grid-capacity-aware siting, hydrogen station siting,
      V2G scheduling

Surveillance and anomaly detection

      Syndromic surveillance: CUSUM, EARS, Farrington, spatial and space-time variants
      Event detection from sensor networks, graph-based anomaly detection, spatial scan
      on counts with covariates

Infrastructure and land-use mapping from imagery

      Solar farm and wind turbine detection, hydropower and mine detection, illegal mining
      mapping
      Aquaculture ponds, greenhouses, rice paddies (SAR phenology), oil palm and tree
      crop mapping, shade coffee and agroforestry mapping
      Building age, roof material and building height estimation from imagery and shadows

Implementation map (representative libraries)

      Geometry and indexing: GEOS, JTS, Shapely, S2, H3, libspatialindex
      Projections and IO: PROJ, GDAL, Rasterio, Fiona, GeoPandas, xarray, rioxarray
      Spatial statistics: PySAL, spatial regression packages in R (spdep, spatialreg, mgcv,
      INLA, gstat), scikit-gstat



                                                                                       Page 36 of 47

<PARSED TEXT FOR PAGE: 37 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Networks and routing: OSMnx, NetworkX, igraph, pgRouting, OSRM, Valhalla,
      GraphHopper, OpenTripPlanner, R5, momepy
      Mobility: scikit-mobility, MovingPandas, Traja
      Remote sensing and EO ML: SNAP, Orfeo Toolbox, eo-learn, TorchGeo, Terratorch,
      Raster Vision, Google Earth Engine, openEO
      Terrain and hydrology: WhiteboxTools, GRASS, SAGA, TauDEM, pysheds
      Big data: Apache Sedona, GeoMesa, cuSpatial, Dask-GeoPandas, DuckDB spatial


18. Additions: moving objects, routing, transit, water and ice,
emissions, data-quality statistics
More methods, many from specialized subfields. Names are from memory, so verify
before citing.

Moving-object databases and spatiotemporal indexes

      Spatiotemporal indexes: HR-tree, MV3R-tree, TPR-tree, 3D R-tree, SETI, PIST, STR-
      tree, TB-tree, grid-based trajectory indexes
      Moving-object queries: future location and predictive range queries, dead-reckoning
      update policies, uncertainty regions for moving objects
      Spatiotemporal data models: snapshot, space-time composite, event-based, object-
      oriented; temporal GIS versioning

Routing speedups and richer route choice

      Speedup techniques: transit node routing, highway hierarchies, reach-based routing,
      arc flags, PHAST and RPHAST, customizable route planning, time-dependent
      contraction hierarchies
      Multi-criteria routing: Pareto label-setting (Martins), bi-objective shortest path,
      skyline routes, eco-routing, scenic and safe routing
      Active-travel quality: bicycle level of traffic stress (LTS), BLOS, wheelchair-accessible
      routing, walkability-weighted paths
      Route choice models: path-size logit, C-logit, stochastic user equilibrium, route
      diversity metrics

Public transport planning

      Line planning, network design problems, stop spacing and consolidation, bus stop
      siting via set covering
      Timetable-based and frequency-based accessibility, transfer optimization, headway
      analysis, GTFS-Realtime processing, transit equity analysis

UAV and survey flight planning


                                                                                          Page 37 of 47

<PARSED TEXT FOR PAGE: 38 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Photogrammetric flight design: ground sample distance, forward and side overlap,
      corridor mapping, terrain-following flight
      Coverage path planning with camera footprints, multi-UAV swarm coverage, battery-
      aware routing

Surface water, altimetry and river remote sensing

      Radar altimetry retracking: OCOG, threshold, Brown model; coastal altimetry; SWOT
      KaRIn processing
      River width and slope extraction (RivWidth-style), discharge estimation (BAM,
      MetroMan, rating curves), lake and reservoir level and storage
      Global surface water dynamics: JRC GSW expert-system classification, floodplain
      mapping, water occurrence and seasonality

Snow, ice and permafrost

      Snow: fractional snow cover retrieval (MODSCAG-style), SWE from passive
      microwave, snow depth from LiDAR and SfM, wet snow detection in SAR, snow albedo
      models
      Glaciers: debris-covered glacier mapping, ice thickness inversion (GlabTop, OGGM,
      Huss-Farinotti), outline delineation, GRACE mascon mass change, input-output ice
      sheet mass balance
      Permafrost: Stefan equation, TTOP model, active layer thickness mapping, thaw
      subsidence from InSAR

Vegetation radiative transfer and fluorescence

      3D RTMs (DART), SCOPE, leaf chlorophyll retrieval, hemispherical photo LAI, gap
      fraction models
      Sun-induced fluorescence retrieval (FLD, SFM), photosynthesis models (FvCB),
      canopy structure retrieval from LiDAR

Emission estimation and atmospheric inversion

      XCO2 retrieval and carbon flux inversion (OCO-2 and GOSAT style), methane
      inversion, NOx emission estimation via divergence methods
      TROPOMI oversampling and wind-rotation methods, EMG fitting for point sources,
      plume-based flux quantification
      Wind profile models (log law, power law), Weibull fits, mass-consistent wind models
      (WindNinja), CFD downscaling

Structural geology and directional statistics

      Circular statistics: Rayleigh test, von Mises distribution, Kuiper and Watson tests,
      rose diagram analysis



                                                                                       Page 38 of 47

<PARSED TEXT FOR PAGE: 39 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Spherical statistics: Fisher and Kent distributions, Bingham distribution, stereonet
      analysis
      Structural measurements from point clouds: plane fitting, discontinuity set
      extraction, fracture network analysis, DFN generation, kinematic slope stability
      Geological modeling: cross-section construction, fault network modeling, implicit
      modeling via RBF or potential fields

Data-quality statistics for spatial data

      Missing data: spatial multiple imputation, MICE, kNN imputation, missForest, GP
      imputation
      Spatial misalignment and change of support: downscaler fusion models (Berrocal-
      style), Berkson and classical measurement error, ecological fallacy diagnostics
      Preferential sampling (Diggle-style models), informative sampling, spatial selection
      bias correction
      Compositional data: Aitchison geometry, log-ratio transforms, compositional kriging
      Spatial graphical models: Gaussian graphical models, spatial Bayesian networks,
      causal discovery on spatial data

Spatial humanities

      Georeferencing historical texts, spatial narrative extraction, literary GIS, deep
      mapping, place-based corpus analysis


19. Additions: African applications, addressing, finance, telecom,
seismology, pitfalls
More methods and applied areas. Names and tools are from memory, so verify before
citing.

Applications common in East and Sub-Saharan Africa

      Desert locust and pest monitoring: habitat suitability from soil moisture and
      vegetation, swarm movement forecasting, eLocust-style field data fusion
      Index-based livestock and crop insurance: NDVI and rainfall index design, basis risk
      analysis, pasture condition mapping
      Pastoral mobility analysis: herd movement tracks, seasonal corridor detection, water
      point and grazing access models
      Disease mapping: malaria prevalence geostatistics (MAP-style), cholera and Rift
      Valley fever risk, health facility accessibility (AccessMod-style travel time models)
      Informal transit: paratransit route mapping from GPS (digital matatu style GTFS),
      mobile-money and mobile-network data for mobility and poverty proxies



                                                                                          Page 39 of 47

<PARSED TEXT FOR PAGE: 40 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Water infrastructure: water point functionality prediction (WPDx-style data),
      borehole siting from geophysics and remote sensing
      Drought early warning: VCI, SPI, soil moisture anomalies, food security outlook
      integration

Addressing and location encoding

      Open Location Code (plus codes), geohash, what3words-style grids, S2 and H3 cell
      addresses
      Descriptive and landmark-based geocoding, building-based addressing, address-free
      geocoding for informal settlements
      Address generation from street segments and building footprints, address quality
      scoring

Insurance, finance and risk transfer with geodata

      Parametric insurance design: trigger selection, index construction, basis risk
      quantification, cat bond trigger design
      Credit and risk models with geospatial features, property valuation (AVM with
      comparable selection by kNN and GWR)
      Exposure modeling: flood zone assignment, wind and quake exposure aggregation,
      portfolio accumulation analysis

Telecom and network planning

      RF planning: coverage prediction, propagation model calibration, cell planning,
      handover analysis, interference mapping
      Backhaul and fiber routing: least-cost corridors, ring design, last-mile network design
      Satellite internet coverage: constellation coverage, beam planning, link budget
      analysis

Seismology and earthquake early warning

      Earthquake location: Geiger method, HypoDD double-difference relocation,
      magnitude estimation, focal mechanism inversion
      Detection and phase picking: STA/LTA, template matching, PhaseNet, EQTransformer-
      style pickers
      Tomography and noise methods: ambient noise tomography, receiver functions
      Early warning: ElarmS, PLUM-style algorithms, GNSS-based rapid magnitude
      estimation, tsunami warning inversion
      Volcanic monitoring: deformation, SO2 and thermal monitoring, failure forecast
      method for eruption forecasting

Atmospheric transport and source attribution



                                                                                        Page 40 of 47
