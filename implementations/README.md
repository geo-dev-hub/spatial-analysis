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
- [Bentley–Ottmann with Python](python/bentley-ottmann/README.md): an exact-coordinate, event-queue sweep prototype with a transparent list-based status and nine tests, plus an intern walkthrough.
