# Source inventory transcription — pages 6–10

> Faithful text extraction from the supplied *Spatial Analysis Algorithms: Complete Compendium*. Original page boundaries are retained below. This is an intake transcription, not a technical verification or editorial rewrite.

<PARSED TEXT FOR PAGE: 6 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Fay-Herriot, unit-level small-area models, Horvitz-Thompson, model-assisted
      estimation, MRP
      Spatial microsimulation (IPF, simulated annealing), areal interpolation, dasymetric
      mapping, WorldPop-style random forest population surfaces
      Statistical downscaling: quantile mapping, BCSD, delta change, analog methods


4. Raster, terrain, hydrology, geomorphology
Grid-based operations, surface derivatives and water-flow modeling.

Raster operations

      Map algebra: local, focal, zonal and global operations; reclassification; resampling
      (nearest, bilinear, cubic, Lanczos)
      Connected component labeling, flood fill, run-length encoding, image pyramids
      Distance: Euclidean distance transform (Felzenszwalb), chamfer, cost-distance, least-
      cost path, fast marching and Eikonal solvers, heat method
      Efficient statistics: integral images for focal statistics, zonal histograms
      Vectorization and contouring: raster-to-vector, marching squares, marching cubes
      Compression: quadtree, JPEG2000, LERC, wavelet; formats such as COG, Zarr,
      GeoParquet

Terrain analysis

      Slope, aspect, curvature (multiscale), hillshade, multi-directional shading, openness,
      sky-view factor, local relief models, red relief image maps
      Position and form: topographic position index, ruggedness, geomorphons, landform
      classification, ridge and valley extraction, pit and peak detection
      Visibility: viewshed (R3, R2, XDraw), cumulative viewshed, isovist, intervisibility, radar
      coverage and shadow, Fresnel clearance
      Solar and microclimate: solar radiation modeling, wind exposure, cold-air drainage,
      insolation indices
      Volumes: cut-and-fill, reservoir volume from DEM, hypsometric curves
      DEM quality: void filling, error modeling, DEM fusion (SRTM, ASTER, TanDEM-X), bare-
      earth extraction, hydro-conditioning, stream burning
      Terrain simplification and rendering: Lindstrom-Pascucci, quadric error metrics,
      ROAM, geometry clipmaps, CDLOD, TIN generalization

Hydrology

      Flow routing: D8, D-infinity, MFD, priority-flood depression filling, sink breaching




                                                                                         Page 6 of 47

<PARSED TEXT FOR PAGE: 7 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Flow accumulation, watershed and basin delineation, stream ordering (Strahler,
      Shreve), HAND, topographic wetness index
      Rainfall-runoff: SCS curve number, unit hydrograph, Green-Ampt, TOPMODEL, SWAT,
      HEC-HMS, LISFLOOD, VIC
      Routing and hydrodynamics: Muskingum, Manning, Saint-Venant, kinematic wave, 2D
      shallow water equations, SPH
      Flood: frequency analysis (GEV, Gumbel, return periods), bathtub versus
      hydrodynamic inundation, SAR flood mapping
      Groundwater: MODFLOW, MODPATH, MT3D, DRASTIC, recharge estimation (water
      table fluctuation, chloride mass balance)
      Land surface models: Noah-MP, CLM, JULES; GRACE downscaling; snow and soil
      moisture assimilation

Geomorphology and slope processes

      Chi analysis, slope-area analysis, knickpoint detection, drainage basin morphometry
      Landslide susceptibility (frequency ratio, logistic regression), SHALSTAB, weights of
      evidence
      Glacier mass balance, snow models, avalanche runout
      Erosion: USLE, RUSLE, hydraulic and thermal erosion simulation

Coastal

      DSAS (end-point rate, linear and weighted regression), waterline extraction, tide-
      coordinated shorelines
      Wave runup (Stockdon), longshore transport (CERC, Kamphuis), Bruun rule, Dean
      profile, coastal vulnerability index
      Bathymetry: satellite-derived (ratio, physics-based, ICESat-2 calibrated), multibeam
      gridding, topo-bathymetric lidar refraction correction



5. Remote sensing, SAR, LiDAR, photogrammetry
Image, point cloud and radar processing from raw sensor data to mapped products.

Preprocessing and correction

      Atmospheric: dark object subtraction, 6S, MODTRAN, FLAASH, Sen2Cor, ocean color
      atmospheric correction
      Topographic and BRDF: C-correction, SCS+C, Minnaert, Ross-Li, BRDF normalization
      Relative normalization: IR-MAD, pseudo-invariant features, histogram matching,
      empirical line calibration




                                                                                       Page 7 of 47

<PARSED TEXT FOR PAGE: 8 / 47>

Spatial Analysis Algorithms: Complete Compendium




      Cloud and shadow masking: Fmask, s2cloudless, CloudSEN12-style models; sensor
      harmonization (HLS)
      Mosaicking, seamline detection (Voronoi, graph cut), color balancing,
      orthorectification, co-registration
      Fusion: pan-sharpening (Brovey, IHS, Gram-Schmidt, PCA, wavelet, CNN),
      spatiotemporal fusion, Bayesian and Kalman fusion, sub-pixel and super-resolution
      mapping

Indices and transforms

      Vegetation and soil: NDVI, EVI, SAVI, NDRE, NDMI, LSWI, tasseled cap (Kauth-Thomas)
      Water, burn, snow, urban: NDWI, MNDWI, AWEI, NBR, dNBR, NDSI, NDBI
      Transforms: PCA, minimum noise fraction (MNF), Fourier, wavelet, Hough, Radon
      Texture and edges: GLCM, Gabor, Sobel, Canny, mathematical morphology, SIFT, SURF
      Thresholding: Otsu, adaptive; Stumpf bathymetry; OC4 chlorophyll
      Compositing: best-pixel, medoid, maximum NDVI

Classification and segmentation

      Pixel-based: maximum likelihood, SVM, random forest, XGBoost, LightGBM, stacked
      generalization, k-means, ISODATA
      Segmentation: watershed, SLIC superpixels, mean shift, region growing,
      multiresolution segmentation, graph cuts, MRF and CRF, active contours, level sets
      Object-based image analysis (OBIA)
      Time-series classification: TempCNN, Transformer, InceptionTime, TimeMatch, DTW,
      TWDTW
      Change detection: differencing, CVA, post-classification, IR-MAD, Siamese networks,
      ChangeFormer
      Fractional cover: spectral mixture analysis, regression trees, vegetation continuous
      fields

Hyperspectral

      Endmember extraction (N-FINDR, PPI, VCA), unmixing (FCLS, sparse, nonlinear, deep)
      Anomaly and target detection: RX, Kernel RX, matched filter, CEM, ACE, subspace
      methods
      Spectral angle mapper, spectral information divergence, band selection, continuum
      removal, absorption feature analysis, red-edge position

SAR and InSAR

      Speckle filtering, polarimetric decomposition (H/A/alpha, Freeman-Durden,
      Yamaguchi), CFAR detection, SAR-to-optical translation



                                                                                      Page 8 of 47

<PARSED TEXT FOR PAGE: 9 / 47>

Spatial Analysis Algorithms: Complete Compendium




      InSAR: PS-InSAR, SBAS, SqueeSAR, distributed scatterers, phase unwrapping
      (SNAPHU, minimum cost flow), coherence change detection, offset tracking,
      tomographic SAR, autofocus

LiDAR and point clouds

      Ground filtering: CSF, progressive morphological; ICP registration; RANSAC shape
      fitting
      Tree segmentation (local maxima, watershed, Dalponte), canopy height models, crown
      delineation
      Classification, voxelization, strip adjustment, GEDI waveform processing, ICESat-2
      ground photon classification
      Deep point networks: PointNet, PointNet++, KPConv, Point Transformer, RandLA-Net,
      MinkowskiNet

Photogrammetry and 3D

      Structure from Motion (COLMAP), bundle adjustment, aerial triangulation, GCP and
      IMU-aided adjustment, direct georeferencing
      Dense matching: SGM, PatchMatch, multi-view stereo; RPC sensor models; satellite
      stereo DSM; DSM, DTM and nDSM derivation
      Lens calibration (Brown-Conrady), boresight calibration, orthomosaic generation,
      mesh texturing
      Surface reconstruction: Poisson, marching cubes, mesh simplification, 3D alpha
      shapes, NeRF, 3D Gaussian splatting

Biophysical and geophysical retrieval

      Evapotranspiration and energy balance: SEBAL, METRIC, SEBS, ALEXI, Penman-
      Monteith, Hargreaves; land surface temperature (split-window, temperature-
      emissivity separation)
      Productivity and structure: light-use efficiency GPP, biomass allometry, LAI and
      fAPAR retrieval, soil moisture retrieval, albedo
      Water and atmosphere: Case 2 water quality inversion, aerosol retrieval (dark target,
      MAIAC), DOAS trace gases, cloud property retrieval
      Cryosphere and ocean: sea ice concentration (NASA Team, Bootstrap), ice motion,
      glacier velocity, DEM differencing, eddy detection (Okubo-Weiss), SST fronts,
      altimetry processing
      Thermal and fire: thermal anomaly and volcanic hotspot detection, active fire
      detection, burned area (MCD64A1)




                                                                                         Page 9 of 47

<PARSED TEXT FOR PAGE: 10 / 47>

Spatial Analysis Algorithms: Complete Compendium




6. Optimization, location science, mobility, transport
Decision-oriented methods: where to place things, how to move, and how people and
vehicles behave in space.

Location-allocation and spatial optimization

      Covering and median: p-median, p-center, p-dispersion, set covering, maximal
      covering (MCLP), MEXCLP, MALP, BACOP, hypercube queuing
      Capacitated and hub location, p-hub median, hierarchical, stochastic and robust
      facility location
      Districting: redistricting, ReCom, MCMC and Flip, compactness scores (Polsby-
      Popper, Reock, Schwartzberg), territory design, set partitioning
      Land-use allocation, spatial reserve design (Marxan), art gallery problem, sensor and
      camera placement, cell tower siting
      Heuristics: genetic algorithms, simulated annealing, NSGA-II, particle swarm, ant
      colony, tabu search, GRASP, variable neighborhood search, matheuristics
      Exact methods: branch-and-bound, Lagrangian relaxation, Benders decomposition,
      min-cost flow, transportation and assignment problems, Hungarian algorithm;
      quantum annealing and QAOA (experimental)

Logistics

      Multi-depot VRP, periodic routing, inventory-routing, drone-truck routing, school bus
      routing
      Snow plow and waste collection arc routing, ride-hailing dispatch, bike rebalancing
      ETA prediction (WDR, DeepTTE, graph neural networks), OR-Tools

Accessibility and spatial interaction

      Gravity models, Huff model, Hansen accessibility, Reilly's law, 2SFCA and variants,
      cumulative opportunities, impedance decay
      Radiation model, intervening opportunities, origin-destination flow models, equity
      accessibility (Gini, Lorenz)
      Trade area analysis (drive-time, Huff, analog), cannibalization, retail gravity, 15-minute
      city metrics

Transport planning

      Four-step model: trip generation, gravity distribution, mode choice (multinomial and
      nested logit), assignment
      Traffic assignment: user equilibrium, Frank-Wolfe, Wardrop equilibrium, dynamic
      traffic assignment, cell transmission model




                                                                                         Page 10 of 47
