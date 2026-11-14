# Intern walkthrough: five proximity graph constructions

## Objective

Turn a finite point set into five different graph structures. The point set is shared; the edge rule changes.

## Step 1 — Establish the metric

The package assumes Euclidean distance in a planar coordinate system. Longitude and latitude are not automatically a suitable Euclidean plane for distance-based graph construction.

## Step 2 — Gabriel graph

For candidate endpoints u and v, another point w blocks the edge if (w-u) dot (w-v) is strictly negative. This avoids square roots and directly tests whether w lies inside the diameter disk. Points on the boundary do not block the edge.

## Step 3 — Relative neighbourhood graph

For candidate edge uv, a third point blocks it when its distance to both endpoints is strictly less than the endpoint distance. This is the open-lune definition.

## Step 4 — Euclidean MST

Generate every pair with its Euclidean length, sort the candidate edges and apply Kruskal's algorithm with a disjoint-set structure. Stop after n-1 edges.

## Step 5 — Extend the neighbourhood model

The lune-based beta-skeleton moves from the diameter disk at beta=1 to the relative-neighbourhood lune at beta=2. The implementation uses a small relative floating-point boundary tolerance for intermediate beta values. The Yao graph partitions directions into equal-angle cones and selects one nearest neighbour in each cone. This package returns the undirected union of those directed selections.

## Step 6 — Compare and test

Run the tests and inspect the square and intermediate-point fixtures. For standard Euclidean definitions, RNG edges are a subset of Gabriel edges, and the Euclidean MST is contained in the RNG when ties and degeneracies are treated consistently.

## Step 7 — Understand the scale limit

The direct Gabriel, RNG and beta-skeleton routines test O(n²) candidate pairs against up to O(n) blockers, so they are O(n³). Yao selects cone neighbours by scanning all other points and is O(n²). The MST materialises O(n²) candidate edges and sorts them. These are transparent reference implementations, not scalable geometric construction algorithms.


## Step 8 — Use Delaunay edges as a sparse candidate set

The package now includes Delaunay-filtered Gabriel and RNG variants. Instead of testing every possible point pair, they:

1. Build a planar Delaunay triangulation with SciPy/Qhull.
2. Extract its undirected triangle edges.
3. Apply the same open-disk or open-lune blocker predicate to those candidates.

For a non-degenerate planar triangulation, there are only O(n) candidate edges. The current implementation still scans all points for each candidate, so its total bound is O(n²), rather than the specialised O(n) RNG filtering result in Lingas (1994). This distinction matters: using a sparse candidate graph is an improvement over the cubic all-pairs reference, but it is not the final optimal algorithm.

Cocircular points require special care. A triangulation chooses one diagonal, while an open-disk Gabriel definition may include both diagonals when the opposite points lie exactly on the disk boundary. Do not use the Delaunay-filtered variant as an exact boundary-tie oracle for such inputs.
