# Maximal covering location (MCLP)

An exact exhaustive solver for small instances. It selects **at most** p candidate facilities to maximize the total weight of demand nodes within a supplied service threshold.

## Run

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Example

```python
from maximal_covering import solve_maximal_covering

costs = [[4, 12, 7], [8, 3, 9], [5, 6, 2]]
sites, covered_weight, covered = solve_maximal_covering(
    costs, p=2, service_threshold=6, demand_weights=[10, 5, 8]
)
print(sites, covered_weight, covered)
```

Rows are demand locations and columns are candidate facilities. The matrix may be asymmetric. Costs and threshold must use the same unit. A demand location is counted once if any selected facility reaches it.

## Contract and limits

- Opens at most p facilities; p may be zero.
- Uses an inclusive threshold: cost <= service_threshold is covered.
- Maximizes covered demand weight, not number of sites or total assignment efficiency.
- Equal objectives prefer fewer facilities, then lexicographically earlier indices.
- Does not assign covered demand to a unique facility and has no capacity or queue constraints.
- Enumerates every subset up to p; use only for small instances and as a correctness oracle.

See the [canonical lesson](../../../algorithms/optimization/maximal-covering.md), [intern walkthrough](implementation-walkthrough.md), [exercise](../../../exercises/maximal-covering.md) and [visual lab](../../../notebooks/maximal-covering-lab.ipynb).
