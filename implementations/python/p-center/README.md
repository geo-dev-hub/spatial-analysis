# Discrete p-center

An exact exhaustive solver for small uncapacitated p-center instances. It opens exactly p candidate facilities and minimizes the maximum nearest-facility assignment cost.

## Run

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Example

```python
from p_center import solve_p_center

sites, radius, assignments = solve_p_center(
    [[1, 8, 5], [7, 3, 4], [6, 7, 2]], p=2
)
print(sites, radius, assignments)
```

Rows are demand locations and columns candidate facilities. The cost matrix may be asymmetric. All values must be finite, non-negative and in a common unit.

## Contract and limits

- Opens exactly p facilities.
- Assigns each demand to its least-cost open site.
- Minimizes the maximum assignment cost, not the sum or average.
- Equal facility-set solutions retain the lexicographically first set.
- Exhaustively checks every p-combination; use for small instances and as a correctness oracle.
- No capacities, queueing, uncertainty or equity constraints.

See the [canonical lesson](../../../algorithms/optimization/p-center.md), [intern walkthrough](implementation-walkthrough.md), [exercise](../../../exercises/p-center.md) and [visual lab](../../../notebooks/p-center-lab.ipynb).
