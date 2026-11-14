# Proximity graphs: turning nearby places into a network

A proximity graph connects points according to a spatial rule. It turns a set of locations into a graph that can support clustering, neighbourhood analysis, network construction and spatial reasoning.

The source inventory groups Gabriel graphs, relative neighbourhood graphs, beta-skeletons, Yao graphs and Euclidean minimum spanning trees. They are related, but they are not interchangeable.

## Start with a point set

Let P be a finite set of distinct points in the Euclidean plane. A proximity graph has one vertex for each point. An edge is included when a geometric test says the pair is sufficiently close or unobstructed by other points.

## Gabriel graph

Two points u and v are connected when the open disk having segment uv as its diameter contains no other point of P.

For a third point w, the blocking test can be expressed without computing a square root:

$$
(w-u)\cdot(w-v)<0
$$

If this is true, w lies strictly inside the diameter disk and blocks the edge. Equality lies on the boundary; this lesson uses the open-disk convention and does not treat boundary points as blockers.

The Gabriel graph is a subgraph of the Delaunay triangulation under the usual Euclidean assumptions.

## Relative neighbourhood graph

An edge uv belongs to the relative neighbourhood graph (RNG) when there is no third point w closer than |uv| to both endpoints:

$$
\max(d(u,w),d(v,w))<d(u,v)
$$

A third point in the open lune blocks the edge. As with the Gabriel graph, the boundary convention must be stated for exact ties.

The RNG is contained in the Gabriel graph under the standard Euclidean definitions. It is therefore no denser than the Gabriel graph for the same point set and convention.

## Beta-skeletons

Beta-skeletons generalise lune-based neighbourhood tests by changing the shape and scale of the region that must be empty. There are multiple beta-skeleton conventions (including lune-based and circle-based definitions), so a bare beta-skeleton label is incomplete. Record the variant, beta range, metric and open/closed boundary convention.

## Yao graphs

A Yao graph partitions the plane around each point into a fixed number of angular cones. Each point selects its nearest neighbour in each cone, and the directed selections are commonly symmetrised to produce an undirected graph.

The cone orientation, tie-breaking rule, metric and symmetrisation rule are part of the algorithm specification. Yao graphs are geometric spanners under suitable assumptions; do not transfer a stretch-factor claim between variants without checking its theorem.

## Euclidean minimum spanning tree

The Euclidean MST is a minimum-total-length spanning tree over the complete Euclidean graph on the point set. It has n−1 edges for n>0, assuming distinct vertices and the usual complete graph.

The MST is not the same object as a Gabriel or RNG graph. It minimises total tree length; the other graphs retain edges according to local geometric neighbourhood tests. In the Euclidean plane, an EMST is contained in the RNG, with tie and degeneracy conventions handled consistently.

## Relationship map

~~~mermaid
flowchart TD
    A[Finite Euclidean point set] --> B[Delaunay triangulation]
    A --> C[Gabriel graph]
    A --> D[Relative neighbourhood graph]
    A --> E[Euclidean MST]
    D --> C
    C --> B
    E --> D
    A --> F[Beta-skeleton variants]
    A --> G[Yao graph variants]
~~~

The containment relationships shown are for standard Euclidean definitions, with degeneracies and ties treated consistently. The diagram is not a claim that every implementation emits identical edges for cocircular or collinear inputs.

## Construction choices

A simple all-pairs implementation is valuable as a correctness oracle for small data:
- Gabriel graph: examine each candidate pair against all other points.
- RNG: examine each candidate pair against all other points.
- Euclidean MST: construct the complete weighted graph and run Kruskal.

These direct methods are intentionally not the fastest known algorithms. For larger planar point sets, use Delaunay-based constructions or specialised geometric algorithms. The literature describes linear-time construction of the RNG from a Delaunay triangulation under stated assumptions.

## Scalable construction routes

The direct implementations are useful as small-input correctness oracles. They are not the only way to build these graphs.

### Delaunay filtering for Gabriel and relative-neighbourhood graphs

For a finite planar Euclidean point set in general position, the Delaunay triangulation is a sparse candidate graph: it has linear size and contains the Euclidean minimum spanning tree, Gabriel graph and relative-neighbourhood graph under consistent definitions and tie handling.

This changes the construction strategy:

1. Construct the Delaunay triangulation.
2. Enumerate only its candidate edges.
3. Apply the exact Gabriel-disk or RNG-lune emptiness test to each candidate.
4. Preserve the chosen open/closed boundary and degeneracy policy.

Because the candidate graph has O(n) edges in the planar case, the filtering stage is linear in the candidate count when the emptiness test is constant-time or supported by the required local structure. The Delaunay construction itself is typically O(n log n). Lingas gives a linear-time construction of the RNG from a Delaunay triangulation and extends the result to beta-skeletons in the range 1 <= beta <= 2 under stated metric conditions. In particular, the Euclidean case is covered.

This is a different implementation from testing every possible point pair. The Delaunay candidate property is a theorem that must match the graph definition and metric; it is not permission to filter arbitrary proximity graphs through a Delaunay triangulation.

### Yao graph construction is a separate problem

A Yao graph asks each point to choose its nearest neighbour in each of k angular cones. A naïve implementation checks every other point for every source point, which is quadratic.

Funke, Sanders and Georgiadis report an implementation of an optimal O(n log n)-time Yao graph construction. Their work describes the priority-queue and data-structure engineering required to realise the bound, as well as a uniform-grid variant designed for medium-sized inputs. This is a useful reminder that a theoretical bound and a working implementation are different deliverables: event ordering, cone boundaries, ties and queue updates all matter.

The Yao construction should not be conflated with Delaunay filtering. The graph family has a different nearest-in-cone definition and requires its own candidate-search method.

### What the current package covers

The current Python package remains a small-input baseline for Gabriel, RNG, one lune-based beta-skeleton variant, one Yao variant and Euclidean MST. It does not implement Lingas's Delaunay-based construction or the optimal Yao algorithm. The research above is a design direction for a future scalable package, not a claim that the current code has those bounds.

## Runnable baseline

The companion package implements small-data baselines for Gabriel, RNG, the lune-based beta-skeleton for 1 ≤ beta ≤ 2, the undirected-union Yao graph and Euclidean MST. It is designed for learning and testing, not millions of points.

- [Implementation](../../implementations/python/proximity-graphs/README.md)
- [Intern walkthrough](../../implementations/python/proximity-graphs/implementation-walkthrough.md)
- [Tests](../../implementations/python/proximity-graphs/test_proximity_graphs.py)

The beta-skeleton implementation is specifically the lune-based family for beta in [1,2], with beta=1 matching the open-disk Gabriel rule and beta=2 matching the open-lune RNG rule. For intermediate beta values, a small relative floating-point tolerance treats near-boundary points as ties; the scale and tolerance must be considered when using coordinates with very different magnitudes. The Yao implementation uses equal-angle cones, nearest-neighbour selection, input-index tie-breaking and undirected union symmetrisation. These conventions are part of the API; other beta-skeleton or Yao variants may produce different graphs.

## Try it

Use a point set with a dense cluster and several outliers. Plot all three implemented graphs on the same points. Compare edge counts, total edge length, connected components and the effect of adding one point.

Then construct a nearly cocircular point set and document how your boundary convention affects ties.

## References

- Gabriel, K. R. and Sokal, R. R. (1969), [A new statistical approach to geographic variation analysis](https://doi.org/10.2307/2412323), Systematic Zoology, 18, 259–278.
- Matula, D. W. and Sokal, R. R. (1980), [Properties of Gabriel graphs relevant to geographic variation research and the clustering of points in the plane](https://doi.org/10.1111/j.1538-4632.1980.tb00031.x), Geographical Analysis, 12, 205–222.
- Lingas, A. (1994), [A linear-time construction of the relative neighborhood graph from the Delaunay triangulation](https://doi.org/10.1016/0925-7721(94)90018-3), Computational Geometry, 4(4), 199–208.
- Funke, D., Sanders, P. and Georgiadis, L. (2023), [Efficient Yao Graph Construction](https://doi.org/10.4230/LIPIcs.SEA.2023.20), 21st International Symposium on Experimental Algorithms (SEA 2023), 20:1–20:20.
- [Computational Geometry: An Introduction](https://www.cs.rpi.edu/~cutler/classes/computationalgeometry/F23/references/Computational_Geometry_An_Introduction.pdf).

**Scope:** small-input implementations cover Gabriel, RNG, one lune-based beta-skeleton variant, one explicitly specified Yao graph variant and Euclidean MST. Efficient Delaunay-based construction and proven large-scale bounds are not implemented.
