# Backup coverage (r-covering)

An exact exhaustive solver for small facility-location instances. It selects at most p candidate facilities and maximizes demand weight that has at least r distinct selected facilities within a supplied service threshold.

## Run

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Example

```python
from backup_coverage import solve_backup_coverage

costs = [[2, 3, 9], [1, 8, 2], [8, 1, 3]]
sites, weight, backed_up, counts = solve_backup_coverage(
    costs, p=3, service_threshold=3, required_cover_count=2,
    demand_weights=[10, 5, 8],
)
print(sites, weight, backed_up, counts)
```

Rows are demand locations and columns are distinct candidate facilities. The matrix may be asymmetric. Costs and threshold must use the same unit.

## Contract and limits

- Opens at most p facilities; p must be at least the required cover count r.
- A demand row is counted only when at least r selected, distinct candidates are within the inclusive threshold.
- Returns the selected indices, covered weight, per-row covered flags and per-row eligible-facility counts.
- Ties prefer fewer facilities, then lexicographically earlier candidate indices.
- Exact subset enumeration is combinatorial; use this as a learning baseline and small-instance oracle.
- Does not model facility capacity, failure probability, correlated outages, queues, staffing or service transfer.

See the [canonical lesson](../../../algorithms/optimization/backup-coverage.md), [intern walkthrough](implementation-walkthrough.md), [exercise](../../../exercises/backup-coverage.md) and [visual lab](../../../notebooks/backup-coverage-lab.ipynb).
