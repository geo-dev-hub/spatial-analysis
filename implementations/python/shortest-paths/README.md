# Shortest-path teaching implementation

Implements four shortest-path baselines for explicit weighted graphs: Dijkstra and A* for non-negative edge weights, Bellman–Ford for negative edges, and Floyd–Warshall for all-pairs shortest distances.

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

A* requires an admissible heuristic for optimality. A consistent heuristic is recommended. Dijkstra and A* require finite non-negative edge weights. Bellman–Ford and Floyd–Warshall accept finite negative edges but detect and reject negative cycles. The caller is responsible for representing one-way edges, access rules, turn restrictions and the chosen cost model.

This is a teaching implementation, not a production routing engine. It does not include bidirectional search, ALT, contraction hierarchies, hub labels, customizable route planning, time-dependent costs or transit routing.
