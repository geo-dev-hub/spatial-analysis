# Section 17 — Additions: geometry II, scalable computation, design, siting, implementations

- **Original source section:** 17
- **Source pages:** 35–37
- **Source transcription:** [pages 31–35](../../source-inventory/pages-31-35.md) and [pages 36–40](../../source-inventory/pages-36-40.md)
- **Review state:** source entries extracted into this index; not every entry independently verified
- **Current canonical records:** none yet

This section extends computational geometry and adds scalable statistics, fast density methods, sampling design, 3D data formats, competitive location, charging infrastructure, surveillance and a representative implementation map.

## Computational geometry II

| Source entry | Kind to review | Source page |
|---|---|---:|
| Voronoi variants: weighted (additively and multiplicatively weighted, Apollonius), order-k, farthest-point, line-segment Voronoi | Voronoi diagram variants | 35 |
| Triangulation variants: regular triangulation, alpha complexes, 3D Delaunay refinement and tetrahedralization (TetGen-style) | Triangulation and mesh-generation methods | 35 |
| Polygon decomposition: Seidel and Chazelle triangulation, monotone partition, Hertel-Mehlhorn, optimal convex partition | Polygon triangulation and decomposition algorithms | 35 |
| Boolean operations: Martinez-Rueda polygon clipping, 3D mesh Booleans; watchman route problem | Polygon and mesh Boolean operations / visibility path problem | 35 |
| Approximate geometry: geometric hashing, BBD-trees for approximate nearest neighbor, coresets for k-means | Geometric hashing / spatial index / approximation methods | 35 |
| Mesh processing: Laplacian and Taubin smoothing, remeshing, mesh repair, ball pivoting, half-edge, winged-edge and quad-edge data structures | Mesh-processing algorithms / mesh data structures | 35 |

## Scalable computation for spatial statistics

| Source entry | Kind to review | Source page |
|---|---|---:|
| Log-determinant approximation: Chebyshev, Monte Carlo trace estimators, Lanczos, Pace-Barry, sparse Cholesky | Numerical approximation / sparse matrix methods | 35 |
| Gaussian Markov random field sampling, conjugate gradient solvers, Kronecker-structured covariances, circulant embedding with FFT on regular grids | Spatial stochastic simulation / numerical solvers / covariance structures | 35 |
| Sparse GP methods: inducing points, SVGP, Nystrom, structured kernel interpolation (KISS-GP), random Fourier features, hierarchical matrices, fast multipole | Scalable Gaussian-process approximations | 35 |
| Variogram estimation: Matheron, Cressie-Hawkins and Genton robust estimators, REML, composite likelihood, cross-validation-based fitting | Variogram estimators / model-fitting methods | 35 |

## Fast density and sketching

| Source entry | Kind to review | Source page |
|---|---|---:|
| Fast KDE: binned KDE with FFT, dual-tree KDE, random Fourier feature KDE, quantized and grid-based DBSCAN | Scalable density estimation / clustering | 35 |
| Streaming sketches for grids and tiles: HyperLogLog for distinct counts, count-min sketch, Bloom filters for tile existence, reservoir sampling for spatial streams | Streaming summaries / probabilistic data structures / sampling | 35 |

## Optimal sampling and experimental design

| Source entry | Kind to review | Source page |
|---|---|---:|
| Space-filling designs: maximin, coffee-house, spatial coverage design (k-means based), Latin hypercube | Spatial sampling and experimental design | 35 |
| Model-based design: kriging variance minimization, Bayesian optimal design, sequential and adaptive designs, mutual information sensor selection (submodular greedy) | Model-based and adaptive experimental design | 36 |
| Robotic sampling: adaptive sampling with AUVs and drones, informative path planning | Mobile sensing / robotic path planning | 36 |

## 3D formats and level-of-detail

| Source entry | Kind to review | Source page |
|---|---|---:|
| Point cloud storage: LAZ compression, COPC, Entwine EPT, Potree octrees | Point-cloud formats / storage and indexing systems | 36 |
| City and terrain streaming: OGC 3D Tiles with screen-space-error refinement, I3S, quantized-mesh terrain, CityGML levels of detail (LoD0 to LoD3) | 3D geospatial formats / streaming and LOD methods | 36 |
| Data models: Simple Features, arc-node topology, TIN model, TopoJSON, GeoSPARQL | Data models / standards and encodings | 36 |

## Competitive location and matching

| Source entry | Kind to review | Source page |
|---|---|---:|
| Competitive facility location: Huff-based, Stackelberg and Nash formulations, Voronoi games | Competitive location models / game-theoretic formulations | 36 |
| Stable matching (Gale-Shapley), auction algorithms, school choice and spatial assignment with preferences | Matching and assignment algorithms / allocation problems | 36 |

## EV charging and refueling siting

| Source entry | Kind to review | Source page |
|---|---|---:|
| Flow-capturing location model (FCLM), flow-refueling location model (FRLM), charging demand estimation from trajectories | Flow-based facility location / demand estimation | 36 |
| Charging coverage with queuing, grid-capacity-aware siting, hydrogen station siting, V2G scheduling | Infrastructure siting / queueing and energy scheduling | 36 |

## Surveillance and anomaly detection

| Source entry | Kind to review | Source page |
|---|---|---:|
| Syndromic surveillance: CUSUM, EARS, Farrington, spatial and space-time variants | Surveillance and outbreak detection methods | 36 |
| Event detection from sensor networks, graph-based anomaly detection, spatial scan on counts with covariates | Event and anomaly detection methods | 36 |

## Infrastructure and land-use mapping from imagery

| Source entry | Kind to review | Source page |
|---|---|---:|
| Solar farm and wind turbine detection, hydropower and mine detection, illegal mining mapping | Infrastructure and land-use detection workflows | 36 |
| Aquaculture ponds, greenhouses, rice paddies (SAR phenology), oil palm and tree crop mapping, shade coffee and agroforestry mapping | Agricultural and land-use mapping workflows | 36 |
| Building age, roof material and building height estimation from imagery and shadows | Building attribute estimation methods | 36 |

## Implementation map (representative libraries)

The source lists software families, not algorithms. Treat this as an orientation list, then verify current project status, supported formats, licences and maintenance before recommending a tool.

| Area | Source-listed implementations | Source page |
|---|---|---:|
| Geometry and indexing | GEOS, JTS, Shapely, S2, H3, libspatialindex | 36 |
| Projections and IO | PROJ, GDAL, Rasterio, Fiona, GeoPandas, xarray, rioxarray | 36 |
| Spatial statistics | PySAL, spdep, spatialreg, mgcv, INLA, gstat, scikit-gstat | 36–37 |
| Networks and routing | OSMnx, NetworkX, igraph, pgRouting, OSRM, Valhalla, GraphHopper, OpenTripPlanner, R5, momepy | 37 |
| Mobility | scikit-mobility, MovingPandas, Traja | 37 |
| Remote sensing and EO ML | SNAP, Orfeo Toolbox, eo-learn, TorchGeo, Terratorch, Raster Vision, Google Earth Engine, openEO | 37 |
| Terrain and hydrology | WhiteboxTools, GRASS, SAGA, TauDEM, pysheds | 37 |
| Big data | Apache Sedona, GeoMesa, cuSpatial, Dask-GeoPandas, DuckDB spatial | 37 |

## Decisions for the next pass

1. Distinguish mathematical algorithms from data structures, standards, formats and libraries.
2. Verify complexity and numerical assumptions for scalable methods before making performance claims.
3. For adaptive sampling, define the objective, observation cost and stopping condition.
4. For siting, record demand, network, capacity and equity constraints.
5. Treat the implementation map as a dated software landscape, not a permanent endorsement list.
