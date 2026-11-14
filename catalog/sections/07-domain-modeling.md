# Section 7 — Domain modeling: environment, hazards, ecology, health, urban, energy, ocean

- **Original source section:** 7
- **Source pages:** 12–14
- **Source transcription:** [pages 11–15](../../source-inventory/pages-11-15.md)
- **Review state:** source entries extracted into this index; not every entry independently verified
- **Current canonical records:** [ELECTRE outranking](../../methods/electre-outranking.md) — researched method-family overview with a scoped ELECTRE I-style relation builder and exact small-instance kernel enumerator, tests, walkthroughs, exercises and visual labs; [TOPSIS](../../methods/topsis.md) — finite-alternative ranking with a tested vector-normalised NumPy implementation; [Ordered Weighted Averaging](../../methods/ordered-weighted-averaging.md) — researched aggregation lesson with standard and GIS weighted NumPy implementations; [Boolean and fuzzy overlay](../../methods/boolean-and-fuzzy-overlay.md) — researched operator-family lesson with tested NumPy implementations; [Analytic Hierarchy Process](../../methods/analytic-hierarchy-process.md) — researched pairwise-weighting lesson with a tested NumPy priority-vector baseline and consistency diagnostics; [Weighted linear combination](../../methods/weighted-linear-combination.md) — researched decision-rule lesson with a tested Python aggregation baseline and interactive suitability lab; [weights of evidence](../../methods/weights-of-evidence.md) — researched Bayesian evidence-combination lesson with a tested NumPy baseline, intern walkthrough and exercise

The source organises methods by application field. The same statistical, geometric, network and machine-learning methods can appear in several domains. Keep domain context, input data, scale and validation requirements visible rather than treating each application label as a separate algorithm.

## Land change and simulation

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Cellular automata (SLEUTH, ANN-CA, logistic-CA, Markov-CA), CLUE-S, FLUS, PLUS, Dinamica EGO, Land Change Modeler | Land-use and land-cover change models / software | 12  Not checked — intake only |
| Agent-based models, Markov chain land-use change, Monte Carlo spatial simulation | Simulation approaches / stochastic models | 12  Not checked — intake only |
| Schelling segregation, Sugarscape, percolation, diffusion-limited aggregation, sandpile and forest fire models, spatial game theory | Spatial simulation models / complex systems | 12  Not checked — intake only |
| Spatial random graphs, preferential attachment with distance decay, small-world and scale-free networks | Spatial graph models | 12  Not checked — intake only |

## Multi-criteria and decision support

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Weighted and Boolean overlay, AHP, fuzzy overlay, TOPSIS, ELECTRE, ordered weighted averaging, weights of evidence | Multi-criteria decision methods / evidence combination | 12  Not checked — intake only |
| Spatial decision support, participatory GIS, scenario analysis, InVEST ecosystem services | Decision-support workflows / software and models | 12  Not checked — intake only |
| Indices: social vulnerability (SoVI), multi-hazard and compound-risk, environmental justice, landscape connectivity (IIC, PC) | Composite indices / risk measures / connectivity metrics | 12  Not checked — intake only |

## Ecology and conservation

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Species distribution: MaxEnt, BIOCLIM, habitat suitability, joint SDMs, occupancy, N-mixture, spatial capture-recapture, distance sampling | Species distribution and ecological inference models | 12  Not checked — intake only |
| Connectivity: Circuitscape, Omniscape, Conefor, least-cost corridors, dispersal kernels, metapopulation models | Connectivity software / graph and movement models | 12  Not checked — intake only |
| Landscape metrics (FRAGSTATS): patch density, edge density, contagion; alpha and beta diversity; species-area relationships | Landscape metrics / biodiversity measures | 12  Not checked — intake only |
| Landscape genetics: isolation by distance and resistance, spatial PCA, Geneland, TESS, wombling, allele frequency autocorrelation | Spatial genetic analysis methods / software | 12  Not checked — intake only |

## Agriculture and forestry

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Crop models: DSSAT, APSIM, WOFOST, AquaCrop; yield estimation (SCYM, regression, deep learning) | Crop simulation models / yield-estimation methods | 12  Not checked — intake only |
| Crop calendar, phenology extraction (TIMESAT, Savitzky-Golay), field boundary delineation, irrigation detection, crop rotation mapping | Remote-sensing and agricultural analysis workflows | 12  Not checked — intake only |
| Forest disturbance, biomass estimation, allometric equations, species classification from hyperspectral and LiDAR | Forest monitoring / biomass models / classification | 12  Not checked — intake only |
| Growing degree days, drought indices (SPI, SPEI, VCI, PDSI), crop stress detection | Agroclimatic measures / indices / detection methods | 12  Not checked — intake only |

## Weather, climate, air quality

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Weather radar: clutter filtering, attenuation correction, Z-R, hydrometeor classification, TITAN, SCIT, TREC, pySTEPS, optical-flow nowcasting | Radar processing / precipitation relations / storm tracking and nowcasting | 13  Not checked — intake only |
| Rainfall retrieval: IMERG, PERSIANN, CMORPH; radar-gauge merging | Precipitation products / retrieval and fusion methods | 13  Not checked — intake only |
| Climate: Köppen, ETCCDI indices, reanalysis (ERA5) processing, bias correction, local climate zones, urban heat island | Climate classifications / indices / data processing and urban climate methods | 13  Not checked — intake only |
| Air quality: land-use regression, AERMOD, CALPUFF, CMAQ, WRF-Chem, GEOS-Chem, AOD-based PM2.5 estimation, low-cost sensor fusion, noise mapping (ISO 9613, CNOSSOS) | Exposure models / dispersion software / sensor fusion / standards | 13  Not checked — intake only |
| Dispersion: Gaussian plume, Lagrangian (HYSPLIT), volcanic ash dispersion | Atmospheric dispersion models | 13  Not checked — intake only |

## Hazards and risk

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Seismic: probabilistic seismic hazard analysis, ground motion prediction equations, ETAS, Coulomb stress, PAGER loss estimation, tsunami propagation | Hazard analysis methods / predictive equations / loss models | 13  Not checked — intake only |
| Fire: Rothermel, FARSITE, elliptical spread, fire risk indices | Fire spread models / simulation software / risk indices | 13  Not checked — intake only |
| Damage and exposure: xBD-style building damage classification, catastrophe loss models, exposure aggregation | Damage classification / catastrophe models / exposure workflows | 13  Not checked — intake only |
| Evacuation: contraflow, capacity-constrained routing, crowd simulation, shelter location | Evacuation planning / network optimisation / simulation | 13  Not checked — intake only |
| Near-repeat analysis, risk terrain modeling, STAC (crime) | Crime analysis methods / risk models | 13  Not checked — intake only |

## Health and epidemiology

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Disease mapping: BYM, standardized ratios, empirical Bayes | Disease mapping models / rate estimation | 13  Not checked — intake only |
| Epidemic models: SIR on networks, reaction-diffusion, metapopulation, gravity-based importation, mobility-driven forecasting | Epidemic and spatial transmission models | 13  Not checked — intake only |
| Vector-borne risk: MaxEnt, mechanistic temperature models; contact tracing graphs; spatial survival analysis | Ecological niche models / mechanistic models / network analysis / survival methods | 13  Not checked — intake only |
| Exposure: personal exposure from trajectories, environmental justice analysis | Exposure assessment / equity analysis | 13  Not checked — intake only |

## Urban and socioeconomic

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Nighttime lights (VIIRS harmonization), poverty and wealth mapping, urban extent (GHSL, WSF), impervious surface mapping, informal settlement detection | Urban measurement / mapping workflows / products | 13  Not checked — intake only |
| Building height and footprint estimation, footprint regularization, orthogonalization, urban morphometrics, walkability | Building extraction / geometry processing / urban metrics | 13  Not checked — intake only |
| Land use inference from POIs (topic models, Place2Vec), functional zone discovery | Semantic classification / representation learning / clustering | 13  Not checked — intake only |
| Urban economics: Alonso-Muth-Mills, von Thünen, Hotelling, central place theory, rank-size, location quotient, shift-share, agglomeration, land value capitalization | Spatial economic theories / models / indicators | 13  Not checked — intake only |
| Urban scaling laws, urban digital twins, CityGML and CityJSON processing, rooftop solar potential | Urban scaling models / digital-twin systems / data standards and workflows | 14  Not checked — intake only |
| Cadastre: parcel subdivision, COGO, traverse computation, survey network adjustment, topological validation | Cadastral operations / survey computation / validation | 14  Not checked — intake only |

## Energy and infrastructure

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Wind: WAsP, Jensen and Park wake models; solar: NREL SPA, Ineichen, Perez, REST2, PV yield; hydropower potential | Energy resource models / solar position and radiation methods / estimation | 14  Not checked — intake only |
| Least-cost transmission corridors, pipeline routing, electrification planning, minigrid sizing, capacity expansion | Infrastructure routing and planning / optimisation models | 14  Not checked — intake only |
| Radio propagation: Okumura-Hata, COST-231, ITM/Longley-Rice, ray tracing | Radio propagation models / simulation methods | 14  Not checked — intake only |

## Ocean, cryosphere and marine

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Wave models (WAVEWATCH III, SWAN), storm surge (ADCIRC), tidal harmonic analysis (T_TIDE, UTide), ocean drift and Lagrangian particle tracking | Ocean and coastal models / harmonic analysis / particle tracking | 14  Not checked — intake only |
| Oil spill and ship detection (SAR), AIS anomaly analysis | Remote-sensing detection / maritime data analysis | 14  Not checked — intake only |
| Mangrove and coral mapping, glacier and sea ice analysis | Habitat mapping / cryosphere analysis workflows | 14  Not checked — intake only |

## Geoscience, mining and planetary

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Seismic tomography, full waveform inversion, migration; gravity and magnetic inversion, Euler deconvolution, reduction to pole, upward and downward continuation | Geophysical inversion and processing methods | 14  Not checked — intake only |
| ERT, GPR processing, implicit geological modeling (RBF), 3D geostatistics, stochastic reservoir modeling, history matching | Geophysical survey methods / geological models / reservoir simulation | 14  Not checked — intake only |
| Mining: block models, grade-tonnage, pit optimization (Lerchs-Grossmann, pseudoflow), mine scheduling, mineral prospectivity, geochemical anomaly detection (U-statistic, concentration-area) | Mining data structures / optimisation / prospectivity and anomaly methods | 14  Not checked — intake only |
| Planetary: crater detection and counting, photoclinometry, shape from shading, mineral mapping, landing site hazard detection | Planetary remote-sensing and terrain-analysis methods | 14  Not checked — intake only |
| Archaeology: predictive modeling, site catchment, cumulative visibility, Tobler's hiking function, cost surfaces | Predictive modelling / spatial interaction / visibility and cost analysis | 14  Not checked — intake only |

## Cross-disciplinary spatial methods

| Source entry | Provisional kind | Source page  Verification status |
|---|---|---: --- |
| Spatial transcriptomics (SpatialDE, cell neighborhood analysis), histopathology point patterns, materials grain boundary analysis | Spatial omics / microscopy and materials analysis | 14  Not checked — intake only |
| Astronomy: two-point correlation, friends-of-friends, HEALPix cross-matching; microscopy particle tracking and Voronoi analysis | Spatial statistics / graph clustering / spherical indexing / particle tracking | 14  Not checked — intake only |

## Current reviewed coverage

Weighted linear combination has a canonical method record, tested numerical aggregation implementation and interactive synthetic suitability lab. Weights of evidence has a separate Bayesian method record, tested NumPy baseline, intern walkthrough, worked exercise and visual lab. ELECTRE has a researched family overview and a scoped ELECTRE I-style relation builder plus exact small-instance kernel enumerator, with tests, walkthroughs, exercises and visual labs. It reports multiple or absent kernels rather than applying undocumented cycle reduction; other ELECTRE variants and larger-scale choice procedures remain open. These methods answer different questions: WLC combines preference scores; weights of evidence estimates associations from labelled occurrences under its specialised conditional-independence assumption; ELECTRE constructs pairwise outranking relations. The wider domain entries still require separate verification.

## Decisions for the next pass

1. Treat these as application areas, not as one large algorithm family.
2. Identify the actual spatial question, data source, unit of analysis and decision context for each example.
3. Verify product and software names separately from the methods they implement.
4. Prefer published case studies and reproducible datasets over generic claims about a domain.
5. Avoid implying that one region, city, ecosystem or population represents all others.
