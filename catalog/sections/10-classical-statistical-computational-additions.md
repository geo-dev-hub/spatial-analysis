# Section 10 — Additions: classical, statistical and computational methods

- **Original source section:** 10
- **Source pages:** 21–23
- **Source transcription:** [pages 21–25](../../source-inventory/pages-21-25.md)
- **Review state:** source entries extracted into this index; not every entry independently verified
- **Current canonical records:** none yet

The source describes these as further methods not listed in sections 1–9. Several entries are cross-cutting techniques that should connect to earlier topic families rather than be treated as entirely new subjects.

## Rasterization, curves and low-level geometry

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Line and polygon rasterization: Bresenham, DDA, Wu's anti-aliased line, scanline polygon fill, supercover lines | Rasterization algorithms | 21 | Captured; names not individually verified |
| Line clipping: Cohen-Sutherland, Liang-Barsky, Cyrus-Beck, Nicholl-Lee-Nicholl | Line clipping algorithms | 21 | Captured; names not individually verified |
| Line simplification variants: Reumann-Witkam, Lang, Opheim, Zhao-Saalfeld, Visvalingam-Whyatt with effective area | Simplification algorithms / variants | 21 | Captured; names not individually verified |
| Curves and smoothing: Chaikin corner cutting, Catmull-Rom, B-splines, NURBS, Bezier fitting (Schneider), Kalman and RTS smoothers | Curve construction / smoothing and filtering methods | 21 | Captured; names not individually verified |
| Geodesics on meshes: MMP exact geodesics, Chen-Han, fast marching on triangle meshes | Mesh geodesic algorithms / numerical methods | 21 | Captured; names not individually verified |
| Spherical and discrete global grids: ISEA3H, rHEALPix, DGGRID, hierarchical triangular mesh (HTM), hexagonal grid operations | Global grid systems / indexing structures / grid operations | 21 | Captured; names not individually verified |

## Time series and change detection

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Change-point detection: CUSUM, PELT, binary segmentation, BEAST, Bayesian online change-point detection | Change-point detection algorithms | 21 | Captured; names not individually verified |
| Trend and seasonality: STL, seasonal-trend decomposition, Prophet, Theil-Sen, Pettitt test, ARIMA, Kalman filtering of EO series | Time-series decomposition / tests / forecasting and filtering methods | 21 | Captured; names not individually verified |
| Hidden Markov models and Viterbi decoding for state sequences (map matching, land cover trajectories) | Probabilistic sequence models / decoding algorithm | 21 | Captured; names not individually verified |

## Forecast verification and nowcasting skill

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Fractions Skill Score, neighborhood verification, SAL (structure, amplitude, location), object-based verification (MODE) | Forecast verification metrics and methods | 21 | Captured; names not individually verified |
| ETS, POD, FAR, CSI, Brier skill score, ROC and AUC, CRPS decomposition, rank histograms | Forecast and probabilistic evaluation metrics | 21 | Captured; names not individually verified |
| Optical flow for advection: Lucas-Kanade, Farneback, DIS, variational optical flow | Motion estimation algorithms | 21 | Captured; names not individually verified |

## Spatial cross-validation and sampling

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| NNDM, kNNDM, buffered leave-one-out, spatial k-fold by clustering, blockCV, spatial+temporal leave-out | Spatial and spatiotemporal validation designs | 21 | Captured; names not individually verified |
| Adaptive and Bayesian sampling: Bayesian optimization on spatial fields, multi-armed bandits for survey design, adaptive cluster sampling, active learning for map validation | Adaptive sampling / active learning / survey design | 22 | Captured; names not individually verified |
| Kernel two-sample tests and domain divergence metrics for spatial distribution shift | Distribution-shift tests / domain comparison metrics | 22 | Captured; names not individually verified |

## Geophysical gridding and potential field processing

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Minimum curvature gridding, nearest-neighbor and triangulation gridding, kriging versus minimum curvature comparison | Gridding methods / interpolation comparison | 22 | Captured; names not individually verified |
| Potential fields: analytic signal, tilt derivative, Euler and Werner deconvolution, matched filtering, continuation, vertical and horizontal derivatives | Potential-field processing / geophysical interpretation methods | 22 | Captured; names not individually verified |
| Airborne EM and magnetotelluric inversion, seismic attribute analysis, receiver functions | Geophysical inversion and signal-analysis workflows | 22 | Captured; names not individually verified |

## Urban microclimate and energy

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Radiation and thermal comfort: SOLWEIG, UMEP, ENVI-met, mean radiant temperature, UTCI, PET | Microclimate software / thermal comfort measures | 22 | Captured; names not individually verified |
| Urban wind and CFD: RANS, LES, lattice Boltzmann for street canyons, pedestrian wind comfort | Computational fluid dynamics methods / urban wind assessment | 22 | Captured; names not individually verified |
| Stormwater and drainage: SWMM, 1D-2D coupled urban flood models, low-impact development siting | Drainage and flood models / site-selection methods | 22 | Captured; names not individually verified |
| Urban building energy modeling: archetype-based simulation, CityBES, shading and view-factor computation | Building energy simulation / geometric calculations | 22 | Captured; names not individually verified |

## Environmental monitoring and MRV

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Deforestation alerts: GLAD, RADD, forest loss detection from SAR and optical fusion | Monitoring systems / change-detection workflows | 22 | Captured; names not individually verified |
| Carbon accounting: forest carbon stock mapping, REDD+ MRV, soil carbon mapping, additionality and leakage analysis | Carbon estimation / monitoring, reporting and verification methods | 22 | Captured; names not individually verified |
| Methane and gas emissions: matched-filter plume detection, deep plume segmentation, integrated mass enhancement (IME), cross-sectional flux, Gaussian plume inversion | Plume detection / segmentation / emissions estimation | 22 | Captured; names not individually verified |
| Illegal fishing and maritime domain awareness: vessel behavior classification, gap detection in AIS, fishing effort mapping from SAR and AIS | Vessel analytics / anomaly detection / monitoring workflows | 22 | Captured; names not individually verified |
| Water quality and harmful algal bloom detection: chlorophyll, turbidity, cyanobacteria indices | Water-quality indicators / detection methods | 22 | Captured; names not individually verified |

## Population and social data

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Gridded population: top-down dasymetric, bottom-up microcensus, building-based disaggregation, settlement-level estimation | Population estimation / areal disaggregation methods | 22 | Captured; names not individually verified |
| Synthetic data for privacy: synthetic microdata, spatial k-anonymity for census, differential privacy for aggregates | Synthetic data generation / privacy methods | 23 | Captured; names not individually verified |
| Segregation and diversity: Reardon-Firebaugh multigroup indices, spatial exposure indices, Shannon and Simpson diversity | Segregation and diversity measures | 23 | Captured; names not individually verified |

## Decisions for the next pass

1. Link these additions to existing foundational records instead of duplicating them.
2. Verify named algorithms and abbreviations before creating canonical pages.
3. Keep forecast verification separate from model training and prediction.
4. Treat spatial cross-validation as a core validity requirement, not an optional evaluation detail.
5. Document the provenance and intended use of any population or environmental monitoring data.
