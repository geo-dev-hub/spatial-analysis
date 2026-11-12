# Source inventory transcription — pages 41–47

> Faithful text extraction from the supplied *Spatial Analysis Algorithms: Complete Compendium*. Original page boundaries are retained below. This is an intake transcription, not a technical verification or editorial rewrite.

`<PARSED TEXT FOR PAGE: 41 / 47>`

Spatial Analysis Algorithms: Complete Compendium




      Back trajectories (HYSPLIT), footprint models (STILT, FLEXPART), potential source
      contribution function (PSCF), concentration-weighted trajectory (CWT)
      Receptor models: PMF, chemical mass balance, source apportionment with spatial
      covariates
      Ionospheric and space weather: TEC mapping, scintillation indices, ionospheric
      correction models

Acoustic and sensor-based spatial analysis

      Sound source localization: TDOA, beamforming, multilateration, acoustic indices for
      soundscape ecology
      Bird call and wildlife detection from acoustic arrays, passive acoustic monitoring
      networks
      Side-scan and sub-bottom sonar processing, seabed classification

Pitfalls and diagnostics checklist for spatial analysis and GeoAI

      Data leakage through spatial autocorrelation, tile overlap and neighboring patches in
      random train-test splits
      MAUP and ecological fallacy checks, edge and boundary effects, tile-boundary
      artifacts in segmentation
      Extrapolation outside covariate space, label shift between regions, temporal drift and
      sensor changes
      Confounding by spatial structure, residual autocorrelation checks, calibration across
      regions
      Reporting practices: report spatial CV scheme, area of applicability, uncertainty
      maps, per-region metrics and class-wise area estimates


20. Additions: indices, microwave and thermal retrieval, event
tracking, information theory, surveys
Names are from memory, so verify before citing. Coverage of the field is now broad, and
new additions are increasingly narrow variants.

More spectral indices

      Vegetation: GNDVI, ARVI, GCI, MSAVI, OSAVI, WDRVI, NIRv, kNDVI, MTCI, REIP,
      TCARI, CIgreen, CIrededge
      Pigments and stress: PSRI, ARI, CRI, SIPI, PRI, NDII, NMDI
      Soil, residue and minerals: BSI, NDTI, STI, CAI (crop residue), clay mineral ratio, iron
      oxide ratio, ferrous iron index, ASTER mineral indices

Thermal and land surface temperature


                                                                                          Page 41 of 47

`<PARSED TEXT FOR PAGE: 42 / 47>`

Spatial Analysis Algorithms: Complete Compendium




      Emissivity: temperature-emissivity separation (TES), NDVI-threshold emissivity
      LST algorithms: mono-window, single-channel, split-window; surface urban heat island
      intensity metrics
      Thermal sharpening and downscaling: DisTrad, TsHARP, regression-based and deep
      learning LST downscaling

Microwave and radar retrieval models

      Backscatter models: Water Cloud Model, Oh, Dubois, IEM, AIEM; change-detection
      soil moisture (TU Wien style), vegetation optical depth
      Forest structure: RVoG, PolInSAR forest height, P-band biomass retrieval
      Radiometry: tau-omega model (SMAP, SMOS retrievals), AMSR2 snow water
      equivalent, GPROF-style rain retrieval
      Ocean radar: CMOD5-type wind retrieval, SAR wave spectra, delay-Doppler altimetry

Product validation and merging without ground truth

      Triple collocation and extended triple collocation, error covariance estimation, signal-
      to-noise ratio of products
      Precipitation merging: gauge-satellite kriging blending (CHIRPS and MSWEP style),
      conditional merging, optimal interpolation

Nighttime lights processing

      Saturation correction, blooming correction, DMSP-VIIRS harmonization, background
      and noise removal, lights-per-capita normalization

Climate and ocean event detection and tracking

      Event definition: marine heatwaves (Hobday), heatwave and cold spell definitions,
      drought events via run theory, percentile thresholds
      Space-time tracking: 3D connected component labeling, storm and cyclone tracking
      (TempestExtremes-style), atmospheric river detection (IVT-based, ARTMIP), blocking
      and jet stream detection, monsoon onset indices
      Ocean: mesoscale eddy tracking, upwelling indices, Lagrangian coherent structures
      (FTLE), geostrophic currents from sea surface height, Ekman and Stokes drift

Information-theoretic and causal methods for spatiotemporal systems

      Entropy measures: Shannon, Renyi, Tsallis, sample entropy, permutation entropy,
      spatial entropy variants
      Dynamics: recurrence plots and recurrence quantification analysis, Lyapunov
      exponents
      Causality: Granger causality, transfer entropy, convergent cross mapping, causal
      networks from gridded fields (PCMCI-style), teleconnection graphs



                                                                                       Page 42 of 47

`<PARSED TEXT FOR PAGE: 43 / 47>`

Spatial Analysis Algorithms: Complete Compendium




      Motif and pattern discovery: SAX, shapelets, matrix profile, motif discovery in spatial
      time series

Phylogeography and survey sampling

      Continuous phylogeographic diffusion (BEAST-style), BSSVS for spread route
      inference, genomic epidemiology with spatial covariates
      Bayesian reproduction number maps, spatial Rt estimation, nowcasting with reporting
      delays, wastewater surveillance spatial models
      Survey sampling: EPI cluster sampling, LQAS, sampling frames from building footprints
      and imagery, DHS cluster GPS displacement and correction

Urban 3D and growth

      Building height from radar and stereo, floor count inference, urban volume estimation,
      3D city model generation from oblique imagery
      Urban growth boundary delineation, urban expansion modeling with spatial
      constraints


21. Additions: neural fields, climate ML, accounting, robust
geometry, semantic maps, integrity
Names are from memory, so verify before citing. These are narrower variants and adjacent
fields.

Neural fields and implicit representations

      Coordinate networks: SIREN, Fourier feature networks, hash-grid encodings (Instant-
      NGP style), location-conditioned INRs
      Satellite NeRF and splatting: S-NeRF, EO-NeRF, SatNeRF, Gaussian splatting for
      satellite imagery, shadow-aware radiance fields
      Implicit DEMs and climate field compression: neural compression of reanalysis and
      model output, continuous-resolution surface models

Climate and Earth-system machine learning

      Emulators and spherical operators: SFNO, ACE-style atmosphere emulators, ocean
      emulators, subseasonal and seasonal ML forecasts
      Learned data assimilation: diffusion-based assimilation, ensemble-free assimilation
      with generative priors
      ML parameterizations: subgrid and convection schemes, stochastic
      parameterizations, hybrid ML-physics coupling stability checks

Land change accounting



                                                                                      Page 43 of 47

`<PARSED TEXT FOR PAGE: 44 / 47>`

Spatial Analysis Algorithms: Complete Compendium




      Intensity analysis (Aldwaik-Pontius), net versus swap change, gain-loss
      decomposition, transition matrices, trajectory analysis
      Legend harmonization and crosswalks (LCCS-style), class hierarchy mapping,
      semantic harmonization across land cover products
      Map comparison metrics: Cramer's V, mean absolute error of areas, Pontius quantity
      and allocation measures

Ecosystem accounting

      SEEA EA extent and condition accounts, ecosystem service supply-use tables,
      natural capital valuation, spatial service flow models

Urban design analytics

      Density metrics (FSI, GSI, Spacematrix), view corridor and view shed analysis, daylight
      and sunlight-hour computation
      Transit-oriented development indices, street connectivity and block morphology
      metrics, urban form classification (morphological tessellation)

Robust geometric computation

      Exact and adaptive predicates (Shewchuk), exact arithmetic, interval arithmetic,
      floating-point robustness in overlay and triangulation
      Snapping, tolerance handling, topological robustness, simulation of simplicity,
      precision models in JTS and GEOS

Time-dependent datums and vertical reference

      Dynamic datums, plate motion models, ITRF realizations and epochs, NAD83 epoch
      handling, HTDP and NADCON transformations
      Vertical datums: geoid-based heights (GEOID18-style), VERTCON, tidal datums,
      ellipsoidal-to-orthometric conversion
      Velocity field interpolation for coordinate updates

Semantic maps and spatial AI for robotics and AR

      3D scene graphs (Hydra-style), topological and hierarchical maps, semantic SLAM,
      open-vocabulary mapping (ConceptFusion, CLIP-Fields, VLMaps)
      Visual positioning systems, geo-anchors, street-level localization for AR, digital twin
      synchronization
      Autonomous driving maps: lane-level HD maps, map change detection, crowdsourced
      mapping, lidar map matching with NDT, road marking extraction

GNSS integrity and location verification




                                                                                        Page 44 of 47

`<PARSED TEXT FOR PAGE: 45 / 47>`

Spatial Analysis Algorithms: Complete Compendium




      Spoofing and jamming detection, signal authentication, anomaly detection in
      pseudorange and Doppler, integrity monitoring
      Crowdsourced and proof-of-location verification, mock-location detection, cross-
      sensor consistency checks

Geology and geoscience machine learning

      Lithology classification from remote sensing and geophysics, geological map
      generation, stratigraphic and basin modeling
      Thermochronology and geochronology spatial analysis, mineral deposit modeling with
      weights of evidence and neural nets

Maritime and aviation analytics

      Ship-to-ship transfer detection, loitering and rendezvous detection, port call
      inference, trade flow estimation from AIS, vessel emissions inventories
      ADS-B trajectory clustering, holding pattern detection, aircraft emissions inventories,
      contrail detection from satellite imagery



22. Additions: inference engines, covariance, spherical statistics,
asset mapping, monitoring
Names are from memory, so verify before citing. Mostly narrower variants and supporting
machinery.

Inference engines for spatial models

      Sampling: Gibbs and Metropolis-within-Gibbs for CAR and SAR models, slice
      sampling, sequential Monte Carlo, pseudo-marginal methods
      Approximation: Laplace approximation, expectation propagation, variational Bayes,
      EM for spatial mixtures
      Optimizers: L-BFGS, Adam, natural gradient for GP hyperparameters
      Probabilistic programming: Stan, NIMBLE, PyMC, INLA-style nested approximations

Covariance functions and basis expansions

      Stationary kernels: Matern, exponential, spherical, Gaussian, Cauchy, powered
      exponential, Wendland compact support
      Non-Euclidean validity: valid covariances on spheres (Gneiting), on networks
      (Anderes), graph kernels; why geodesic-distance Gaussian kernels can fail
      Space-time covariances: Gneiting nonseparable class, Cressie-Huang, product-sum
      and metric models




                                                                                       Page 45 of 47

`<PARSED TEXT FOR PAGE: 46 / 47>`

Spatial Analysis Algorithms: Complete Compendium




      Bases: thin plate, B-splines and tensor products, wavelets, Slepian functions, Zernike,
      radial bases, multiresolution Haar, FRK bases, Moran basis

Spherical and Riemannian statistics for location data

      Frechet mean on the sphere, spherical k-means, von Mises-Fisher mixtures, spherical
      kernel density estimation
      Spherical splines, geodesic regression, spherical Gaussian processes
      Geodesic operations on the ellipsoid: Karney polygon area, geodesic buffers,
      azimuthal equidistant buffers, antipodal and dateline handling

Sensor artifact and geometry correction

      Destriping (Fourier, wavelet), noise estimation, MTF compensation, deblurring, jitter
      correction
      Line-scan and rolling-shutter geometric models, attitude and star tracker processing,
      boresight refinement
      Cloud removal with SAR guidance, SAR-optical fusion, hyperspectral destriping

Road and roadway asset mapping

      Street-level extraction: traffic sign, pole and lane marking detection from street
      imagery and mobile mapping point clouds
      Sidewalk and curb ramp inventories, pavement distress detection, road roughness
      from accelerometers (IRI estimation)
      Crowdsourced street imagery pipelines (Mapillary style), map feature conflation with
      OSM

Utilities, rail and power line analytics

      Water networks: EPANET hydraulic simulation, leak detection, district metered area
      sectorization, water loss analysis
      Power grid: power flow with geography, outage detection and restoration routing,
      vegetation encroachment along power lines from LiDAR, conductor sag and clearance
      analysis, pole detection
      Rail: track geometry from LiDAR, rail asset inventories, vegetation encroachment

Engineering geodesy and structural monitoring

      Stockpile volume, earthwork cut and fill, construction progress monitoring, as-built
      versus design comparison
      Deformation monitoring: total station network adjustment, tunnel convergence,
      bridge and dam deformation, settlement monitoring from InSAR and GNSS
      Terrestrial laser scanning registration, change detection on dense point clouds
      (M3C2)


                                                                                        Page 46 of 47

`<PARSED TEXT FOR PAGE: 47 / 47>`

Spatial Analysis Algorithms: Complete Compendium




Citizen science and presence-only modeling

      Observer effort and detectability models, eBird-style spatiotemporal exploratory
      models (STEM)
      Presence-only bias correction: target-group background, bias grids, integrated SDMs,
      point process SDMs, iNaturalist-style data cleaning
      Occupancy with false positives, camera trap density estimation, eDNA spatial
      sampling models

Fire danger and post-fire hazards

      Fire danger systems: Canadian FWI, KBDI, McArthur, NFDRS; fuel moisture
      estimation, fuel type mapping
      Burn severity (dNBR, RdNBR, RBR), post-fire debris flow models (USGS-style
      empirical models), smoke dispersion coupling




                                                                                     Page 47 of 47
