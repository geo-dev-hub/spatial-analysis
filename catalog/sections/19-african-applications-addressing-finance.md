# Section 19 — Additions: African applications, addressing, finance, telecom, seismology, pitfalls

- **Original source section:** 19
- **Source pages:** 39–41
- **Source transcription:** [pages 36–40](../../source-inventory/pages-36-40.md) and [pages 41–47](../../source-inventory/pages-41-47.md)
- **Review state:** intake extracted; source says names and tools are from memory and require verification
- **Current canonical records:** none yet

**Source caution:** the compendium labels these names and tools as memory-based. Treat the regional applications as useful prompts for research, not verified descriptions of current African systems or a representative list of the continent.

## Applications common in East and Sub-Saharan Africa

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Desert locust and pest monitoring: habitat suitability from soil moisture and vegetation, swarm movement forecasting, eLocust-style field data fusion | Ecological suitability / movement forecasting / field-data workflows | 39 | Not checked — intake only |
| Index-based livestock and crop insurance: NDVI and rainfall index design, basis risk analysis, pasture condition mapping | Parametric insurance / index design / risk analysis | 39 | Not checked — intake only |
| Pastoral mobility analysis: herd movement tracks, seasonal corridor detection, water point and grazing access models | Movement analysis / corridor and accessibility modelling | 39 | Not checked — intake only |
| Disease mapping: malaria prevalence geostatistics (MAP-style), cholera and Rift Valley fever risk, health facility accessibility (AccessMod-style travel time models) | Disease mapping / risk modelling / accessibility workflows | 39 | Not checked — intake only |
| Informal transit: paratransit route mapping from GPS (digital matatu style GTFS), mobile-money and mobile-network data for mobility and poverty proxies | Transit network reconstruction / mobility analysis / socioeconomic proxies | 39 | Not checked — intake only |
| Water infrastructure: water point functionality prediction (WPDx-style data), borehole siting from geophysics and remote sensing | Infrastructure condition prediction / siting methods | 40 | Not checked — intake only |
| Drought early warning: VCI, SPI, soil moisture anomalies, food security outlook integration | Drought indicators / monitoring and early-warning workflows | 40 | Not checked — intake only |

## Addressing and location encoding

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Open Location Code (plus codes), geohash, what3words-style grids, S2 and H3 cell addresses | Location encoding systems / spatial indexing schemes | 40 | Not checked — intake only |
| Descriptive and landmark-based geocoding, building-based addressing, address-free geocoding for informal settlements | Geocoding approaches / addressing workflows | 40 | Not checked — intake only |
| Address generation from street segments and building footprints, address quality scoring | Address assignment / data quality methods | 40 | Not checked — intake only |

## Insurance, finance and risk transfer with geodata

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Parametric insurance design: trigger selection, index construction, basis risk quantification, cat bond trigger design | Insurance product and risk-model design | 40 | Not checked — intake only |
| Credit and risk models with geospatial features, property valuation (AVM with comparable selection by kNN and GWR) | Credit and risk models / automated valuation methods | 40 | Not checked — intake only |
| Exposure modeling: flood zone assignment, wind and quake exposure aggregation, portfolio accumulation analysis | Exposure assessment / portfolio risk workflows | 40 | Not checked — intake only |

## Telecom and network planning

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| RF planning: coverage prediction, propagation model calibration, cell planning, handover analysis, interference mapping | Radio network planning / propagation modelling | 40 | Not checked — intake only |
| Backhaul and fiber routing: least-cost corridors, ring design, last-mile network design | Telecommunications network design / routing optimisation | 40 | Not checked — intake only |
| Satellite internet coverage: constellation coverage, beam planning, link budget analysis | Satellite communications coverage and engineering analysis | 40 | Not checked — intake only |

## Seismology and earthquake early warning

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Earthquake location: Geiger method, HypoDD double-difference relocation, magnitude estimation, focal mechanism inversion | Earthquake location / relocation and source estimation | 40 | Not checked — intake only |
| Detection and phase picking: STA/LTA, template matching, PhaseNet, EQTransformer-style pickers | Signal detection / phase-picking models | 40 | Not checked — intake only |
| Tomography and noise methods: ambient noise tomography, receiver functions | Seismic imaging and signal-analysis methods | 40 | Not checked — intake only |
| Early warning: ElarmS, PLUM-style algorithms, GNSS-based rapid magnitude estimation, tsunami warning inversion | Early-warning systems / rapid estimation and inversion | 40 | Not checked — intake only |
| Volcanic monitoring: deformation, SO2 and thermal monitoring, failure forecast method for eruption forecasting | Multi-sensor monitoring / forecasting methods | 40 | Not checked — intake only |

## Atmospheric transport and source attribution

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Back trajectories (HYSPLIT), footprint models (STILT, FLEXPART), potential source contribution function (PSCF), concentration-weighted trajectory (CWT) | Atmospheric transport / receptor and source attribution methods | 41 | Not checked — intake only |
| Receptor models: PMF, chemical mass balance, source apportionment with spatial covariates | Receptor modelling / source apportionment | 41 | Not checked — intake only |
| Ionospheric and space weather: TEC mapping, scintillation indices, ionospheric correction models | Ionospheric mapping / space-weather measures and correction | 41 | Not checked — intake only |

## Acoustic and sensor-based spatial analysis

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Sound source localization: TDOA, beamforming, multilateration, acoustic indices for soundscape ecology | Acoustic localisation / signal processing / ecological measures | 41 | Not checked — intake only |
| Bird call and wildlife detection from acoustic arrays, passive acoustic monitoring networks | Acoustic classification / sensor network workflows | 41 | Not checked — intake only |
| Side-scan and sub-bottom sonar processing, seabed classification | Sonar processing / marine classification | 41 | Not checked — intake only |

## Pitfalls and diagnostics checklist for spatial analysis and GeoAI

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Data leakage through spatial autocorrelation, tile overlap and neighboring patches in random train-test splits | Validation failure modes / leakage diagnostics | 41 | Not checked — intake only |
| MAUP and ecological fallacy checks, edge and boundary effects, tile-boundary artifacts in segmentation | Spatial inference and image-boundary diagnostics | 41 | Not checked — intake only |
| Extrapolation outside covariate space, label shift between regions, temporal drift and sensor changes | Generalisation and distribution-shift diagnostics | 41 | Not checked — intake only |
| Confounding by spatial structure, residual autocorrelation checks, calibration across regions | Model diagnostics / spatial confounding and calibration | 41 | Not checked — intake only |
| Reporting practices: report spatial CV scheme, area of applicability, uncertainty maps, per-region metrics and class-wise area estimates | Reporting and evaluation standards | 41 | Not checked — intake only |

## Decisions for the next pass

1. Ground each regional example in local evidence and a clearly identified country, city or ecological region.
2. Avoid treating one East African or Sub-Saharan example as representative of all African contexts.
3. Verify the availability, licensing, date and coverage of regional datasets and products.
4. Apply privacy and safety review to mobile-money, telecom, health, pastoral and mobility data.
5. Treat the diagnostics checklist as a core quality standard across the whole collection.
