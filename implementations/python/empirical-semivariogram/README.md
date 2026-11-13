# Empirical semivariogram: Python example

Calculate the omnidirectional Matheron estimator for a set of observations and explicit distance-bin edges.

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

```python
from semivariogram import experimental_semivariogram

points = [(0,), (1,), (2,), (3,)]
values = [1, 2, 4, 7]
print(experimental_semivariogram(points, values, [0.5, 1.5, 2.5, 3.5]))
```

Each output row contains the bin midpoint (`lag`), empirical semivariance and number of pairs. Empty bins are retained with `semivariance=None`.

The implementation uses Euclidean distances and a simple Matheron estimator. It does not fit a theoretical model, calculate directional variograms or estimate kriging parameters. Choose a coordinate system and lag bins appropriate to the data.

See the [canonical explanation](../../../methods/empirical-semivariogram.md), [walkthrough](implementation-walkthrough.md) and [interactive lab](../../../notebooks/empirical-semivariogram-lab.ipynb).
