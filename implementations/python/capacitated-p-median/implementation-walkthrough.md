# Intern walkthrough: a small capacitated p-median solver

## 1. Separate the three inputs

The cost matrix says how expensive it is to serve each demand row from each candidate facility. Demand quantity says how much capacity a row consumes. Demand weight says how strongly its assignment cost counts in the objective.

Do not substitute one for another. A clinic may have patient counts as capacity load and a separate priority weight in a planning objective.

## 2. State the optimisation model

Let \(I\) be demand locations and \(J\) candidate sites. Let \(q_i\) be indivisible demand quantity, \(u_j\) facility capacity, \(c_{ij}\) assignment cost, and \(w_i\) objective weight. Binary \(x_{ij}\) indicates assignment and \(y_j\) indicates an open facility.

\[
\min \sum_{i\in I}\sum_{j\in J} w_i c_{ij}x_{ij}
\]

subject to:

\[
\sum_{j\in J}x_{ij}=1,\quad x_{ij}\le y_j,\quad
\sum_{i\in I}q_i x_{ij}\le u_j y_j,\quad
\sum_{j\in J}y_j=p.
\]

Every demand row is assigned once, only to an open facility, each facility load fits its capacity, and exactly \(p\) sites open.

## 3. Understand the search

The solver enumerates every set of exactly \(p\) candidate sites. For each set it enumerates every assignment of the \(n\) demand rows to those \(p\) sites. It calculates facility loads, rejects assignments that exceed capacity, then scores feasible assignments using weighted costs.

The upper bound on combinations is \(\binom{m}{p}p^n\). This is deliberately transparent but expensive, so the implementation is an exact tiny-instance oracle rather than a practical large-scale solver.

## 4. Read and verify the result

The function returns opened candidate indices, weighted objective and one assigned candidate index per demand row. Recalculate loads from the assignment and check every capacity. Recalculate the objective from the assigned costs and weights.

## 5. Test infeasibility and edge cases

Tests cover capacity-forced assignments, higher-cost feasible assignments, separate capacity quantities and objective weights, infeasible total capacity, deterministic ties and invalid inputs.

## 6. Know the limits

A demand row is indivisible. The model does not represent split deliveries, multiple commodities, time periods, opening costs, queues or stochastic capacity. A facility with capacity 100 is not necessarily able to serve 100 people to an acceptable waiting-time standard; service rates and queueing assumptions require a separate model.
