# Spatial indexing: find the places worth checking

**Status:** Four lesson topics are available: a packed R-tree, filter-and-refine spatial joins, point-region quadtrees and k-d tree nearest-neighbour search. The k-d tree now has a tested static 2D teaching implementation and walkthrough. The quadtree remains a conceptual draft; neither new topic has a dedicated notebook yet.

## Why an index helps

A spatial query often starts with a simple question: which features might overlap this window? Which buildings could be within a search area? Which roads could intersect a proposed corridor?

Checking every geometry can be expensive. A spatial index helps narrow the search to a smaller set of candidates.

The index does not replace the exact geometry operation. It helps decide which objects are worth checking.

## Follow the first lessons

### 1. Organise bounding boxes into a tree

[Read the STR-packed R-tree lesson](../algorithms/indexing/str-packed-rtree.md) and run its [interactive notebook](../notebooks/str-packed-rtree-lab.ipynb).

You will learn:
- how a minimum bounding rectangle represents a geometry for indexing;
- how internal nodes group nearby bounding boxes;
- how Sort-Tile-Recursive packing builds a static hierarchy;
- how a query prunes branches that cannot intersect;
- why envelope candidates still need exact predicate checks.

Run the [teaching implementation](../implementations/python/str-packed-rtree/README.md) and compare its results with a brute-force scan.

## A useful distinction

A spatial index answers: “Which objects could match?”

The exact geometry operation answers: “Which of those objects actually match?”

Keeping those steps separate is the basis of filter-and-refine spatial query processing.

## Try it

1. Change the node capacity. Do the results change, or only the grouping?
2. Create overlapping bounding boxes. How does that affect query selectivity?
3. Find a concave polygon whose bounding box contains empty space. Query that empty space and compare candidates with exact intersections.
4. Use Shapely's STRtree with and without a predicate. Explain the difference.

## 2. Use the index to join two geometry layers

[Read the filter-and-refine spatial join lesson](../algorithms/query-processing/filter-refine-spatial-join.md) and run its [interactive notebook](../notebooks/filter-refine-spatial-join-lab.ipynb).

You will see how an STRtree narrows the possible geometry pairs, how the exact predicate refines those candidates and why predicate direction and boundary rules matter. The [tested Shapely implementation](../implementations/python/spatial-join/README.md) returns stable pairs of original input indices.

## Compare the structures

The [quadtree lesson](../algorithms/indexing/quadtree.md) introduces recursive spatial subdivision, with a focus on point-region trees and their stopping rules. The [k-d tree lesson](../algorithms/indexing/kd-tree-nearest-neighbour.md) introduces exact nearest-neighbour search by branch-and-bound and explains why coordinate metrics and dimensionality matter.

Run the [k-d tree teaching implementation](../implementations/python/kd-tree/README.md) and follow its [step-by-step walkthrough](../implementations/python/kd-tree/implementation-walkthrough.md). Use the [quadtrees and k-d trees exercises](../exercises/spatial-indexing-quadtrees-kdtree.md) to compare both structures with brute-force baselines. The quadtree exercise is currently a design-and-analysis task; a runnable implementation is still to come.

## What comes next

The next additions to this path will cover:
- dynamic R-tree variants and update operations;
- octrees, ball trees, VP-trees and other structures;
- range, reverse nearest-neighbour and closest-pair queries;
- space-filling curves and grid systems such as Morton, Hilbert, H3 and S2;
- spatial skyline, top-k and geofencing queries.

Each index makes different trade-offs. We will compare them only after the query workload, update pattern, dimensionality and data shape are clear.
