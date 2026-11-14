# Ordinary kriging: PyKrige example

This example uses PyKrige's `OrdinaryKriging` implementation. It fits a variogram model to the supplied observations, estimates values at target locations and returns kriging variance.

## Install

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Minimal example

```python
import numpy as np
from pykrige.ok import OrdinaryKriging

x = np.array([0.3, 1.9, 1.1, 3.3, 4.7])
y = np.array([1.2, 0.6, 3.2, 4.4, 3.8])
z = np.array([0.47, 0.56, 0.74, 1.47, 1.74])

model = OrdinaryKriging(
    x, y, z,
    variogram_model="spherical",
    verbose=False,
    enable_plotting=False,
)
prediction, variance = model.execute("points", np.array([2.0]), np.array([2.0]))
print(float(prediction[0]), float(variance[0]))
```

## Reproduce

The tests exercise point and grid predictions, finite output, and exact-value behaviour when a zero nugget is specified.

See the [ordinary kriging lesson](../../../algorithms/interpolation/ordinary-kriging.md) and [interactive notebook](../../../notebooks/ordinary-kriging-lab.ipynb).

## Important

The example is not a recommendation to accept automatic variogram fitting without inspection. Check the empirical semivariogram, model family, parameter conventions, CRS, neighbourhood, residuals and validation design. Kriging variance is conditional on the fitted model and assumptions.
