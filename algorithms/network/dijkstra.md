# Dijkstra's algorithm: find the least-cost route through a network

- **Stable ID:** `SA-NETWORK-DIJKSTRA-SINGLE-SOURCE`
- **Kind:** algorithm
- **Domain:** graph theory, network analysis and routing
- **Status:** researched teaching record; implementation and tests added; independent review pending
- **Version:** 0.1
- **Source inventory:** Section 1, pages 2–3 — shortest paths and network analysis
- **Related methods:** breadth-first search, A*, Bellman–Ford, Floyd–Warshall, contraction hierarchies, time-dependent routing

## The question

You are at one node in a network. What is the least-cost way to reach every other node?

The network might be a road map, a rail network, a computer network or a graph of places connected by some kind of movement. Each connection has a cost. That cost could represent distance, travel time, money, energy or another quantity that can be added along a route.

Dijkstra's algorithm finds shortest paths from one starting node to every reachable node, provided that every edge has a **non-negative weight**.

It is a foundational algorithm for understanding route planning. It also gives us a useful way to reason about why a route is optimal, rather than simply drawing a line between two places.

## A network is more than a map

Represent the network as a weighted graph (G=(V,E)):

- (V) is the set of nodes;
- (E) is the set of directed or undirected edges;
- (w(u,v)) is the non-negative cost of travelling from node (u) to node (v).

A path is a sequence of connected edges. Its total cost is the sum of its edge weights:

$$
C(P)=\sum_{(u,v)\in P}w(u,v).
$$

The shortest path minimises this total cost. It does not necessarily use the fewest edges, and it does not necessarily follow the visually shortest line on a map.

## The key idea: make the closest unsettled node final

Dijkstra's algorithm keeps a tentative best-known distance from the source to each node.

1. Give the source a distance of zero. Give every other node infinity.
2. Put the source in a priority queue ordered by tentative distance.
3. Remove the node with the smallest tentative distance.
4. If this queue entry is stale, skip it.
5. Otherwise, examine each outgoing edge and try to improve the neighbour's distance.
6. When a shorter route is found, update the distance, record the predecessor and add a new queue entry.
7. Continue until the queue is empty.

The predecessor of a node records the previous node on the best route found so far. Following predecessors backwards reconstructs a route.

## Edge relaxation

Suppose the best-known distance to (u) is (d(u)), and an edge from (u) to (v) has cost (w(u,v)).

The route through (u) proposes this alternative distance:

$$
d_{\mathrm{candidate}}(v)=d(u)+w(u,v).
$$

If that value is smaller than the current estimate, update it:

$$
\text{if }d(u)+w(u,v)<d(v):
$$

$$
\begin{aligned}
d(v)&\leftarrow d(u)+w(u,v),\\
\operatorname{pred}(v)&\leftarrow u.
\end{aligned}
$$

This operation is called **relaxation**. It is the repeated comparison that gradually improves the route estimates.

## A worked example

Consider these directed connections:

| From | To | Cost |
|---|---|---:|
| S | A | 4 |
| S | B | 2 |
| B | A | 1 |
| A | C | 3 |
| B | C | 5 |
| A | T | 7 |
| C | T | 1 |
| B | T | 9 |

Start at (S).

- Initially, (d(S)=0); all other distances are infinity.
- Process (S): discover (A=4) and (B=2).
- Process (B): improve (A) from 4 to 3; discover (C=7) and (T=11).
- Process (A): improve (C) from 7 to 6 and (T) from 11 to 10.
- Process (C): improve (T) from 10 to 7.
- Process (T): its distance is final.

The least-cost route from (S) to (T) is:

$$
S\rightarrow B\rightarrow A\rightarrow C\rightarrow T
$$

with total cost:

$$
2+1+3+1=7.
$$

Notice that the route is not the one with the fewest edges. Its total cost is lower.

## Why the greedy choice is safe

When the algorithm removes the unsettled node with the smallest tentative distance, that distance is final.

The non-negative edge condition is essential. Any alternative route to this node that goes through another unsettled node must first reach that other node at a distance no smaller than the one already selected. Adding a non-negative edge cannot make that alternative route cheaper.

This is the reason Dijkstra can safely finalise nodes in increasing order of distance. Negative edge weights break this argument.

## A useful implementation detail: stale priority-queue entries

A binary heap does not normally support changing an item's priority in place. A common implementation inserts a new queue entry whenever a distance improves.

An older entry for the same node can remain in the heap. When it is eventually removed, compare its stored distance with the current best distance. If it is larger, skip it.

This is often called a *lazy decrease-key* strategy. It keeps the implementation simple while preserving the algorithm's result.

## Complexity

With an adjacency-list graph and a binary heap, each successful relaxation can add a queue entry. The resulting time complexity is:

$$
O((|V|+|E|)\log |V|)
$$

for the usual simple-graph setting, commonly written as (O((|V|+|E|)\log |V|)). The graph, distance table, predecessor table and priority queue require (O(|V|+|E|)) storage in total.

A simple array-based implementation that scans all unsettled vertices for the next minimum takes (O(|V|^2)) time. Which implementation is preferable depends on graph size and density.

## When Dijkstra is the wrong tool

| Situation | Better starting point | Why |
|---|---|---|
| Every edge has equal cost and only hop count matters | Breadth-first search | It finds shortest paths in an unweighted graph in (O(|V|+|E|)) |
| Some edges can have negative weights | Bellman–Ford | Dijkstra's finalisation argument no longer holds |
| You need all-pairs shortest paths on a small dense graph | Floyd–Warshall | It computes distances between every pair |
| You have one destination and a useful lower-bound heuristic | A* | It can focus the search toward the target |
| Edge costs change with departure time | Time-dependent shortest-path methods | A single static edge weight does not describe the network |
| You need a route through many stops in a fixed order or with service constraints | A routing optimisation model | This is not a single-source shortest-path problem |

## What a route cost really means

In a transport network, edge weights need careful interpretation.

- **Distance:** length of a road or path segment.
- **Travel time:** expected time for traversing the segment under a stated traffic or timetable condition.
- **Generalised cost:** a model that combines time, money, transfers or other disutilities.

The algorithm minimises the number you provide. It does not decide whether that number represents a good passenger experience, a safe route or an equitable transport service.

For time-dependent travel, the cost of an edge may depend on when the traveller reaches it. That requires a model beyond the static weighted graph used in this lesson.

## Try it yourself

1. **Predict:** If you reduce the cost of edge (B\rightarrow A), which later distances might change?
2. **Trace:** Write the priority queue after each node is processed. Keep old entries when a distance improves.
3. **Break it:** Add a negative edge. Why can the finalised distance become wrong?
4. **Compare:** Run breadth-first search on the same graph after making every edge cost 1. Compare the route objective.
5. **Change the meaning:** Replace distance with travel time. What data would you need to justify those weights?
6. **Extend:** Add a target-only stopping condition. When is it safe to stop?

## Runnable material

- [Python implementation, tests and walkthrough](../../implementations/python/dijkstra/README.md)
- [Interactive Dijkstra lab](../../notebooks/dijkstra-lab.ipynb)

## References

1. Dijkstra, E. W. (1959). “A Note on Two Problems in Connexion with Graphs.” *Numerische Mathematik*, 1, 269–271. [https://doi.org/10.1007/BF01386390](https://doi.org/10.1007/BF01386390)
2. [NetworkX: Dijkstra's algorithm](https://networkx.org/documentation/stable/reference/algorithms/shortest_paths/dijkstra.html) — a maintained reference for the non-negative weight condition, relaxation, priority queues and implementation trade-offs.
3. [NetworkX: shortest paths](https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html) — compares BFS, Dijkstra, Bellman–Ford, Floyd–Warshall and other shortest-path methods.

## Review still required

- Compare the teaching implementation against NetworkX on generated directed and undirected graphs.
- Add an example using a documented street or transit network with clear data provenance and cost semantics.
- Extend the path with A* and a comparison of heuristic admissibility.
- Do not treat static edge weights as a model of timetable or time-dependent travel.

## Change history

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-11-14 | Initial shortest-path lesson, Python implementation and interactive lab |
