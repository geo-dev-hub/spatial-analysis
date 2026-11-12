# Section 14 — Additions: databases, graphics, morphology, hazards, inventory, cartographic math

- **Original source section:** 14
- **Source pages:** 28–30
- **Source transcription:** [pages 26–30](../../source-inventory/pages-26-30.md)
- **Review state:** source entries extracted into this index; not every entry independently verified
- **Current canonical records:** none yet

This section combines spatial database internals, graphics algorithms, image morphology, accessibility, hazard models, inventory methods and cartographic mathematics. Keep system internals distinct from the algorithms they support.

## Spatial database and distributed systems internals

| Source entry | Kind to review | Source page |
|---|---|---:|
| R-tree node split heuristics (linear, quadratic, R*), bulk loading (Nearest-X, Hilbert packing, STR, OMT), buffer trees, LSM-based spatial indexes | Spatial index structures / split and bulk-loading algorithms | 29 |
| PostgreSQL index types for spatial data: GiST, SP-GiST, BRIN; time-partitioned spatial tables | Database index types / storage and partitioning strategies | 29 |
| Distributed spatial joins: broadcast joins, quadtree and KDB-tree partitioning, skew handling, Z-order partitioning, DITA and Simba-style trajectory engines | Distributed join strategies / partitioning / trajectory processing systems | 29 |
| Streaming spatial analytics: continuous range queries, sliding-window geofencing, incremental kNN maintenance | Stream-processing queries / incremental spatial algorithms | 29 |

## 3D graphics algorithms used in geospatial analysis

| Source entry | Kind to review | Source page |
|---|---|---:|
| Ray-triangle intersection (Moller-Trumbore), BVH construction with surface area heuristic, kd-tree ray traversal | Geometric intersection / acceleration structures / traversal algorithms | 29 |
| Frustum and occlusion culling, level-of-detail selection, shadow mapping and shadow volumes for city shadow analysis | Rendering and visibility algorithms | 29 |
| Photon mapping and radiosity for urban radiation, sky-view and sunlight-hours computation on 3D city models | Global illumination / urban environmental analysis | 29 |
| IFC to CityGML conversion, scan-to-BIM, point cloud to BIM, BIM-GIS integration, 3D utility network mapping | Data conversion / reconstruction and integration workflows | 29 |

## Mathematical morphology and image structure

| Source entry | Kind to review | Source page |
|---|---|---:|
| Erosion, dilation, opening, closing, hit-or-miss, geodesic reconstruction, granulometry | Morphological operations | 29 |
| Component trees: max-tree, min-tree, alpha-tree, attribute filters, area and shape openings | Image data structures / connected filtering methods | 29 |
| Thinning and skeletonization (Zhang-Suen), Moore neighbor and Suzuki contour tracing, two-pass connected components | Skeletonisation / contour tracing / connected-component algorithms | 29 |
| Interactive segmentation: GrabCut, random walker, seeded region growing | Interactive segmentation algorithms | 29 |
| Morphological spatial pattern analysis (MSPA) for habitat structure | Landscape pattern analysis method | 29 |

## Accessibility and public health catchments

| Source entry | Kind to review | Source page |
|---|---|---:|
| Floating catchment variants: E2SFCA, 3SFCA, M2SFCA, G2SFCA, KD2SFCA | Accessibility measures / floating catchment methods | 29 |
| Travel-time decay functions (Gaussian, power, kernel density), multimodal accessibility, spatial mismatch indices | Accessibility modelling / decay functions / equity measures | 29 |
| Disease mapping extensions: Leroux CAR, Knorr-Held space-time interaction models, age standardization, Poisson-gamma models | Disease mapping and spatiotemporal model families | 29 |
| Cluster tests for case data: Cuzick-Edwards, Whittemore, spatial scan with covariates | Spatial epidemiology tests | 29 |

## Mass movement and volcanic runout

| Source entry | Kind to review | Source page |
|---|---|---:|
| Rockfall trajectory simulation (CRSP, Rockyfor3D), debris flow runout (RAMMS, r.avaflow), energy cone and energy line models | Mass-movement simulation / empirical runout models | 29 |
| Pyroclastic flow and lahar models (TITAN2D, LaharZ), lava flow models (MAGFLOW, probabilistic path models) | Volcanic flow simulation / probabilistic runout models | 30 |
| Tsunami inundation and runup coupling, coastal landslide hazard | Coastal and tsunami hazard modelling | 30 |

## Precision agriculture and forest inventory

| Source entry | Kind to review | Source page |
|---|---|---:|
| Management zone delineation (fuzzy c-means, MZA), variable-rate prescriptions, yield monitor data cleaning, on-farm experiment analysis with spatially varying coefficients | Precision agriculture analysis / optimisation and experimental design | 30 |
| UAV plant counting, weed mapping, row detection, stand emergence and canopy cover from imagery | Crop and vegetation detection workflows | 30 |
| Forest inventory: area-based approach with LiDAR, individual tree approach, k-NN and gradient nearest neighbor imputation, stand delineation, volume and basal area models, small-area estimation for inventory | Forest inventory methods / estimation models | 30 |

## Cartographic mathematics

| Source entry | Kind to review | Source page |
|---|---|---:|
| Projection families: Robinson, Winkel Tripel, Equal Earth, Natural Earth, Goode homolosine, Dymaxion, azimuthal and conic equidistant | Projection families | 30 |
| Distortion analysis: Tissot indicatrix computation, areal and angular distortion indices, projection selection algorithms | Projection distortion measures / selection methods | 30 |
| Contiguous cartograms by rubber sheet and diffusion, tile grid maps via Hungarian assignment, Voronoi treemaps, hexagon maps | Cartogram and map-layout algorithms | 30 |
| Perceptual color: CIELAB and CIECAM interpolation, ColorBrewer rules, viridis-style perceptual uniformity, color-blind safe palette generation | Colour-space methods / perceptual design rules | 30 |

## Geovisualization and interaction

| Source entry | Kind to review | Source page |
|---|---|---:|
| Origin-destination maps (Wood and Dykes layout), Sankey flows, space-time cube, small multiples, brushing and linking | Visualisation methods / interactive exploration patterns | 30 |
| Uncertainty visualization: bivariate and value-suppressing palettes, ensemble maps, hypothetical outcome plots | Uncertainty visualisation methods | 30 |
| Animation and temporal generalization, data-driven scrollytelling, level-of-detail streaming | Temporal visualisation / narrative and rendering workflows | 30 |

## Linguistic, political and social geography

| Source entry | Kind to review | Source page |
|---|---|---:|
| Dialect mapping, isogloss detection, spatial lexical variation analysis | Linguistic geography methods | 30 |
| Ecological inference (King's EI, Goodman regression), spatial voting models, partisan bias metrics (efficiency gap, mean-median, declination) | Ecological inference / spatial political models and measures | 30 |
| Gerrymandering detection via ensemble simulation, packing and cracking diagnostics | Redistricting evaluation / simulation methods | 30 |

## Decisions for the next pass

1. Separate database storage and query systems from individual index and join algorithms.
2. Connect morphology to raster and remote-sensing lessons without treating it as only an image-processing technique.
3. Document accessibility assumptions, travel-time inputs and population denominators.
4. Verify hazard model versions, calibration domains and intended operational use.
5. Treat cartographic mathematics and visualisation as part of analytical validity, not as decorative output.
