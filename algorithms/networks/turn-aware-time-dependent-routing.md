# Turn-aware and time-dependent routing

A route can be shortest in a node graph and still be illegal or unrealistic on the road. At an intersection, the next movement can depend on the road used to arrive. Travel time can also depend on the time a traveller reaches an edge.

These are changes to the routing model, not cosmetic options added after path search.

## Turn restrictions require more state

In a node-based graph, a search state is the current intersection. That is insufficient when two arrivals at the same intersection have different legal next movements.

An edge-based state records the incoming directed edge. A transition from incoming edge e to outgoing edge f has:
- a legality rule (allowed or prohibited);
- an optional turn penalty;
- the traversal cost of f.

A turn-expanded graph can be viewed as a graph whose vertices represent directed road edges and whose arcs represent legal consecutive edge pairs. This makes ordinary non-negative shortest-path search applicable to the expanded state space.

~~~mermaid
flowchart LR
  A[Incoming edge e] --> B{Turn e to f allowed?}
  B -->|No| C[Reject transition]
  B -->|Yes| D[Add turn penalty]
  D --> E[Traverse outgoing edge f]
  E --> F[New state: f]
~~~

## Time-dependent edge costs

Let c_e(t) be the travel duration on edge e when entered at time t. The arrival-time function is:

$$
A_e(t)=t+c_e(t)
$$

A FIFO edge satisfies:

$$
t_1\leq t_2\implies A_e(t_1)\leq A_e(t_2)
$$

In plain language: entering the same edge later must not let a traveller arrive earlier. Under the FIFO condition, an earliest-arrival label-setting Dijkstra variant can settle the earliest known arrival at each node.

The algorithm evaluates each outgoing edge at the current arrival time, not at the original departure time:

$$
t_v = t_u + c_{(u,v)}(t_u)
$$

A static travel-time graph is the special case where c_e(t) is constant.

## Why non-FIFO behaviour matters

If an edge's arrival function is non-FIFO, a traveller who arrives at its tail earlier may need to wait for a better departure time. A basic label-setting implementation that immediately traverses every edge may then miss the true earliest arrival. Waiting choices and non-FIFO routing need a different model and algorithm.

A time-dependent callable is not automatically FIFO. The profile must be validated. For piecewise profiles, test arrival-time continuity or monotonicity at every breakpoint, including the boundary between adjacent intervals.

## Runnable examples

The [road-routing package](../../implementations/python/road-routing/README.md) contains:
- edge-based Dijkstra with prohibited turns and turn penalties;
- FIFO time-dependent earliest-arrival Dijkstra using an edge/time travel-duration function;
- tests for legal alternative turns, penalties, absolute arrival times and invalid costs.

The implementation explicitly does not claim to validate FIFO for an arbitrary Python callable. That remains the caller's responsibility.

## What is still outside this example

- Piecewise profile parsing and exact FIFO validation;
- waiting and departure-time choice under non-FIFO costs;
- vehicle-specific access and turn restrictions from real network data;
- transit service calendars, transfers and timetable-based routing;
- RAPTOR, Connection Scan and multimodal routing;
- route geometry, map matching and network snapping.

## Try it

Create an intersection where a left turn is prohibited. Compare a node-only shortest path with the edge-based result. Add a turn penalty and observe when the preferred route changes.

Then define two time-dependent edge profiles. Plot c_e(t) and A_e(t), and identify whether each profile is FIFO. Explain why plotting travel time alone is not enough to test the FIFO property.

## References

- Orda, A. and Rom, R. (1990), [Shortest-path and minimum-delay algorithms in networks with time-dependent edge-length](https://doi.org/10.1109/90.58099), Journal of the ACM, 37(3), 607–625.
- [OSRM routing algorithms overview](https://github.com/Project-OSRM/osrm-backend/wiki/Algorithms).
- [OpenStreetMap turn restriction relations](https://wiki.openstreetmap.org/wiki/Relation:restriction).

**Scope:** edge-based turn constraints and FIFO time-dependent earliest-arrival baselines are implemented. Transit routing and non-FIFO algorithms remain separate research and implementation tasks.
