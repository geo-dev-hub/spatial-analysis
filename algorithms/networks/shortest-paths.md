# Shortest paths: from graph search to road routing

A routing problem starts with a graph, not a map. The graph represents which movements are possible; edge weights represent the cost being minimised. A road network may use travel time, distance, toll, energy or a multi-criteria cost.

The shortest path is the path with minimum total edge cost under that model. It is not necessarily the geometrically shortest line.

## Model the network first

A directed weighted graph is G=(V,E,w), where V is the set of vertices, E is the set of directed edges and w(e) is the edge cost.

For a path p=(e1,...,ek), its cost is:

$$
C(p)=\sum_{i=1}^{k} w(e_i)
$$

For Dijkstra's algorithm, all edge weights must be non-negative. Negative edges require a different algorithm and negative cycles make finite shortest paths undefined for affected pairs.

Road-network modelling adds details that ordinary graph examples omit:
- one-way restrictions and access rules;
- turn restrictions and turn penalties;
- edge-based versus node-based state;
- time-dependent travel costs;
- vehicle and mode restrictions;
- disconnected components and snapping a query to the network.

## Core algorithms

| Algorithm | Main idea | Conditions and role |
|---|---|---|
| Dijkstra | Expand the unsettled vertex with smallest known distance | Non-negative edge weights; foundational single-source algorithm |
| A* | Order by f(v)=g(v)+h(v) using a lower-bound heuristic | Optimal with an admissible heuristic under the algorithm's reopening/consistency conditions |
| Bellman–Ford | Repeatedly relax all edges | Supports negative edges and detects reachable negative cycles |
| Floyd–Warshall | Dynamic programming over allowed intermediate vertices | All-pairs shortest paths; O(V³) time |
| Bidirectional Dijkstra | Search forward from source and backward from target | Directed reverse graph needed; stopping condition must be correct |
| ALT | A* with landmark-based triangle-inequality lower bounds | Preprocessing distances to/from selected landmarks |
| Contraction hierarchies | Contract less important vertices and add shortcut edges | Preprocessing-heavy, fast queries on suitable road networks |
| Hub labeling | Store selected forward/backward hub distances | Large preprocessing/index trade-off; query intersects labels |
| Customizable route planning | Separate metric-independent partitioning from metric customization | Useful when topology is stable but edge costs change |

These are families, not one universally ranked list. Performance depends on graph structure, query distribution, update frequency, memory budget and cost model.

## Dijkstra and A*

Dijkstra maintains the best known cost g(v) from the source. When a vertex is removed from the priority queue with its current best label, that label is final for non-negative edge weights.

A* adds a heuristic h(v), an estimate of the remaining cost to the goal:

$$
f(v)=g(v)+h(v)
$$

For optimality, the heuristic must not overestimate the true remaining cost (admissibility). A consistent heuristic additionally satisfies the triangle inequality across every edge. The implementation must match the heuristic contract; a visually plausible straight-line heuristic is only a lower bound when the edge-cost model supports that relationship.

For example, straight-line distance is not an admissible estimate of travel time unless it is scaled by a valid upper speed bound and the graph's travel-time costs obey the assumptions.

## Road routing is not just A*

~~~mermaid
flowchart TD
    A[Road network data] --> B[Build directed graph]
    B --> C[Apply access and turn rules]
    C --> D[Choose cost model]
    D --> E{Query volume and update pattern}
    E -->|Few queries| F[Dijkstra or A*]
    E -->|Many static queries| G[ALT or contraction hierarchies]
    E -->|Frequent metric changes| H[Customizable route planning]
    F --> I[Path reconstruction and validation]
    G --> I
    H --> I
~~~

A turn restriction may require the search state to include the incoming edge, not just the current intersection. Time-dependent routing requires evaluating edge costs at the time of traversal. A node-only static graph may therefore be an incorrect model for the requested journey.

## Runnable baseline

The companion implementation provides Dijkstra and A* over an explicit adjacency mapping. It supports directed graphs, rejects negative or non-finite edge weights, reconstructs a path and returns its total cost.

- [Implementation](../../implementations/python/shortest-paths/README.md)
- [Intern walkthrough](../../implementations/python/shortest-paths/implementation-walkthrough.md)
- [Tests](../../implementations/python/shortest-paths/test_shortest_paths.py)

It is a teaching baseline, not a production road router. It does not implement turn-expanded graphs, time-dependent edges, ALT, contraction hierarchies, hub labels or transit routing.

## Try it

Build a small directed road graph with a short route containing a slow edge, a longer route with a lower total travel time, a one-way edge and an unreachable destination. Run Dijkstra and A* with a zero heuristic. Then introduce a heuristic that is admissible for your chosen cost units. Compare path cost, expanded vertices and correctness.

Finally, add a turn restriction. Explain why the state may need to represent the incoming edge as well as the current node.

## References

- Dijkstra, E. W. (1959), [A note on two problems in connexion with graphs](https://doi.org/10.1007/BF01386390), Numerische Mathematik, 1, 269–271.
- Hart, P. E., Nilsson, N. J. and Raphael, B. (1968), [A formal basis for the heuristic determination of minimum cost paths](https://doi.org/10.1109/TSSC.1968.300136), IEEE Transactions on Systems Science and Cybernetics, 4(2), 100–107.
- Geisberger, R., Sanders, P., Schultes, D. and Delling, D. (2008), [Contraction Hierarchies: Faster and Simpler Hierarchical Routing in Road Networks](https://i11www.iti.kit.edu/extra/publications/gssd-chfsh-08.pdf).
- [OSRM routing algorithms overview](https://github.com/Project-OSRM/osrm-backend/wiki/Algorithms).

**Scope:** Dijkstra and A* have runnable baselines. The remaining algorithms are surveyed with their design roles and assumptions, not claimed as implemented.
