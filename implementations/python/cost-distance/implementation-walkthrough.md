# Intern walkthrough: raster least-cost distance

## 1. Convert the raster into a graph

Each valid raster cell is a graph node. A node is connected to its four orthogonal neighbours, and optionally its four diagonal neighbours. NoData cells are absent from the traversable graph.

The grid spacing determines the physical length of each move. A diagonal step on a rectangular grid is not necessarily the same length as a horizontal or vertical step.

## 2. Define edge cost

Let c(u) and c(v) be non-negative cost-per-distance values at adjacent cells. This implementation uses the arithmetic mean of endpoint costs:

$$w(u,v)=\frac{c(u)+c(v)}{2}\ell(u,v)$$

For a horizontal move, ℓ is the east-west cell spacing; for a vertical move it is the north-south spacing; for a diagonal move it is the hypotenuse.

This is one discretisation convention. Some applications use a different integration rule or directional friction model. The convention must be documented because it changes the result.

## 3. Apply multi-source Dijkstra

All source cells are initialised at distance zero and inserted into a min-priority queue. The smallest tentative distance is removed first. For each traversable neighbour, relax the edge:

$$D(v)\leftarrow\min(D(v),D(u)+w(u,v))$$

Because all edge costs are non-negative, Dijkstra finalises nodes in non-decreasing accumulated-cost order. Multiple sources calculate the minimum cost from the nearest source in the cost metric.

## 4. Diagonal corner policy

When diagonal movement is enabled, the code can prohibit a diagonal step if either of the two orthogonal cells touching that corner is blocked. This avoids crossing through a zero-width corner gap. It is an explicit modelling policy, not a universal GIS default.

## 5. Interpret output and units

The output is accumulated cost. If cost is time per metre, the output can represent travel time under the chosen discretisation. If cost is a dimensionless friction multiplier, the output is a relative weighted distance. It is not ordinary Euclidean distance unless the cost surface is uniformly one and the selected grid graph permits the corresponding path.

Valid cells unreachable from every source remain infinity; NoData cells remain NaN.

## 6. Complexity and limitations

With a binary heap, the standard bound is O((V+E) log V), where V is valid cells and E is neighbour links. For a fixed 8-neighbour grid, E=O(V), giving O(V log V).

This is not a continuous Eikonal solver, fast marching method, anisotropic travel model, or vector-network routing algorithm. The raster resolution, cost model, connectivity and barrier policy all influence the path.
