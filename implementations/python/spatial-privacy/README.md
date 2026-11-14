# Differential privacy for spatial aggregates

This package implements a single-release user-level Laplace mechanism for counts over a fixed set of spatial cells.

Each person is deduplicated and capped to at most k distinct cells. Under add/remove-one-person adjacency, the vector of cell counts has L1 sensitivity k. Independent Laplace noise with scale k/epsilon is added to every cell count.

This is a bounded contribution mechanism, not a complete privacy system. The cell domain is public/fixed, identifiers are not returned, and the output is not postprocessed to non-negative integers. Repeated releases compose privacy loss and require an accountant. The caller must choose a defensible contribution bound, adjacency definition, epsilon budget and release policy. The mechanism does not protect location traces when one person's many records are not correctly grouped under a stable person identifier.

Run `python -m pip install -r requirements.txt` and `python -m pytest -q`.


## Repeated-release accounting

The package also includes an in-memory [basic sequential composition accountant](composition.py). It adds epsilon and delta across named releases, reports remaining budget, rejects duplicate names and refuses over-budget releases without mutating the ledger. It does not implement advanced composition or Rényi DP. See the [walkthrough](composition-walkthrough.md), [tests](test_composition.py) and [composition lab](../../../notebooks/spatial-privacy-composition-lab.ipynb). This is a teaching component, not durable production governance.


## Hierarchical spatial k-anonymity

The package includes a [quadtree generalisation baseline](spatial_k_anonymity.py). It splits a cell only when every occupied child contains at least k records; otherwise it publishes the parent cell. Every emitted group is disjoint and has at least k records, while a total population smaller than k is suppressed. This is location-only k-anonymity, not differential privacy or a complete re-identification defence. See the [walkthrough](spatial-k-anonymity-walkthrough.md), [tests](test_spatial_k_anonymity.py) and [lab](../../../notebooks/spatial-k-anonymity-lab.ipynb).
