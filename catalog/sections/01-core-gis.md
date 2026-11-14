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
| Overlay: buffer, clip, intersect, union, difference, dissolve, centroid, minimum bounding geometry | Operations / geometry processing | 1 | [Polygon intersection](../../algorithms/geometry/polygon-intersection.md) introduces intersection; [polygon overlay](../../algorithms/geometry/overlay-operations.md) explains all four Boolean operations and links to a tested Shapely/GEOS package. Buffer, dissolve, centroid and minimum bounding geometry still need separate records |
| Hulls and tessellations: convex hull (Graham scan, Jarvis march, Quickhull), concave hull (alpha shapes), Voronoi (Fortune sweep), Delaunay (Bowyer-Watson, incremental, divide and conquer), constrained Delaunay, Ruppert refinement | Algorithm families / geometric structures | 1 | [Convex hull](../../algorithms/geometry/convex-hull.md) explains Graham scan and links to a tested teaching implementation and visual lab; [Voronoi and Delaunay](../../algorithms/geometry/voronoi-delaunay.md) now connects nearest-site regions, Fortune's sweep and the Delaunay dual with a tested SciPy/Qhull workflow and visual lab. Jarvis march, Quickhull, concave hull, constrained Delaunay and Ruppert refinement still need separate records and verification |
| Point-in-polygon (ray casting, winding number) | Geometric predicate / point-location methods | 1 | [Point in polygon](../../algorithms/geometry/point-in-polygon.md) |
| Point location (slab method, trapezoid map) | Point-location algorithms / data structures | 1 | [Planar point location](../../algorithms/geometry/point-location.md) compares static slab decompositions and randomized trapezoidal maps; a tested static slab locator covers disjoint polygon faces, while the randomized trapezoidal map remains unimplemented |
| Segment intersection (Bentley-Ottmann) | Geometric predicate / all-segment reporting algorithm | 1 | [Segment intersection](../../algorithms/geometry/segment-intersection.md); [Bentley–Ottmann](../../algorithms/geometry/bentley-ottmann.md) |
| Polygon clipping: Sutherland-Hodgman, Weiler-Atherton, Vatti, Greiner-Hormann | Polygon clipping algorithms | 1 | [Polygon clipping](../../algorithms/geometry/polygon-clipping.md) compares the algorithm families; a tested, dependency-free Sutherland–Hodgman teaching implementation covers convex subject and clip rings. The other families are researched but not implemented here |
| Offsetting (Clipper) | Geometry operation / software implementation name in source | 1 | [Polygon offsetting](../../algorithms/geometry/offsetting.md) separates the geometric operation from Clipper2; a tested Shapely/GEOS wrapper and a native [Clipper2 C# example](../../implementations/clipper2-csharp/README.md) now demonstrate distinct implementation contracts |
| Cascaded union | Geometry operation / implementation strategy | 1 | Not yet catalogued |
| Self-intersection repair; validity checking | Geometry repair / validation operations | 1 | [Polygon validity](../../algorithms/geometry/polygon-validity.md) explains the validity model and links to a tested Shapely inspection/explicit-repair workflow; repair outputs remain a modelling decision |
| Simplification and generalization: Douglas-Peucker, Visvalingam, topology-preserving simplification, snap rounding | Generalisation algorithms / precision operation | 1 | [Line simplification](../../algorithms/geometry/simplification.md) and tested open-polyline implementations cover Douglas–Peucker and Visvalingam–Whyatt; [coverage-aware polygon simplification](../../algorithms/geometry/coverage-simplification.md) now has a tested Shapely/GEOS wrapper for edge-matched coverages. A tested [fixed-grid precision package](../../implementations/python/precision-grid/README.md) wraps coordinate precision reduction and GEOS fixed-grid overlay. A dedicated [snap-rounding lesson](../../algorithms/geometry/snap-rounding.md), exact-arithmetic hot-pixel noder, tests, intern walkthrough, exercise and visual lab now cover a scoped teaching implementation; output-sensitive production algorithms remain outside its scope. [Precision models](../../algorithms/geometry/precision-models.md) distinguish these operations from the full algorithm |
| Triangulation and decomposition: ear clipping, trapezoidal and convex decomposition, medial axis, straight skeleton, Minkowski sum | Algorithm families / geometric structures and operations | 1 | [Ear clipping](../../algorithms/geometry/ear-clipping.md) now has a simple-ring lesson, exact-predicate teaching baseline, tests, walkthrough and visual lab. [Convex decomposition](../../algorithms/geometry/convex-decomposition.md) distinguishes triangulate-and-merge, exact optimal partitions and approximate convex decompositions, with a learner exercise. A tested exact-predicate greedy triangulate-and-merge baseline is now available with an intern walkthrough and visual lab. It is not an optimized Hertel–Mehlhorn implementation and makes no approximation-guarantee claim. The [convex Minkowski-sum edge merge](../../implementations/python/minkowski-convex/README.md) now has exact rational arithmetic, tests, an intern walkthrough and a visual lab; non-convex sums remain library-backed research. [Medial axis](../../algorithms/geometry/medial-axis.md) and [straight skeleton](../../algorithms/geometry/straight-skeleton.md) now have separate lessons and exercises that distinguish the metric maximal-disc structure from the parallel-wavefront structure. [Minkowski sums](../../algorithms/geometry/minkowski-sum.md) now explains convex edge merging, decomposition and convolution strategies, offsets and configuration-space obstacles |
| Distance and extent: Hausdorff and Fréchet distance, rotating calipers, smallest enclosing circle (Welzl), largest empty circle, pole of inaccessibility (polylabel), oriented minimum bounding rectangle | Metrics / geometric algorithms | 1 | Not yet catalogued as individual records |
| Proximity graphs: Gabriel, relative neighborhood, beta-skeleton, Yao, Euclidean minimum spanning tree | Graph constructions / spatial structures | 1 | [Proximity graphs](../../algorithms/geometry/proximity-graphs.md) and tested small-input baselines cover Gabriel, RNG, a specified lune-based beta-skeleton, a specified Yao graph and Euclidean MST. Research now documents Delaunay-based RNG/beta-skeleton construction and an optimal O(n log n) Yao implementation route; these scalable algorithms are not yet implemented |
| Visibility polygons, funnel algorithm, CSG and BSP Boolean operations, DCEL overlay, arrangements, planarization | Algorithms / operations / data structures; split before canonicalisation | 1 | Not yet catalogued as individual records |

## Spatial indexing and query processing

| Source entry | Kind to review | Source page | Current record |
|---|---|---:|---|
| Trees: R-tree (R*, R+, Hilbert, STR bulk loading), quadtree, octree, k-d tree, ball tree, VP-tree, BSP tree, KD-B-tree, Grid File | Index structures / variants / bulk-loading method | 1 | [STR-packed R-tree](../../algorithms/indexing/str-packed-rtree.md), [point-region quadtree](../../algorithms/indexing/quadtree.md) and [k-d tree nearest-neighbour search](../../algorithms/indexing/kd-tree-nearest-neighbour.md) have separate teaching records, connected by a [spatial index selection guide](../../algorithms/indexing/choosing-spatial-index.md); other structures remain unverified |
| Space-filling curves and grids: Z-order (Morton), Hilbert, Geohash, H3, S2, quadkeys, HEALPix | Spatial encodings / grid systems / indexing schemes | 1 | Not yet catalogued as individual records |
| Queries: range, kNN, reverse kNN, closest pair, spatial skyline, top-k spatial keyword, geofencing | Query types / spatial operations | 1 | Not yet catalogued |
| Joins: filter-and-refine, plane-sweep, PBSM, TOUCH, partition-based, kNN joins | Join algorithms / query-processing strategies | 2 | Not yet catalogued as individual records |
| Approximate search: locality-sensitive hashing, HNSW, IVF-PQ, ScaNN | Approximate search methods / index systems | 2 | Not yet catalogued as individual records |
| Learned indexes (ZM index, RSMI, LISA), selectivity estimation, spatial histograms | Learned index methods / query estimation / statistics | 2 | Names and scope need individual verification |

## Proximity, topology and relations

| Source entry | Kind to review | Source page | Current record |
|---|---|---:|---|
| Nearest neighbor, distance matrices (Euclidean, geodesic), spatial joins | Spatial queries / distance operations | 2 | [Filter-and-refine spatial join](../../algorithms/query-processing/filter-refine-spatial-join.md) covers indexed spatial joins; [k-d tree nearest-neighbour search](../../algorithms/indexing/kd-tree-nearest-neighbour.md) is a foundational point-search draft; distance matrices and geodesic nearest-neighbour methods remain unverified |
| DE-9IM topological relations, RCC-8, cardinal direction relations | Formal relation models / qualitative spatial relations | 2 | Not yet catalogued |
| Spatial weights: contiguity, distance band, kNN | Weight-matrix construction methods | 2 | [Spatial weights matrix](../../methods/spatial-weights-matrix.md) covers Rook, Queen, distance-band and kNN definitions, transformations and isolates |

## Network analysis

| Source entry | Kind to review | Source page | Current record |
|---|---|---:|---|
| Shortest path: Dijkstra, A*, Bellman-Ford, Floyd-Warshall, bidirectional Dijkstra, ALT, contraction hierarchies, hub labeling, customizable route planning | Shortest-path algorithms / preprocessing and labelling methods | 2 | [Shortest paths](../../algorithms/networks/shortest-paths.md) surveys the family and links tested Dijkstra, A*, bidirectional Dijkstra, directed ALT, Yen's k-shortest loopless paths, Bellman–Ford and Floyd–Warshall baselines. The [turn-aware and time-dependent routing dossier](../../algorithms/networks/turn-aware-time-dependent-routing.md) and [road-routing package](../../implementations/python/road-routing/README.md) add edge-based turn restrictions, turn penalties and FIFO earliest-arrival search; contraction hierarchies, hub labels, customizable route planning, non-FIFO routing and transit algorithms remain open |
| Service areas and isochrones, many-to-many routing, Yen's k-shortest paths, alternative routes | Network operations / routing algorithms | 2 | Yen's k-shortest loopless paths now have a tested implementation in [the shortest-path package](../../implementations/python/shortest-paths/README.md); many-to-many routing and service-area isochrones remain open |
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
7. Keep the new validity, clipping and overlay records in draft status until their edge cases, mathematical claims, implementation versions and rendered references have been reviewed.

Related practice: [geometry overlay and validity exercises](../../exercises/geometry-overlay-and-validity.md).

The source is broad by design. Do not force every operation, metric, model, data structure or software name into the category “algorithm.”

- [Ear clipping](../../algorithms/geometry/ear-clipping.md) — triangulate a simple polygon ring; the current exact-predicate teaching implementation is intentionally transparent and has an O(n^3) worst-case bound.
