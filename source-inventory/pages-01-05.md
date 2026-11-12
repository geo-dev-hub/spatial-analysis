# Source inventory transcription — pages 1–5

> Faithful text extraction from the supplied *Spatial Analysis Algorithms: Complete Compendium*. Original page boundaries are retained below. This is an intake transcription, not a technical verification or editorial rewrite.

`<PARSED TEXT FOR PAGE: 1 / 47>`

Spatial Analysis Algorithms: Complete Compendium




Spatial Analysis Algorithms: Complete
Compendium
  Nov 12, 2026       ·   ​@chatgpt




1. Core GIS: geometry, indexing, proximity, networks, routing
The foundational vector and network operations behind nearly every GIS workflow.

Vector and computational geometry

      Overlay: buffer, clip, intersect, union, difference, dissolve, centroid, minimum
      bounding geometry
      Hulls and tessellations: convex hull (Graham scan, Jarvis march, Quickhull), concave
      hull (alpha shapes), Voronoi (Fortune sweep), Delaunay (Bowyer-Watson,
      incremental, divide and conquer), constrained Delaunay, Ruppert refinement
      Point-in-polygon (ray casting, winding number), point location (slab method, trapezoid
      map), segment intersection (Bentley-Ottmann)
      Polygon clipping: Sutherland-Hodgman, Weiler-Atherton, Vatti, Greiner-Hormann;
      offsetting (Clipper); cascaded union; self-intersection repair; validity checking
      Simplification and generalization: Douglas-Peucker, Visvalingam, topology-preserving
      simplification, snap rounding
      Triangulation and decomposition: ear clipping, trapezoidal and convex decomposition,
      medial axis, straight skeleton, Minkowski sum
      Distance and extent: Hausdorff and Fréchet distance, rotating calipers, smallest
      enclosing circle (Welzl), largest empty circle, pole of inaccessibility (polylabel),
      oriented minimum bounding rectangle
      Proximity graphs: Gabriel, relative neighborhood, beta-skeleton, Yao, Euclidean
      minimum spanning tree
      Visibility polygons, funnel algorithm, CSG and BSP Boolean operations, DCEL overlay,
      arrangements, planarization

Spatial indexing and query processing

      Trees: R-tree (R*, R+, Hilbert, STR bulk loading), quadtree, octree, k-d tree, ball tree,
      VP-tree, BSP tree, KD-B-tree, Grid File
      Space-filling curves and grids: Z-order (Morton), Hilbert, Geohash, H3, S2, quadkeys,
      HEALPix
      Queries: range, kNN, reverse kNN, closest pair, spatial skyline, top-k spatial keyword,
      geofencing




                                                                                           Page 1 of 47

`<PARSED TEXT FOR PAGE: 2 / 47>`

Spatial Analysis Algorithms: Complete Compendium




      Joins: filter-and-refine, plane-sweep, PBSM, TOUCH, partition-based, kNN joins
      Approximate search: locality-sensitive hashing, HNSW, IVF-PQ, ScaNN
      Learned indexes (ZM index, RSMI, LISA), selectivity estimation, spatial histograms

Proximity, topology and relations

      Nearest neighbor, distance matrices (Euclidean, geodesic), spatial joins
      DE-9IM topological relations, RCC-8, cardinal direction relations
      Spatial weights: contiguity, distance band, kNN

Network analysis

      Shortest path: Dijkstra, A*, Bellman-Ford, Floyd-Warshall, bidirectional Dijkstra, ALT,
      contraction hierarchies, hub labeling, customizable route planning
      Service areas and isochrones, many-to-many routing, Yen's k-shortest paths,
      alternative routes
      Centrality: betweenness, closeness, PageRank; space syntax (axial, integration);
      street network metrics (orientation, circuity, intersection density)
      Community detection: Louvain, Leiden, Infomap, label propagation; partitioning:
      Kernighan-Lin, spectral, METIS
      Flows and trees: max flow and min cut, minimum spanning tree, Steiner tree, k-core
      decomposition
      Map matching: HMM, ST-Matching, IVMM, Fast Map Matching, neural
      Transit routing: RAPTOR, Connection Scan; time-dependent, stochastic, multimodal
      and turn-restricted routing
      Road network generalization and stroke generation

Classic routing

      TSP: 2-opt, Lin-Kernighan, Christofides; VRP: Clarke-Wright savings, sweep; Chinese
      postman and arc routing
      CVRP, VRPTW, pickup-and-delivery, dial-a-ride, ALNS, column generation, branch-
      and-price


2. Spatial statistics: autocorrelation, point patterns, clustering,
regression, econometrics
Methods for testing and modeling spatial dependence, heterogeneity and clustering.

Autocorrelation and local statistics

      Global: Moran's I, Geary's C, join count, Lee's L, bivariate Moran's I, Mantel and partial
      Mantel tests



                                                                                          Page 2 of 47

`<PARSED TEXT FOR PAGE: 3 / 47>`

Spatial Analysis Algorithms: Complete Compendium




      Local: Local Moran's I (LISA), Getis-Ord Gi*, Moran scatterplot
      Summary geometry: mean center, median center, standard distance, standard
      deviational ellipse
      Inference: permutation and Monte Carlo tests, Bonferroni, FDR and Šidák correction,
      Dutilleul's modified t-test, spatial and block bootstrap
      Spatial eigenvector filtering (Moran eigenvectors), Spatial+, restricted spatial
      regression

Point pattern analysis

      Quadrat analysis, Clark-Evans, nearest neighbor index
      Ripley's K and L; G, F and J functions; pair correlation function
      Models: Poisson, Cox, Neyman-Scott, Gibbs and Strauss processes, log-Gaussian Cox
      processes, marked patterns
      Cluster tests: Besag-Newell, Tango, SaTScan scan statistics, elliptic and flexible
      shapes (FleXScan)
      Kernel density estimation: adaptive and variable bandwidth, Silverman and cross-
      validated bandwidth selection
      Network K-function, network KDE (NKDE), SANET methods

Clustering and regionalization

      Density-based: DBSCAN, HDBSCAN, OPTICS, DENCLUE, density peaks, ST-DBSCAN,
      T-DBSCAN
      Partitioning: k-means, k-medoids, CLARA, CLARANS, constrained and equal-size k-
      means
      Hierarchical and grid: BIRCH, STING, CLIQUE, Ward, mean shift, affinity propagation,
      spectral, Gaussian mixtures, fuzzy c-means, self-organizing maps, growing neural gas,
      consensus and co-clustering
      Spatially constrained: SKATER, REDCAP, AZP, Max-p, spatial LDA
      Geodemographic classification (OAC-style), principal components and factor analysis

Regression and spatial econometrics

      Lag and error: SAR, CAR, spatial lag, spatial error, SLX, SDEM, SAC/SARAR, Spatial
      Durbin, Manski model
      Local and varying coefficients: GWR, MGWR, GTWR, GW principal components, GW
      summary statistics, spatially varying coefficient models, GeoDetector
      Diagnostics: LM-lag, LM-error and robust variants, Wald and LR tests, Moran's I on
      residuals, Chow and regime tests, Breusch-Pagan, Koenker, GWR significance tests




                                                                                           Page 3 of 47

`<PARSED TEXT FOR PAGE: 4 / 47>`

Spatial Analysis Algorithms: Complete Compendium




      Estimation: spatial GMM, spatial HAC standard errors, spatial panel and dynamic
      panel models, spatial probit, spatial Heckman, spatial quantile regression, spatial
      stochastic frontier, spatial SUR, hedonic regression, endogenous weights, Bayesian
      model averaging over weights
      Bayesian: BYM, INLA/SPDE, hierarchical CAR models, spatial Dirichlet process,
      Gaussian process mixtures

Smoothing and outlier detection

      Empirical Bayes rate smoothing, head-banging, median polish
      Gaussian, Laplacian, median, bilateral and non-local means filters, anisotropic
      diffusion, total-variation denoising, guided filters
      Spatial outlier tests: Z-value, scatterplot approach, variogram cloud, isolation forest,
      spatial LOF, geographically weighted outliers

Inequality, entropy and scale

      Spatial Gini, Theil, spatial entropy, segregation indices (dissimilarity, isolation)
      Fractal dimension, lacunarity, Hurst exponent, multifractal analysis, scale-space
      theory, MAUP analysis
      Spatial spectral analysis: 2D periodogram, EOF, SSA and MSSA, canonical correlation,
      maximum covariance analysis, cross-spectral coherence, wavelet coherence, Hilbert-
      Huang transform



3. Geostatistics, interpolation, uncertainty, spatiotemporal models
Surface estimation, simulation, uncertainty quantification and space-time modeling.

Interpolation

      Deterministic: IDW, natural neighbor, spline, thin plate spline, RBF, Shepard, Cressman,
      Barnes, trend surface, TIN, Whittaker smoother
      Climate and gap filling: PRISM, Daymet, ANUSPLIN, DINEOF, HANTS, matrix and
      tensor completion, deep inpainting, spatiotemporal fusion (STARFM, ESTARFM,
      FSDAF)

Kriging and geostatistics

      Kriging: simple, ordinary, universal, co-kriging, regression kriging, external drift,
      indicator, disjunctive, block, area-to-point, area-to-area, spatiotemporal
      Variogram modeling, anisotropy, nonstationary covariance, spatial deformation,
      process convolution, multiscale kriging
      Large-data Gaussian processes: Vecchia, NNGP, covariance tapering, fixed rank
      kriging, predictive processes, lattice kriging, multi-resolution approximation


                                                                                              Page 4 of 47

`<PARSED TEXT FOR PAGE: 5 / 47>`

Spatial Analysis Algorithms: Complete Compendium




      Simulation: sequential Gaussian, indicator simulation, multiple-point statistics
      (SNESIM, direct sampling), object-based, p-field
      Extremes and dependence: max-stable processes (Brown-Resnick), spatial copulas,
      GEV and Gumbel fits
      Sampling design: spatially balanced (GRTS, BAS), cLHS, stratified, spatial thinning
      Digital soil mapping: SCORPAN, pedotransfer functions, equal-area splines, SoilGrids-
      style stacking

Spatiotemporal statistics

      STARMA, space-time ARIMA, GTWR, dynamic linear and state-space models
      Spatiotemporal GP (separable and non-separable kernels), spatiotemporal INLA,
      functional data analysis
      Space-time scan statistics, Knox test, space-time K function, space-time cube,
      emerging hot spot analysis
      Spatial survival and frailty models
      Spatiotemporal point processes: Hawkes, LGCP, ETAS
      Trend and change: Mann-Kendall, Sen's slope, harmonic regression, BFAST,
      LandTrendr, CCDC

Data assimilation and inverse methods

      Optimal interpolation, 3D-Var, 4D-Var, ensemble Kalman filter, LETKF, particle filters
      Variational and Bayesian inversion, adjoint methods, emulators and surrogate models
      Radiative transfer inversion (PROSAIL, look-up tables)

Uncertainty, accuracy and sensitivity

      Positional accuracy (RMSE), error propagation, Monte Carlo, Latin hypercube, Sobol
      sensitivity, polynomial chaos
      Classification accuracy: confusion matrix, kappa, area-adjusted accuracy (Olofsson),
      fuzzy kappa, Figure of Merit, quantity and allocation disagreement
      Bayesian: MCMC (Metropolis, HMC, NUTS), variational inference, approximate
      Bayesian computation, Bayesian model averaging
      Probabilistic and fuzzy maps: ensemble spread, interval-valued, possibilistic
      Conformal prediction (including locally adaptive), quantile regression forests, area of
      applicability, dissimilarity index
      Reasoning under imprecision: fuzzy and rough sets, Dempster-Shafer, Bayesian belief
      networks, possibility theory

Small-area and survey estimation




                                                                                         Page 5 of 47
