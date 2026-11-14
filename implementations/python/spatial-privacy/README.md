# Differential privacy for spatial aggregates

This package implements a single-release user-level Laplace mechanism for counts over a fixed set of spatial cells.

Each person is deduplicated and capped to at most k distinct cells. Under add/remove-one-person adjacency, the vector of cell counts has L1 sensitivity k. Independent Laplace noise with scale k/epsilon is added to every cell count.

This is a bounded contribution mechanism, not a complete privacy system. The cell domain is public/fixed, identifiers are not returned, and the output is not postprocessed to non-negative integers. Repeated releases compose privacy loss and require an accountant. The caller must choose a defensible contribution bound, adjacency definition, epsilon budget and release policy. The mechanism does not protect location traces when one person's many records are not correctly grouped under a stable person identifier.

Run `python -m pip install -r requirements.txt` and `python -m pytest -q`.
