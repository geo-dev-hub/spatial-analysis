# Notebooks and interactive labs

Notebooks are used when changing values, inspecting intermediate calculations or plotting a result makes a method easier to understand. They supplement the canonical Markdown lesson and tested implementation; they do not replace either.

## Available labs

### Geometry

- [Geometry foundations lab](geometry-foundations-lab.ipynb): move a point, adjust a segment and change two rectangles to inspect point location, segment intersection and polygon overlay.
- [Polygon overlay lab](polygon-overlay-lab.ipynb): visualise intersection, union, difference and symmetric difference; inspect lower-dimensional contacts, holes, multipart output and precision-grid effects.
- [Convex hull lab](convex-hull-lab.ipynb): see Graham scan build a hull, inspect orientation and collinear policies, and experiment with degenerate point sets.
- [Voronoi and Delaunay lab](voronoi-delaunay-lab.ipynb): compare nearest-site regions with their Delaunay dual, inspect equidistant Voronoi vertices and check empty circumcircles.
- [Core GIS algorithms continuation lab](core-gis-algorithms-lab.ipynb): compare Douglas–Peucker and Visvalingam–Whyatt simplification, inspect polygon offsets and proximity graphs, and compare Dijkstra with A*.
- [Coverage simplification and advanced routing lab](coverage-simplification-routing-lab.ipynb): simplify a shared-edge polygon coverage, inspect fixed-grid precision changes, then compare Dijkstra, bidirectional Dijkstra, ALT A*, turn restrictions and FIFO time-dependent arrival on directed graphs.
- [Planar point-location lab](point-location-lab.ipynb): inspect x-event lines, open slabs, face transitions, holes and boundary queries using the tested static slab locator.
- [Ear-clipping lab](ear-clipping-lab.ipynb): inspect a concave polygon, its triangle partition, triangle count and area invariant.

### Spatial indexing

- [STR-packed R-tree](str-packed-rtree-lab.ipynb): compare bounding-box candidates with exact geometry intersections and inspect how node capacity affects grouping.
- [Filter-and-refine spatial join](filter-refine-spatial-join-lab.ipynb): join points to polygons, inspect candidate pairs and compare exact predicates with a brute-force result.
- [Point-region quadtree](quadtree-lab.ipynb): explore recursive cell subdivision and compare inclusive rectangular window queries with brute force.

### Decision support

- [Weighted linear combination lab](weighted-linear-combination-lab.ipynb): explore standardised criteria, relative weights, hard exclusions, sensitivity and strict NoData handling using a synthetic suitability surface.
- [Weights-of-evidence lab](weights-of-evidence-lab.ipynb): estimate binary evidence weights, map model-based posterior odds and inspect how duplicated evidence and pseudocount choices affect results.
- [ELECTRE I-style outranking lab](electre-i-outranking-lab.ipynb): inspect pairwise concordance, discordance, the outranking relation and threshold sensitivity for discrete alternatives.
- [Snap-rounding noder lab](snap-rounding-noder-lab.ipynb): inspect arrangement vertices, hot pixels, snapped polylines, grid-size changes and precision edge cases.

### Optimization and location science

- [p-median facility-location lab](p-median-facility-location-lab.ipynb): select candidate facilities, assign demand and inspect the effect of demand weights.
- [2SFCA accessibility lab](two-step-fca-accessibility-lab.ipynb): compare provider supply-to-demand ratios and population accessibility under different catchment thresholds.

### Remote sensing

- [NDVI lab](ndvi-lab.ipynb): calculate a synthetic vegetation index and inspect NoData, non-finite values and quality masking.

### Raster analysis

- [Euclidean distance transform lab](raster-distance-transform-lab.ipynb): compare square and rectangular cell spacing and inspect distance to multiple target cells.
- [Focal raster statistics lab](focal-raster-statistics-lab.ipynb): compare focal means, edge-window counts and NoData handling.
- [Priority-Flood lab](priority-flood-lab.ipynb): fill a synthetic DEM depression, inspect the spill elevation and compare the fill-depth layer.
- [D8 flow direction lab](d8-flow-direction-lab.ipynb): inspect steepest-descent direction codes, rectangular cell spacing, sinks and NoData.
- [D8 flow accumulation lab](d8-flow-accumulation-lab.ipynb): trace upstream contributing cells, weighted flow and confluences.
- [Watershed delineation lab](watershed-delineation-lab.ipynb): select an outlet and map all cells that drain to it.
- [Stream order lab](stream-order-lab.ipynb): compare Strahler order and Shreve magnitude at headwaters and confluences.
- [Slope and aspect lab](slope-aspect-lab.ipynb): calculate Horn slope and downslope aspect, derive local hillshade and topographic wetness index, and inspect cell spacing, flat cells and NoData masking.
- [Raster cost-distance lab](cost-distance-lab.ipynb): compare 4/8-neighbour Dijkstra, weighted barriers, cell spacing and unreachable cells.
- [Raster resampling lab](raster-resampling-lab.ipynb): compare nearest neighbour and bilinear interpolation for categorical and continuous surfaces, including NoData policies.
- [Zonal statistics lab](zonal-statistics-lab.ipynb): summarize raster values by zone and inspect NoData and empty-zone behavior.
- [Connected-components lab](raster-connected-components-lab.ipynb): compare 4/8-connectivity and invalid-cell barriers.
- [Contrastive learning lab](contrastive-info-nce-lab.ipynb): inspect paired embeddings, cosine similarity, temperature and negative samples.
- [CRS transformation lab](crs-transformation-lab.ipynb): transform longitude/latitude to Web Mercator and UTM with explicit axis order.

### Geostatistics and covariance

- [Covariance functions lab](covariance-functions-lab.ipynb): compare five Euclidean covariance shapes, inspect matrix eigenvalues, vary the range and examine duplicate sites.
- [Spherical covariance lab](spherical-covariance-lab.ipynb): convert global coordinates to unit vectors, compare non-negative Legendre spectra and inspect a valid spherical covariance matrix.
- [Graph-spectral covariance lab](graph-spectral-covariance-lab.ipynb): build a graph Laplacian, inspect spectral modes and compare heat-kernel covariance across path, star and cycle graphs.

### Geostatistics and interpolation

- [Spatial interpolation lab](geostatistics-interpolation-lab.ipynb): compare IDW powers, inspect an ordinary-kriging estimate and model-based variance, and evaluate a simple spatial holdout.

### Point-pattern analysis

- [Clark–Evans lab](clark-evans-lab.ipynb): compare nearest-neighbour spacing in clustered, random and regular synthetic patterns.
- [Ripley's K and L lab](ripley-k-lab.ipynb): compare uncorrected pair-count summaries with the homogeneous Poisson reference across distance scales.

- [Point-pattern KDE lab](point-pattern-kde-lab.ipynb): compare Gaussian bandwidths and weighted event intensity on a synthetic point pattern.

### Spatial clustering

- [DBSCAN lab](dbscan-clustering-lab.ipynb): inspect core, border and noise points and compare the effect of eps and min_samples.

### Spatial statistics and weights

- [Global Moran's I](global-morans-i-lab.ipynb): build a four-area neighbourhood graph, compare binary and row-standardised weights, inspect the spatial lag, enumerate a small permutation distribution, and use sliders to compare Moran's I with Geary's C as the values change.
- [Global Geary's C](gearys-c-lab.ipynb): compare squared differences between neighbours, contrast similar and alternating values, and inspect all 24 permutations of a four-unit example.
- [Local Moran's I](local-morans-i-lab.ipynb): build a synthetic neighbour graph, inspect High–High and Low–Low clusters and spatial outliers, and apply an FDR cutoff to conditional permutation results.
- [Local Geary](local-geary-lab.ipynb): compare each unit with its neighbours, inspect local squared-difference values and compare raw labels with an FDR-filtered classification.
- [Global Getis-Ord G](global-getis-ord-g-lab.ipynb): test overall concentration of positive values and inspect the permutation reference distribution.
- [Getis-Ord Gi*](getis-ord-gi-star-lab.ipynb): calculate local hotspot and coldspot z-scores, inspect permutation p-values and apply FDR control.
- [Spatial weights](spatial-weights-lab.ipynb): compare Rook and Queen contiguity, distance bands, kNN, row standardisation and isolates.

## Run a notebook

Install the dependencies from the repository root. The spatial-weights lab uses GeoPandas GeoSeries as input to the libpysal Graph builders:

~~~bash
python -m pip install -r notebooks/requirements.txt
python -m pip install jupyterlab
jupyter lab
~~~

Open a notebook from JupyterLab and run the cells in order. The Global Moran's I lab includes live controls built with ipywidgets; change the four area values or the weights style to update the statistics and scatterplot. The other notebooks are editable labs: change an input in a code cell and rerun it to inspect the result.

### Open a lab in Google Colab

The links below point to notebooks already available on the default branch. The planar point-location and weighted suitability labs are available on the current continuation branch and can be opened directly in Colab.

- [Geometry foundations](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/geometry-foundations-lab.ipynb)
- [Planar point location — continuation branch](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/compendium/section-01-geometry-continuation/notebooks/point-location-lab.ipynb)
- [Weighted linear combination — continuation branch](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/compendium/section-01-geometry-continuation/notebooks/weighted-linear-combination-lab.ipynb)
- [Nonseparable space-time covariance — continuation branch](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/compendium/section-01-geometry-continuation/notebooks/nonseparable-space-time-covariance-lab.ipynb)
- [Global Moran's I](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/global-morans-i-lab.ipynb)
- [Global Geary's C](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/gearys-c-lab.ipynb)
- [Local Moran's I](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/local-morans-i-lab.ipynb)
- [Local Geary](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/local-geary-lab.ipynb)
- [Global Getis-Ord G](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/global-getis-ord-g-lab.ipynb)
- [Getis-Ord Gi*](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/getis-ord-gi-star-lab.ipynb)
- [STR-packed R-tree](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/str-packed-rtree-lab.ipynb)
- [Filter-and-refine spatial join](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/filter-refine-spatial-join-lab.ipynb)
- [Spatial weights](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/spatial-weights-lab.ipynb)

The repository workflow executes all forty-seven notebooks on relevant pushes and pull requests. A successful run checks that the cells execute in the configured environment; it does not replace review of the statistical assumptions or geometry contracts.

These notebooks are learning materials. For production analysis, check the input assumptions, use maintained geospatial libraries and record the environment used to produce results.
