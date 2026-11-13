# Network routing foundations: from graph to journey

A route planner is only as sound as the network model beneath it. This path starts with weighted graphs and then moves toward the details that make road and transit routing different from a classroom shortest-path problem.

## 1. Define the graph and cost

Start with [Shortest paths](../algorithms/networks/shortest-paths.md). Decide whether edges represent distance, travel time, energy, money or another cost. State whether the graph is directed and how disconnected components are represented.

## 2. Implement the baseline

Run the [Dijkstra and A* package](../implementations/python/shortest-paths/README.md). Compare path cost, predecessor reconstruction and the effect of an admissible heuristic.

## 3. Add road-network constraints

Extend the model with one-way streets, access rules, turn penalties and turn restrictions. Decide whether a node-based graph is sufficient or whether the search state must include the incoming edge.

## 4. Scale repeated queries

Study ALT landmarks, bidirectional search, contraction hierarchies, hub labels and customizable route planning. Compare their preprocessing, memory, query and metric-update trade-offs.

## 5. Move toward transit and time-dependent networks

The source inventory separately identifies RAPTOR, Connection Scan, stochastic and multimodal routing. These need their own problem definitions and implementation paths; they are not simply Dijkstra with different labels.

## Practice

Use the [Core GIS continuation exercises](../exercises/core-gis-continuation.md), then design a directed graph with a turn restriction and a time-dependent edge. Document the state representation and cost function before choosing an algorithm.
