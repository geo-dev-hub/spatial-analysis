# Snap-rounding noder: put intersections on a fixed grid

This package is an exact-arithmetic teaching baseline for hot-pixel snap rounding. It finds arrangement vertices, maps them to a fixed grid and reroutes each segment through every hot pixel it intersects.

## Run it

Use Python 3.10 or newer. The implementation uses only the standard library.

    python -m pip install -r requirements.txt
    python -m pytest -q

## Example

    from snap_rounding import snap_round
    result = snap_round([
        ((0, 0), (2, 2)),
        ((0, 2), (2, 0)),
    ], grid_size=1)
    print(result.hot_pixels)
    print(result.polylines)
    print(result.edges)

Each noded edge retains its source segment index. Polyline coordinates are grid indices; multiply them by result.grid_size to recover the snapped coordinate in input units.

## What happens?

1. Convert coordinates to exact rational values and scale them into grid units.
2. Collect input endpoints and find pairwise segment intersections.
3. Map every arrangement vertex to its nearest integer grid centre.
4. Call the cells centred there hot pixels.
5. For each segment, find every hot-pixel square it intersects.
6. Order those pixels along the segment and connect their centres.
7. Split each polyline into consecutive, non-zero noded edges.

## Precision and boundary policy

- Arithmetic uses fractions.Fraction; float inputs are converted from their decimal string representation.
- Exact half-grid ties round toward positive infinity, including for negative coordinates.
- Hot pixels are closed squares of width one grid unit. A segment on a shared pixel boundary can intersect both adjacent pixels.
- Equal along-segment projection parameters are ordered lexicographically by grid coordinate.
- Zero-length inputs are accepted as point-like inputs and produce a one-pixel polyline with no edges.

These are explicit teaching conventions, not universal defaults.

## Scope and limitations

This implementation is deliberately transparent, not fast. It uses pairwise segment intersection to discover arrangement vertices and scans all hot pixels for every segment. Its broad cost is O(n² + nH), where n is the number of input segments and H is the number of distinct hot pixels, excluding arithmetic bit complexity.

It does not implement indexed segment/pixel intersection structures, output-sensitive bounds or all formal guarantees of production snap-rounding algorithms. It is not a replacement for JTS/GEOS precision reduction or a production noder. Closed-pixel boundary ties can produce multiple hits at the same projected position; the stable ordering makes output reproducible, but this package does not claim a complete proof of topology preservation for every degenerate arrangement.

Read the method lesson and intern walkthrough alongside this implementation.
