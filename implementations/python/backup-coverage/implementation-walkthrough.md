# Intern walkthrough: backup coverage

## 1. Start with the failure question

Ordinary coverage asks whether at least one selected facility is within a service threshold. Backup coverage asks whether at least r distinct selected facilities are eligible. This is a deterministic redundancy screen, not a probability calculation.

## 2. Read the matrix

In `backup_coverage.py`, rows are demand locations and columns are candidate facilities. The values must share a unit with the threshold: for example, minutes of walk-network travel time at a named time of day. Directed costs are allowed.

## 3. Turn costs into eligibility

The Boolean expression `matrix <= service_threshold` marks each demand–candidate pair that meets the service standard. The solver counts eligible selected columns for every demand row. A row is backup-covered only when its count is at least r.

## 4. Enumerate facility subsets

The implementation tests every candidate subset with size r through p. For each subset it calculates per-row counts, applies the r threshold, and sums the weights of covered demand. This is exact but combinatorial.

## 5. Read the outputs

- `selected_sites`: candidate column indices.
- `covered_weight`: sum of demand weights whose eligible selected-site count is at least r.
- `covered`: Boolean backup-coverage status for each demand row.
- `counts`: number of selected candidates within the service threshold for each row.

Counts are useful because a row with one nearby selected site is not equivalent to a row with zero.

## 6. Reproduce the tests and lab

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

Then execute `notebooks/backup-coverage-lab.ipynb`. Change r, p and the threshold and explain why the covered set changes.

## 7. Challenge the independence assumption

Two candidate sites may share a bridge, power source, staff pool or hazard zone. The model counts them as two backups even if one disruption can disable both. Before calling the result resilient, document shared dependencies and test explicit failure scenarios.

For a real project, record the demand definition, candidate inventory date, cost units, routing mode, time period, threshold rationale, redundancy level, shared dependencies and validation evidence.
