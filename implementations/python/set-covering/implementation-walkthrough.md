# Intern walkthrough: location set covering

## 1. Translate the service requirement

Set covering requires every demand row to be within the threshold of at least one selected candidate. Unlike MCLP, it cannot intentionally leave demand uncovered.

## 2. Inspect the matrix

Rows are demand locations; columns are candidate facilities. The threshold uses the same cost unit. A candidate is eligible for a row when its cost is less than or equal to the threshold.

## 3. Check feasibility

Before enumeration, the solver checks whether every demand row has at least one eligible candidate. If not, it raises a ValueError and lists the unreachable row indices.

## 4. Search by facility count

The solver enumerates combinations of size one, two and so on. The first subset that covers every row has minimum cardinality. Combinations are lexicographic, so equal-cardinality solutions are deterministic.

## 5. Assign demand for inspection

After choosing a set, each demand row is assigned to the first selected facility that covers it. This assignment is only a deterministic reporting convention; it is not a capacity-constrained allocation.

## 6. Validate

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

Run `notebooks/set-covering-lab.ipynb` and vary the service threshold. Record feasibility, selected sites and the number of facilities.

## 7. Challenge the model

The model assumes equal facility opening costs and unlimited capacity. It does not account for queues, outages, backup coverage, unequal service quality or equity. A coverage guarantee is only as meaningful as the travel-cost matrix and threshold.
