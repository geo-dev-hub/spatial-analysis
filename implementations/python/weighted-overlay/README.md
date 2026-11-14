# Weighted linear combination in Python

This package demonstrates the aggregation step of a GIS weighted linear combination (WLC). It combines already-standardised, same-shaped two-dimensional criterion arrays. It does not decide how raw measurements should be standardised or how weights should be chosen.

## Install and test

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Example

```python
import numpy as np
from weighted_overlay import weighted_linear_combination

criteria = {
    "road_access": np.array([[0.8, 0.4], [0.2, 0.9]]),
    "terrain": np.array([[0.6, 0.9], [1.0, 0.5]]),
    "low_flood_exposure": np.array([[0.9, 0.7], [0.8, 0.3]]),
}
weights = {
    "road_access": 0.50,
    "terrain": 0.30,
    "low_flood_exposure": 0.20,
}
eligible = np.array([[True, True], [False, True]])

scores = weighted_linear_combination(criteria, weights, eligible=eligible)
print(scores)
```

## Input contract

- Supply at least one named criterion.
- Each criterion must be a non-empty two-dimensional array.
- Every criterion array must have the same shape and represent the same grid.
- Finite criterion scores must already be standardised to [0, 1], where larger means more preferred.
- Non-finite values are treated as NoData.
- Every criterion must have exactly one weight.
- Weights must be finite and non-negative, and at least one must be positive. They are normalised internally to sum to one.
- An optional eligibility mask must be a same-shaped Boolean array. False cells are excluded.
- A cell is scored only when all criteria are finite and it is eligible.

## Scope and limitations

The strict common-footprint NoData policy avoids silently renormalising weights differently from cell to cell. It can, however, exclude more cells than a method designed to handle partial criteria coverage. The caller is responsible for deciding whether this policy is suitable.

This implementation does not standardise raw measurements, derive weights, resample or align rasters, resolve conflicting stakeholder preferences, perform sensitivity analysis or validate a real decision. WLC is compensatory: a strong score on one factor can offset a weak score on another. Keep hard exclusions in the eligibility mask rather than treating them as ordinary factors.

See the [WLC method lesson](../../../methods/weighted-linear-combination.md), [implementation walkthrough](implementation-walkthrough.md) and [interactive suitability lab](../../../notebooks/weighted-linear-combination-lab.ipynb).
