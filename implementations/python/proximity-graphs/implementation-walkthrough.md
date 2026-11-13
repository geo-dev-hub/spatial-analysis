# Intern walkthrough: three proximity graph constructions

## Objective

Turn a finite point set into three different graph structures. The point set is shared; the edge rule changes.

## Step 1 — Establish the metric

The package assumes Euclidean distance in a planar coordinate system. Longitude and latitude are not automatically a suitable Euclidean plane for distance-based graph construction.

## Step 2 — Gabriel graph

For candidate endpoints u and v, another point w blocks the edge if (w-u) dot (w-v) is strictly negative. This avoids square roots and directly tests whether w lies inside the diameter disk.

## Step 3 — Relative neighbourhood graph

For candidate edge uv, a third point blocks it when its distance to both endpoints is strictly less than the endpoint distance. This is the open-lune definition.

## Step 4 — Euclidean MST

Generate every pair with its Euclidean length, sort the candidate edges and apply Kruskal's algorithm with a disjoint-set structure. Stop after n-1 edges.

## Step 5 — Extend the neighbourhood model\n\nThe lune-based beta-skeleton moves from the diameter disk at beta=1 to the relative-neighbourhood lune at beta=2. The Yao graph partitions directions into equal-angle cones and selects one nearest neighbour in each cone. This package returns the undirected union of those directed selections.\n\n## Step 6 — Compare and test

Run the tests and inspect the square and intermediate-point fixtures. For the standard Euclidean definitions, RNG edges are a subset of Gabriel edges, and the Euclidean MST is contained in the RNG when ties and degeneracies are treated consistently.

## Step 7 — Understand the scale limit

The direct graph routines test O(n²) candidate pairs against up to O(n) blockers, so the simple Gabriel and RNG baselines are O(n³). The MST materialises O(n²) candidate edges and sorts them. These are transparent reference implementations, not scalable geometric construction algorithms.
