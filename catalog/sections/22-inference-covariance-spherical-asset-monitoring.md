# Section 22 — Additions: inference engines, covariance, spherical statistics, asset mapping, monitoring

- **Original source section:** 22
- **Source pages:** 45–47
- **Source transcription:** [pages 41–47](../../source-inventory/pages-41-47.md)
- **Review state:** intake extracted; source says names are from memory and mostly narrower variants or supporting machinery
- **Current canonical records:** none yet

**Source caution:** the compendium says these are memory-based and mostly narrower variants or supporting machinery. Verify exact names, software versions and mathematical conditions before creating canonical records.

## Inference engines for spatial models

| Source entry | Kind to review | Source page |
|---|---|---:|
| Sampling: Gibbs and Metropolis-within-Gibbs for CAR and SAR models, slice sampling, sequential Monte Carlo, pseudo-marginal methods | Bayesian sampling algorithms | 45 |
| Approximation: Laplace approximation, expectation propagation, variational Bayes, EM for spatial mixtures | Approximate inference and optimisation methods | 45 |
| Optimizers: L-BFGS, Adam, natural gradient for GP hyperparameters | Numerical optimisation methods | 45 |
| Probabilistic programming: Stan, NIMBLE, PyMC, INLA-style nested approximations | Probabilistic programming systems / inference frameworks | 45 |

## Covariance functions and basis expansions

| Source entry | Kind to review | Source page |
|---|---|---:|
| Stationary kernels: Matern, exponential, spherical, Gaussian, Cauchy, powered exponential, Wendland compact support | Covariance and kernel functions | 45 |
| Non-Euclidean validity: valid covariances on spheres (Gneiting), on networks (Anderes), graph kernels; why geodesic-distance Gaussian kernels can fail | Covariance validity theory / spherical and network kernels | 45 |
| Space-time covariances: Gneiting nonseparable class, Cressie-Huang, product-sum and metric models | Spatiotemporal covariance models | 45 |
| Bases: thin plate, B-splines and tensor products, wavelets, Slepian functions, Zernike, radial bases, multiresolution Haar, FRK bases, Moran basis | Basis functions / low-rank representations | 46 |

## Spherical and Riemannian statistics for location data

| Source entry | Kind to review | Source page |
|---|---|---:|
| Frechet mean on the sphere, spherical k-means, von Mises-Fisher mixtures, spherical kernel density estimation | Spherical statistics / clustering and density estimation | 46 |
| Spherical splines, geodesic regression, spherical Gaussian processes | Spherical interpolation and regression models | 46 |
| Geodesic operations on the ellipsoid: Karney polygon area, geodesic buffers, azimuthal equidistant buffers, antipodal and dateline handling | Ellipsoidal geodesic algorithms / geometry operations | 46 |

## Sensor artifact and geometry correction

| Source entry | Kind to review | Source page |
|---|---|---:|
| Destriping (Fourier, wavelet), noise estimation, MTF compensation, deblurring, jitter correction | Sensor artifact correction / image restoration | 46 |
| Line-scan and rolling-shutter geometric models, attitude and star tracker processing, boresight refinement | Sensor geometry and calibration workflows | 46 |
| Cloud removal with SAR guidance, SAR-optical fusion, hyperspectral destriping | Multisensor restoration and fusion | 46 |

## Road and roadway asset mapping

| Source entry | Kind to review | Source page |
|---|---|---:|
| Street-level extraction: traffic sign, pole and lane marking detection from street imagery and mobile mapping point clouds | Roadside asset detection and extraction | 46 |
| Sidewalk and curb ramp inventories, pavement distress detection, road roughness from accelerometers (IRI estimation) | Road and pedestrian infrastructure inventory / condition assessment | 46 |
| Crowdsourced street imagery pipelines (Mapillary style), map feature conflation with OSM | Crowdsourced mapping / conflation workflows | 46 |

## Utilities, rail and power line analytics

| Source entry | Kind to review | Source page |
|---|---|---:|
| Water networks: EPANET hydraulic simulation, leak detection, district metered area sectorization, water loss analysis | Water network simulation / leak detection and operational analysis | 46 |
| Power grid: power flow with geography, outage detection and restoration routing, vegetation encroachment along power lines from LiDAR, conductor sag and clearance analysis, pole detection | Power network modelling / outage and asset monitoring | 46 |
| Rail: track geometry from LiDAR, rail asset inventories, vegetation encroachment | Rail infrastructure mapping and monitoring | 46 |

## Engineering geodesy and structural monitoring

| Source entry | Kind to review | Source page |
|---|---|---:|
| Stockpile volume, earthwork cut and fill, construction progress monitoring, as-built versus design comparison | Engineering survey and construction monitoring workflows | 46 |
| Deformation monitoring: total station network adjustment, tunnel convergence, bridge and dam deformation, settlement monitoring from InSAR and GNSS | Geodetic adjustment / structural deformation monitoring | 46 |
| Terrestrial laser scanning registration, change detection on dense point clouds (M3C2) | Point-cloud registration and change-detection methods | 46 |

## Citizen science and presence-only modeling

| Source entry | Kind to review | Source page |
|---|---|---:|
| Observer effort and detectability models, eBird-style spatiotemporal exploratory models (STEM) | Observation-bias and detectability models | 47 |
| Presence-only bias correction: target-group background, bias grids, integrated SDMs, point process SDMs, iNaturalist-style data cleaning | Presence-only modelling / bias correction and data quality | 47 |
| Occupancy with false positives, camera trap density estimation, eDNA spatial sampling models | Occupancy and ecological sampling models | 47 |

## Fire danger and post-fire hazards

| Source entry | Kind to review | Source page |
|---|---|---:|
| Fire danger systems: Canadian FWI, KBDI, McArthur, NFDRS; fuel moisture estimation, fuel type mapping | Fire danger indices / fuel estimation and mapping | 47 |
| Burn severity (dNBR, RdNBR, RBR), post-fire debris flow models (USGS-style empirical models), smoke dispersion coupling | Burn severity metrics / post-fire hazard and dispersion models | 47 |

## Decisions for the next pass

1. Separate inference algorithms from the probabilistic programming systems that implement them.
2. Verify covariance validity under the stated geometry; do not assume a Euclidean kernel remains valid on a sphere or network.
3. Treat geodesic and ellipsoidal calculations with explicit reference ellipsoid, units and edge cases.
4. For asset mapping, state the asset definition, inventory completeness, positional accuracy and update frequency.
5. Treat monitoring and citizen-science data with clear observation-effort, bias and privacy assumptions.
