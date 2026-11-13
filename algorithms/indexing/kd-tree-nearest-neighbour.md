# k-d trees: searching for nearby points

A nearest-neighbour query asks which stored point is closest to a query point. If the dataset is small, calculate every distance and keep the minimum. For a large point set, a spatial data structure can help avoid evaluating every candidate.

A k-d tree (k-dimensional tree) organises point records by recursively splitting coordinate space along one axis at a time. It supports range and nearest-neighbour queries, among other associative searches.

## The basic idea

At each internal node, choose a coordinate axis and a split value. Points on one side go to the left child; points on the other side go to the right child. The next level usually uses the next axis in a cycle, although construction strategies vary.

For two-dimensional points, a simple cyclic strategy alternates x and y:

~~~mermaid
flowchart TD
    A["Root: split by x"]
    B["Left: split by y"]
    C["Right: split by y"]
    D["Continue alternating axes"]
    A --> B
    A --> C
    B --> D
    C --> D
~~~

This creates axis-aligned regions. A node's split plane gives a lower bound on how close any point in the opposite subtree could be to the query.

## Nearest-neighbour search

Let query point q=(q_x,q_y) and candidate point p=(p_x,p_y). Under planar Euclidean distance:

$$
d(q,p)^2 = (q_x-p_x)^2 + (q_y-p_y)^2
$$

Comparing squared distances avoids a square root and preserves the ordering.

A branch-and-bound search works as follows:

1. Descend toward the child whose region contains the query point.
2. Keep the best candidate found so far and its squared distance D².
3. Visit the other child only if the minimum possible distance from the query to that child's region is no greater than D².
4. Update the best candidate whenever a closer point is found.
5. Continue until every unvisited region has a lower bound greater than the current best distance.

For a split at x=s, if the query is on one side, the distance to the split plane is |q_x-s|. If its square is already greater than the best squared distance, the opposite side cannot contain a closer point. In a full implementation, use the distance to the node's entire bounding region, not just one split plane, for tighter pruning.

## Why the search can be fast—and when it is not

A well-shaped tree over low-dimensional, suitably distributed data can prune many branches. But the nearest-neighbour query is not guaranteed to take logarithmic time for arbitrary data.

Performance can deteriorate when:
- points are clustered or highly anisotropic;
- splits create very unbalanced subtrees;
- the dimension is high;
- the query is far from the data distribution;
- many regions have lower bounds smaller than the current best distance.

The curse of dimensionality is important: as dimensionality grows, distance bounds become less selective and a tree search may approach a scan. Scikit-learn's documentation discusses this limitation and compares KDTree with BallTree and brute-force methods.

## Construction choices

A simple tree may split at the median along alternating axes. This often creates balanced point counts, but the geometry of the resulting cells can still be poor for some distributions.

Other construction choices include:
- choose the axis with greatest spread;
- choose a median or another quantile as the split value;
- use bucket leaves rather than one point per leaf;
- rebuild periodically when updates make the tree unbalanced.

These choices affect performance, memory and update costs. Record them when benchmarking.

## Tie handling and exactness

Two or more points can be equally near to the query. A reproducible implementation should define whether it returns one result using a stable tie-break, or all points within the minimum distance.

For k-nearest neighbours, maintain the best k candidates and prune a subtree only when its lower bound is greater than the current kth-best distance. Equality must be handled according to the tie policy.

## Coordinate systems matter

Euclidean distance in longitude/latitude degrees is not ground distance. A k-d tree built on raw longitude and latitude uses a planar coordinate metric and can produce misleading nearest-neighbour results, especially over large extents or near the poles and antimeridian.

For local analysis, transform to an appropriate projected CRS with suitable units. For global geographic distance, use a geodesic-aware method or a representation whose lower bounds are valid for the chosen metric. Do not use Euclidean k-d tree pruning with a different distance metric unless the node bounds are mathematically valid for that metric.

## Compare with other indexes

| Structure | Data model | Natural strength | Important limitation |
|---|---|---|---|
| k-d tree | Points in k-dimensional coordinate space | Point range and nearest-neighbour queries | High-dimensional pruning can weaken |
| Point-region quadtree | Points assigned to recursively subdivided 2D cells | Spatial partitioning and window queries | Depth and cell visits depend on distribution and stopping rules |
| R-tree | Extended objects represented by bounding rectangles | Range and intersection candidate search | Overlapping rectangles can reduce selectivity |
| Ball tree | Points enclosed by nested metric balls | Neighbour search where ball bounds are useful | Construction and bounds depend on metric/data |

## Try it

Create a 2D point dataset and compare:
1. brute-force nearest-neighbour search;
2. a k-d tree using median splits;
3. the same tree with a different axis-selection strategy.

Use the same deterministic query points and tie policy. Check every tree result against brute force.

Then repeat with:
- uniform points;
- a long narrow cluster;
- several identical points;
- points concentrated around one location;
- a higher-dimensional synthetic dataset.

Record build time, query time, visited nodes, exact distance calculations and memory. Do not report a single timing as a general performance claim.

## Reproduce the teaching example

The [Python k-d tree implementation](../../implementations/python/kd-tree/README.md) demonstrates exact 2D Euclidean nearest-neighbour search, deterministic tie handling and brute-force differential tests. Follow its [step-by-step walkthrough](../../implementations/python/kd-tree/implementation-walkthrough.md).

## References

- Bentley, J. L. (1975), [Multidimensional binary search trees used for associative searching](https://doi.org/10.1145/361002.361007), Communications of the ACM. The foundational k-d tree paper.
- Bentley, J. L. (1979), [Multidimensional binary search trees in database applications](https://doi.org/10.1109/TSE.1979.230200), IEEE Transactions on Software Engineering.
- Friedman, J. H., Bentley, J. L. and Finkel, R. A. (1977), [An algorithm for finding best matches in logarithmic expected time](https://doi.org/10.1145/355744.355745), ACM Transactions on Mathematical Software.
- [scikit-learn nearest-neighbours documentation](https://scikit-learn.org/stable/modules/neighbors.html), for implementation options and the limitations of KDTree in higher dimensions.

**Evidence state:** the k-d tree's foundational role is grounded in Bentley's original paper. Search procedure and pruning are presented as a standard exact branch-and-bound pattern; complexity is intentionally workload-qualified rather than promised as a universal logarithmic bound.
