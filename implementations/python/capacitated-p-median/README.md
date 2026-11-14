# Exact capacitated p-median for small instances

The capacitated p-median problem selects exactly \(p\) candidate facilities, assigns every indivisible demand location to one selected facility, and minimises weighted assignment cost while respecting facility capacities.

This package is an exhaustive exact teaching baseline. It enumerates candidate sets and assignments, so its running time grows combinatorially. Use it for small examples and verification, not city-scale production optimisation.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
from capacitated_p_median import solve_capacitated_p_median
costs = [[0, 5, 9], [1, 4, 8], [8, 1, 4], [9, 0, 3]]
opened, objective, assignment = solve_capacitated_p_median(
    costs, p=2, capacities=[2, 2, 4], demand_quantities=[2, 1, 2, 1],
)
print(opened, objective, assignment)
~~~

Rows are demand locations and columns are candidate facilities. The cost matrix contains assignment cost. Demand quantities consume facility capacity; optional demand weights multiply assignment cost. These inputs are deliberately separate: one describes operational load, the other describes the objective's importance weight.

## Model contract

- Exactly \(p\) facilities open.
- Every demand row is assigned whole to exactly one open facility.
- The sum of assigned demand quantities cannot exceed a facility's capacity.
- Capacity and demand use the same unit, such as visits per day.
- Costs and objective weights are finite and non-negative.
- Ties are resolved deterministically.
- An infeasible instance raises ValueError.

## What is not modelled

Demand is indivisible; a zone cannot be split between facilities. The solver has no opening costs, multiple capacity dimensions, service-distance limit, queues, stochastic demand, time periods, backup assignment, equity objective or facility expansion decisions. A hard capacity limit does not guarantee an acceptable waiting time or service quality.

The implementation considers \(\binom{m}{p}\) facility sets and up to \(p^n\) assignments per set for \(m\) candidates and \(n\) demand rows. It is a tiny-instance teaching baseline.

See the [canonical lesson](../../../algorithms/optimization/capacitated-p-median.md) and [intern walkthrough](implementation-walkthrough.md).
