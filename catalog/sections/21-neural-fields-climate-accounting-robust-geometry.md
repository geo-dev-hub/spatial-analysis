# Section 21 — Additions: neural fields, climate ML, accounting, robust geometry, semantic maps, integrity

- **Original source section:** 21
- **Source pages:** 43–45
- **Source transcription:** [pages 41–47](../../source-inventory/pages-41-47.md)
- **Review state:** intake extracted; source says names are from memory and should be verified
- **Current canonical records:** [Exact orientation predicate](../../methods/exact-orientation-predicate.md), with a rational-arithmetic reference implementation, near-degenerate regression test, intern walkthrough, exercise and visual notebook. This is not an implementation of Shewchuk's adaptive expansion predicates; exact/adaptive production kernels and robust constructions remain open.

**Source caution:** the source describes these as narrower variants and adjacent fields. Verify named models, standards and software before citation.

## Neural fields and implicit representations

| Source entry | Kind to review | Source page |
|---|---|---:|
| Coordinate networks: SIREN, Fourier feature networks, hash-grid encodings (Instant-NGP style), location-conditioned INRs | Coordinate-based neural representations | 43 |
| Satellite NeRF and splatting: S-NeRF, EO-NeRF, SatNeRF, Gaussian splatting for satellite imagery, shadow-aware radiance fields | Neural rendering and scene representations | 43 |
| Implicit DEMs and climate field compression: neural compression of reanalysis and model output, continuous-resolution surface models | Implicit spatial fields / neural compression | 43 |

## Climate and Earth-system machine learning

| Source entry | Kind to review | Source page |
|---|---|---:|
| Emulators and spherical operators: SFNO, ACE-style atmosphere emulators, ocean emulators, subseasonal and seasonal ML forecasts | Climate and Earth-system emulators / spherical architectures | 43 |
| Learned data assimilation: diffusion-based assimilation, ensemble-free assimilation with generative priors | Data assimilation methods using generative models | 43 |
| ML parameterizations: subgrid and convection schemes, stochastic parameterizations, hybrid ML-physics coupling stability checks | Learned physical parameterisations / hybrid modelling | 43 |

## Land change accounting

| Source entry | Kind to review | Source page |
|---|---|---:|
| Intensity analysis (Aldwaik-Pontius), net versus swap change, gain-loss decomposition, transition matrices, trajectory analysis | Land-change accounting methods | 44 |
| Legend harmonization and crosswalks (LCCS-style), class hierarchy mapping, semantic harmonization across land cover products | Classification harmonisation / legend crosswalks | 44 |
| Map comparison metrics: Cramer's V, mean absolute error of areas, Pontius quantity and allocation measures | Map comparison and change-accounting metrics | 44 |

## Ecosystem accounting

| Source entry | Kind to review | Source page |
|---|---|---:|
| SEEA EA extent and condition accounts, ecosystem service supply-use tables, natural capital valuation, spatial service flow models | Environmental-economic accounting framework / spatial valuation and flow models | 44 |

## Urban design analytics

| Source entry | Kind to review | Source page |
|---|---|---:|
| Density metrics (FSI, GSI, Spacematrix), view corridor and view shed analysis, daylight and sunlight-hour computation | Urban form metrics / visibility and solar analysis | 44 |
| Transit-oriented development indices, street connectivity and block morphology metrics, urban form classification (morphological tessellation) | Urban design indicators / morphology and classification methods | 44 |

## Robust geometric computation

| Source entry | Kind to review | Source page |
|---|---|---:|
| Exact and adaptive predicates (Shewchuk), exact arithmetic, interval arithmetic, floating-point robustness in overlay and triangulation | Robust predicate and arithmetic methods | 44 |
| Snapping, tolerance handling, topological robustness, simulation of simplicity, precision models in JTS and GEOS | Robust geometric computation / precision strategies / implementation behaviour | 44 |

## Time-dependent datums and vertical reference

| Source entry | Kind to review | Source page |
|---|---|---:|
| Dynamic datums, plate motion models, ITRF realizations and epochs, NAD83 epoch handling, HTDP and NADCON transformations | Dynamic reference frames / datum transformations | 44 |
| Vertical datums: geoid-based heights (GEOID18-style), VERTCON, tidal datums, ellipsoidal-to-orthometric conversion | Vertical reference systems / height transformations | 44 |
| Velocity field interpolation for coordinate updates | Geodetic interpolation / coordinate epoch update | 44 |

## Semantic maps and spatial AI for robotics and AR

| Source entry | Kind to review | Source page |
|---|---|---:|
| 3D scene graphs (Hydra-style), topological and hierarchical maps, semantic SLAM, open-vocabulary mapping (ConceptFusion, CLIP-Fields, VLMaps) | Scene representations / semantic mapping and SLAM | 44 |
| Visual positioning systems, geo-anchors, street-level localization for AR, digital twin synchronization | Visual localisation / AR and digital-twin workflows | 44 |
| Autonomous driving maps: lane-level HD maps, map change detection, crowdsourced mapping, lidar map matching with NDT, road marking extraction | HD mapping / map maintenance / point-cloud matching | 44 |

## GNSS integrity and location verification

| Source entry | Kind to review | Source page |
|---|---|---:|
| Spoofing and jamming detection, signal authentication, anomaly detection in pseudorange and Doppler, integrity monitoring | GNSS signal integrity and anomaly detection | 45 |
| Crowdsourced and proof-of-location verification, mock-location detection, cross-sensor consistency checks | Location verification / sensor consistency and fraud detection | 45 |

## Geology and geoscience machine learning

| Source entry | Kind to review | Source page |
|---|---|---:|
| Lithology classification from remote sensing and geophysics, geological map generation, stratigraphic and basin modeling | Geological mapping / classification and modelling | 45 |
| Thermochronology and geochronology spatial analysis, mineral deposit modeling with weights of evidence and neural nets | Geochronological analysis / mineral prospectivity modelling | 45 |

## Maritime and aviation analytics

| Source entry | Kind to review | Source page |
|---|---|---:|
| Ship-to-ship transfer detection, loitering and rendezvous detection, port call inference, trade flow estimation from AIS, vessel emissions inventories | Maritime behaviour and event analysis / emissions inventory | 45 |
| ADS-B trajectory clustering, holding pattern detection, aircraft emissions inventories, contrail detection from satellite imagery | Aviation trajectory analysis / emissions and remote-sensing detection | 45 |

## Decisions for the next pass

1. Verify the original publication and exact implementation before citing model names.
2. For robust geometry, explain predicates, constructions, precision models and topology as distinct concerns.
3. For dynamic datums, state the reference-frame realisation and coordinate epoch.
4. Keep accounting definitions and map-change metrics tied to their stated framework.
5. Treat GNSS integrity and proof-of-location as safety and security topics with carefully scoped claims.
