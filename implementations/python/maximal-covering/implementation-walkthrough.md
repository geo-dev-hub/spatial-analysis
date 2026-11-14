# Intern walkthrough: maximal covering

## 1. Translate the policy question

MCLP starts with a budget ceiling (at most p facilities) and a service standard (maximum cost S). It asks how much demand can be reached. It does not minimize everyone's total travel cost.

## 2. Inspect the inputs

Open `maximal_covering.py`. Rows of the cost matrix are demand locations; columns are candidate facilities. Demand weights align with rows. The threshold uses the same unit as the matrix. An asymmetric matrix is valid.

## 3. Build the coverage relation

The expression `costs <= service_threshold` creates a Boolean matrix. For a selected set, a demand row is covered if any selected column is true. It is counted once even if several sites reach it.

## 4. Enumerate subsets

The solver considers every subset of size 0, 1, …, p, sums the weights of covered demand and retains the best solution. This is exact but combinatorial, so it is a small-instance teaching baseline and test oracle.

## 5. Understand tie-breaking

Equal objective values prefer fewer facilities, then lexicographically earlier candidate indices. This makes output reproducible. It is not an extra optimization objective.

## 6. Validate and experiment

Run:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

Then execute `notebooks/maximal-covering-lab.ipynb`. Change p and the threshold, and record covered and uncovered demand.

## 7. Challenge the model

The solver does not model capacity, congestion, service quality, land availability, staffing, outages or uncertainty. Being within a travel-time threshold does not guarantee that a facility can actually serve the person.

Record the demand definition, candidate set, cost units, routing mode, time of day, threshold rationale, model version and validation evidence.
