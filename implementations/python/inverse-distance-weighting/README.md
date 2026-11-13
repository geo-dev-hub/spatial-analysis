# Inverse distance weighting: Python example

This dependency-free reference implementation estimates a value at a target coordinate using inverse-distance weights.

## Run it

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Use it

```python
from idw import predict

stations = [(0, 0), (2, 0), (4, 0)]
rainfall = [10, 20, 40]
estimate = predict(stations, rainfall, (1, 0), power=2)
print(round(estimate, 2))  # 16.32
```

Optional `max_neighbors` and `radius` parameters restrict contributing observations. Coincident observations are averaged. If no observation falls inside a requested radius, the function raises `ValueError`.

## Scope and limits

The function uses Euclidean distance in the coordinate units provided. It does not reproject coordinates, calculate geodesic distance, fit the power parameter, account for barriers or anisotropy, or estimate prediction uncertainty.

See the [canonical lesson](../../../algorithms/interpolation/inverse-distance-weighting.md) and [step-by-step walkthrough](implementation-walkthrough.md).
