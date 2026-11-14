# Intern walkthrough: Dijkstra and A*

## Objective

Implement a reliable shortest-path baseline on a weighted directed graph, then introduce A* without changing the graph model.

## Step 1 — State the graph contract

The graph maps each node to outgoing (neighbour, cost) pairs. Direction is explicit: if travel is allowed both ways, both arcs must be present. Edge costs must be finite and non-negative.

## Step 2 — Maintain best-known labels

The best mapping stores the cheapest discovered cost to each node. The priority queue stores candidate labels. When an outdated queue entry is popped, skip it.

## Step 3 — Reconstruct the path

Whenever a cheaper route to a neighbour is found, store its predecessor. When the goal is removed with its current best label, walk backward through predecessors and reverse the result.

## Step 4 — Add A*

A* changes queue priority from g to g+h. The path cost g remains the value used for relaxation. The heuristic must never overestimate the true remaining cost if an optimal result is required.

## Step 5 — Validate with an oracle

A* with a zero heuristic must return the same result as Dijkstra. Add fixtures for unreachable goals, zero-cost edges, equal-cost paths and directed asymmetry.

## Step 6 — Do not overgeneralise

Real routing may require edge-based state for turn restrictions, time-dependent costs, vehicle profiles and network snapping. These concerns belong in the graph model and search state, not in a map drawing layer.
