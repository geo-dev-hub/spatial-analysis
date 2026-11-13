# Shortest-path teaching implementation

Implements Dijkstra and A* for an explicit directed adjacency mapping.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
from shortest_paths import dijkstra, astar

graph = {
    "A": [("B", 2), ("C", 1)],
    "B": [("D", 2)],
    "C": [("B", 0.5)],
    "D": [],
}
print(dijkstra(graph, "A", "D"))
print(astar(graph, "A", "D", lambda node, goal: 0))
~~~

A* requires an admissible heuristic for optimality. A consistent heuristic is recommended. The graph must contain finite non-negative edge weights. The caller is responsible for representing one-way edges, access rules, turn restrictions and the chosen cost model.

This is a teaching implementation, not a production routing engine. It does not include ALT, bidirectional search, contraction hierarchies, time-dependent costs or transit routing.
