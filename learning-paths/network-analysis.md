# Network analysis: find your way through a graph

A network is a set of places or entities connected by links. The links might represent roads, rail services, rivers, pipes, communication lines or relationships between people.

Network analysis asks questions about how those connections work: how to get somewhere, which links matter most, where flows can pass and how a network behaves when something changes.

This path begins with the shortest-path problem. Other network methods will be added as their assumptions, examples and implementations are ready.

## Start with the route cost

A shortest path is not always the route with the fewest links or the shortest line on a map. It is the path with the lowest sum of the edge weights you choose.

Before running an algorithm, decide what a weight means:

- distance along a link;
- travel time under a stated condition;
- monetary cost;
- energy use or another additive cost.

The algorithm minimises the numbers it receives. It cannot decide whether those numbers represent a good transport service or a useful real-world outcome.

## First lesson: find the least-cost paths

[Dijkstra's algorithm](../algorithms/network/dijkstra.md)

Start from one node and calculate the least-cost route to every reachable node, assuming all edge weights are non-negative.

You will learn:

- how a weighted graph represents a network;
- how tentative distances and predecessors are stored;
- why the smallest tentative distance can be finalised safely;
- how edge relaxation improves a route;
- how a priority queue selects the next node;
- why negative weights invalidate the method.

Run the [Python implementation](../implementations/python/dijkstra/README.md), follow its [step-by-step walkthrough](../implementations/python/dijkstra/implementation-walkthrough.md), and use the [interactive lab](../notebooks/dijkstra-lab.ipynb) to inspect each queue step.

## Which shortest-path method should you consider?

| Method | A useful starting point | Important condition |
|---|---|---|
| Breadth-first search | Shortest paths by number of edges | Every edge has equal cost |
| Dijkstra | Single-source shortest paths with weighted edges | All edge weights are non-negative |
| Bellman–Ford | Single-source shortest paths when negative weights may occur | Can detect a reachable negative cycle |
| A* | A route to one target, with a useful heuristic | Heuristic must be appropriate for the required guarantee |
| Floyd–Warshall | Shortest paths between all pairs in a smaller graph | (O(|V|^3)) time and (O(|V|^2)) storage |

These algorithms solve related but different problems. Choose by graph structure, weight assumptions and query type—not by name recognition.

## What comes next

The next network lessons should connect the foundations to practical spatial problems:

1. A* and admissible heuristics for target-directed search.
2. Network distance, service areas and isochrones.
3. K-shortest and alternative routes.
4. Map matching: relating observed movement to a network.
5. Public transport routing, including RAPTOR and Connection Scan.
6. Time-dependent routing and multimodal transfers.

Each topic needs its own model of the network, cost semantics, input data and validation. A road shortest-path example is not automatically a public-transport journey planner.

## Check your understanding

1. Why can a route with more edges have a lower total cost?
2. Why does Dijkstra require non-negative weights?
3. What is stored in the predecessor table?
4. Why can an old priority-queue entry be ignored?
5. What would need to change if an edge's travel time depends on the time of day?

A useful next step is to work through the Dijkstra lab, then explain the result without looking at the code.
