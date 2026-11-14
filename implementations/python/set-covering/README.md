# Location set covering

An exact exhaustive solver for small uncapacitated set-covering location instances. It minimizes the number of candidate facilities required to cover every demand row within a supplied service threshold.

## Run

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Example

```python
from set_covering import solve_set_cover

sites, count, assignments = solve_set_cover(
    [[1, 9, 9], [1, 1, 9], [9, 1, 1], [9, 9, 1]],
    service_threshold=2,
)
print(sites, count, assignments)
```

Rows are demand locations and columns candidate sites. The matrix may be asymmetric. Costs and threshold must use the same unit.

## Contract and limits

- Every demand row must be covered by at least one selected site.
- Minimizes the number of open facilities; all opening costs are equal.
- Raises ValueError with unreachable demand-row indices when the instance is infeasible.
- Returns a deterministic first-cover assignment for inspection; it is not capacity constrained.
- Enumerates candidate subsets in increasing cardinality; worst-case search is exponential.
- No capacity, queueing, backup coverage, stochastic reliability or equity constraints.

See the [canonical lesson](../../../algorithms/optimization/set-covering.md), [intern walkthrough](implementation-walkthrough.md), [exercise](../../../exercises/set-covering.md) and [visual lab](../../../notebooks/set-covering-lab.ipynb).
