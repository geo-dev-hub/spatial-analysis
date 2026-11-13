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
