# How the ordinary kriging example works

This example deliberately uses PyKrige rather than presenting a short hand-written matrix solver as a complete geostatistics implementation.

## 1. Prepare the observations

PyKrige receives separate arrays for x coordinates, y coordinates and observed values. They must refer to the same observations in the same order. Coordinates should use a distance system that makes sense for the study area.

## 2. Choose a variogram model

`OrdinaryKriging` accepts a model name such as `spherical`, `exponential` or `gaussian`. If parameters are not supplied, PyKrige estimates parameters from a binned empirical semivariogram.

That convenience is not a substitute for reviewing the empirical points, lag bins, fitted curve and parameter conventions. The package's definition of a range or sill may differ from another package.

## 3. Build the kriging object

```python
model = OrdinaryKriging(
    x, y, z,
    variogram_model="spherical",
    verbose=False,
    enable_plotting=False,
)
```

This object stores the observations and the fitted variogram model needed to construct kriging systems.

## 4. Predict at target locations

```python
prediction, variance = model.execute(
    "points",
    np.array([2.0]),
    np.array([2.0]),
)
```

The first output is the estimated value. The second is the model-based kriging variance at the same target.

For a grid, use `execute("grid", gridx, gridy)`. The returned arrays have one row per y coordinate and one column per x coordinate.

## 5. Read the variance carefully

The variance depends on the observation geometry and fitted variogram. It is conditional on the model and assumptions. It does not automatically include uncertainty in variogram selection, fitted parameters, the local-mean assumption or unmodelled measurement processes.

## 6. Why the tests are limited

The tests check that point and grid predictions are finite, that grid shapes match the requested coordinates, and that a zero-nugget exact-value configuration reproduces sample values.

Those tests check software behaviour for a small fixture. They do not prove that ordinary kriging is suitable for a real dataset or that the selected variogram model is appropriate.

## Reproduce

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```
