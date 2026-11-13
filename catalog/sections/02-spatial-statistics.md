# Section 2 — Spatial statistics: autocorrelation, point patterns, clustering, regression, econometrics

- **Original source section:** 2
- **Source pages:** 2–4
- **Source transcription:** [pages 1–5](../../source-inventory/pages-01-05.md)
- **Review state:** source entries extracted into this index; not every entry independently verified
- **Source-derived records:** [Global Moran's I](../../algorithms/statistics/global-morans-i.md); [Global Geary's C](../../algorithms/statistics/gearys-c.md); [Local Moran's I](../../algorithms/statistics/local-morans-i.md); [Getis-Ord Gi*](../../algorithms/statistics/getis-ord-gi-star.md)
- **Supplementary companions:** [Local Geary](../../algorithms/statistics/local-geary.md); [Global Getis-Ord G](../../algorithms/statistics/global-getis-ord-g.md)

The source groups together descriptive statistics, inferential procedures, point-process models, clustering methods, regression families, filters, inequality measures and spatial spectral analysis. The [Local Geary](../../algorithms/statistics/local-geary.md) and [Global Getis-Ord G](../../algorithms/statistics/global-getis-ord-g.md) lessons are supplementary companions added during research; neither is a separate entry in the original compendium. These are not all algorithms in the same sense. Keep the original grouping, then decide the right record type during research.

## Autocorrelation and local statistics

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Global: [Moran's I](../../algorithms/statistics/global-morans-i.md), [Geary's C](../../algorithms/statistics/gearys-c.md), join count, Lee's L, bivariate Moran's I, Mantel and partial Mantel tests | Global statistics / tests | 2 | Captured; names not individually verified |
| Local: [Local Moran's I (LISA)](../../algorithms/statistics/local-morans-i.md), [Getis-Ord Gi*](../../algorithms/statistics/getis-ord-gi-star.md), Moran scatterplot | Local statistics / diagnostic visualisation | 3 | Captured; names not individually verified |
| Summary geometry: mean center, median center, standard distance, standard deviational ellipse | Descriptive spatial summaries / geometric measures | 3 | Captured; names not individually verified |
| Inference: permutation and Monte Carlo tests, Bonferroni, FDR and Šidák correction, Dutilleul's modified t-test, spatial and block bootstrap | Inferential procedures / multiple-testing corrections / resampling | 3 | Captured; names not individually verified |
| Spatial eigenvector filtering (Moran eigenvectors), Spatial+, restricted spatial regression | Regression approaches / spatial dependence adjustments | 3 | Captured; names not individually verified |

## Point pattern analysis

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Quadrat analysis, Clark-Evans, nearest neighbor index | Exploratory methods / spatial statistics | 3 | Captured; names not individually verified |
| Ripley's K and L; G, F and J functions; pair correlation function | Point-pattern summary functions | 3 | Captured; names not individually verified |
| Models: Poisson, Cox, Neyman-Scott, Gibbs and Strauss processes, log-Gaussian Cox processes, marked patterns | Stochastic point-process models | 3 | Captured; names not individually verified |
| Cluster tests: Besag-Newell, Tango, SaTScan scan statistics, elliptic and flexible shapes (FleXScan) | Cluster-detection tests / scan statistics | 3 | Captured; names not individually verified |
| Kernel density estimation: adaptive and variable bandwidth, Silverman and cross-validated bandwidth selection | Density estimation / bandwidth-selection methods | 3 | Captured; names not individually verified |
| Network K-function, network KDE (NKDE), SANET methods | Network-constrained point-pattern methods / software-method families | 3 | Captured; names not individually verified |

## Clustering and regionalization

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Density-based: DBSCAN, HDBSCAN, OPTICS, DENCLUE, density peaks, ST-DBSCAN, T-DBSCAN | Clustering algorithms | 3 | Captured; names not individually verified |
| Partitioning: k-means, k-medoids, CLARA, CLARANS, constrained and equal-size k-means | Clustering algorithms / constrained variants | 3 | Captured; names not individually verified |
| Hierarchical and grid: BIRCH, STING, CLIQUE, Ward, mean shift, affinity propagation, spectral, Gaussian mixtures, fuzzy c-means, self-organizing maps, growing neural gas, consensus and co-clustering | Clustering algorithms / model families / grid methods | 3 | Captured; names not individually verified |
| Spatially constrained: SKATER, REDCAP, AZP, Max-p, spatial LDA | Regionalisation algorithms / spatial clustering methods | 3 | Captured; names not individually verified |
| Geodemographic classification (OAC-style), principal components and factor analysis | Classification approaches / dimensionality reduction | 3 | Captured; names not individually verified |

## Regression and spatial econometrics

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Lag and error: SAR, CAR, spatial lag, spatial error, SLX, SDEM, SAC/SARAR, Spatial Durbin, Manski model | Spatial regression model families | 3 | Captured; names not individually verified |
| Local and varying coefficients: GWR, MGWR, GTWR, GW principal components, GW summary statistics, spatially varying coefficient models, GeoDetector | Local modelling methods / geographically weighted methods | 3 | Captured; names not individually verified |
| Diagnostics: LM-lag, LM-error and robust variants, Wald and LR tests, Moran's I on residuals, Chow and regime tests, Breusch-Pagan, Koenker, GWR significance tests | Model diagnostics / statistical tests | 3 | Captured; names not individually verified |
| Estimation: spatial GMM, spatial HAC standard errors, spatial panel and dynamic panel models, spatial probit, spatial Heckman, spatial quantile regression, spatial stochastic frontier, spatial SUR, hedonic regression, endogenous weights, Bayesian model averaging over weights | Estimators / regression models / inference methods | 4 | Captured; names not individually verified |
| Bayesian: BYM, INLA/SPDE, hierarchical CAR models, spatial Dirichlet process, Gaussian process mixtures | Bayesian spatial model families / computational frameworks | 4 | Captured; names not individually verified |

## Smoothing and outlier detection

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Empirical Bayes rate smoothing, head-banging, median polish | Smoothing / exploratory procedures | 4 | Captured; names not individually verified |
| Gaussian, Laplacian, median, bilateral and non-local means filters, anisotropic diffusion, total-variation denoising, guided filters | Image and spatial filtering methods | 4 | Captured; names not individually verified |
| Spatial outlier tests: Z-value, scatterplot approach, variogram cloud, isolation forest, spatial LOF, geographically weighted outliers | Outlier diagnostics / anomaly-detection methods | 4 | Captured; names not individually verified |

## Inequality, entropy and scale

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Spatial Gini, Theil, spatial entropy, segregation indices (dissimilarity, isolation) | Inequality and segregation measures | 4 | Captured; names not individually verified |
| Fractal dimension, lacunarity, Hurst exponent, multifractal analysis, scale-space theory, MAUP analysis | Scale measures / spatial analysis concepts | 4 | Captured; names not individually verified |
| Spatial spectral analysis: 2D periodogram, EOF, SSA and MSSA, canonical correlation, maximum covariance analysis, cross-spectral coherence, wavelet coherence, Hilbert-Huang transform | Spectral and multivariate analysis methods | 4 | Captured; names not individually verified |

## Decisions for the next pass

1. Separate global and local spatial autocorrelation from the models used to explain it.
2. Verify each named statistic, test and model against primary or authoritative sources.
3. State the spatial weights, null hypothesis, sampling assumptions and inferential procedure for statistical examples.
4. Distinguish clustering algorithms from regionalisation objectives and constraints.
5. Do not treat a model acronym as a complete specification; document its likelihood, spatial structure, estimation and assumptions.
6. Use synthetic data only when it makes the statistical property easier to see, and state how the data were generated.
