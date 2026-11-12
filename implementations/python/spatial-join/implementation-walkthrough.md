# How the indexed spatial join implementation works

This walkthrough explains the small Shapely 2.x spatial join helper in `spatial_join.py`.

## 1. Define the input and output

The function accepts two geometry collections:
- `left_geometries`, the geometries we query with;
- `right_geometries`, the collection stored in the spatial index.

It returns pairs of integer positions:

`(left_index, right_index)`

Those positions refer to the original input sequences. The helper does not construct a GeoDataFrame or copy attributes.

## 2. Convert the inputs to tuples

The function converts both inputs to tuples.

This gives us:
- a stable input order;
- a known length;
- repeatable integer positions;
- protection against a caller's generator being consumed more than once.

If either collection is empty, there cannot be a matching pair, so the function returns an empty list.

## 3. Build the index over the right side

`STRtree(right)` builds an immutable packed index over the right-hand geometries.

The index stores their envelopes. It can quickly reject objects whose bounding boxes cannot match the query.

Why index the right side? Because the left geometries are the inputs to the query, and Shapely returns their indices in the first row of the pair array. Indexing the other side would also be valid, but the direction of the returned pairs would need to be handled consistently.

## 4. Ask the tree to filter and refine

The key call is:

```python
pair_indices = tree.query(left, predicate=predicate)
```

Shapely performs two operations:
1. use the bounding boxes to find candidate pairs;
2. apply the exact predicate to those candidate geometries.

The predicate is evaluated as:

`predicate(input_geometry, tree_geometry)`

The left input geometries are the first argument. The right geometries stored in the tree are the second.

This is why `within` is correct for points on the left and polygons on the right. Reversing the collections changes the meaning of `within` and `contains`.

## 5. Understand the two-row result

When querying an array of geometries, Shapely returns a 2-by-k array:
- row 0 contains indices into the left input array;
- row 1 contains indices into the tree's right input array.

Each column is one matching pair.

If there are no pairs, the array contains no columns and the helper returns an empty list.

## 6. Convert to stable Python pairs

The implementation zips the two rows, converts NumPy integer values to regular Python integers and sorts the resulting pairs.

Sorting makes the output stable and easy to compare in tests. It does not imply that the pairs are ordered geographically or by distance.

## 7. Why the tests focus on predicate semantics

The tests cover more than a basic point-in-polygon example:

- a point inside a polygon;
- a point exactly on a polygon boundary;
- one point matching multiple overlapping polygons;
- preservation of the original input indices;
- empty input collections and empty geometries;
- predicate direction;
- a polygon with a hole;
- equivalence with a brute-force join.

The boundary test is especially useful. A point on a polygon boundary intersects the polygon, but is not within it. Choosing a predicate changes the join result.

## 8. Reproduce the example

From this directory:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

For the full visual explanation, run the [interactive notebook](../../../notebooks/filter-refine-spatial-join-lab.ipynb). For the conceptual method, read the [filter-and-refine spatial join lesson](../../../algorithms/query-processing/filter-refine-spatial-join.md).
