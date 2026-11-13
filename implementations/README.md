# Working examples

This directory contains runnable examples linked to the explanations in [the algorithm collection](../algorithms/).

An example should make one thing clear: is it demonstrating a library operation, or is it implementing a named method from first principles? State that distinction plainly.

Each implementation should state:
- the language and exact library versions;
- how to install dependencies and run it;
- expected output, including units and coordinate assumptions;
- tests and the edge cases they cover;
- coordinate reference system, units and precision policy where relevant;
- known limitations and what the example does not implement;
- a step-by-step walkthrough that explains the code, decisions and validation.

## Examples

### Geometry and computational geometry

- [Polygon intersection with Python and Shapely](python/polygon-intersection/README.md): a library-backed overlay operation with nine tests and a [step-by-step walkthrough](python/polygon-intersection/implementation-walkthrough.md).
- [Point in polygon with Python](python/point-in-polygon/README.md): a transparent ray-crossing implementation with 12 tests and a [step-by-step walkthrough](python/point-in-polygon/implementation-walkthrough.md).
- [Segment intersection with Python](python/segment-intersection/README.md): exact integer orientation tests and rational intersection coordinates, with 11 tests and a [step-by-step walkthrough](python/segment-intersection/implementation-walkthrough.md).
- [Bentley–Ottmann with Python](python/bentley-ottmann/README.md): paired list-status and implicit-treap implementations, exact rational event coordinates, differential tests, an intern walkthrough and a reproducible benchmark.
- [Polygon validity with Shapely](python/polygon-validity/README.md): a read-only validity inspection and explicit make-valid workflow, with tests for invalid rings, holes, overlapping MultiPolygon components and repair outputs, plus a [step-by-step walkthrough](python/polygon-validity/implementation-walkthrough.md).

### Raster analysis\n\n- [Euclidean distance transform](python/raster-distance/README.md): a SciPy-backed exact Euclidean distance wrapper with anisotropic cell spacing, tests and an [intern walkthrough](python/raster-distance/implementation-walkthrough.md).\n\n### Geostatistics and interpolation\n\n- [IDW and ordinary kriging](python/geostatistics/README.md): transparent IDW and a dense ordinary-kriging solver using a specified exponential variogram, with tests and an [intern walkthrough](python/geostatistics/implementation-walkthrough.md).\n\n### Spatial statistics

- [Global Moran's I in Python](python/global-morans-i/README.md): a dependency-free dense-matrix calculation, row-standardisation helper and 13 tests. It computes the statistic only; use a spatial statistics library for inference. Follow the [Global Moran's I walkthrough](python/global-morans-i/implementation-walkthrough.md).
- [Global Geary's C in Python](python/geary-c/README.md): a dependency-free dense-matrix calculation and 16 tests. It computes the statistic only; use a spatial statistics library for inference. Follow the [Geary's C walkthrough](python/geary-c/implementation-walkthrough.md).

### Indexing and query processing

- [STR-packed R-tree in Python](python/str-packed-rtree/README.md): an immutable 2D bounding-box index using STR packing, checked against brute force across 300 entries and 60 query windows, with a [step-by-step walkthrough](python/str-packed-rtree/implementation-walkthrough.md).
- [Indexed spatial join with Shapely](python/spatial-join/README.md): filter-and-refine join using STRtree, with tests for predicate direction, boundaries, holes and brute-force equivalence, plus a [step-by-step walkthrough](python/spatial-join/implementation-walkthrough.md).
- [2D k-d tree in Python](python/kd-tree/README.md): a static median-built tree for exact planar Euclidean nearest-neighbour search, with brute-force differential tests and a [step-by-step walkthrough](python/kd-tree/implementation-walkthrough.md).
- [Point-region quadtree in Python](python/quadtree/README.md): a bucket PR quadtree for inclusive rectangular window queries, with explicit midpoint, root-boundary and stopping rules, brute-force differential tests and a [step-by-step walkthrough](python/quadtree/implementation-walkthrough.md).
- [Sutherland–Hodgman polygon clipping](python/polygon-clipping/README.md): a dependency-free convex-polygon intersection implementation, with explicit input limits, edge-case tests and a [step-by-step walkthrough](python/polygon-clipping/implementation-walkthrough.md).
- [Polygon overlay operations with Shapely](python/polygon-overlay/README.md): validated intersection, union, difference and symmetric difference, with topology and precision tests, an [intern walkthrough](python/polygon-overlay/implementation-walkthrough.md) and a [visual notebook](../notebooks/polygon-overlay-lab.ipynb).
- [Graham scan convex hull](python/convex-hull/README.md): a dependency-free convex hull implementation with duplicate, collinear and degenerate-input tests, an [intern walkthrough](python/convex-hull/implementation-walkthrough.md) and a [visual notebook](../notebooks/convex-hull-lab.ipynb).
- [Voronoi and Delaunay with SciPy](python/voronoi-delaunay/README.md): a validated Qhull-backed workflow with equidistance and empty-circumcircle tests, an [intern walkthrough](python/voronoi-delaunay/implementation-walkthrough.md) and a [visual notebook](../notebooks/voronoi-delaunay-lab.ipynb).
- [Coverage-aware polygon simplification](python/coverage-simplification/README.md): a Shapely/GEOS wrapper with input/output coverage validation and edge-matched fixtures.
- [Fixed-grid precision operations](python/precision-grid/README.md): explicit coordinate precision reduction and GEOS fixed-grid overlay, with tests that distinguish these operations from full snap rounding.
- [Clipper2 native offsetting in C#](clipper2-csharp/README.md): an integer-path implementation using the Clipper2 NuGet package, with an executable CI smoke test.
- [Shortest-path baselines](python/shortest-paths/README.md): Dijkstra, A*, bidirectional Dijkstra, directed ALT landmarks, Yen's k-shortest loopless paths, Bellman–Ford and Floyd–Warshall with tests.
- [Road-routing baselines](python/road-routing/README.md): edge-based turn restrictions, turn penalties and FIFO time-dependent earliest-arrival search.

## Automated checks

The [Python examples workflow](../.github/workflows/python-tests.yml) is configured to run the test suites for all twenty-five Python example packages and the Clipper2 C# smoke test, and execute all eighteen learning notebooks on relevant pushes and pull requests, using Python 3.13. The Local Moran notebook uses PySAL's maintained implementation rather than presenting a new from-scratch implementation. The Bentley–Ottmann job also adds the sibling segment-intersection package to `PYTHONPATH`.

A successful automated run means the tests in the repository passed in that environment. It does not prove correctness for every possible geometry or make a restricted teaching implementation production-ready. Always read the input contract and limitations before adapting an example.

## How the examples fit together

The canonical lesson explains the problem and method. The implementation shows one concrete way to put it into practice. Tests make expected behaviour explicit. The walkthrough explains how the code is built and why. A notebook is added when changing values or inspecting intermediate results makes the idea easier to learn.

These are connected teaching materials, not interchangeable copies of the same explanation.
