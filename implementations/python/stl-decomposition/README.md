# STL seasonal-trend decomposition

This package exposes a small teaching interface to the established STL
implementation in `statsmodels.tsa.seasonal.STL`. It does **not** claim to
reimplement LOESS or Cleveland et al.'s full procedure from scratch.

```python
from stl_decomposition import stl_decompose
parts = stl_decompose(values, period=12, seasonal=7, robust=True)
```

Install with `python -m pip install -r requirements.txt`; test with
`python -m pytest -q`.

Input contract: finite, one-dimensional, regularly sampled observations;
at least two complete cycles; seasonal period >= 2; odd seasonal smoother
>= 3. Missing observations must be handled explicitly upstream. STL is
additive. Trend and seasonal windows affect the result. Robust fitting
downweights outliers but does not solve sensor drift, missing-data bias,
calendar effects, spatial dependence or forecast leakage. STL does not forecast.
