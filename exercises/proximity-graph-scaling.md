# Exercise: scale a proximity-graph construction

Use the [proximity-graph lesson](../algorithms/geometry/proximity-graphs.md) and the [small-input Python package](../implementations/python/proximity-graphs/README.md).

## Part A — Compare the graph definitions

For one fixed point set, construct the Gabriel graph, relative-neighbourhood graph, lune-based beta-skeleton at beta=1.5, Yao graph and Euclidean minimum spanning tree.

Record:
- number of vertices and edges;
- connected components;
- total Euclidean edge length;
- the effect of adding one point near an existing cluster.

## Part B — Identify the quadratic work

Inspect the small-input implementation. For each graph, identify the loops that examine candidate pairs and the points that might block a candidate edge.

Estimate how the number of candidate tests grows when the point count doubles.

## Part C — Design a Delaunay-based construction

1. Construct or obtain a Euclidean Delaunay triangulation.
2. Explain why its planar edge set is a sparse candidate set for the Gabriel graph, RNG and Euclidean MST under consistent assumptions.
3. Describe how the exact lune or diameter-disk test filters candidate edges.
4. Read Lingas (1994) and state the beta range and metric conditions for the linear-time result from a Delaunay triangulation.
5. Explain why the theorem does not justify using Delaunay candidates for every proximity graph.

## Part D — Design a scalable Yao construction

1. Divide the plane into k cones around each point.
2. State the angular boundary and tie-breaking rules.
3. Identify the nearest-neighbour query needed in each cone.
4. Read Funke, Sanders and Georgiadis (2023). List the data-structure and event-queue challenges that separate an O(n log n) implementation from a quadratic baseline.
5. Explain why a grid-based heuristic and an optimal worst-case algorithm should be benchmarked and described separately.

## Submission

Submit the point set, graph plots, edge-count table, complexity discussion and a short design note for a future scalable implementation. Do not claim that the existing package implements the researched Delaunay or optimal Yao constructions.
