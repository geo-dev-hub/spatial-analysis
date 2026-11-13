# How the Dijkstra implementation works

This walkthrough follows `dijkstra.py` from input validation to path reconstruction.

## 1. Represent the network

The input is an adjacency mapping. Each node has a list of its outgoing neighbours and the cost of each edge.

For a directed edge from A to B, include B in A's adjacency list. To represent an undirected connection, include both A-to-B and B-to-A entries.

The algorithm does not need coordinates. It only needs nodes, edges and weights.

## 2. Validate weights and collect vertices

The implementation converts each weight to a float and rejects negative, infinite or NaN values. It also includes neighbour nodes that do not have their own adjacency entry; these are treated as nodes with no outgoing edges.

The source must be present in the resulting vertex set.

## 3. Initialise the distance and predecessor tables

Every distance starts at infinity, except the source, which starts at zero:

$$
d(s)=0,\qquad d(v)=\infty\quad(v\ne s).
$$

Every predecessor starts as `None`. A predecessor is filled in when a better route to that node is found.

## 4. Use a priority queue

The heap stores the next node to examine, ordered by its tentative distance. A sequence number breaks ties so Python never needs to compare node objects with one another.

This matters when graph nodes are custom objects that cannot be sorted.

## 5. Relax each outgoing edge

For each neighbour, calculate the route through the current node:

$$
d_{\mathrm{candidate}}=d(u)+w(u,v).
$$

If it improves the neighbour's current distance, update the distance and predecessor, then push a new queue entry.

## 6. Skip stale entries

A node can receive several improving distances before its best entry is removed from the heap. Older entries remain in the heap, but they are no longer useful.

When an entry is popped, compare its distance with the current best distance. If it is larger, skip it. This is the lazy decrease-key pattern.

## 7. Reconstruct a path

To recover a path to a target, follow predecessor links backwards until reaching the source, then reverse the list.

If the target is unknown or unreachable, `path_to` returns `None`. If the target is the source, the path contains only the source.

## 8. Reproduce and inspect

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

The tests cover weighted alternatives, directed and undirected representations, disconnected nodes, zero-weight edges, duplicate edges, non-orderable node objects, invalid weights and path reconstruction.

## 9. What this implementation does not prove

The implementation solves a static graph problem. It does not model changing traffic, scheduled services, turn restrictions, passenger transfers or time-dependent edge costs. A shortest path is only as meaningful as the graph and cost model supplied to it.
