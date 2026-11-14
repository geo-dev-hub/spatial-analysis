# Intern walkthrough: building a hot-pixel snap-rounding noder

## Goal

Convert intersecting line segments into polylines whose vertices lie on a fixed grid. A downstream overlay operation may require a common precision model, but independently rounding endpoints can change which segments intersect.

## 1. Find arrangement vertices exactly

The implementation stores coordinates as fractions. It starts with every input endpoint and compares every pair of segments.

For non-parallel segments, cross-product equations produce exact segment parameters. If both lie in [0, 1], the exact crossing is added. For collinear segments, shared endpoints are added. A zero-length segment is treated as a point.

This pairwise discovery step is easy to inspect but costs O(n²) comparisons. Production arrangement builders use more efficient spatial or sweep-line structures.

## 2. Create hot pixels

Coordinates are divided by the grid size. Each arrangement vertex is assigned to its nearest integer grid centre. The cell centred there is a hot pixel.

The half-grid tie rule is explicit: exact ties go toward positive infinity. This avoids depending on language-specific rounding defaults.

## 3. Reroute every segment

For each original segment, test whether it intersects each hot-pixel square. The code uses an exact Liang–Barsky interval clip against the square's four sides.

A segment is replaced by a polyline connecting the centres of all hot pixels it intersects, ordered by projection along the original segment.

The pixel squares are closed. A segment lying exactly on a pixel boundary can meet both adjacent cells. Equal projection positions use a deterministic lexicographic tie-break. This makes output reproducible, but it is not a proof that every degenerate arrangement has all the topological guarantees of a production snap-rounding algorithm.

## 4. Produce noded edges

Every consecutive pair of distinct pixel centres becomes a noded edge. The edge retains the source segment index so the output can be traced to its input.

The implementation does not dissolve duplicate edges or infer polygon faces. Those are separate operations.

## 5. Reproduce the tests

The tests cover proper and fractional crossings, endpoint contact, collinear overlap, zero-length point-like input, negative half-grid ties, non-unit grid size, source-segment identity, empty input and invalid values.

Run:

    python -m pip install -r requirements.txt
    python -m pytest -q

## 6. Extension exercise

Add a segment that passes exactly along a hot-pixel boundary. Inspect which adjacent pixels are included and how the tie ordering changes the polyline.

Then compare the teaching baseline with a production snap-rounding implementation. Record differences in output, precision model, topology guarantees, complexity and degeneracy policy.
