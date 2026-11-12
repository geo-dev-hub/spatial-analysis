# Section 1 — Core GIS: geometry, indexing, proximity, networks, routing

- **Original source section:** 1
- **Source pages:** 1–2
- **Source transcription:** [pages 1–5](../../source-inventory/pages-01-05.md)
- **Section map:** [all 22 original sections](../source-sections.md)
- **Review state:** source entries extracted into this index; not every entry independently verified
- **Important:** source labels and groupings are preserved as intake. A grouped label may contain several methods or variants; it is not automatically one canonical algorithm record.

This is the first item-level catalogue pass. The catalogue distinguishes a broad source entry from the individual names inside it. Canonical records are created separately when a method has a sufficiently clear scope and evidence base.

## Vector and computational geometry

| Source entry | Kind to review | Source page | Current record |
|---|---|---:|---|
| Overlay: buffer, clip, intersect, union, difference, dissolve, centroid, minimum bounding geometry | Operations / geometry processing | 1 | [Polygon intersection](../../algorithms/geometry/polygon-intersection.md) covers the intersection operation only |
| Hulls and tessellations: convex hull (Graham scan, Jarvis march, Quickhull), concave hull (alpha shapes), Voronoi (Fortune sweep), Delaunay (Bowyer-Watson, incremental, divide and conquer), constrained Delaunay, Ruppert refinement | Algorithm families / geometric structures | 1 | Not yet catalogued as individual records |
| Point-in-polygon (ray casting, winding number) | Geometric predicate / point-location methods | 1 | [Point in polygon](../../algorithms/geometry/point-in-polygon.md) |
| Point location (slab method, trapezoid map) | Point-location algorithms / data structures | 1 | Not yet catalogued as individual records |
| Segment intersection (Bentley-Ottmann) | Geometric predicate / all-segment reporting algorithm | 1 | [Segment intersection](../../algorithms/geometry/segment-intersection.md); [Bentley–Ottmann](../../algorithms/geometry/bentley-ottmann.md) |
| Polygon clipping: Sutherland-Hodgman, Weiler-Atherton, Vatti, Greiner-Hormann | Polygon clipping algorithms | 1 | Not yet catalogued as individual records |
| Offsetting (Clipper) | Geometry operation / software implementation name in source | 1 | Needs name and scope verification |
| Cascaded union | Geometry operation / implementation strategy | 1 | Not yet catalogued |
| Self-intersection repair; validity checking | Geometry repair / validation operations | 1 | Not yet catalogued |
| Simplification and generalization: Douglas-Peucker, Visvalingam, topology-preserving simplification, snap rounding | Generalisation algorithms / precision operation | 1 | Not yet catalogued as individual records |
| Triangulation and decomposition: ear clipping, trapezoidal and convex decomposition, medial axis, straight skeleton, Minkowski sum | Algorithm families / geometric structures and operations | 1 | Not yet catalogued as individual records |
| Distance and extent: Hausdorff and Fréchet distance, rotating calipers, smallest enclosing circle (Welzl), largest empty circle, pole of inaccessibility (polylabel), oriented minimum bounding rectangle | Metrics / geometric algorithms | 1 | Not yet catalogued as individual records |
| Proximity graphs: Gabriel, relative neighborhood, beta-skeleton, Yao, Euclidean minimum spanning tree | Graph constructions / spatial structures | 1 | Not yet catalogued as individual records |
| Visibility polygons, funnel algorithm, CSG and BSP Boolean operations, DCEL overlay, arrangements, planarization | Algorithms / operations / data structures; split before canonicalisation | 1 | Not yet catalogued as individual records |

## Spatial indexing and query processing

| Source entry | Kind to review | Source page | Current record |
|---|---|---:|---|
| Trees: R-tree (R*, R+, Hilbert, STR bulk loading), quadtree, octree, k-d tree, ball tree, VP-tree, BSP tree, KD-B-tree, Grid File | Index structures / variants / bulk-loading method | 1 | Not yet catalogued as individual records |
| Space-filling curves and grids: Z-order (Morton), Hilbert, Geohash, H3, S2, quadkeys, HEALPix | Spatial encodings / grid systems / indexing schemes | 1 | Not yet catalogued as individual records |
| Queries: range, kNN, reverse kNN, closest pair, spatial skyline, top-k spatial keyword, geofencing | Query types / spatial operations | 1 | Not yet catalogued |
| Joins: filter-and-refine, plane-sweep, PBSM, TOUCH, partition-based, kNN joins | Join algorithms / query-processing strategies | 2 | Not yet catalogued as individual records |
| Approximate search: locality-sensitive hashing, HNSW, IVF-PQ, ScaNN | Approximate search methods / index systems | 2 | Not yet catalogued as individual records |
| Learned indexes (ZM index, RSMI, LISA), selectivity estimation, spatial histograms | Learned index methods / query estimation / statistics | 2 | Names and scope need individual verification |

## Proximity, topology and relations

| Source entry | Kind to review | Source page | Current record |
|---|---|---:|---|
| Nearest neighbor, distance matrices (Euclidean, geodesic), spatial joins | Spatial queries / distance operations | 2 | Not yet catalogued |
| DE-9IM topological relations, RCC-8, cardinal direction relations | Formal relation models / qualitative spatial relations | 2 | Not yet catalogued |
| Spatial weights: contiguity, distance band, kNN | Weight-matrix construction methods | 2 | Not yet catalogued |

## Network analysis

| Source entry | Kind to review | Source page | Current record |
|---|---|---:|---|
| Shortest path: Dijkstra, A*, Bellman-Ford, Floyd-Warshall, bidirectional Dijkstra, ALT, contraction hierarchies, hub labeling, customizable route planning | Shortest-path algorithms / preprocessing and labelling methods | 2 | Not yet catalogued |
| Service areas and isochrones, many-to-many routing, Yen's k-shortest paths, alternative routes | Network operations / routing algorithms | 2 | Not yet catalogued |
| Centrality: betweenness, closeness, PageRank; space syntax (axial, integration); street network metrics (orientation, circuity, intersection density) | Graph metrics / spatial network measures | 2 | Not yet catalogued |
| Community detection: Louvain, Leiden, Infomap, label propagation; partitioning: Kernighan-Lin, spectral, METIS | Graph clustering / partitioning algorithms and software | 2 | Not yet catalogued |
| Flows and trees: max flow and min cut, minimum spanning tree, Steiner tree, k-core decomposition | Graph algorithms / graph structures | 2 | Not yet catalogued |
| Map matching: HMM, ST-Matching, IVMM, Fast Map Matching, neural | Probabilistic methods / algorithms / model families | 2 | Not yet catalogued |
| Transit routing: RAPTOR, Connection Scan; time-dependent, stochastic, multimodal and turn-restricted routing | Public transport and time-dependent routing algorithms / problem variants | 2 | Not yet catalogued |
| Road network generalization and stroke generation | Network generalisation methods | 2 | Not yet catalogued |

## Classic routing

| Source entry | Kind to review | Source page | Current record |
|---|---|---:|---|
| TSP: 2-opt, Lin-Kernighan, Christofides; VRP: Clarke-Wright savings, sweep; Chinese postman and arc routing | Combinatorial optimisation problems / heuristics / algorithms | 2 | Not yet catalogued |
| CVRP, VRPTW, pickup-and-delivery, dial-a-ride, ALNS, column generation, branch-and-price | Routing problem variants / metaheuristics / exact optimisation methods | 2 | Not yet catalogued |

## Decisions for the next pass

1. Split grouped entries into individual source labels without losing the grouping that appeared in the compendium.
2. Verify ambiguous names and variants against primary papers, specifications or maintainer documentation.
3. Decide whether a candidate deserves a canonical record, a section in a broader record, or only a reference link.
4. Add stable IDs only after scope is clear.
5. Link prerequisites and related methods instead of forcing the section into a single sequence.
6. Add examples, tests and visuals only when they materially help explain the method.

The source is broad by design. Do not force every operation, metric, model, data structure or software name into the category “algorithm.”
