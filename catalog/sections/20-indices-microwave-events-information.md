# Section 20 — Additions: indices, microwave and thermal retrieval, event tracking, information theory, surveys

- **Original source section:** 20
- **Source pages:** 41–43
- **Source transcription:** [pages 41–47](../../source-inventory/pages-41-47.md)
- **Review state:** intake extracted; source says names are from memory and should be verified
- **Current canonical records:** [Triple collocation](../../methods/triple-collocation.md), with a tested NumPy baseline, intern walkthrough, exercise and visual notebook. The lesson covers the classical three-product error-variance estimator only; extended TC, error covariance estimation and product merging remain open. A researched [marine heatwave detection lesson](../../methods/marine-heatwave-detection.md) and tested single-series event detector cover the Hobday-style threshold-run and short-gap stage; seasonal climatology construction and gridded spatial feature tracking remain open.

**Source caution:** the source says coverage is broad and additions are increasingly narrow variants. Verify the name, formula, sensor requirements and intended use of every index or retrieval method.

## More spectral indices

| Source entry | Kind to review | Source page |
|---|---|---:|
| Vegetation: GNDVI, ARVI, GCI, MSAVI, OSAVI, WDRVI, NIRv, kNDVI, MTCI, REIP, TCARI, CIgreen, CIrededge | Spectral indices | 41 |
| Pigments and stress: PSRI, ARI, CRI, SIPI, PRI, NDII, NMDI | Spectral indices | 41 |
| Soil, residue and minerals: BSI, NDTI, STI, CAI (crop residue), clay mineral ratio, iron oxide ratio, ferrous iron index, ASTER mineral indices | Spectral indices / mineral retrieval ratios | 41 |

## Thermal and land surface temperature

| Source entry | Kind to review | Source page |
|---|---|---:|
| Emissivity: temperature-emissivity separation (TES), NDVI-threshold emissivity | Emissivity estimation methods | 42 |
| LST algorithms: mono-window, single-channel, split-window; surface urban heat island intensity metrics | Land-surface temperature retrieval / urban heat measures | 42 |
| Thermal sharpening and downscaling: DisTrad, TsHARP, regression-based and deep learning LST downscaling | Thermal image sharpening / spatial downscaling methods | 42 |

## Microwave and radar retrieval models

| Source entry | Kind to review | Source page |
|---|---|---:|
| Backscatter models: Water Cloud Model, Oh, Dubois, IEM, AIEM; change-detection soil moisture (TU Wien style), vegetation optical depth | Radar backscatter and soil-moisture retrieval models | 42 |
| Forest structure: RVoG, PolInSAR forest height, P-band biomass retrieval | Radar interferometry / forest structure retrieval | 42 |
| Radiometry: tau-omega model (SMAP, SMOS retrievals), AMSR2 snow water equivalent, GPROF-style rain retrieval | Passive microwave retrieval models | 42 |
| Ocean radar: CMOD5-type wind retrieval, SAR wave spectra, delay-Doppler altimetry | Ocean wind and wave retrieval / altimetry | 42 |

## Product validation and merging without ground truth

| Source entry | Kind to review | Source page |
|---|---|---:|
| Triple collocation and extended triple collocation, error covariance estimation, signal-to-noise ratio of products | Product validation / error estimation | 42 |
| Precipitation merging: gauge-satellite kriging blending (CHIRPS and MSWEP style), conditional merging, optimal interpolation | Data fusion / precipitation estimation | 42 |

## Nighttime lights processing

| Source entry | Kind to review | Source page |
|---|---|---:|
| Saturation correction, blooming correction, DMSP-VIIRS harmonization, background and noise removal, lights-per-capita normalization | Radiometric correction / sensor harmonisation / derived indicators | 42 |

## Climate and ocean event detection and tracking

| Source entry | Kind to review | Source page |
|---|---|---:|
| Event definition: marine heatwaves (Hobday), heatwave and cold spell definitions, drought events via run theory, percentile thresholds | Event definitions / threshold and run-theory methods | 42 |
| Space-time tracking: 3D connected component labeling, storm and cyclone tracking (TempestExtremes-style), atmospheric river detection (IVT-based, ARTMIP), blocking and jet stream detection, monsoon onset indices | Spatiotemporal tracking / detection methods / climate indices | 42 |
| Ocean: mesoscale eddy tracking, upwelling indices, Lagrangian coherent structures (FTLE), geostrophic currents from sea surface height, Ekman and Stokes drift | Ocean feature tracking / dynamical and transport measures | 42 |

## Information-theoretic and causal methods for spatiotemporal systems

| Source entry | Kind to review | Source page |
|---|---|---:|
| Entropy measures: Shannon, Renyi, Tsallis, sample entropy, permutation entropy, spatial entropy variants | Information-theoretic measures | 42 |
| Dynamics: recurrence plots and recurrence quantification analysis, Lyapunov exponents | Nonlinear time-series analysis methods | 42 |
| Causality: Granger causality, transfer entropy, convergent cross mapping, causal networks from gridded fields (PCMCI-style), teleconnection graphs | Causal and information-flow methods | 42 |

## Phylogeography and survey sampling

| Source entry | Kind to review | Source page |
|---|---|---:|
| Motif and pattern discovery: SAX, shapelets, matrix profile, motif discovery in spatial time series | Time-series representation and motif discovery | 43 |
| Continuous phylogeographic diffusion (BEAST-style), BSSVS for spread route inference, genomic epidemiology with spatial covariates | Phylogeographic inference / genomic epidemiology | 43 |
| Bayesian reproduction number maps, spatial Rt estimation, nowcasting with reporting delays, wastewater surveillance spatial models | Epidemic estimation / spatial nowcasting | 43 |
| Survey sampling: EPI cluster sampling, LQAS, sampling frames from building footprints and imagery, DHS cluster GPS displacement and correction | Survey designs / sampling-frame construction / positional adjustment | 43 |

## Urban 3D and growth

| Source entry | Kind to review | Source page |
|---|---|---:|
| Building height from radar and stereo, floor count inference, urban volume estimation, 3D city model generation from oblique imagery | 3D urban measurement and reconstruction | 43 |
| Urban growth boundary delineation, urban expansion modeling with spatial constraints | Urban growth analysis / constrained modelling | 43 |

## Decisions for the next pass

1. Verify index formulae against sensor bands, atmospheric assumptions and intended targets.
2. Record calibration, validation and uncertainty separately from the retrieval method.
3. Distinguish event definition, event detection and event tracking.
4. State temporal resolution and observation gaps for climate and ocean event examples.
5. Treat causal language carefully: temporal association or information transfer does not by itself establish causal identification.
