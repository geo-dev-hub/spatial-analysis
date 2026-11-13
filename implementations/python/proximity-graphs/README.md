# Proximity graph baselines

Implements:
- Gabriel graph using the open-diameter-disk definition;
- relative neighbourhood graph using the open-lune definition;
- Euclidean minimum spanning tree using Kruskal over all point pairs.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Contract and limits

Points are distinct finite planar x,y pairs. Edges are returned as input-index pairs; MST edges also include Euclidean length. The implementation uses direct all-pairs tests and is intended for small datasets and correctness checks, not large production workloads.

The strict interior tests implement open-region conventions. Points exactly on a Gabriel disk or RNG lune boundary do not block an edge. Tie conventions should be documented when comparing to another library.

Yao graphs and beta-skeletons are not implemented in this package.
