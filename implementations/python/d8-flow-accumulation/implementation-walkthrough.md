# Intern walkthrough: D8 flow accumulation

## 1. What the input means

Flow accumulation is downstream of flow-direction assignment. Each valid cell has either a D8 direction code or code 0 for a terminal cell. Code -1 marks invalid/NoData.

The implementation accepts an already-computed direction grid. It deliberately does not infer directions from elevation or fill depressions.

## 2. Build the directed graph

Each valid cell is a node. A nonzero direction points to at most one downstream neighbour. If the direction exits the raster or enters a NoData cell, the flow leaves the valid analysis domain.

This graph representation makes the key assumption explicit: the direction grid should describe an acyclic drainage network. A loop is not a meaningful downhill flow path.

## 3. Initialise each cell's contribution

Let $w_i$ be the input contribution at cell $i$. With no weights supplied, $w_i=1$. Accumulation includes the cell itself:

$$
A_i=w_i+\sum_{j\to i}A_j
$$

The sum is over immediate upstream neighbours that flow into cell $i$.

## 4. Process cells in topological order

A cell can be finalised only after all upstream neighbours have contributed. The code calculates each node's incoming-edge count (indegree), queues cells with indegree zero, and propagates their accumulated value downstream.

When a node's final upstream contribution arrives, its indegree becomes zero and it is queued. This is Kahn's topological sorting algorithm applied to the D8 graph.

If the number of processed cells is smaller than the number of valid cells, some directed cycle exists. The function raises an error rather than returning misleading partial values.

## 5. Complexity and limitations

Every valid cell is inspected a constant number of times, so the method is O(n) in the number of valid cells, with O(n) graph/queue storage.

The result depends on the supplied flow directions. Depressions, flats, DEM noise, grid resolution and the chosen flow-routing model all affect the network. D8 routes each cell to one neighbour; D-infinity and multiple-flow-direction methods distribute flow differently and require different accumulation equations.

## 6. Test and investigate

The tests cover a linear channel, a confluence, weighted source contributions, NoData/domain exits, invalid codes and cycle detection. A passing test suite verifies these implementation contracts; it does not validate the hydrological conditioning of a real DEM.
