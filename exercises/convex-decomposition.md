# Exercise: from triangles to convex pieces

## Goal

Understand how a triangulation can be simplified into a convex partition, and why a useful partition is not always a minimum-piece partition.

## Start with a triangulation

Use the concave polygon from the ear-clipping lab:

~~~python
ring = [(0, 0), (6, 0), (6, 5), (4, 2), (2, 4), (0, 5)]
~~~

Run the [ear-clipping implementation](../implementations/python/ear-clipping/README.md) and draw its triangles. Treat each internal triangle edge as a candidate merge boundary.

## Part 1 — Identify candidate merges

For each internal diagonal:

1. Identify the two triangles sharing it.
2. Construct the boundary of their union.
3. Check whether the merged polygon is convex.
4. If it is convex, mark the diagonal as removable.
5. If it is not convex, retain the diagonal.

Do not test convexity by looking only at the two endpoints of the removed diagonal. Inspect all turns around the merged boundary and ensure the union is a valid simple polygon.

## Part 2 — Explain the objective

Write down which of these goals your proposed decomposition optimizes:

- minimum number of convex pieces;
- no Steiner vertices;
- short internal boundary;
- pieces below a maximum size;
- small deviation from a preferred shape;
- tolerance for small concavities.

Explain why these objectives can lead to different answers.

## Part 3 — Validate the partition

For each output piece, record:
- its ordered boundary;
- its signed area;
- whether it is convex;
- which original boundary edges it contains.

Then verify that the union equals the input, pairwise interiors do not overlap, and the total area matches. Explain why the area sum alone cannot prove the absence of overlap and gaps.

## Part 4 — Research comparison

Compare the following approaches using the references in the lesson:

1. Hertel–Mehlhorn: triangulate, then remove unnecessary diagonals.
2. Greene: optimal dynamic programming and sweep-line approximation.
3. Lien–Amato: tolerance-based approximate convex decomposition.

For each, state the input assumptions, objective, output guarantee and complexity only where the source specifies it. Do not transfer a bound from one variant to another.

## Part 5 — Design the next implementation

Propose a small Hertel–Mehlhorn-style teaching package. Specify:
- how triangles and shared edges are represented;
- how adjacent triangles are found;
- how a candidate merged boundary is assembled;
- how convexity and topology are checked;
- how stale candidate edges are invalidated after a merge;
- how coverage, overlap and area are tested.

Your implementation must label itself as an approximation unless it implements and proves an optimal algorithm.

## Submission

Submit a diagram of the original triangulation and merged pieces, a table of candidate diagonals and decisions, your validation results, and a short explanation of the difference between exact convex partitioning and approximate convex decomposition.
