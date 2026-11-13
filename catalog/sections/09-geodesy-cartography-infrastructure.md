# Section 9 — Geodesy, cartography, data infrastructure, privacy, text and semantics

- **Original source section:** 9
- **Source pages:** 18–20
- **Source transcription:** [pages 16–20](../../source-inventory/pages-16-20.md)
- **Review state:** source entries extracted into this index; not every entry independently verified
- **Current canonical records:** none yet

This section contains the supporting systems and concepts that make spatial work possible: coordinate reference systems, georeferencing, geocoding, map design, data infrastructure, quality assurance, privacy and geographic language. It also includes graph, topology and causal-analysis methods. These should become connected topic families rather than one oversized “GIS tools” lesson.

## Geodesy and coordinate systems

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Projections: Transverse Mercator (Gauss-Krüger), UTM, Lambert conformal, Web Mercator, Tobler hyperelliptical, adaptive composite projections | Map projections / projection families | 18 | Captured; names not individually verified |
| Datum transformations: Helmert, Molodensky, Bursa-Wolf 7-parameter, NTv2 grids; ECEF, ENU and geodetic conversions; antimeridian and pole handling | Coordinate transformations / reference-frame conversions / edge-case handling | 18 | Captured; names not individually verified |
| Geoid and gravity: EGM2008 evaluation, Stokes integral, spherical harmonic analysis, gravity anomaly and terrain correction, IGRF and WMM magnetic models | Geoid and gravity models / geophysical calculations | 18 | Captured; names not individually verified |
| Spherical geometry: spherical polygon area, spherical Voronoi and Delaunay, spherical wavelets, icosahedral and cubed-sphere grids | Spherical geometry / spatial structures / grid systems | 18 | Captured; names not individually verified |
| Space geodesy: SLR, DORIS, VLBI, GNSS time series, velocity fields, strain rate, TEC maps, tropospheric delay (Saastamoinen, VMF), precise orbit determination, GRACE gravity recovery, altimetry crossover adjustment | Space-geodetic techniques / estimation and correction methods | 18 | Captured; names not individually verified |
| Satellite orbits: SGP4/SDP4, TLE processing, ground tracks and swaths, revisit analysis, sun-synchronous design, Walker constellations, conjunction analysis | Orbit propagation / mission and constellation analysis | 18 | Captured; names not individually verified |
| Astronomical: solar position, sunrise and sunset, tidal prediction, least-squares network adjustment | Astronomical calculations / prediction / adjustment | 18 | Captured; names not individually verified |

## Georeferencing and transformation

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Affine, polynomial and rubber-sheeting transforms; thin plate spline rectification; co-registration | Geometric transformations / image registration | 19 | Captured; names not individually verified |
| Historical map digitization: control point selection, line-following vectorization, map text spotting, symbol segmentation, legend parsing, color quantization | Digitisation and document/image-processing workflows | 19 | Captured; names not individually verified |
| Conflation: road and building matching, shape-based matching (turning function, Fourier descriptors, Procrustes, shape context), OSM quality and vandalism detection, completeness estimation | Feature matching / conflation / data quality assessment | 19 | Captured; names not individually verified |

## Geocoding and record linkage

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Geocoding, reverse geocoding, rooftop and parcel geocoding, address interpolation, address parsing (libpostal-style CRFs, transformers) | Geocoding operations / address-parsing models | 19 | Captured; names not individually verified |
| String similarity: Levenshtein, Jaro-Winkler, n-gram, Soundex, Metaphone; Fellegi-Sunter, blocking, canopy clustering | String similarity / record-linkage algorithms | 19 | Captured; names not individually verified |
| POI deduplication, gazetteer fusion, entity resolution at scale, embedding-based place matching | Entity resolution / gazetteer and place-matching workflows | 19 | Captured; names not individually verified |

## Cartography and geovisualization

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Classification: Jenks natural breaks, quantiles, equal interval, bivariate choropleth, perceptual color scales | Map classification methods / visual encoding | 19 | Captured; names not individually verified |
| Generalization: smoothing (Bezier, Gaussian, PAEK), aggregation, displacement, exaggeration, building generalization | Cartographic generalisation methods | 19 | Captured; names not individually verified |
| Labeling: label placement optimization, collision-free layouts, glyph placement | Label placement and layout optimisation | 19 | Captured; names not individually verified |
| Special maps: dot density, cartograms (Dorling, Gastner-Newman), flow maps with edge bundling (FDEB), hexbin maps, schematic and metro layout | Thematic map forms / cartogram and flow-map algorithms | 19 | Captured; names not individually verified |
| Rendering: isosurfaces, streamlines and LIC, ray marching, hillshade variants, vector tile styling, tile pyramids, level-of-detail, WebGL and WebGPU pipelines | Rendering algorithms / tile and graphics pipelines | 19 | Captured; names not individually verified |

## Data infrastructure and computing

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Formats and catalogs: COG, Zarr, GeoParquet, FlatGeobuf, STAC, Mapbox Vector Tile, TopoJSON, WKB and WKT, Google polyline, Draco, spatial deduplication | Data formats / catalogue standards / encoding and deduplication methods | 19 | Captured; names not individually verified |
| Distributed and GPU computing: Sedona, GeoMesa, Dask, Spark, cuSpatial, GPU raster algebra, parallel viewshed and flow accumulation, out-of-core and streaming raster algorithms | Distributed systems / GPU libraries / scalable algorithms | 19 | Captured; names not individually verified |
| Pipelines: openEO, xarray, Rasterio, Snakemake, Airflow; process graphs, lineage tracking, data versioning | Software tools / workflow orchestration / provenance systems | 19 | Captured; names not individually verified |
| Numerical methods: finite difference, finite volume, finite element, spectral, semi-Lagrangian, multigrid, conjugate gradient, FFT solvers, lattice Boltzmann, level set | Numerical discretisation and solver methods | 19 | Captured; names not individually verified |
| Collision detection: sweep and prune, BVH, spatial hash grids | Collision detection algorithms / spatial data structures | 19 | Captured; names not individually verified |
| Procedural terrain: Perlin and simplex noise, fractional Brownian motion, diamond-square, Poisson disk sampling, wave function collapse, L-systems, synthetic city generation | Procedural generation / stochastic sampling / synthetic data workflows | 20 | Captured; names not individually verified |

## Quality assurance and validation

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Topology checks, DE-9IM validation rules, temporal consistency checks, automated QA/QC, outlier rules | Data validation rules / quality assurance workflows | 20 | Captured; names not individually verified |
| Benchmark design and geographic bias audits for GeoAI | Evaluation design / geographic representativeness audits | 20 | Captured; names not individually verified |

## Location privacy

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Geomasking (random perturbation, donut masking), spatial k-anonymity and cloaking, geo-indistinguishability, differential privacy for location data | Privacy protection methods / formal privacy models | 20 | Captured; names not individually verified |
| Synthetic population and trajectory generation, federated learning on spatial data | Synthetic data generation / privacy-preserving distributed learning | 20 | Captured; names not individually verified |

## Text, social and semantic geography

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Geoparsing, place NER, toponym resolution, spatial relation extraction, qualitative spatial reasoning (RCC-8, Allen intervals, cone-based directions), natural-language route instructions | Geographic language processing / spatial reasoning methods | 20 | Captured; names not individually verified |
| Geographic information retrieval: spatial keyword search, query understanding, map search ranking, geographic topic models | Information retrieval / geographic search methods | 20 | Captured; names not individually verified |
| Social sensing: tweet and post geolocation, burst and event detection, VGI validation, tourist trajectory mining from photo sharing sites | Social-media analysis / event detection / volunteered geographic information validation | 20 | Captured; names not individually verified |
| Knowledge graphs: GeoSPARQL, spatial RDF, ontology alignment, entity linking, GeoQA, ontology-driven reasoning (SWRL) | Standards / knowledge representation / semantic reasoning systems | 20 | Captured; names not individually verified |

## Indoor, sports and retail analytics

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Indoor: IndoorGML, indoor routing, floor plan reconstruction, indoor SLAM | Standards / routing and reconstruction workflows | 20 | Captured; names not individually verified |
| Sports: Voronoi pitch control, expected threat, passing networks, player tracking | Spatial analytics metrics / network analysis / tracking methods | 20 | Captured; names not individually verified |
| Retail: customer flow, indoor heatmaps, dwell-time analysis | Movement and behavioural analytics workflows | 20 | Captured; names not individually verified |

## Topological, graph and geometric data analysis

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Persistent homology, Mapper, Reeb graphs, Morse-Smale complexes | Topological data analysis methods / data structures | 20 | Captured; names not individually verified |
| Optimal transport (Wasserstein, Sinkhorn, Gromov-Wasserstein), manifold learning (t-SNE, UMAP, Isomap) | Optimisation and transport methods / dimensionality reduction | 20 | Captured; names not individually verified |
| Graph signal processing, spectral clustering, graph kernels, random walk with restart, HITS, heat kernel diffusion, graph Laplacian smoothing, motif mining | Graph analysis / signal processing / ranking and diffusion methods | 20 | Captured; names not individually verified |

## Spatial causal inference

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Spatial difference-in-differences, synthetic control, geographic regression discontinuity, spatial instrumental variables | Causal inference designs / econometric methods | 20 | Captured; names not individually verified |

## Decisions for the next pass

1. Keep coordinate reference systems, transformations and geodesic calculations distinct.
2. Treat data formats and standards as infrastructure records, not algorithms.
3. Explain map design as a decision about communication, not only a rendering technique.
4. Treat location privacy as a first-class requirement; do not publish identifiable trajectories or sensitive location data as teaching examples.
5. Verify standard names and software support against current specifications and maintained documentation.
6. Separate causal identification assumptions from the mechanics of fitting a spatial model.
