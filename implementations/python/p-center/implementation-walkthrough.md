# Intern walkthrough: p-center

## 1. Understand the objective

p-center minimizes the largest assignment cost. It is not an average-distance model. One remote demand point can determine the result.

## 2. Inspect the cost matrix

Rows are demand locations; columns are candidate sites. The values must be finite, non-negative and use a common unit. An asymmetric matrix is valid.

## 3. Enumerate facility sets

The solver examines every combination of exactly p candidates. For each combination it finds the least-cost open site for every demand row, then takes the maximum of those nearest-site costs.

## 4. Keep assignments reproducible

Candidate combinations are visited lexicographically. The first solution with the best radius is retained. Within a selected set, NumPy's first-minimum behaviour resolves equal assignment costs to the earliest candidate.

## 5. Validate

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

Run `notebooks/p-center-lab.ipynb`, vary p and inspect which demand location determines the radius.

## 6. Challenge the model

The model has no capacity, congestion, facility reliability, equity constraints or uncertainty. A worst-case guarantee is only as meaningful as the demand set and cost matrix used to calculate it.
