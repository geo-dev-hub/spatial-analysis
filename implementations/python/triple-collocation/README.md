# Triple collocation — Python baseline

A small NumPy implementation of classical three-product triple-collocation error-variance estimates.

## Requirements

- Python 3.10+
- NumPy

## Run

From the repository root:

```bash
python -m pip install -r implementations/python/triple-collocation/requirements.txt
python -m pytest implementations/python/triple-collocation/test_triple_collocation.py
```

## Contract

- Supply three one-dimensional arrays with equal lengths.
- Each row must represent the same variable over matched spatial and temporal support.
- Non-finite rows are removed jointly, not independently.
- At least three complete rows are required.
- The output contains three error-variance estimates, the sample covariance matrix and retained sample size.
- Negative estimates are deliberately preserved.
- A near-zero cross-covariance raises an error rather than returning an unstable result.

This is a teaching baseline, not a complete validation system. It does not collocate geospatial products or verify the assumptions for you.
