# Section 12 — Additions: signal processing, GNSS, regional science, resilience

- **Original source section:** 12
- **Source pages:** 24–26
- **Source transcription:** [pages 21–25](../../source-inventory/pages-21-25.md) and [pages 26–30](../../source-inventory/pages-26-30.md)
- **Review state:** source entries extracted into this index; the source describes these as methods borrowed from adjacent fields
- **Current canonical records:** none yet

The source explicitly frames these as methods from adjacent fields that spatial analysts regularly borrow. That is useful context: explain the original method first, then show what changes when it is applied to spatial data.

## Smoothing and semiparametric spatial models

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| GAM and GAMM with spatial smooths (thin plate, Duchon splines, soap film smoothers), Bayesian P-splines | Generalised additive models / spatial smoothing bases | 25 | Not checked — intake only |
| Penalized spatial regression: geographically weighted LASSO, spatial LASSO, fused LASSO on graphs, spatially varying coefficients with regularization | Regularised regression methods / graph penalties | 25 | Not checked — intake only |
| Intensity estimation: Voronoi and Delaunay-based estimators, STKDE (space-time KDE), prospective hotspot mapping | Spatial intensity estimators / hotspot methods | 25 | Not checked — intake only |
| Palm distributions, nearest neighbor distance distributions, inhomogeneous K and pair correlation functions | Point-process summary statistics | 25 | Not checked — intake only |

## Matrix and tensor methods for spatial data

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| NMF, ICA, MAF (maximum autocorrelation factors), dictionary learning, sparse coding, compressive sensing | Matrix factorisation / representation and signal-processing methods | 25 | Not checked — intake only |
| Tensor decomposition: CP, Tucker, tensor train; low-rank spatiotemporal completion | Tensor factorisation / completion methods | 25 | Not checked — intake only |
| Kalman variants: EKF, UKF, ensemble square-root filters, RTS smoothing, particle smoothing | State estimation and smoothing algorithms | 25 | Not checked — intake only |

## GNSS and geodetic adjustment

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Ambiguity resolution (LAMBDA), cycle slip detection, ionosphere-free and geometry-free combinations, PPP-AR | GNSS ambiguity and signal-processing methods | 25 | Not checked — intake only |
| Multipath mitigation, RAIM and fault detection, Baarda data snooping, least squares collocation | GNSS error mitigation / integrity monitoring / geodetic estimation | 25 | Not checked — intake only |
| Time transfer, clock modeling, kinematic positioning with INS integration (loosely and tightly coupled) | Timing and positioning models / sensor-fusion architectures | 25 | Not checked — intake only |

## Sensor calibration and image quality

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Vicarious and cross-sensor radiometric calibration, MTF estimation, GIQE and NIIRS image quality scoring | Calibration methods / image-quality measures | 25 | Not checked — intake only |
| Perceptual hashing and content-based image retrieval for EO archives, near-duplicate tile detection | Image retrieval / deduplication methods | 25 | Not checked — intake only |
| Lossy and learned compression for imagery (neural codecs), rate-distortion evaluation for downstream tasks | Compression methods / rate-distortion evaluation | 25 | Not checked — intake only |

## SAR and polarimetric deep learning

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Deep despeckling, SAR ship detection, SAR target recognition (ATR), polarimetric feature learning | Deep learning methods for radar imagery | 25 | Not checked — intake only |
| Cross-modal SAR-optical matching, SAR image registration, interferogram denoising networks | Multimodal matching / registration / denoising models | 25 | Not checked — intake only |

## Quantitative spatial economics and regional science

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Garin-Lowry and Lowry models, input-output and spatial CGE models, quantitative spatial equilibrium (Rosen-Roback style) | Regional economic models / spatial equilibrium frameworks | 26 | Not checked — intake only |
| Gravity trade models (PPML estimation), market access, spatial price equilibrium | Trade and interaction models / estimation methods | 26 | Not checked — intake only |
| Regional convergence analysis, spatial Markov chains, LISA transitions, spatial dynamics of income distributions | Regional convergence and spatial transition analysis | 26 | Not checked — intake only |

## Network resilience and infrastructure risk

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Critical node and edge detection, percolation on road networks, cascading failure models | Network vulnerability and resilience analysis | 26 | Not checked — intake only |
| Interdependent infrastructure modeling, vulnerability and fragility curves, HAZUS-style loss estimation | Infrastructure risk models / loss estimation | 26 | Not checked — intake only |
| Reliability analysis for networks (Monte Carlo, minimal cut sets), post-disaster restoration scheduling | Reliability analysis / optimisation and scheduling | 26 | Not checked — intake only |

## Computational geometry for districting and partitioning

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Power diagrams, centroidal Voronoi tessellation (Lloyd's algorithm), capacity-constrained Voronoi, semi-discrete optimal transport | Geometric partitioning / tessellation / optimal transport methods | 26 | Not checked — intake only |
| Balanced partitioning with compactness constraints, graph partitioning for equal-population districts | Constrained spatial and graph partitioning | 26 | Not checked — intake only |

## Climate analysis and attribution

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Teleconnection indices, regime detection, pattern scaling, ensemble weighting of CMIP models | Climate indices / regime and ensemble analysis | 26 | Not checked — intake only |
| Extreme event attribution, detection and attribution, return level estimation with covariates | Climate attribution / extreme-value analysis | 26 | Not checked — intake only |
| Multivariate bias correction (MBCn), spatial coherence-preserving downscaling (Schaake shuffle, ECC) | Bias correction / spatial downscaling methods | 26 | Not checked — intake only |

## Terrain traversability and off-road mobility

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Traversability estimation from LiDAR and imagery, rover path planning, slope and roughness cost maps | Terrain classification / robotics path planning / cost-surface methods | 26 | Not checked — intake only |
| Soil-vehicle interaction models, swarm and multi-robot coverage planning | Physical interaction models / multi-agent planning | 26 | Not checked — intake only |

## Decisions for the next pass

1. Identify which methods are borrowed from signal processing, statistics, geodesy, economics or network science.
2. Preserve the original domain assumptions when adapting a method to spatial data.
3. Verify abbreviations and named procedures before assigning stable records.
4. Keep resilience, regional economics and geodetic adjustment distinct despite their shared mathematical tools.
5. Connect these methods to the relevant foundations in sections 1–9.
