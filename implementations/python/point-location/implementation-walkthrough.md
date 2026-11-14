# Intern walkthrough: build a static slab point locator

## Objective

Preprocess a restricted planar subdivision so repeated queries can identify which polygon face contains a point. The implementation is deliberately narrower than a general trapezoidal map.

## Step 1 — Define the subdivision

Input is a mapping from face identifiers to polygon rings. The polygons must be valid and pairwise interior-disjoint. The first ring is the shell; later rings are holes. Boundaries must not cross.

## Step 2 — Create x-events

Collect all vertex x-coordinates. Consecutive event coordinates define open vertical slabs. Within a slab, non-crossing edges preserve their vertical order.

## Step 3 — Build each slab's crossing groups

At the slab midpoint, find non-vertical edges crossing the slab and sort them by y. Coincident crossings are grouped. Sweeping upward toggles polygon membership; the face after each crossing group is stored.

## Step 4 — Query

Binary-search the x-event array. For an interior slab, binary-search the preordered crossing groups using the edge's y-coordinate at query x. The last crossing below the query determines the containing face.

A query on an event line uses a direct boundary-aware point-in-polygon fallback. This is slower, but it keeps vertical edges and vertices explicit.

## Step 5 — Test shared boundaries and holes

The test suite includes adjacent faces, a shared edge, a hole, a vertical boundary, a vertex and overlapping input polygons. The overlapping case is rejected because it violates the subdivision contract.

## Step 6 — State the complexity honestly

An edge can cross many x-slabs, so the straightforward structure can use O(n²) storage. Interior-slab queries use logarithmic comparisons. This is not the randomized incremental trapezoidal map in Seidel's paper and does not inherit its bounds.
