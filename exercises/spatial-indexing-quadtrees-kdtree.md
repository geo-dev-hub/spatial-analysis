# Spatial indexing exercises: quadtrees and k-d trees

These exercises follow the [spatial indexing path](../learning-paths/spatial-indexing.md). They extend the packed R-tree and filter-and-refine lessons with two structures that partition coordinate space in different ways.

## Exercise 1 — Build a point-region quadtree

Create a square root extent and insert a point dataset using a bucket capacity of four.

Include:
- uniformly distributed points;
- a dense cluster;
- duplicate coordinates;
- points on quadrant boundaries.

Implement a window query. Compare its result with a brute-force scan.

**Record:** node count, maximum depth, cells visited, candidates tested and exact matches. State the split-line and duplicate-coordinate policies.

## Exercise 2 — Quadtree family classification

For each use case, identify the likely quadtree family and explain why:

1. compressing a binary raster region;
2. indexing point locations for rectangular window queries;
3. indexing line segments in a road network;
4. storing point data in a linear code on disk.

Do not answer only “quadtree.” Name the data model and the rule that determines subdivision.

## Exercise 3 — Exact nearest neighbour

Implement a brute-force nearest-neighbour function and a k-d tree search. Use squared Euclidean distance for candidate ordering.

Test:
- a query exactly on a split plane;
- two equidistant candidates;
- duplicate points;
- a query outside the data extent;
- a highly unbalanced point distribution.

**Required check:** every returned distance must equal the brute-force minimum. Document the tie policy.

## Exercise 4 — When does pruning stop helping?

Generate point clouds with increasing dimension. Compare brute-force and k-d tree search while recording distance calculations and visited nodes.

Explain why the number of dimensions can make geometric pruning less selective. Do not infer a universal dimensionality threshold from one experiment.

## Exercise 5 — Choose the index for the workload

Compare STR-packed R-tree, point-region quadtree and k-d tree for these workloads:

- repeated window queries over static polygons;
- frequent insertions of point observations;
- exact nearest-neighbour queries over 2D projected points;
- raster-like region representation;
- global point search using a geodesic distance.

For each, identify a plausible index, the assumptions it needs, and one reason it might be a poor choice.

## Review checklist

- [ ] Did I distinguish point, region and extended-geometry data models?
- [ ] Did I specify root extent, boundary policy and stopping conditions?
- [ ] Did I validate results against brute force?
- [ ] Did I use a distance metric consistent with the coordinate system?
- [ ] Did I measure pruning work rather than timing alone?
- [ ] Did I avoid universal complexity claims?
