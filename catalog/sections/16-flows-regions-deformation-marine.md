# Section 16 — Additions: flows, regions, deformation, marine, biodiversity, humanitarian

- **Original source section:** 16
- **Source pages:** 33–34
- **Source transcription:** [pages 31–35](../../source-inventory/pages-31-35.md)
- **Review state:** source entries extracted into this index; not every entry independently verified
- **Current canonical records:** none yet

This section groups applied methods across spatial interaction, functional regions, classification, movement, geophysics, marine systems, biodiversity and humanitarian analysis.

## Spatial interaction models (advanced)

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Entropy-maximizing models (Wilson), production, attraction and doubly constrained forms, Poisson and negative binomial gravity models | Spatial interaction models / statistical specifications | 33 | Captured; names not individually verified |
| Competing destinations, intervening opportunities variants, spatial autocorrelation in flows (Griffith eigenvector filtering, LeSage-Pace origin-destination models) | Interaction models / flow autocorrelation and econometric methods | 33 | Captured; names not individually verified |
| Flow clustering and flow mapping: flow-based community detection, flow KDE, OD flow hotspot detection | Flow clustering / density estimation / hotspot methods | 33 | Captured; names not individually verified |

## Functional regions and urban boundaries

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Functional region delineation from flows: Intramax, CURDS, Louvain and Leiden on flow networks, commuting zone definition | Functional regionalisation algorithms / network clustering | 33 | Captured; names not individually verified |
| Urban boundary delineation: city clustering algorithm (CCA), DBSCAN on building density, percolation-based clustering, natural cities via head/tail breaks | Urban boundary detection / clustering and classification methods | 33 | Captured; names not individually verified |
| Home and work location inference from traces, activity space delineation, co-location and contact pattern extraction | Mobility inference / activity-space and contact analysis | 33 | Captured; names not individually verified |

## Classification schemes and aggregation

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Head/tail breaks, maximum breaks, geometric interval, standard deviation, box plot, pretty breaks, Dalenius-Hodges, optimal 1D k-means (ckmeans) | Classification and binning methods | 33 | Captured; names not individually verified |
| Zone design and aggregation: AMOEBA, automated zoning procedures, scale-effect analysis, variance by aggregation level | Spatial regionalisation / aggregation and scale analysis | 33 | Captured; names not individually verified |

## Cost surfaces and movement through terrain

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Anisotropic cost surfaces (Tobler hiking function, Naismith, Langmuir), path distance with vertical factors, backlink rasters | Cost-surface construction / terrain travel models | 33 | Captured; names not individually verified |
| Least-cost corridors, cost-weighted distance with turning penalties, energy-expenditure models for walking and loaded travel | Corridor analysis / movement cost models | 33 | Captured; names not individually verified |

## SAR geometry, InSAR time series and crustal deformation

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| SAR geometry: radiometric terrain correction (RTC), geocoding, multilooking, calibration, enhanced spectral diversity (ESD) coregistration | SAR geometry and preprocessing workflows | 34 | Captured; names not individually verified |
| Phase corrections: atmospheric phase screen estimation, GACOS and ERA5-based tropospheric correction, orbital ramp removal, DEM error correction | Interferometric phase correction methods | 34 | Captured; names not individually verified |
| Time-series InSAR workflows: SBAS variants, NSBAS, MintPy-style and LiCSBAS-style pipelines, GNSS-InSAR integration for 3D velocity decomposition | InSAR time-series processing / geodetic data integration | 34 | Captured; names not individually verified |
| Source modeling: Okada dislocation, Mogi source, finite fault slip inversion, elastic and viscoelastic deformation models | Geophysical source and deformation models | 34 | Captured; names not individually verified |

## Marine and fisheries spatial analysis

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| CPUE standardization (GAM and spatiotemporal models such as VAST-style vector autoregressive models), spatial stock assessment, fishing effort allocation | Fisheries statistical models / stock assessment / allocation | 34 | Captured; names not individually verified |
| Larval dispersal and ocean connectivity: Lagrangian tools (Parcels, OpenDrift), connectivity matrices, marine protected area network design | Particle tracking / connectivity analysis / reserve design | 34 | Captured; names not individually verified |
| Marine spatial planning with Marxan and Zonation, benthic habitat mapping from multibeam backscatter | Spatial planning software / habitat mapping workflows | 34 | Captured; names not individually verified |

## Biodiversity assessment and conservation planning

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| IUCN range metrics: extent of occurrence (convex hull, alpha hull), area of occupancy, range fragmentation indices | Range metrics / spatial biodiversity measures | 34 | Captured; names not individually verified |
| Essential biodiversity variables, protected area gap analysis, key biodiversity area delineation, species richness and endemism indices (weighted endemism, phylogenetic diversity) | Biodiversity indicators / conservation planning and assessment | 34 | Captured; names not individually verified |
| Wildlife crime and anti-poaching: green security games, learned patrol planning, risk maps from patrol data | Security games / patrol optimisation / risk mapping | 34 | Captured; names not individually verified |

## Climate analogs, velocity and refugia

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Climate analogs and novel climates (Mahalanobis distance based), climate velocity, climate-change refugia, bioclimatic envelope shifts | Climate similarity and velocity metrics / ecological modelling | 34 | Captured; names not individually verified |
| Land degradation analysis: RESTREND, NPP residual methods, desertification indicators, soil salinity mapping | Land degradation assessment / remote-sensing indicators | 34 | Captured; names not individually verified |

## Humanitarian, food security and conflict

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Relief facility location, humanitarian logistics routing, displacement camp mapping, tent and structure counting from imagery | Humanitarian location and routing / settlement mapping | 34 | Captured; names not individually verified |
| Food security: IPC-style analysis, FEWS NET-style outlooks, livelihood zone delineation, market integration and price transmission models | Food-security analysis / early-warning and regional economic methods | 34 | Captured; names not individually verified |
| Conflict analysis: ACLED-style event analysis, conflict diffusion models, forecasting systems such as ViEWS, spatial event clustering and early warning indicators | Event analysis / diffusion and forecasting models | 34 | Captured; names not individually verified |

## Decisions for the next pass

1. Define the spatial unit and temporal interval for flow and regionalisation methods.
2. Distinguish interaction models from observed flow datasets and from network clustering.
3. Record uncertainty and sensor limitations in deformation and marine applications.
4. Use conservation and humanitarian examples with transparent data provenance and careful privacy review.
5. Treat named products and tools as implementations or data sources, not interchangeable with the underlying method.
