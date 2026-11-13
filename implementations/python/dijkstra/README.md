# Dijkstra's algorithm: Python example

This example implements single-source shortest paths for a weighted directed graph using Python's `heapq`.

## Run it

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Use it

```python
from dijkstra import dijkstra

graph = {
    "S": [("A", 4), ("B", 2)],
    "B": [("A", 1), ("C", 5), ("T", 9)],
    "A": [("C", 3), ("T", 7)],
    "C": [("T", 1)],
    "T": [],
}

result = dijkstra(graph, "S")
print(result.distances["T"])  # 7.0
print(result.path_to("T"))    # ['S', 'B', 'A', 'C', 'T']
```

## Input contract

- The graph is an adjacency mapping: each node maps to an iterable of `(neighbour, weight)` pairs.
- Edges are directed. Add the reverse adjacency entry to represent an undirected edge.
- Weights must be finite and non-negative.
- Neighbours without their own mapping entry are treated as sink nodes.
- The source must appear as a graph key or neighbour.
- Equal-cost alternatives keep the predecessor discovered first.

## Scope and limitations

This is a teaching implementation of static single-source Dijkstra. It does not support negative weights, time-dependent travel costs, turn restrictions, multimodal transfer penalties or route geometry. It uses floating-point weights; applications requiring exact arithmetic or strict reproducibility should define a suitable numeric model.

See the [Dijkstra lesson](../../../algorithms/network/dijkstra.md) and [step-by-step walkthrough](implementation-walkthrough.md).
