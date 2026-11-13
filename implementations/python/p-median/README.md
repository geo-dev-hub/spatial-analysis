# Exact p-median for small instances

The p-median problem selects exactly p facilities from a finite candidate set to minimise weighted demand-to-facility assignment cost.

This package uses exhaustive enumeration. It is exact and useful as a teaching baseline or a small-instance oracle, but the number of candidate sets grows as $\binom{m}{p}$. It is not a large-scale optimisation solver.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
import numpy as np
from p_median import solve_p_median

costs = np.array([
    [2, 8, 5, 9],
    [7, 3, 4, 8],
    [6, 7, 2, 4],
])
facilities, objective, assignment = solve_p_median(costs, p=2)
print(facilities, objective, assignment)
~~~

Rows are demand locations; columns are candidate facilities. Costs can represent distance, travel time or another additive impedance, but must be finite and non-negative. Demand weights scale the contribution of each row.

## Contract and limits

- Exactly p candidate facilities are opened.
- Every demand point is assigned to its least-cost open facility.
- Ties are resolved deterministically by candidate index.
- Demand weights must be non-negative and at least one must be positive.
- The objective is weighted sum of assignment costs, not maximum distance or facility capacity.
- No fixed opening cost, capacity, service threshold, uncertainty or equity constraint is included.
- Exhaustive enumeration is exponential/combinatorial in the number of candidate sites.

Read the [canonical lesson](../../../algorithms/optimization/p-median.md) and [intern walkthrough](implementation-walkthrough.md).
