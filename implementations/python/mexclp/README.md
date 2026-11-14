# MEXCLP: maximum expected covering

This dependency-light teaching package enumerates exact placements for small instances. It allows multiple units at one candidate site and assumes every unit has the same independent busy probability.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
from mexclp import solve_mexclp

costs = [[2, 8], [7, 3], [4, 6]]
sites, expected, contributions = solve_mexclp(
    costs, p=2, service_threshold=5, busy_fraction=0.25,
    demand_weights=[100, 80, 60],
)
print(sites, expected, contributions)
~~~

The returned site tuple contains one candidate index per deployed unit; repeated indices mean co-location. The expected value is the sum of demand weight multiplied by the probability that at least one eligible unit is available.

See the [canonical lesson](../../../algorithms/optimization/mexclp.md) and [intern walkthrough](implementation-walkthrough.md). This is not a hypercube queueing model or a production-scale optimiser.
