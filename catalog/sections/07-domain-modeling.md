# Section 7 — Domain modeling: environment, hazards, ecology, health, urban, energy, ocean

- **Original source section:** 7
- **Source pages:** 12–14
- **Source transcription:** [pages 11–15](../../source-inventory/pages-11-15.md)
- **Review state:** source entries extracted into this index; not every entry independently verified
- **Current canonical records:** [ELECTRE outranking](../../methods/electre-outranking.md) — researched method-family overview; no implementation is claimed; [TOPSIS](../../methods/topsis.md) — finite-alternative ranking with a tested vector-normalised NumPy implementation; [Ordered Weighted Averaging](../../methods/ordered-weighted-averaging.md) — researched aggregation lesson with standard and GIS weighted NumPy implementations; [Boolean and fuzzy overlay](../../methods/boolean-and-fuzzy-overlay.md) — researched operator-family lesson with tested NumPy implementations; [Analytic Hierarchy Process](../../methods/analytic-hierarchy-process.md) — researched pairwise-weighting lesson with a tested NumPy priority-vector baseline and consistency diagnostics; [Weighted linear combination](../../methods/weighted-linear-combination.md) — researched decision-rule lesson with a tested Python aggregation baseline and interactive suitability lab; [weights of evidence](../../methods/weights-of-evidence.md) — researched Bayesian evidence-combination lesson with a tested NumPy baseline, intern walkthrough and exercise

The source organises methods by application field. The same statistical, geometric, network and machine-learning methods can appear in several domains. Keep domain context, input data, scale and validation requirements visible rather than treating each application label as a separate algorithm.

## Land change and simulation

| Source entry | Kind to review | Source page |
|---|---|---:|
| Cellular automata (SLEUTH, ANN-CA, logistic-CA, Markov-CA), CLUE-S, FLUS, PLUS, Dinamica EGO, Land Change Modeler | Land-use and land-cover change models / software | 12 |
| Agent-based models, Markov chain land-use change, Monte Carlo spatial simulation | Simulation approaches / stochastic models | 12 |
| Schelling segregation, Sugarscape, percolation, diffusion-limited aggregation, sandpile and forest fire models, spatial game theory | Spatial simulation models / complex systems | 12 |
| Spatial random graphs, preferential attachment with distance decay, small-world and scale-free networks | Spatial graph models | 12 |

## Multi-criteria and decision support

| Source entry | Kind to review | Source page |
|---|---|---:|
| Weighted and Boolean overlay, AHP, fuzzy overlay, TOPSIS, ELECTRE, ordered weighted averaging, weights of evidence | Multi-criteria decision methods / evidence combination | 12 |
| Spatial decision support, participatory GIS, scenario analysis, InVEST ecosystem services | Decision-support workflows / software and models | 12 |
| Indices: social vulnerability (SoVI), multi-hazard and compound-risk, environmental justice, landscape connectivity (IIC, PC) | Composite indices / risk measures / connectivity metrics | 12 |

## Ecology and conservation

| Source entry | Kind to review | Source page |
|---|---|---:|
| Species distribution: MaxEnt, BIOCLIM, habitat suitability, joint SDMs, occupancy, N-mixture, spatial capture-recapture, distance sampling | Species distribution and ecological inference models | 12 |
| Connectivity: Circuitscape, Omniscape, Conefor, least-cost corridors, dispersal kernels, metapopulation models | Connectivity software / graph and movement models | 12 |
| Landscape metrics (FRAGSTATS): patch density, edge density, contagion; alpha and beta diversity; species-area relationships | Landscape metrics / biodiversity measures | 12 |
| Landscape genetics: isolation by distance and resistance, spatial PCA, Geneland, TESS, wombling, allele frequency autocorrelation | Spatial genetic analysis methods / software | 12 |

## Agriculture and forestry

| Source entry | Kind to review | Source page |
|---|---|---:|
| Crop models: DSSAT, APSIM, WOFOST, AquaCrop; yield estimation (SCYM, regression, deep learning) | Crop simulation models / yield-estimation methods | 12 |
| Crop calendar, phenology extraction (TIMESAT, Savitzky-Golay), field boundary delineation, irrigation detection, crop rotation mapping | Remote-sensing and agricultural analysis workflows | 12 |
| Forest disturbance, biomass estimation, allometric equations, species classification from hyperspectral and LiDAR | Forest monitoring / biomass models / classification | 12 |
| Growing degree days, drought indices (SPI, SPEI, VCI, PDSI), crop stress detection | Agroclimatic measures / indices / detection methods | 12 |

## Weather, climate, air quality

| Source entry | Kind to review | Source page |
|---|---|---:|
| Weather radar: clutter filtering, attenuation correction, Z-R, hydrometeor classification, TITAN, SCIT, TREC, pySTEPS, optical-flow nowcasting | Radar processing / precipitation relations / storm tracking and nowcasting | 13 |
| Rainfall retrieval: IMERG, PERSIANN, CMORPH; radar-gauge merging | Precipitation products / retrieval and fusion methods | 13 |
| Climate: Köppen, ETCCDI indices, reanalysis (ERA5) processing, bias correction, local climate zones, urban heat island | Climate classifications / indices / data processing and urban climate methods | 13 |
| Air quality: land-use regression, AERMOD, CALPUFF, CMAQ, WRF-Chem, GEOS-Chem, AOD-based PM2.5 estimation, low-cost sensor fusion, noise mapping (ISO 9613, CNOSSOS) | Exposure models / dispersion software / sensor fusion / standards | 13 |
| Dispersion: Gaussian plume, Lagrangian (HYSPLIT), volcanic ash dispersion | Atmospheric dispersion models | 13 |

## Hazards and risk

| Source entry | Kind to review | Source page |
|---|---|---:|
| Seismic: probabilistic seismic hazard analysis, ground motion prediction equations, ETAS, Coulomb stress, PAGER loss estimation, tsunami propagation | Hazard analysis methods / predictive equations / loss models | 13 |
| Fire: Rothermel, FARSITE, elliptical spread, fire risk indices | Fire spread models / simulation software / risk indices | 13 |
| Damage and exposure: xBD-style building damage classification, catastrophe loss models, exposure aggregation | Damage classification / catastrophe models / exposure workflows | 13 |
| Evacuation: contraflow, capacity-constrained routing, crowd simulation, shelter location | Evacuation planning / network optimisation / simulation | 13 |
| Near-repeat analysis, risk terrain modeling, STAC (crime) | Crime analysis methods / risk models | 13 |

## Health and epidemiology

| Source entry | Kind to review | Source page |
|---|---|---:|
| Disease mapping: BYM, standardized ratios, empirical Bayes | Disease mapping models / rate estimation | 13 |
| Epidemic models: SIR on networks, reaction-diffusion, metapopulation, gravity-based importation, mobility-driven forecasting | Epidemic and spatial transmission models | 13 |
| Vector-borne risk: MaxEnt, mechanistic temperature models; contact tracing graphs; spatial survival analysis | Ecological niche models / mechanistic models / network analysis / survival methods | 13 |
| Exposure: personal exposure from trajectories, environmental justice analysis | Exposure assessment / equity analysis | 13 |

## Urban and socioeconomic

| Source entry | Kind to review | Source page |
|---|---|---:|
| Nighttime lights (VIIRS harmonization), poverty and wealth mapping, urban extent (GHSL, WSF), impervious surface mapping, informal settlement detection | Urban measurement / mapping workflows / products | 13 |
| Building height and footprint estimation, footprint regularization, orthogonalization, urban morphometrics, walkability | Building extraction / geometry processing / urban metrics | 13 |
| Land use inference from POIs (topic models, Place2Vec), functional zone discovery | Semantic classification / representation learning / clustering | 13 |
| Urban economics: Alonso-Muth-Mills, von Thünen, Hotelling, central place theory, rank-size, location quotient, shift-share, agglomeration, land value capitalization | Spatial economic theories / models / indicators | 13 |
| Urban scaling laws, urban digital twins, CityGML and CityJSON processing, rooftop solar potential | Urban scaling models / digital-twin systems / data standards and workflows | 14 |
| Cadastre: parcel subdivision, COGO, traverse computation, survey network adjustment, topological validation | Cadastral operations / survey computation / validation | 14 |

## Energy and infrastructure

| Source entry | Kind to review | Source page |
|---|---|---:|
| Wind: WAsP, Jensen and Park wake models; solar: NREL SPA, Ineichen, Perez, REST2, PV yield; hydropower potential | Energy resource models / solar position and radiation methods / estimation | 14 |
| Least-cost transmission corridors, pipeline routing, electrification planning, minigrid sizing, capacity expansion | Infrastructure routing and planning / optimisation models | 14 |
| Radio propagation: Okumura-Hata, COST-231, ITM/Longley-Rice, ray tracing | Radio propagation models / simulation methods | 14 |

## Ocean, cryosphere and marine

| Source entry | Kind to review | Source page |
|---|---|---:|
| Wave models (WAVEWATCH III, SWAN), storm surge (ADCIRC), tidal harmonic analysis (T_TIDE, UTide), ocean drift and Lagrangian particle tracking | Ocean and coastal models / harmonic analysis / particle tracking | 14 |
| Oil spill and ship detection (SAR), AIS anomaly analysis | Remote-sensing detection / maritime data analysis | 14 |
| Mangrove and coral mapping, glacier and sea ice analysis | Habitat mapping / cryosphere analysis workflows | 14 |

## Geoscience, mining and planetary

| Source entry | Kind to review | Source page |
|---|---|---:|
| Seismic tomography, full waveform inversion, migration; gravity and magnetic inversion, Euler deconvolution, reduction to pole, upward and downward continuation | Geophysical inversion and processing methods | 14 |
| ERT, GPR processing, implicit geological modeling (RBF), 3D geostatistics, stochastic reservoir modeling, history matching | Geophysical survey methods / geological models / reservoir simulation | 14 |
| Mining: block models, grade-tonnage, pit optimization (Lerchs-Grossmann, pseudoflow), mine scheduling, mineral prospectivity, geochemical anomaly detection (U-statistic, concentration-area) | Mining data structures / optimisation / prospectivity and anomaly methods | 14 |
| Planetary: crater detection and counting, photoclinometry, shape from shading, mineral mapping, landing site hazard detection | Planetary remote-sensing and terrain-analysis methods | 14 |
| Archaeology: predictive modeling, site catchment, cumulative visibility, Tobler's hiking function, cost surfaces | Predictive modelling / spatial interaction / visibility and cost analysis | 14 |

## Cross-disciplinary spatial methods

| Source entry | Kind to review | Source page |
|---|---|---:|
| Spatial transcriptomics (SpatialDE, cell neighborhood analysis), histopathology point patterns, materials grain boundary analysis | Spatial omics / microscopy and materials analysis | 14 |
| Astronomy: two-point correlation, friends-of-friends, HEALPix cross-matching; microscopy particle tracking and Voronoi analysis | Spatial statistics / graph clustering / spherical indexing / particle tracking | 14 |

## Current reviewed coverage

Weighted linear combination has a canonical method record, tested numerical aggregation implementation and interactive synthetic suitability lab. Weights of evidence now has a separate Bayesian method record, tested NumPy baseline, intern walkthrough and worked exercise. These methods answer different questions: WLC combines preference scores; weights of evidence estimates associations from labelled occurrences under conditional independence. The remaining multi-criteria methods and wider domain entries still require separate verification.

## Decisions for the next pass

1. Treat these as application areas, not as one large algorithm family.
2. Identify the actual spatial question, data source, unit of analysis and decision context for each example.
3. Verify product and software names separately from the methods they implement.
4. Prefer published case studies and reproducible datasets over generic claims about a domain.
5. Avoid implying that one region, city, ecosystem or population represents all others.
