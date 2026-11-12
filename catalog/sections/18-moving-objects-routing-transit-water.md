# Section 18 — Additions: moving objects, routing, transit, water and ice, emissions, data-quality statistics

- **Original source section:** 18
- **Source pages:** 37–39
- **Source transcription:** [pages 36–40](../../source-inventory/pages-36-40.md)
- **Review state:** intake extracted; names are explicitly described by the source as coming from memory and requiring verification
- **Current canonical records:** none yet

**Source caution:** the source says many methods are from specialised subfields and names are from memory. Treat all named methods, systems and products as leads until checked.

## Moving-object databases and spatiotemporal indexes

| Source entry | Kind to review | Source page |
|---|---|---:|
| Spatiotemporal indexes: HR-tree, MV3R-tree, TPR-tree, 3D R-tree, SETI, PIST, STR-tree, TB-tree, grid-based trajectory indexes | Spatiotemporal index structures | 37 |
| Moving-object queries: future location and predictive range queries, dead-reckoning update policies, uncertainty regions for moving objects | Moving-object query types / update and uncertainty models | 37 |
| Spatiotemporal data models: snapshot, space-time composite, event-based, object-oriented; temporal GIS versioning | Spatiotemporal data models / versioning approaches | 37 |

## Routing speedups and richer route choice

| Source entry | Kind to review | Source page |
|---|---|---:|
| Speedup techniques: transit node routing, highway hierarchies, reach-based routing, arc flags, PHAST and RPHAST, customizable route planning, time-dependent contraction hierarchies | Shortest-path preprocessing and acceleration methods | 37 |
| Multi-criteria routing: Pareto label-setting (Martins), bi-objective shortest path, skyline routes, eco-routing, scenic and safe routing | Multi-objective routing algorithms / route criteria | 37 |
| Active-travel quality: bicycle level of traffic stress (LTS), BLOS, wheelchair-accessible routing, walkability-weighted paths | Active mobility metrics / accessibility-aware routing | 37 |
| Route choice models: path-size logit, C-logit, stochastic user equilibrium, route diversity metrics | Route choice and equilibrium models / diversity measures | 37 |

## Public transport planning

| Source entry | Kind to review | Source page |
|---|---|---:|
| Line planning, network design problems, stop spacing and consolidation, bus stop siting via set covering | Transit network design / optimisation | 37 |
| Timetable-based and frequency-based accessibility, transfer optimization, headway analysis, GTFS-Realtime processing, transit equity analysis | Transit accessibility / timetable and frequency methods / real-time data workflows | 37 |

## UAV and survey flight planning

| Source entry | Kind to review | Source page |
|---|---|---:|
| Photogrammetric flight design: ground sample distance, forward and side overlap, corridor mapping, terrain-following flight | Survey mission design / photogrammetric planning | 38 |
| Coverage path planning with camera footprints, multi-UAV swarm coverage, battery-aware routing | Coverage path planning / multi-agent routing and scheduling | 38 |

## Surface water, altimetry and river remote sensing

| Source entry | Kind to review | Source page |
|---|---|---:|
| Radar altimetry retracking: OCOG, threshold, Brown model; coastal altimetry; SWOT KaRIn processing | Altimetry retracking and sensor-processing methods | 38 |
| River width and slope extraction (RivWidth-style), discharge estimation (BAM, MetroMan, rating curves), lake and reservoir level and storage | River geometry extraction / discharge and storage estimation | 38 |
| Global surface water dynamics: JRC GSW expert-system classification, floodplain mapping, water occurrence and seasonality | Surface-water mapping and temporal analysis workflows | 38 |

## Snow, ice and permafrost

| Source entry | Kind to review | Source page |
|---|---|---:|
| Snow: fractional snow cover retrieval (MODSCAG-style), SWE from passive microwave, snow depth from LiDAR and SfM, wet snow detection in SAR, snow albedo models | Snow retrieval and modelling methods | 38 |
| Glaciers: debris-covered glacier mapping, ice thickness inversion (GlabTop, OGGM, Huss-Farinotti), outline delineation, GRACE mascon mass change, input-output ice sheet mass balance | Glacier mapping / inversion and mass-balance methods | 38 |
| Permafrost: Stefan equation, TTOP model, active layer thickness mapping, thaw subsidence from InSAR | Permafrost models / mapping and deformation workflows | 38 |

## Vegetation radiative transfer and fluorescence

| Source entry | Kind to review | Source page |
|---|---|---:|
| 3D RTMs (DART), SCOPE, leaf chlorophyll retrieval, hemispherical photo LAI, gap fraction models | Radiative transfer models / biophysical retrieval | 38 |
| Sun-induced fluorescence retrieval (FLD, SFM), photosynthesis models (FvCB), canopy structure retrieval from LiDAR | Fluorescence retrieval / photosynthesis and canopy models | 38 |

## Emission estimation and atmospheric inversion

| Source entry | Kind to review | Source page |
|---|---|---:|
| XCO2 retrieval and carbon flux inversion (OCO-2 and GOSAT style), methane inversion, NOx emission estimation via divergence methods | Atmospheric retrieval and emissions inversion | 38 |
| TROPOMI oversampling and wind-rotation methods, EMG fitting for point sources, plume-based flux quantification | Satellite data aggregation / plume fitting and flux estimation | 38 |
| Wind profile models (log law, power law), Weibull fits, mass-consistent wind models (WindNinja), CFD downscaling | Wind profile and flow models / downscaling | 38 |

## Structural geology and directional statistics

| Source entry | Kind to review | Source page |
|---|---|---:|
| Circular statistics: Rayleigh test, von Mises distribution, Kuiper and Watson tests, rose diagram analysis | Directional and circular statistical methods | 38 |
| Spherical statistics: Fisher and Kent distributions, Bingham distribution, stereonet analysis | Spherical distributions / structural geology analysis | 39 |
| Structural measurements from point clouds: plane fitting, discontinuity set extraction, fracture network analysis, DFN generation, kinematic slope stability | Point-cloud structural analysis / fracture-network and stability methods | 39 |
| Geological modeling: cross-section construction, fault network modeling, implicit modeling via RBF or potential fields | Geological modelling workflows | 39 |

## Data-quality statistics for spatial data

| Source entry | Kind to review | Source page |
|---|---|---:|
| Missing data: spatial multiple imputation, MICE, kNN imputation, missForest, GP imputation | Missing-data methods / spatial imputation | 39 |
| Spatial misalignment and change of support: downscaler fusion models (Berrocal-style), Berkson and classical measurement error, ecological fallacy diagnostics | Spatial data integration / measurement-error and support models | 39 |
| Preferential sampling (Diggle-style models), informative sampling, spatial selection bias correction | Sampling models / selection-bias correction | 39 |
| Compositional data: Aitchison geometry, log-ratio transforms, compositional kriging | Compositional data analysis / geostatistical methods | 39 |
| Spatial graphical models: Gaussian graphical models, spatial Bayesian networks, causal discovery on spatial data | Graphical models / causal discovery | 39 |

## Spatial humanities

| Source entry | Kind to review | Source page |
|---|---|---:|
| Georeferencing historical texts, spatial narrative extraction, literary GIS, deep mapping, place-based corpus analysis | Digital humanities / spatial text-analysis workflows | 39 |

## Decisions for the next pass

1. Verify moving-object index names and the assumptions behind their update and query models.
2. Distinguish routing acceleration from route choice and multi-objective optimisation.
3. For transit examples, record service calendar, feed version, frequency and real-time data semantics.
4. Document sensor, temporal resolution and retrieval assumptions for water, ice and emissions.
5. Treat trajectory and location data as sensitive; apply privacy review before publishing examples.
