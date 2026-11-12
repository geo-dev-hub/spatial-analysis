# Working examples

This directory contains runnable examples linked to the explanations in [the algorithm collection](../algorithms/).

Each implementation should state:
- the language and exact library versions;
- how to install dependencies and run it;
- expected output;
- tests and edge cases;
- coordinate reference system and units where relevant;
- known limitations and what the example does not implement.

Examples demonstrate a named software implementation unless they explicitly reimplement an algorithm. Do not describe a library call as a from-scratch implementation of the underlying algorithm.

## Examples

- [Polygon intersection with Python and Shapely](python/polygon-intersection/README.md): a library-backed overlay operation with nine tests.
- [Point in polygon with Python](python/point-in-polygon/README.md): a transparent ray-crossing implementation with 11 tests.
- [Segment intersection with Python](python/segment-intersection/README.md): exact integer orientation tests and rational intersection coordinates, with 11 tests.
- [Bentley–Ottmann with Python](python/bentley-ottmann/README.md): paired list-status and implicit-treap implementations, exact rational event coordinates, differential tests, an intern walkthrough and a reproducible benchmark.

- [Global Moran's I in Python](python/global-morans-i/README.md): dependency-free dense-matrix calculation, row-standardisation helper and 13 tests. It computes the statistic only; use a spatial statistics library for inference.
- [Global Geary's C in Python](python/geary-c/README.md): dependency-free dense-matrix calculation and 16 tests. It computes the statistic only; use a spatial statistics library for inference.
- [STR-packed R-tree in Python](python/str-packed-rtree/README.md): immutable 2D bounding-box index using STR packing, checked against brute force across 300 entries and 60 query windows.
- [Indexed spatial join with Shapely](python/spatial-join/README.md): filter-and-refine join using STRtree, with tests for predicate direction, boundaries, holes and brute-force equivalence.

## Automated checks

The [Python examples workflow](../.github/workflows/python-tests.yml) is configured to run the test suites for all eight examples and execute all eight learning notebooks on relevant pushes and pull requests, using Python 3.13. The Local Moran notebook uses PySAL's maintained implementation rather than presenting a new from-scratch implementation. The Bentley–Ottmann job also adds the sibling segment-intersection package to `PYTHONPATH`.

A successful automated run means the tests in the repository passed in that environment. It does not prove correctness for every possible geometry or make a restricted teaching implementation production-ready. Always read the input contract and limitations before adapting an example.
