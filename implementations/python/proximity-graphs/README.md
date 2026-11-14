# Proximity graph baselines

Implements:
- Gabriel graph using the open-diameter-disk definition;
- relative neighbourhood graph using the open-lune definition;
- lune-based beta-skeleton for beta in [1,2] (beta=1 Gabriel, beta=2 RNG under the stated open-region convention);\n- Yao graph using equal-angle cones, nearest selection, deterministic tie-breaking and undirected union;\n- Euclidean minimum spanning tree using Kruskal over all point pairs.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Contract and limits

Points are distinct finite planar x,y pairs. Edges are returned as input-index pairs; MST edges also include Euclidean length. The implementation uses direct all-pairs tests and is intended for small datasets and correctness checks, not large production workloads.

The strict interior tests implement open-region conventions. Points exactly on a Gabriel disk or RNG lune boundary do not block an edge. Tie conventions should be documented when comparing to another library.

The implementations are O(n³) for Gabriel/RNG/beta-skeleton and O(n²) for Yao/MST candidate generation. They are transparent small-data baselines, not the efficient Delaunay-based constructions from the literature.


## Delaunay-filtered variants

The package also exposes `delaunay_filtered_gabriel_graph` and `delaunay_filtered_rng`. They construct a SciPy/Qhull Delaunay triangulation, then apply the corresponding open-region blocker test only to triangulation edges. This reduces the candidate set from all O(n²) pairs to O(n) planar edges, and the straightforward blocker scan gives an O(n²) total baseline.

These functions are intended for non-degenerate, general-position Euclidean point sets. Qhull selects one triangulation in cocircular cases, so boundary-tie edges omitted by that triangulation may also be absent from the filtered graph. The implementation is not the specialised linear-time RNG post-processing algorithm in Lingas (1994). Compare the Delaunay-filtered results with the all-pairs reference functions on general-position fixtures.
