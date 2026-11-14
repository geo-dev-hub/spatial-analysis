# Section 10 algorithm-level completion register

This is the first algorithm-level reconciliation of the original Section 10 source (pages 21–22). It deliberately separates a named algorithm from the grouped source row that contains it. It is a working audit, not a claim that Section 10 or the compendium is complete.

**Status meanings**

- **Implemented / tested** — a corresponding executable implementation and tests are present in the repository. This does not by itself mean independent review or publication-ready completion.
- **Partial** — related code or a family lesson exists, but the named algorithm is absent, only one variant is implemented, or validation/learning material is incomplete.
- **Research / lesson only** — explanatory material exists, but no matching tested implementation is present.
- **Open** — no adequate algorithm-specific treatment has yet been verified.

A shared family lesson or notebook is not counted as a separate derivation for every child algorithm. Rights review and source-entry verification remain separate release checks.

## Rasterisation and low-level geometry — source page 21

| Source family | Child algorithm | Verified repository treatment | Status |
|---|---|---|---|
| Rasterisation | DDA line rasterisation | `implementations/python/rasterization/` implementation, tests and lab | Implemented / tested |
| Rasterisation | Bresenham line rasterisation | Same package; all-octant variant | Implemented / tested |
| Rasterisation | Wu anti-aliased line | Same package and tests | Implemented / tested |
| Rasterisation | Scanline polygon fill | Same package; centre-sampled even-odd fill | Implemented / tested |
| Rasterisation | Supercover line | Same package; closed-cell convention | Implemented / tested |
| Line clipping | Cohen–Sutherland | `implementations/python/line-clipping/`, tests and lab | Implemented / tested |
| Line clipping | Liang–Barsky | Same package, tests and lab | Implemented / tested |
| Line clipping | Cyrus–Beck | Same package; convex polygon window contract | Implemented / tested |
| Line clipping | Nicholl–Lee–Nicholl | Canonical-region transformations and slope-based boundary selection; randomized differential tests against Liang–Barsky | Implemented / tested candidate; primary-reference and numerical review pending |
| Line simplification | Reumann–Witkam | Consolidated `implementations/python/line-simplification/` implementation, tests and comparison lab; this pass added regression cases for repeated vertices and empty/singleton inputs across all six simplifiers | Implemented / tested candidate; independent reference comparison pending |
| Line simplification | Lang | Bounded look-ahead teaching implementation, tests and walkthrough added; vertex-count lookahead contract stated | Implemented / tested candidate; independent reference comparison pending |
| Line simplification | Opheim | Constrained moving-strip implementation with explicit half-width/min/max-radius contract and tests | Implemented / tested candidate; exact-reference variant comparison pending |
| Line simplification | Zhao–Saalfeld narrow sleeve | Sector-bound narrow-sleeve implementation, supporting-line tolerance tests and notebook | Implemented / tested candidate; other two variants and reference review pending |
| Line simplification | Visvalingam–Whyatt effective area | `implementations/python/line-simplification/` implementation and tests | Implemented / tested |
| Curves and smoothing | Chaikin corner cutting | `implementations/python/curves-smoothing/`, tests and notebook | Implemented / tested |
| Curves and smoothing | Catmull–Rom spline | Same package; uniform, centripetal and chordal parameterisations | Implemented / tested |
| Curves and smoothing | B-splines | de Boor evaluator, tests, walkthrough and spline notebook added | Implemented / tested candidate; reference review pending |
| Curves and smoothing | NURBS | Homogeneous de Boor evaluator, rational quarter-circle test and notebook added | Implemented / tested candidate; reference review pending |
| Curves and smoothing | Schneider Bezier fitting | Recursive cubic fitter with chord-length parameterisation, least-squares handles, Newton reparameterisation, tests, walkthrough and executable notebook | Implemented / tested candidate; reference and tolerance review pending |
| Curves and smoothing | Kalman smoother | Linear-Gaussian vector-state filter and RTS smoother; tests, walkthrough and notebook added | Implemented / tested candidate; model/reference review pending |
| Curves and smoothing | Rauch–Tung–Striebel smoother | Backward fixed-interval RTS pass added to tested Kalman package | Implemented / tested candidate; model/reference review pending |
| Mesh geodesics | Mitchell–Mount–Papadimitriou exact geodesics | Comparative method guide; no executable package verified | Research / lesson only |
| Mesh geodesics | Chen–Han exact geodesics | Comparative method guide; no executable package verified | Research / lesson only |
| Mesh geodesics | Fast marching on triangle meshes | Comparative method guide; no executable package verified | Research / lesson only |
| Discrete global grids | ISEA3H | Family guide; no algorithm implementation verified | Research / lesson only |
| Discrete global grids | rHEALPix | Family guide; no algorithm implementation verified | Research / lesson only |
| Discrete global grids | DGGRID | Software/tool, not a single algorithm; guide discusses it | Research / lesson only |
| Discrete global grids | Hierarchical triangular mesh (HTM) | Family guide; no algorithm implementation verified | Research / lesson only |
| Discrete global grids | Hexagonal grid operations | Family guide; no operation-specific implementation verified | Research / lesson only |

## Time series, change detection and state sequences — source page 21

| Source family | Child algorithm / method | Verified repository treatment | Status |
|---|---|---|---|
| Change points | CUSUM | Two-sided Page-style mean-shift implementation, tests and walkthrough added | Implemented / tested candidate; threshold calibration and reference review pending |
| Change points | Binary segmentation | Greedy SSE split implementation and tests added | Implemented / tested candidate; comparison review pending |
| Change points | PELT | Pruned exact SSE mean-shift implementation, brute-force partition test and walkthrough added | Implemented / tested candidate; independent reference review pending |
| Change points | BEAST | Family comparison guide; no matching implementation verified | Research / lesson only |
| Change points | Bayesian online change-point detection | Conjugate Gaussian-mean run-length recursion, tests and notebook added | Implemented / tested candidate; reference/model review pending |
| Trend / seasonality | STL decomposition | `implementations/python/stl-decomposition/` validated wrapper around statsmodels STL, reconstruction and input-contract tests, walkthrough and lab; not a from-scratch LOESS implementation | Implemented via documented reference dependency; independent numerical review pending |
| Trend / seasonality | Prophet | External software/model; family guide only | Research / lesson only |
| Trend / seasonality | Theil–Sen trend estimator | `implementations/python/theil-sen/` pairwise-median slope, irregular-time handling, outlier and input tests, walkthrough and lab | Implemented / tested candidate; independent reference review pending |
| Trend / seasonality | Pettitt test | `implementations/python/change-point-detection/` rank statistic, tie-aware tests, walkthrough and change-point lab; approximate p-value under independent-observation null | Implemented / tested candidate; reference calibration review pending |
| Trend / seasonality | ARIMA / seasonal ARIMA | `implementations/python/arima-forecasting/` statsmodels-backed ARIMA/SARIMA wrapper, forecast and interval outputs, synthetic tests, walkthrough and lab | Implemented via documented reference dependency; diagnostics and independent model review pending |
| Trend / seasonality | Kalman filtering of EO series | Family guide; no matching implementation verified | Research / lesson only |
| State sequences | Hidden Markov model (discrete model / filtering) | Viterbi package implements decoding, not HMM parameter estimation or full inference | Partial |
| State sequences | Viterbi decoding | `implementations/python/hmm-viterbi/`, tests, walkthrough and notebook | Implemented / tested |

## Forecast verification and motion — source page 21

| Source family | Child metric / algorithm | Verified repository treatment | Status |
|---|---|---|---|
| Spatial verification | Fractions Skill Score (FSS) | Regular-grid square-neighbourhood implementation, tests and scale notebook | Implemented / tested |
| Spatial verification | SAL | Guide discusses it; no matching implementation verified | Research / lesson only |
| Spatial verification | MODE object-based verification | Guide discusses it; no matching implementation verified | Research / lesson only |
| Categorical / probabilistic verification | ETS | Tested forecast-verification package | Implemented / tested |
| Categorical / probabilistic verification | POD | Tested forecast-verification package | Implemented / tested |
| Categorical / probabilistic verification | FAR | Tested forecast-verification package | Implemented / tested |
| Categorical / probabilistic verification | CSI | Tested forecast-verification package | Implemented / tested |
| Probabilistic verification | Brier score and Brier skill score | Tested forecast-verification package | Implemented / tested |
| Probabilistic verification | ROC and AUC | Tested forecast-verification package; tied-rank ROC AUC | Implemented / tested |
| Probabilistic verification | CRPS decomposition | Not implemented; ensemble CRPS score is now separate and tested | Open |
| Probabilistic verification | Rank histograms | Expected rank histogram with fractional tie handling, tests and notebook added | Implemented / tested candidate; calibration review pending |
| Optical flow | Lucas–Kanade | Single-scale dense local implementation, tests, walkthrough and synthetic translation notebook added | Implemented / tested candidate; benchmark/reference review pending |
| Optical flow | Farnebäck | OpenCV-backed dense wrapper, parameter contract and synthetic translation test in `implementations/python/optical-flow/` | Implemented via reference dependency; broader benchmark and independent validation pending |
| Optical flow | DIS | OpenCV DISOpticalFlow wrapper with preset/refinement parameters and synthetic translation test in `implementations/python/optical-flow/` | Implemented via reference dependency; broader benchmark and independent validation pending |
| Optical flow | Variational optical flow | Family guide; no matching implementation verified | Research / lesson only |

## Spatial validation and adaptive sampling — source pages 21–22

| Source family | Child method | Verified repository treatment | Status |
|---|---|---|---|
| Spatial validation | NNDM | `implementations/python/nndm/` greedy prediction-distance-matching LOO fold generator, tests and walkthrough; projected Euclidean teaching scope | Implemented candidate; reference-equivalence, geographic distances, scale/performance and full test execution remain open |
| Spatial validation | kNNDM | `implementations/python/knndm/` bounded KMeans/Euclidean candidate with tests and walkthrough; not an exact CAST port | Implemented candidate; reference-equivalence, full tests and geographic-distance variants remain open |
| Spatial validation | Buffered leave-one-out | One-test-point-per-fold implementation with exclusion tests added | Implemented / tested candidate; distance-design review pending |
| Spatial validation | Spatial k-fold by clustering | Deterministic farthest-first k-means grouping with whole-cluster folds and tests added | Implemented / tested candidate; geographic grouping review pending |
| Spatial validation | blockCV | External R package / method reference, not a Python algorithm to clone | Research / lesson only |
| Spatial validation | Spatial + temporal leave-out (strict LLTO) | `implementations/python/spatiotemporal-validation/` generates observed location/time test folds, excludes the held-out location and time from training through an explicit buffer set, and includes tests, walkthrough and lab notebook | Implemented / tested candidate; deployment-specific grouping and reference review pending |
| Adaptive sampling | Bayesian optimisation on spatial fields | GP-UCB candidate-site selection with stationary RBF GP, tests, walkthrough and notebook added | Implemented / tested candidate; hyperparameter and spatial-model review pending |
| Adaptive sampling | Multi-armed bandits for survey design | Generic UCB1 simulator and tests added; independent stationary arms only | Implemented / tested candidate; spatially correlated reward modelling remains open |
| Adaptive sampling | Adaptive cluster sampling | Network expansion from initial sample, tests, walkthrough and notebook added; estimator/inclusion probabilities remain separate | Implemented / tested candidate; design-based estimator review pending |
| Adaptive sampling | Active learning for map validation | One-round uncertainty-per-cost batch selector with minimum spatial separation and tests | Implemented / tested candidate; iterative model-update loop and sampling-design review pending |
| Distribution shift | Kernel two-sample tests / MMD | Unbiased Gaussian-kernel MMD, tests, walkthrough and notebook added | Implemented / tested candidate; spatial null design remains open |
| Distribution shift | Energy distance | Unbiased sample energy-distance statistic and tests added | Implemented / tested candidate; spatial null design remains open |
| Distribution shift | Domain-classifier divergence | `implementations/python/domain-classifier-shift/` standardised logistic-regression classifier with out-of-fold ROC AUC and balanced accuracy; optional StratifiedGroupKFold; tests, walkthrough and lab | Implemented / tested candidate; classifier/feature sensitivity and spatial grouping review pending |

## What this audit says right now

1. **There is real executable work already present.** The strongest Section 10 implementation clusters include rasterisation, four line-clipping algorithms, six line simplifiers (Douglas–Peucker, Visvalingam–Whyatt, Reumann–Witkam, Lang, Opheim and Zhao–Saalfeld), curve construction/fitting and smoothing, Viterbi decoding, CUSUM, binary segmentation, PELT mean-shift segmentation, forecast metrics and FSS. The line-simplification test suite was expanded in this pass to make threshold, degenerate-endpoint, repeated-vertex and short-input contracts more explicit.
2. **Several family guides are not algorithm completion.** Mesh geodesics, discrete global grids, change points, trend/seasonality, optical flow, adaptive sampling and distribution shift still need child-level development.
3. **Some apparent matches are deliberately marked partial.** Bezier evaluation is not Schneider fitting; Viterbi decoding is not a complete HMM estimation package; spatial cross-validation baselines are not NNDM/kNNDM.
4. **This is not yet a complete Section 10 ledger.** The original source also includes geophysical processing, microclimate, environmental monitoring, population methods and other families on pages 22–23. Those will be split into child records next. Sections 1–9 and 11–22 still need the same reconciliation.

## Immediate algorithm-first queue

1. Nicholl–Lee–Nicholl: implementation and differential tests are already present; complete the primary-reference and numerical review rather than creating another package.
2. Opheim and Zhao–Saalfeld: develop and compare each simplification algorithm separately rather than treating them as one generic simplifier.
3. B-splines and NURBS: derive basis evaluation and knot/weight behaviour before adding code.
4. BOCPD and BEAST: specify the probabilistic model, priors/hazard and computational strategy before implementation.
5. Mesh geodesics: choose a bounded reference reproduction and state the exact mesh assumptions before coding.

## Evidence consulted for the first reconciliation

- Original source transcription: [pages 21–25](../source-inventory/pages-21-25.md).
- Repository implementation and test files are linked in the corresponding package READMEs and test modules.
- Nicholl–Lee–Nicholl identity and scope: Nicholl, Lee & Nicholl (1987), “An efficient new algorithm for 2-D line clipping: Its development and analysis,” SIGGRAPH '87, DOI [10.1145/37401.37432](https://doi.org/10.1145/37401.37432); see also the [2022 line-clipping survey](https://www.mdpi.com/2313-433X/8/10/286) and [Brown University graphics notes](https://cs.brown.edu/media/filer_public/88/9c/889c4b64-6979-4d31-a4fe-3904a681b978/dasilva.pdf).


## 14 November 2026 — implementation update

Two additional algorithm families now have executable teaching baselines and learning artefacts:

- Line simplification: Reumann–Witkam and Lang added beside Douglas–Peucker and Visvalingam–Whyatt; package tests and intern walkthrough updated; comparison notebook added.
- Change points: CUSUM, binary segmentation and PELT for piecewise-constant mean/SSE added; tests include brute-force partition comparison for PELT; walkthrough and synthetic lab notebook added.

These are implementation candidates, not independently verified release completions. Reference-equivalence checks, notebook execution in CI, rights review and technical review remain open. Opheim, Zhao–Saalfeld, BOCPD and BEAST remain open algorithm tasks.


Additional update: B-spline and NURBS evaluation by de Boor has been added to the curves package, with polynomial and rational validation fixtures, a walkthrough and a dedicated notebook. Schneider fitting and Kalman/RTS smoothing remain separate, unimplemented methods.


Further implementation update: polynomial B-spline and rational NURBS evaluation (de Boor) plus linear-Gaussian Kalman filtering and RTS smoothing are now present in the curves package, with tests, walkthroughs and dedicated notebooks. Schneider's curve fitting remains open. These are implementation candidates pending CI and independent technical/reference review.


Bayesian online change-point detection has now been added as a bounded conjugate-Gaussian teaching model with run-length posterior, change probabilities, tests and a lab notebook. BEAST remains open.


## Additional Section 10 child record — potential-field derivatives

| Source page | Child algorithm / measure | Current treatment | Status |
|---|---|---|---|
| 22 | Spectral horizontal derivatives | Fourier differentiation operators on regular grids; exact periodic-cosine test | Implemented / tested candidate |
| 22 | Spectral first vertical derivative | Radial-wavenumber operator under explicit potential-field sign convention | Implemented / tested candidate |
| 22 | Analytic-signal amplitude | Derived from x, y and vertical derivatives; synthetic lab | Implemented / tested candidate |
| 22 | Tilt derivative | atan2(vertical derivative, total horizontal gradient); synthetic lab | Implemented / tested candidate |
| 22 | Euler deconvolution | Windowed least-squares homogeneity-equation solver; synthetic exact-recovery and rank-deficiency tests | Implemented / tested candidate; structural-index and field-model review pending |
| 22 | Werner deconvolution | Windowed linearized 2D single-thin-dike solver; seven-point default, centered/scaled least squares, source position/depth and model coefficients; synthetic recovery tests, walkthrough and lab | Implemented / tested candidate; thick-interface, regional-interference, multi-source and nonlinear-refinement variants remain open |
| 22 | Upward continuation | Spectral exponential attenuation `exp(-kh)` with known-mode attenuation tests and explicit periodic-grid contract | Implemented / tested candidate |
| 22 | Downward continuation | Tikhonov spectral inverse of upward continuation with positive regularisation, DC-mean preservation, low-frequency recovery and high-frequency damping tests | Implemented / tested candidate; regularisation selection and boundary/reference review pending |
| 22 | Matched filtering | Supplied-model equivalent-layer amplitude matched-bandpass decomposition; tests, walkthrough and synthetic lab; automatic radial-spectrum fitting and azimuthal filters remain open | Implemented / tested candidate; model fitting and boundary/reference review pending |

The package assumes a regular grid and periodic FFT boundary conditions. It is not an inversion or source-depth estimator. Technical review and reference-equivalence checks remain pending.


## Remaining Section 10 source families — pages 22–23

The source also includes applied methods, measures, software and workflows. These are recorded here so they are not silently dropped, but only the entries that are actual algorithms should receive from-scratch algorithm implementations.

| Source family | Child record | Primary kind | Current treatment | Status |
|---|---|---|---|---|
| Geophysical gridding | Minimum-curvature gridding | method / algorithm family | Thin-plate-spline minimum-bending-energy interpolation plus a separate fixed-perimeter discrete biharmonic solver minimizing squared five-point Laplacian curvature; both have tests and labs; neither is claimed as the full Briggs scattered-data algorithm | Partial — bounded discrete and variational baselines implemented; Briggs scattered-point constraints, regional initialization and iterative block method remain open |
| Geophysical gridding | Nearest-neighbour gridding | algorithm | `implementations/python/geophysical-gridding/` k-d-tree nearest assignment with optional maximum-distance masking, tests and lab | Implemented / tested candidate; sampling-distance and coordinate review pending |
| Geophysical gridding | Triangulation-based gridding | algorithm family | Delaunay triangulation with barycentric piecewise-linear interpolation, convex-hull fill contract and affine-plane tests | Implemented / tested candidate; triangulation robustness and sampling review pending |
| Geophysical gridding | Ordinary kriging | algorithm / estimator | Fixed exponential covariance ordinary-kriging system; prediction and conditional variance; caller supplies range, sill and nugget; tests, walkthrough and lab | Implemented / tested candidate; variogram fitting, parameter uncertainty and spatial validation pending |
| Geophysical gridding | Kriging versus minimum-curvature comparison | method comparison | Nearest, Delaunay, thin-plate spline and fixed-model ordinary kriging now share a synthetic lab; no fair spatially blocked benchmark or Briggs-equivalent minimum-curvature baseline yet | Partial — comparative experiment and matched validation design remain open |
| Potential fields | Analytic-signal amplitude | metric / attribute | Spectral derivative package and tests added | Implemented / tested candidate |
| Potential fields | Tilt derivative | metric / attribute | Spectral derivative package and tests added | Implemented / tested candidate |
| Potential fields | Horizontal derivatives | numerical operation | Spectral x/y derivatives and periodic-cosine test added | Implemented / tested candidate |
| Potential fields | First vertical derivative | numerical operation | Radial-wavenumber spectral operator and periodic-cosine test added | Implemented / tested candidate |
| Potential fields | Euler deconvolution | algorithm / estimator | Windowed least-squares homogeneity equation with synthetic parameter-recovery tests | Implemented / tested candidate; model assumptions and structural-index sensitivity review pending |
| Potential fields | Werner deconvolution | algorithm / estimator | Windowed linearized 2D single-thin-dike solver; synthetic recovery tests, walkthrough and lab | Implemented / tested candidate; thick-interface, regional-interference and multi-source variants remain open |
| Potential fields | Matched filtering | signal-processing method | Supplied-model equivalent-layer amplitude matched-bandpass decomposition; tests, walkthrough and synthetic lab | Implemented / tested candidate; automatic radial-spectrum fitting and azimuthal filters remain open |
| Potential fields | Upward continuation | spectral operation | `implementations/python/potential-field/` Fourier multiplier `exp(-kh)`; exact periodic-mode attenuation test | Implemented / tested candidate; boundary/reference review pending |
| Potential fields | Downward continuation | unstable inverse spectral operation | Tikhonov-regularised spectral inverse with positive regularisation and DC-mean preservation | Implemented / tested candidate; regularisation selection and boundary/reference review pending |
| Potential fields | Matched filtering | signal-processing method | No implementation verified | Open |
| Geophysical methods | Airborne EM inversion | inverse problem / workflow | No implementation verified | Research required |
| Geophysical methods | Magnetotelluric inversion | inverse problem / workflow | No implementation verified | Research required |
| Geophysical methods | Seismic attribute analysis | method family | Must split into named attributes before implementation | Research required |
| Geophysical methods | Receiver-function analysis | signal-processing workflow | No implementation verified | Research required |
| Urban microclimate | Mean radiant temperature (MRT) | metric | No verified treatment | Open |
| Urban microclimate | UTCI | metric / model | No verified treatment | Open |
| Urban microclimate | PET | metric / model | No verified treatment | Open |
| Urban microclimate | SOLWEIG / UMEP / ENVI-met | software | External maintained tools; integration/reproduction, not cloning | Research required |
| Urban wind | RANS | numerical model family | No verified implementation | Research required |
| Urban wind | LES | numerical model family | No verified implementation | Research required |
| Urban wind | Lattice Boltzmann street-canyon flow | numerical algorithm / model | No verified implementation | Open |
| Urban wind | Pedestrian wind comfort | applied assessment method | Needs criteria, exposure and validation context | Research required |
| Stormwater | SWMM | software / model | External software integration, not reimplementation | Research required |
| Stormwater | 1D–2D coupled urban flood models | model / workflow | No verified implementation | Research required |
| Stormwater | Low-impact development siting | spatial optimisation method | No verified implementation | Open |
| Building energy | Archetype-based simulation | workflow / model | No verified implementation | Research required |
| Building energy | Shading and view-factor computation | geometry / numerical method | No verified implementation | Open |
| Environmental monitoring | GLAD alerts | system / dataset / workflow | External alert product; verify versions and provenance | Research required |
| Environmental monitoring | RADD alerts | system / dataset / workflow | External alert product; verify versions and provenance | Research required |
| Forest monitoring | SAR–optical fusion for forest-loss detection | workflow / model | No reproducible workflow verified | Open |
| Carbon accounting | Forest carbon stock mapping | model / workflow | No verified implementation | Research required |
| Carbon accounting | REDD+ MRV | standard / workflow | Must identify normative framework and measurement components | Research required |
| Carbon accounting | Soil carbon mapping | model / workflow | No verified implementation | Research required |
| Carbon accounting | Additionality and leakage analysis | causal / accounting method | No verified implementation | Research required |
| Methane detection | Matched-filter plume detection | algorithm | `implementations/python/methane-emissions/` Gaussian template bank, normalized correlation score, amplitude estimate, synthetic injection tests and lab | Implemented / tested candidate; correlated-noise and operational retrieval validation pending |
| Methane detection | Deep plume segmentation | model / workflow | External model families and data needed | Research required |
| Methane quantification | Integrated mass enhancement (IME) | estimator / method | `ime_emission_rate` implements Q = IME × wind speed / characteristic length with unit-contract tests | Implemented / tested arithmetic baseline; physical input/retrieval validation pending |
| Methane quantification | Cross-sectional flux | estimator / method | `cross_sectional_flux` integrates concentration × signed normal wind × segment width; tests include reversed flow | Implemented / tested numerical baseline; sampling and uncertainty review pending |
| Methane quantification | Gaussian plume inversion | inverse model | `implementations/python/methane-emissions/gaussian_plume_inversion.py` fits non-negative Q and constant background for a fixed-source, vertically integrated Gaussian column plume; synthetic recovery tests, walkthrough and lab added | Implemented / tested candidate; source geometry and dispersion are fixed inputs, operational physics and uncertainty review pending |
| Maritime monitoring | Vessel behaviour classification | model / workflow | No verified implementation | Research required |
| Maritime monitoring | AIS gap detection | algorithm / data-quality method | `implementations/python/ais-gap-detection/` groups and sorts vessel tracks, flags long report intervals and excessive great-circle implied speeds, with tests, walkthrough and synthetic lab | Implemented / tested candidate; threshold calibration, reception coverage and operational review pending |
| Maritime monitoring | Fishing effort mapping from SAR and AIS | workflow / estimator | No reproducible workflow verified | Research required |
| Water quality | Chlorophyll indices | metric / index | Existing spectral-index package may overlap; source-specific review required | Partial |
| Water quality | Turbidity indices | metric / index | Existing spectral-index package may overlap; source-specific review required | Partial |
| Water quality | Cyanobacteria indices | metric / index | Existing spectral-index package may overlap; source-specific review required | Partial |
| Population | Top-down weighted dasymetric disaggregation | allocation algorithm | `implementations/python/dasymetric-allocation/` normalizes ancillary weights within each source zone, conserves source totals, supports an explicit eligibility mask and tested zero-weight fallback policy; tests, walkthrough and notebook added | Implemented / tested candidate; geometry/ancillary-data and independent accuracy review pending |
| Population | Bottom-up microcensus estimation | estimator / workflow | No verified implementation | Research required |
| Population | Building-based population disaggregation | algorithm / model | No verified implementation | Open |
| Population | Settlement-level population estimation | model / estimator | No verified implementation | Research required |
| Privacy | Synthetic spatial microdata generation | model / workflow | No verified implementation | Research required |
| Privacy | Spatial k-anonymity | privacy method | `implementations/python/spatial-privacy/spatial_k_anonymity.py` adaptive quadtree generalisation; disjoint groups each contain at least k records or are suppressed; tests, walkthrough and lab added | Implemented / tested candidate; location-only guarantee, attribute/linkage threat model and utility review pending |
| Privacy | Differential privacy for spatial aggregates | algorithm / privacy mechanism | `implementations/python/spatial-privacy/` user-level Laplace mechanism with bounded per-person cell contributions plus a basic sequential accountant that sums epsilon/delta across releases; tests, walkthroughs and labs | Implemented / tested candidate; adjacency, contribution governance, durable accounting and advanced composition review pending |
| Segregation / diversity | Reardon–Firebaugh multigroup entropy index implemented with tests and lab | Implemented / tested candidate; source-entry review pending |
| Segregation / diversity | Areal-unit group exposure matrix and isolation diagonal implemented; distance-weighted exposure not included | Implemented / tested candidate; spatial interaction review pending |
| Segregation / diversity | Shannon entropy implementation with zero-category handling and tests | Implemented / tested candidate |
| Segregation / diversity | Simpson concentration implementation with tests | Implemented / tested candidate |

This is the explicit remaining Section 10 backlog, not a claim that the listed software, models, metrics and workflows should all be cloned. Their correct deliverable may be a validated integration, derivation, metric implementation or research dossier according to the record-type and completion standards.


Ensemble verification update: empirical ensemble CRPS and an expected rank histogram with deterministic fractional tie handling are implemented, tested and documented in a dedicated lab. CRPS decomposition remains open; the CRPS score itself must not be mistaken for a full reliability-resolution-uncertainty decomposition.


## Geophysical gridding update — source page 22

Nearest-neighbour gridding and Delaunay piecewise-linear triangulation gridding now have a NumPy/SciPy teaching package, tests (including affine-plane reproduction), walkthrough and comparison notebook. These are not minimum-curvature gridding and do not extrapolate beyond their stated support.


Optical-flow update: a single-scale dense local Lucas–Kanade teaching implementation is now added with a known-translation test and notebook. Farnebäck, DIS and variational flow remain separate algorithm tasks.


Distribution-shift update: unbiased Gaussian-kernel MMD, energy distance and a reproducible exchangeability-based permutation test now have executable implementations, tests, walkthrough and a lab. The permutation procedure is explicitly not spatially valid under autocorrelation; block-aware inference remains open.


Opheim update: a constrained moving-strip variant is now implemented and tested. Its half-width and minimum/maximum radial-distance conventions are explicit; it does not claim to reproduce the road-network-specific improved Opheim variant. Zhao–Saalfeld remains open.


Zhao–Saalfeld update: the narrow-sleeve, original-vertex variant is implemented using intersecting angular sector bounds. Tests check straight-line reduction, direction changes, angle wrap, duplicate vertices and supporting-line tolerance. The wider sleeve with perturbed vertices and the middle trimming variant remain open.


Line clipping update: Nicholl–Lee–Nicholl is now implemented for axis-aligned rectangular windows, with explicit transformations into inside/left/top-left canonical cases and differential tests against Liang–Barsky. It is not a general convex polygon clipper.


Schneider fitting update: a piecewise-cubic fitter is now added with chord-length parameterisation, least-squares tangent handles, bounded Newton–Raphson refinement and recursive maximum-error splitting. It is explicitly distinct from Bezier curve evaluation.


## Population diversity and segregation update — source page 23

Shannon entropy, Simpson concentration, the Reardon–Firebaugh multigroup entropy index and an areal-unit group exposure matrix are now implemented with tests, derivation, walkthrough and synthetic notebook. The exposure statistic is not distance-weighted; spatially explicit exposure remains a separate task.


Spatial validation update: buffered leave-one-out and deterministic cluster-based k-fold splitters remain in the spatial-cross-validation package. Separate bounded NNDM LOO and kNNDM candidates now exist with tests and walkthroughs; exact reference equivalence and geographic-distance variants remain open.


Adaptive sampling update: adaptive cluster-sample network expansion is now implemented and tested. The realised sample is not a population estimator; inclusion probabilities and a valid design-based estimator remain separate open work.


Bayesian optimisation update: GP-UCB candidate-site selection is now implemented with a fixed-hyperparameter isotropic RBF Gaussian process. This is a bounded baseline; nonstationary kernels, barriers, costs, batch acquisition and model fitting remain open.


Bandit update: generic UCB1 selection and a stationary Gaussian-arm simulator are implemented and tested. It is not a spatially correlated bandit; contextual/spatial reward models remain open.


Active-learning update: a greedy spatially constrained uncertainty sampler is implemented for one-round candidate selection. It is not a full iterative active-learning loop and does not provide design-based inclusion probabilities.


## 14 November 2026 — spatiotemporal validation and privacy-accounting refinements

- Strict leave-location-and-time-out (LLTO) now has a tested fold generator, explicit train/test/buffer indices, intern walkthrough and visual notebook. It evaluates joint transfer to unseen location/time combinations; it is not NNDM, kNNDM, rolling-origin forecasting or a distance-buffer design.
- The sequential privacy accountant now normalizes release names before duplicate detection, preventing whitespace variants from reserving the same named release twice. A regression test covers the collision.


## 14 November 2026 — top-down dasymetric allocation

A bounded weighted dasymetric allocation baseline is now implemented. It allocates known source-zone totals to eligible target units using normalized non-negative ancillary weights and checks per-source conservation. The package does not perform polygon overlay or validate the ancillary proxy; bottom-up microcensus, settlement estimation and a full building-based population model remain separate open work.


## 14 November 2026 — Werner thin-dike deconvolution

The potential-field package now includes a bounded 2D single-thin-dike Werner deconvolution: moving-window linear least squares, coordinate centering/scaling, depth/position recovery, condition diagnostics, rejection reasons, synthetic recovery tests, walkthrough and notebook. It is not the complete later Ku–Sharp workflow; thick-interface derivative transforms, polynomial regional/interference terms, multi-source clustering and Marquardt refinement remain open.
