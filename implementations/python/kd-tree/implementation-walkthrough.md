# How the k-d tree implementation works

This walkthrough explains the teaching implementation in kd_tree.py. It follows the data from input validation through tree construction and exact nearest-neighbour search.

## 1. Define the contract first

The implementation accepts an iterable of 2D points. Each point must contain exactly two finite numeric coordinates.

The index stores the points as an immutable tuple and assigns each point its original input position. Query results return this stable index so a caller can retrieve the corresponding feature or attribute from its own array.

The distance metric is planar Euclidean distance. The class does not transform coordinates or infer a CRS.

## 2. Represent one node

Each node stores:
- the original input index;
- the point coordinates;
- the axis used for this node's split;
- a left child;
- a right child.

The structure is static. There are no insertion or deletion methods, so the lesson can focus on construction and query correctness.

## 3. Choose a split axis

At each recursive build step, calculate the spread of the remaining points on x and y. Select the axis with the greater spread. If the spreads are equal, select x.

This is a simple teaching heuristic. Other k-d tree builders may cycle axes, choose medians under different rules, use bucket leaves or optimise for query workloads.

## 4. Select the median

Sort the current points by the selected coordinate, then by original input index. Choose the middle record as the node.

The median divides the remaining records into two groups. This gives a balanced point count at each recursive step, even when coordinates are repeated, because the input index provides a stable secondary ordering.

The left and right subsets are built recursively.

## 5. Search the query-side branch first

For a query point, compare its coordinate on the node's split axis with the node's split value. Visit the side containing the query first. This tends to find a nearby candidate early, although it does not guarantee the nearest point lies on that side.

Calculate squared Euclidean distance to the node's point:

$$
d^2 = (q_x-p_x)^2 + (q_y-p_y)^2
$$

The current best result is ordered by (squared distance, original index). This makes ties deterministic.

## 6. Decide whether the far branch can be skipped

The split plane is a lower bound on the distance to any point in the opposite half-space. Let delta be the query coordinate minus the split coordinate.

If delta squared is greater than the current best squared distance, every point in the far branch must be farther away. The branch can be skipped.

If delta squared is equal to the current best distance, the branch must still be visited because it may contain a point at the same distance with a smaller original index.

The code therefore visits the far branch when:

$$
\delta^2 \leq d_{best}^2
$$

This equality detail is important for deterministic tie handling.

## 7. Validate against brute force

The test suite uses a simple exhaustive scan as an oracle. It checks the tree across:
- empty and singleton inputs;
- duplicate coordinates;
- equal-distance ties;
- split-plane queries;
- queries outside the data extent;
- random point clouds;
- clustered and anisotropic distributions.

The brute-force implementation is intentionally simple. It is the correctness reference, not the performance competitor to beat in every small dataset.

## 8. What to improve next

Possible extensions include:
- bucket leaves;
- k-nearest-neighbour search;
- all-neighbours-within-radius queries;
- incremental updates or periodic rebuilding;
- node bounding boxes for tighter lower bounds;
- instrumentation for visited-node and distance-calculation counts;
- benchmarks across distributions and dimensions.

Each extension should preserve a brute-force oracle and an explicit tie policy.

## Reproduce

From this directory, run:

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

Then compare the implementation with the conceptual [k-d tree lesson](../../../algorithms/indexing/kd-tree-nearest-neighbour.md).
