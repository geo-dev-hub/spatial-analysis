# Core GIS continuation exercises

These exercises connect line generalisation, offset geometry, proximity graphs, point location and shortest paths. Read the relevant algorithm dossier before coding.

## 1. Compare line simplifiers

Use a river centreline with at least 100 vertices.

- Run Douglas–Peucker with three distance tolerances.
- Run Visvalingam–Whyatt with three area thresholds.
- Record retained vertices, line length and Hausdorff distance.
- Explain why distance and area thresholds cannot be compared numerically.
- Plot the original and simplified lines at two map scales.

## 2. Offset a constrained site

Create a concave polygon with a narrow corridor and one hole.

- Expand it by a positive distance.
- Contract it by a negative distance.
- Repeat with round, bevel and miter joins.
- Record area, component count, hole count, validity and whether the corridor survives.
- Explain the CRS and unit assumptions.

## 3. Compare proximity graphs

Use a point set with a cluster, an outlier and a nearly cocircular group.

- Construct Gabriel, RNG and Euclidean MST.
- Check that RNG edges are contained in Gabriel edges for the selected convention.
- Check the MST has n−1 edges for n>0.
- Compare total edge length, degree distribution and connected components.
- Explain the strict open-region tie convention.

## 4. Design a point-location fixture

Draw a planar subdivision with at least six faces. Create queries strictly inside each face, on an edge, on a vertex and outside the bounded area.

- Specify the returned face or boundary result.
- Identify vertical edges and shared vertices.
- Sketch the x-slabs and the order of edges in each open slab.
- Explain what additional search structure is needed to obtain logarithmic query time.

Do not substitute repeated point-in-polygon tests and call them a trapezoidal map.

## 5. Route on a directed weighted graph

Create a directed graph with a short but slow route and a longer but faster route.

- Compare Dijkstra and A* using a zero heuristic.
- Add an admissible heuristic expressed in the same cost units.
- Add a one-way edge and an unreachable goal.
- Add a turn restriction and explain why a node-only state may be insufficient.

## Submission checklist

- [ ] State coordinate reference system and units.
- [ ] State every algorithm's input assumptions.
- [ ] Include expected results before running code.
- [ ] Test boundary and degenerate cases.
- [ ] Compare with a trusted oracle where appropriate.
- [ ] Record software versions and unresolved limitations.
