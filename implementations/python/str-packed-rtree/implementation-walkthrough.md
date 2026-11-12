# How the STR-packed R-tree implementation works

This walkthrough follows `str_packed_rtree.py` from its input contract to its query result. The goal is not only to run the code, but to understand why each part exists.

## 1. Decide what the index stores

The implementation stores a 2D axis-aligned bounding box for each input item:

```python
Bounds = tuple[float, float, float, float]
```

The four numbers are `(minx, miny, maxx, maxy)`. The index does not store polygon rings or line coordinates. It stores the envelope that contains each geometry.

The original input position becomes the stable integer index returned by a query. This is important: callers can keep their own geometry and attribute arrays in the same order.

## 2. Represent entries and nodes

Two frozen dataclasses represent the hierarchy:

- `_Entry` stores an input index and its bounds.
- `_Node` stores its own bounds, its children and whether those children are leaf entries.

A leaf node contains entries. An internal node contains other nodes. Every node's bounds are the union of its children.

This is the core R-tree invariant: a parent rectangle must contain every rectangle below it.

## 3. Validate the input

`_validate_bounds()` converts each coordinate to a float and checks:
- exactly four values were supplied;
- every coordinate is finite;
- minimum x does not exceed maximum x;
- minimum y does not exceed maximum y.

Invalid bounds are rejected at construction and query time. It is easier to find a malformed rectangle at the boundary of the program than to debug a wrong query result later.

## 4. Calculate a node's bounding rectangle

`_union_bounds()` takes a group of entries or child nodes and finds:
- the smallest minimum x;
- the smallest minimum y;
- the largest maximum x;
- the largest maximum y.

That rectangle becomes the parent node's MBR.

## 5. Pack one level using STR

`_pack()` performs the Sort-Tile-Recursive grouping for one level.

Given (N) items and node capacity (M):

1. Estimate the number of nodes: (P=\lceil N/M\rceil).
2. Estimate the number of x-slices: (S=\lceil\sqrt{P}\rceil).
3. Sort items by their x-centre.
4. Split the ordered list into slices.
5. Sort each slice by y-centre.
6. Group each slice into batches of at most (M) children.
7. Create one node for each batch and calculate its MBR.

The same function works for both leaf entries and internal nodes. Only the child type and the leaf flag change.

## 6. Build the hierarchy from the bottom up

The constructor:
1. validates and stores every input bound;
2. creates one `_Entry` per input item;
3. packs the entries into leaf nodes;
4. repeatedly packs the resulting nodes into parent nodes;
5. stops when only one root remains.

An empty input produces no root. A small input may fit into one leaf node, which also becomes the root.

The tree is immutable after this build. There are no insertion, deletion or update methods.

## 7. Query by pruning branches

`query()` first validates the query rectangle. It then uses a stack:

1. Pop a node.
2. Test the query rectangle against the node MBR.
3. If they do not intersect, skip the whole branch.
4. If the node is a leaf, test each entry's bounds.
5. Otherwise, push only the child nodes whose MBRs intersect.
6. Sort and return the matching original input indices.

The intersection test is inclusive: boxes that touch at an edge or corner count as intersecting.

## 8. Why the result is a candidate set

The tree only knows bounding boxes. For a concave polygon or a polygon with holes, the MBR can overlap a query even when the actual geometry does not.

That is why the implementation is described as an envelope index. The caller must apply the exact geometry predicate when the application needs an exact spatial relationship.

The [filter-and-refine spatial join](../../../algorithms/query-processing/filter-refine-spatial-join.md) shows this second step using Shapely's STRtree.

## 9. How the tests check correctness

The test suite covers:
- empty and one-entry trees;
- intersections and non-intersections;
- edge-touching boxes;
- overlapping boxes;
- preservation of original input indices;
- invalid capacities and bounds;
- a brute-force comparison across 300 generated boxes, 60 query windows and five node capacities.

The brute-force comparison is especially important. It checks that changing the packing capacity changes the tree structure but not the query answer.

## 10. What is intentionally missing

This implementation is for learning. It does not implement:
- dynamic insertion, deletion or update;
- nearest-neighbour search;
- 3D indexing;
- exact geometry predicates;
- disk-backed pages or concurrency control.

For production use, compare with [Shapely's STRtree](https://shapely.readthedocs.io/en/stable/strtree.html) and benchmark against the actual data and query workload.

## Reproduce the example

From this directory:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```
