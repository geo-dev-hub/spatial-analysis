# Intern walkthrough: turn-aware and time-dependent routing

## Part A — Turn-aware search

1. Represent each directed road segment with a stable edge ID, tail node,
   head node and traversal cost.
2. Notice that the cost of taking an outgoing edge can depend on the edge used
   to enter the intersection.
3. Store the incoming edge as the search state. A prohibited pair blocks a
   transition; a turn penalty adds cost to it.
4. Reconstruct the route as an ordered list of edge IDs.
5. Test a prohibited turn, a penalised turn, a disconnected destination and
   invalid edge/penalty values.

A node-only Dijkstra state cannot distinguish two arrivals at the same
intersection when their legal next movements differ.

## Part B — Time-dependent earliest arrival

1. Store directed edges by origin node, with a stable edge ID.
2. Maintain the earliest known absolute arrival time at each node.
3. When an edge is considered, evaluate its travel duration at the time the
   traveller would enter that edge.
4. Relax the neighbour using the resulting arrival time.
5. Reconstruct the node path and return the absolute arrival time.

The label-setting method assumes FIFO edge-arrival functions. For an edge with
travel-time function c(t), the arrival function t+c(t) must be non-decreasing.
A callable can hide a non-FIFO interval, so a production implementation must
validate its profiles or use an algorithm that supports non-FIFO behaviour.

## Further work

Add explicit piecewise travel-time profiles with exact FIFO validation,
turn-expanded state benchmarks, waiting and transfer choices, service
calendars, transit routing, and multimodal path reconstruction.
