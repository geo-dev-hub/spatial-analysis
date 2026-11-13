# Section 4 — Raster, terrain, hydrology, geomorphology

- **Original source section:** 4
- **Source pages:** 6–7
- **Source transcription:** [pages 6–10](../../source-inventory/pages-06-10.md)
- **Review state:** source entries extracted into this index; not every entry independently verified
- **Current canonical records:** none yet

The source groups raster operations, terrain analysis, hydrological modelling, geomorphology and coastal methods. The list includes algorithms, physical models, metrics, software packages, data formats and applied workflows. Preserve those differences during research.

## Raster operations

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Map algebra: local, focal, zonal and global operations; reclassification; resampling (nearest, bilinear, cubic, Lanczos) | Raster operations / resampling methods | 6 | Captured; names not individually verified |
| Connected component labeling, flood fill, run-length encoding, image pyramids | Image and raster algorithms / data structures | 6 | Captured; names not individually verified |
| Distance: Euclidean distance transform (Felzenszwalb), chamfer, cost-distance, least-cost path, fast marching and Eikonal solvers, heat method | Distance transforms / path methods / numerical solvers | 6 | Captured; names not individually verified |
| Efficient statistics: integral images for focal statistics, zonal histograms | Data structures / statistical summaries | 6 | Captured; names not individually verified |
| Vectorization and contouring: raster-to-vector, marching squares, marching cubes | Conversion / contouring / surface extraction algorithms | 6 | Captured; names not individually verified |
| Compression: quadtree, JPEG2000, LERC, wavelet; formats such as COG, Zarr, GeoParquet | Compression methods / data formats / storage layouts | 6 | Captured; names not individually verified |

## Terrain analysis

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Slope, aspect, curvature (multiscale), hillshade, multi-directional shading, openness, sky-view factor, local relief models, red relief image maps | Terrain derivatives / visualisation methods / metrics | 6 | Captured; names not individually verified |
| Position and form: topographic position index, ruggedness, geomorphons, landform classification, ridge and valley extraction, pit and peak detection | Terrain metrics / classification and feature extraction | 6 | Captured; names not individually verified |
| Visibility: viewshed (R3, R2, XDraw), cumulative viewshed, isovist, intervisibility, radar coverage and shadow, Fresnel clearance | Visibility algorithms / propagation and clearance methods | 6 | Captured; names not individually verified |
| Solar and microclimate: solar radiation modeling, wind exposure, cold-air drainage, insolation indices | Environmental models / derived indices | 6 | Captured; names not individually verified |
| Volumes: cut-and-fill, reservoir volume from DEM, hypsometric curves | Volume calculations / terrain summaries | 6 | Captured; names not individually verified |
| DEM quality: void filling, error modeling, DEM fusion (SRTM, ASTER, TanDEM-X), bare-earth extraction, hydro-conditioning, stream burning | Data correction / fusion / terrain-processing workflows | 6 | Captured; names not individually verified |
| Terrain simplification and rendering: Lindstrom-Pascucci, quadric error metrics, ROAM, geometry clipmaps, CDLOD, TIN generalization | Simplification algorithms / rendering methods / metrics | 6 | Captured; names not individually verified |

## Hydrology

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Flow routing: D8, D-infinity, MFD, priority-flood depression filling, sink breaching | Flow-direction algorithms / terrain conditioning | 6–7 | Captured; names not individually verified |
| Flow accumulation, watershed and basin delineation, stream ordering (Strahler, Shreve), HAND, topographic wetness index | Hydrological operations / network metrics / terrain indices | 7 | Captured; names not individually verified |
| Rainfall-runoff: SCS curve number, unit hydrograph, Green-Ampt, TOPMODEL, SWAT, HEC-HMS, LISFLOOD, VIC | Hydrological models / software systems | 7 | Captured; names not individually verified |
| Routing and hydrodynamics: Muskingum, Manning, Saint-Venant, kinematic wave, 2D shallow water equations, SPH | Flow-routing methods / physical equations / numerical methods | 7 | Captured; names not individually verified |
| Flood: frequency analysis (GEV, Gumbel, return periods), bathtub versus hydrodynamic inundation, SAR flood mapping | Statistical methods / inundation models / remote-sensing workflow | 7 | Captured; names not individually verified |
| Groundwater: MODFLOW, MODPATH, MT3D, DRASTIC, recharge estimation (water table fluctuation, chloride mass balance) | Groundwater models / assessment index / estimation methods | 7 | Captured; names not individually verified |
| Land surface models: Noah-MP, CLM, JULES; GRACE downscaling; snow and soil moisture assimilation | Land-surface models / downscaling / data assimilation | 7 | Captured; names not individually verified |

## Geomorphology and slope processes

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Chi analysis, slope-area analysis, knickpoint detection, drainage basin morphometry | Geomorphic analysis methods / morphometric measures | 7 | Captured; names not individually verified |
| Landslide susceptibility (frequency ratio, logistic regression), SHALSTAB, weights of evidence | Susceptibility models / statistical methods | 7 | Captured; names not individually verified |
| Glacier mass balance, snow models, avalanche runout | Cryosphere models / hazard modelling | 7 | Captured; names not individually verified |
| Erosion: USLE, RUSLE, hydraulic and thermal erosion simulation | Empirical models / physical simulation | 7 | Captured; names not individually verified |

## Coastal

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| DSAS (end-point rate, linear and weighted regression), waterline extraction, tide-coordinated shorelines | Shoreline change analysis / extraction workflows | 7 | Captured; names not individually verified |
| Wave runup (Stockdon), longshore transport (CERC, Kamphuis), Bruun rule, Dean profile, coastal vulnerability index | Coastal process models / empirical rules / vulnerability index | 7 | Captured; names not individually verified |
| Bathymetry: satellite-derived (ratio, physics-based, ICESat-2 calibrated), multibeam gridding, topo-bathymetric lidar refraction correction | Bathymetric retrieval / gridding / sensor correction | 7 | Captured; names not individually verified |

## Decisions for the next pass

1. Separate raster algebra and data structures from terrain-specific algorithms.
2. Document grid resolution, cell alignment, NoData handling and resampling choices in raster examples.
3. State the assumptions behind flow direction, depression treatment and watershed delineation.
4. Distinguish empirical indices from physical models and numerical solvers.
5. Use a small, known DEM or synthetic surface for teaching, then compare with a documented real dataset where licensing permits.
