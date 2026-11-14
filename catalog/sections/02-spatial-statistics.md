# Section 2 — Spatial statistics: autocorrelation, point patterns, clustering, regression, econometrics

- **Original source section:** 2
- **Source pages:** 2–4
- **Source transcription:** [pages 1–5](../../source-inventory/pages-01-05.md)
- **Review state:** source entries extracted into this index; not every entry independently verified
- **Source-derived records:** [Ripley's K and L](../../algorithms/statistics/ripley-k.md) — uncorrected and rectangular-window translation-corrected estimators, conditional-CSR simulation envelopes and a global studentised maximum-deviation test; [Clark–Evans nearest-neighbour index](../../algorithms/statistics/clark-evans.md); [Planar Gaussian KDE](../../algorithms/statistics/point-pattern-kde.md); [DBSCAN](../../algorithms/statistics/dbscan.md); [Global Moran's I](../../algorithms/statistics/global-morans-i.md); [Global Geary's C](../../algorithms/statistics/gearys-c.md); [Local Moran's I](../../algorithms/statistics/local-morans-i.md); [Getis-Ord Gi*](../../algorithms/statistics/getis-ord-gi-star.md)
- **Supplementary companions:** [Local Geary](../../algorithms/statistics/local-geary.md); [Global Getis-Ord G](../../algorithms/statistics/global-getis-ord-g.md)

The source groups together descriptive statistics, inferential procedures, point-process models, clustering methods, regression families, filters, inequality measures and spatial spectral analysis. The [Local Geary](../../algorithms/statistics/local-geary.md) and [Global Getis-Ord G](../../algorithms/statistics/global-getis-ord-g.md) lessons are supplementary companions added during research; neither is a separate entry in the original compendium. These are not all algorithms in the same sense. Keep the original grouping, then decide the right record type during research.

## Autocorrelation and local statistics

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Global: [Moran's I](../../algorithms/statistics/global-morans-i.md), [Geary's C](../../algorithms/statistics/gearys-c.md), join count, Lee's L, bivariate Moran's I, Mantel and partial Mantel tests | Global statistics / tests | 2 | Partial — related record exists; source-entry review pending |
| Local: [Local Moran's I (LISA)](../../algorithms/statistics/local-morans-i.md), [Getis-Ord Gi*](../../algorithms/statistics/getis-ord-gi-star.md), Moran scatterplot | Local statistics / diagnostic visualisation | 3 | Partial — related record exists; source-entry review pending |
| Summary geometry: mean center, median center, standard distance, standard deviational ellipse | Descriptive spatial summaries / geometric measures | 3 | Not checked — intake only |
| Inference: permutation and Monte Carlo tests, Bonferroni, FDR and Šidák correction, Dutilleul's modified t-test, spatial and block bootstrap | Inferential procedures / multiple-testing corrections / resampling | 3 | Not checked — intake only |
| Spatial eigenvector filtering (Moran eigenvectors), Spatial+, restricted spatial regression | Regression approaches / spatial dependence adjustments | 3 | Not checked — intake only |

## First audited clustering lesson

The [DBSCAN lesson](../../algorithms/statistics/dbscan.md) introduces core, border and noise points, the eps/min_samples parameters and the input-order policy for ambiguous border points. A tested O(n²) planar implementation and interactive notebook provide a small-data baseline; HDBSCAN, OPTICS and indexed large-data search remain open.

## Point pattern analysis

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Quadrat analysis, Clark-Evans, nearest neighbor index | Exploratory methods / spatial statistics | 3 | Not checked — intake only |
| [Ripley's K and L](../../algorithms/statistics/ripley-k.md); G, F and J functions; pair correlation function | Point-pattern summary functions | 3 | Partial — related record exists; source-entry review pending |
| Models: Poisson, Cox, Neyman-Scott, Gibbs and Strauss processes, log-Gaussian Cox processes, marked patterns | Stochastic point-process models | 3 | Not checked — intake only |
| Cluster tests: Besag-Newell, Tango, SaTScan scan statistics, elliptic and flexible shapes (FleXScan) | Cluster-detection tests / scan statistics | 3 | Not checked — intake only |
| Kernel density estimation: adaptive and variable bandwidth, Silverman and cross-validated bandwidth selection | Density estimation / bandwidth-selection methods | 3 | Not checked — intake only |
| Network K-function, network KDE (NKDE), SANET methods | Network-constrained point-pattern methods / software-method families | 3 | Not checked — intake only |

## First audited point-pattern lessons

The [planar Gaussian KDE lesson](../../algorithms/statistics/point-pattern-kde.md) explains the fixed-bandwidth Gaussian kernel, intensity units, projected-coordinate requirement and uncorrected study-window edge effect. A tested NumPy implementation and interactive notebook compare bandwidths and weighted events. The [Clark–Evans lesson](../../algorithms/statistics/clark-evans.md) compares observed nearest-neighbour spacing with a homogeneous Poisson reference, while explicitly withholding a significance claim because this baseline does not apply edge correction or calculate a test statistic. The [Ripley's K/L lesson](../../algorithms/statistics/ripley-k.md) compares pair counts across distance scales with both uncorrected and rectangular-window translation-corrected estimators. All four point-pattern/clustering lessons have tested implementations, intern walkthroughs and notebooks. Isotropic/border corrections, formal nearest-neighbour inference, inhomogeneous point-process models, adaptive bandwidths and network KDE remain open.

## Clustering and regionalization

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Density-based: DBSCAN, HDBSCAN, OPTICS, DENCLUE, density peaks, ST-DBSCAN, T-DBSCAN | Clustering algorithms | 3 | Not checked — intake only |
| Partitioning: k-means, k-medoids, CLARA, CLARANS, constrained and equal-size k-means | Clustering algorithms / constrained variants | 3 | Not checked — intake only |
| Hierarchical and grid: BIRCH, STING, CLIQUE, Ward, mean shift, affinity propagation, spectral, Gaussian mixtures, fuzzy c-means, self-organizing maps, growing neural gas, consensus and co-clustering | Clustering algorithms / model families / grid methods | 3 | Not checked — intake only |
| Spatially constrained: SKATER, REDCAP, AZP, Max-p, spatial LDA | Regionalisation algorithms / spatial clustering methods | 3 | Not checked — intake only |
| Geodemographic classification (OAC-style), principal components and factor analysis | Classification approaches / dimensionality reduction | 3 | Not checked — intake only |

## Regression and spatial econometrics

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Lag and error: SAR, CAR, spatial lag, spatial error, SLX, SDEM, SAC/SARAR, Spatial Durbin, Manski model | Spatial regression model families | 3 | Not checked — intake only |
| Local and varying coefficients: GWR, MGWR, GTWR, GW principal components, GW summary statistics, spatially varying coefficient models, GeoDetector | Local modelling methods / geographically weighted methods | 3 | Not checked — intake only |
| Diagnostics: LM-lag, LM-error and robust variants, Wald and LR tests, Moran's I on residuals, Chow and regime tests, Breusch-Pagan, Koenker, GWR significance tests | Model diagnostics / statistical tests | 3 | Not checked — intake only |
| Estimation: spatial GMM, spatial HAC standard errors, spatial panel and dynamic panel models, spatial probit, spatial Heckman, spatial quantile regression, spatial stochastic frontier, spatial SUR, hedonic regression, endogenous weights, Bayesian model averaging over weights | Estimators / regression models / inference methods | 4 | Not checked — intake only |
| Bayesian: BYM, INLA/SPDE, hierarchical CAR models, spatial Dirichlet process, Gaussian process mixtures | Bayesian spatial model families / computational frameworks | 4 | Not checked — intake only |

## Smoothing and outlier detection

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Empirical Bayes rate smoothing, head-banging, median polish | Smoothing / exploratory procedures | 4 | Not checked — intake only |
| Gaussian, Laplacian, median, bilateral and non-local means filters, anisotropic diffusion, total-variation denoising, guided filters | Image and spatial filtering methods | 4 | Not checked — intake only |
| Spatial outlier tests: Z-value, scatterplot approach, variogram cloud, isolation forest, spatial LOF, geographically weighted outliers | Outlier diagnostics / anomaly-detection methods | 4 | Not checked — intake only |

## Inequality, entropy and scale

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Spatial Gini, Theil, spatial entropy, segregation indices (dissimilarity, isolation) | Inequality and segregation measures | 4 | Not checked — intake only |
| Fractal dimension, lacunarity, Hurst exponent, multifractal analysis, scale-space theory, MAUP analysis | Scale measures / spatial analysis concepts | 4 | Not checked — intake only |
| Spatial spectral analysis: 2D periodogram, EOF, SSA and MSSA, canonical correlation, maximum covariance analysis, cross-spectral coherence, wavelet coherence, Hilbert-Huang transform | Spectral and multivariate analysis methods | 4 | Not checked — intake only |

## Decisions for the next pass

1. Separate global and local spatial autocorrelation from the models used to explain it.
2. Verify each named statistic, test and model against primary or authoritative sources.
3. State the spatial weights, null hypothesis, sampling assumptions and inferential procedure for statistical examples.
4. Distinguish clustering algorithms from regionalisation objectives and constraints.
5. Do not treat a model acronym as a complete specification; document its likelihood, spatial structure, estimation and assumptions.
6. Use synthetic data only when it makes the statistical property easier to see, and state how the data were generated.

## Bibliographic checks on selected spatial-statistics foundations

Publisher or authoritative bibliographic records were checked for these core references:

- Moran (1950), “Notes on continuous stochastic phenomena,” *Biometrika*, 37(1–2), 17–23, [10.1093/biomet/37.1-2.17](https://doi.org/10.1093/biomet/37.1-2.17).
- Geary (1954), “The contiguity ratio and statistical mapping,” *The Incorporated Statistician*, 5(3), [10.2307/2986645](https://doi.org/10.2307/2986645).
- Getis and Ord (1992), “The analysis of spatial association by use of distance statistics,” *Geographical Analysis*, 24(3), 189–206, [10.1111/j.1538-4632.1992.tb00261.x](https://doi.org/10.1111/j.1538-4632.1992.tb00261.x).
- Anselin (1995), “Local Indicators of Spatial Association—LISA,” *Geographical Analysis*, 27(2), 93–115, [10.1111/j.1538-4632.1995.tb00338.x](https://doi.org/10.1111/j.1538-4632.1995.tb00338.x).
- Ripley (1976), “The second-order analysis of stationary point processes,” *Journal of Applied Probability*, 13(2), 255–266, [10.2307/3212829](https://doi.org/10.2307/3212829).
- Ripley (1977), “Modelling spatial patterns,” *Journal of the Royal Statistical Society: Series B (Methodological)*, 39(2), 172–192, [10.1111/j.2517-6161.1977.tb01615.x](https://doi.org/10.1111/j.2517-6161.1977.tb01615.x).

This is a bibliographic metadata check for selected foundations, not a complete verification of all Section 2 source entries, inferential assumptions or software behaviour.
