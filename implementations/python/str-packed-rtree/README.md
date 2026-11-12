# STR-packed R-tree: a small reference implementation

This example builds an immutable R-tree using Sort-Tile-Recursive (STR) packing. It stores axis-aligned 2D bounding boxes and returns the input indices whose boxes intersect a query box.

It is a teaching implementation of the packing and search ideas. It is not a replacement for a production spatial index.

## Run it

From this directory:

```bash
python -m pip install -r requirements.txt
python - <<'PY'
from str_packed_rtree import STRPackedRTree

bounds = [
    (0, 0, 1, 1),
    (2, 0, 3, 1),
    (4, 0, 5, 1),
    (0, 2, 1, 3),
    (2, 2, 3, 3),
]

tree = STRPackedRTree(bounds, node_capacity=3)
print(tree.query((0.5, 0.5, 2.5, 2.5)))
PY
```

Expected output:

```text
[0, 1, 3, 4]
```

## Run the tests

```bash
python -m pytest -q
```

The tests compare the index against a brute-force bounding-box scan across 300 generated boxes, 60 query windows and five node capacities. They also cover empty trees, boundary touches, invalid bounds and original input-index preservation.

## What this implementation does

- creates leaf entries in the original input order;
- sorts item centres along the x-axis;
- divides the sorted items into vertical slices;
- sorts each slice by y-centre;
- packs entries into leaf nodes up to the chosen capacity;
- repeats the packing process over node bounding boxes until one root remains;
- searches by pruning any node whose bounding box does not intersect the query.

## Important limits

- The tree is immutable after construction. It does not support insertion, deletion or update.
- It indexes 2D axis-aligned bounding boxes, not full geometry topology.
- A query returns envelope candidates. For a polygon or line, a candidate may not satisfy the exact geometry predicate.
- Boundary touching counts as bounding-box intersection in this example.
- The implementation uses Python objects and is designed for learning, not high-throughput production workloads.

For a production-ready interface, see [Shapely's STRtree documentation](https://shapely.readthedocs.io/en/stable/strtree.html). Shapely's STRtree is query-only, returns indices in input order, supports vectorised queries and can apply exact predicates during the query.

Continue with the [STR-packed R-tree lesson](../../../algorithms/indexing/str-packed-rtree.md), the [step-by-step implementation walkthrough](implementation-walkthrough.md) and the [interactive notebook](../../../notebooks/str-packed-rtree-lab.ipynb).
