# Spatial interpolation: IDW and ordinary kriging

This package compares two ways to estimate a continuous surface from point observations and includes an exploratory empirical semivariogram:

- **Inverse distance weighting (IDW):** a deterministic weighted average. Nearby observations receive greater weight.
- **Ordinary kriging:** a linear predictor whose weights are derived from a specified stationary isotropic variogram and the unbiasedness constraint.

The package is deliberately small. It does not fit variogram parameters, select a model, handle anisotropy, co-kriging, block support, measurement error or spatiotemporal covariance.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## IDW example

~~~python
from interpolation import idw_predict

samples = [(0, 0, 10), (10, 0, 20), (0, 10, 30)]
print(idw_predict(samples, [(2, 2)], power=2))
~~~

IDW uses weights $w_i=d_i^{-p}$, normalised to sum to one. An exact sample-location query returns the observed value. A query with no samples inside an optional search radius returns `None`.

## Ordinary kriging example

~~~python
from interpolation import ordinary_kriging_predict

samples = [(0, 0, 10), (10, 0, 20), (0, 10, 30), (10, 10, 40)]
predictions = ordinary_kriging_predict(
    samples,
    [(5, 5)],
    partial_sill=100,
    range_scale=8,
)
print(predictions)  # (prediction, kriging variance)
~~~

The empirical semivariogram is exposed as `empirical_variogram(samples, bin_edges)`. It reports mean pair distance, classical semivariance and pair count for caller-defined bins. Bins are left-closed/right-open except the final bin, which includes its upper edge; empty bins remain visible with a midpoint and `None` semivariance. Pair summaries are accumulated online, using O(B) auxiliary memory for B bins. It is not a fitted model.

The exponential semivariogram is

$$
\gamma(h)=c\left(1-e^{-h/a}\right), \quad h>0,
$$

with $\gamma(0)=0$, partial sill $c>0$ and range scale $a>0$. The ordinary-kriging system is solved with the sum-of-weights constraint. The returned variance is conditional on this model and its parameters; it is not a guarantee of real-world prediction error.

## Coordinate and modelling contract

- Coordinates are planar 2D values in one consistent projected CRS.
- Distances, range scale and any search radius use those coordinate units.
- The model is stationary and isotropic; directional anisotropy is not represented.
- The variogram parameters are supplied by the caller, not fitted from the sample.
- Sample locations must be unique; duplicate coordinates require an explicit aggregation or measurement-error policy.
- This teaching implementation solves a dense linear system. It is intended for small examples, not large datasets.
- IDW is not kriging and does not provide a model-based prediction variance.

Read the [interpolation lesson](../../../algorithms/geostatistics/interpolation.md), the [empirical semivariogram method record](../../../methods/empirical-semivariogram.md) and the [intern walkthrough](implementation-walkthrough.md) before interpreting the results.
