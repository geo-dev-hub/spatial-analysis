# Global Geary's C in Python

This small reference implementation calculates global Geary's C from a numeric attribute and a dense spatial weights matrix. It is intentionally short enough to read alongside the formula.

It does **not** calculate analytical or permutation-based significance tests. For those, use a maintained spatial statistics library such as PySAL's `esda` package.

## Run it

From this directory:

```bash
python -m pip install -r requirements.txt
python - <<'PY'
from geary_c import gearys_c

weights = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
]

print(gearys_c([1, 2, 3, 4], weights))
print(gearys_c([1, 4, 1, 4], weights))
PY
```

Expected output:

```text
0.3
1.5
```

## Run the tests

```bash
python -m pytest -q
```

The 16 tests cover hand-calculated examples, translation and scale invariance, weight scaling, the expected mean over all permutations for a symmetric graph, asymmetric weights and invalid inputs.

## Step-by-step walkthrough

Follow the [implementation walkthrough](implementation-walkthrough.md) to trace the weights validation, squared-difference numerator, total variation and final formula.

## Limits

- The dense implementation uses (O(n^2)) time and (O(n^2)) weight storage.
- It assumes finite, non-negative weights and zero self-weights.
- It does not build weights from geometry, align IDs, handle missing values or calculate inference.
- The weight matrix is part of the model. Record its construction and transformation.

Continue with the [canonical Geary's C lesson](../../../algorithms/statistics/gearys-c.md) and the [interactive notebook](../../../notebooks/gearys-c-lab.ipynb).

For production analysis, consult the [official PySAL global Geary's C guide](https://pysal.org/esda/stable/user-guide/geary.html) and the [esda Geary API](https://pysal.org/esda/stable/generated/esda.Geary.html).
