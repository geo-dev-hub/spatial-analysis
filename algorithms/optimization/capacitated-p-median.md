# Capacitated p-median: locate facilities with finite capacity

Stable ID: SA-OPT-CAP-P-MEDIAN · Draft 0.1 · Source compendium section 6

## The planning question

An uncapacitated p-median model can assign every demand location to the nearest open facility, even if that facility could not serve the assigned load. The capacitated p-median adds an upper bound on demand assigned to each selected facility.

Examples include assigning clinic catchments to facilities with a daily service limit, delivery zones to depots with throughput limits, or students to schools with seat capacity. Capacity units must be explicit.

## Mathematical model

Let \(I\) be demand locations and \(J\) candidate sites. Define \(c_{ij}\) as assignment cost, \(q_i\) as indivisible demand quantity, \(u_j\) as candidate capacity, \(w_i\) as a non-negative objective weight, \(x_{ij}\in\{0,1\}\) as assignment decision and \(y_j\in\{0,1\}\) as opening decision.

\[
\min \sum_{i\in I}\sum_{j\in J}w_i c_{ij}x_{ij}
\]

subject to:

\[
\sum_{j\in J}x_{ij}=1 \quad \forall i,\qquad x_{ij}\le y_j \quad \forall i,j,
\]

\[
\sum_{i\in I}q_i x_{ij}\le u_j y_j \quad \forall j,\qquad
\sum_{j\in J}y_j=p,
\]

\[
x_{ij},y_j\in\{0,1\}.
\]

Every demand row is assigned exactly once, only to an open facility, and each facility's assigned demand must fit its capacity. Exactly \(p\) facilities open.

## Capacity is not an objective weight

- \(q_i\) consumes capacity. Its unit must match \(u_j\).
- \(w_i\) scales the cost contribution. It may represent population importance or another planning weight.

They may be numerically equal in an application, but that is a modelling choice, not an identity.

## Exact teaching implementation

The [Python package](../../implementations/python/capacitated-p-median/README.md) enumerates facility subsets and assignments for small instances. It returns selected candidate indices, weighted objective and assigned facility for each demand row. If no assignment respects capacity, it raises an explicit infeasibility error.

It considers up to:

\[
\binom{|J|}{p}p^{|I|}
\]

facility-set/assignment combinations. This is a transparent tiny-instance baseline, not a city-scale solver.

## Assumptions and limitations

- Demand zones are indivisible and assigned wholly to one open site.
- Exactly \(p\) facilities open; all demand must be assigned.
- Capacities are deterministic, static and scalar.
- There are no opening costs, multiple capacity dimensions, service thresholds, queues, stochastic demand, time periods or backup assignments.
- Capacity alone does not guarantee acceptable waiting time or service level.
- A directed network travel-time matrix may be more appropriate than Euclidean distance.

## Workflow

1. Define demand unit and time period (for example, patient visits per weekday).
2. Estimate each candidate's usable capacity for the same period.
3. Construct an impedance matrix with documented direction and units.
4. Decide whether demand zones are indivisible. If not, this formulation is not suitable.
5. Solve and inspect assignments and capacity utilisation.
6. Test sensitivity to demand, capacity and travel-cost assumptions.
7. Report overflow, unmet demand or expansion needs for a more complete model.

## Exercise

Work through the [capacitated p-median exercise](../../exercises/capacitated-p-median.md), compare the uncapacitated and capacitated assignments, and verify each selected facility's load.

## References

- Daskin, M. S. (2013), *Network and Discrete Location: Models, Algorithms, and Applications*, 2nd ed., Wiley.

**Scope:** exact-p capacitated median with indivisible demand and deterministic scalar capacities; not a queueing model or general facility-location solver.
