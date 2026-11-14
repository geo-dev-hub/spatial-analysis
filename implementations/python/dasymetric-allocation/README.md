# Weighted dasymetric allocation

This package implements a bounded top-down dasymetric allocation baseline. Each source-zone total is distributed among eligible target units in proportion to a supplied non-negative ancillary weight, such as building floor area or built-up fraction.

For source zone i and eligible target j:

    allocation[i, j] = source_total[i] * weight[i, j] / sum_j(weight[i, j])

Each source row conserves its total. An optional eligibility mask separates geometric overlap from the ancillary weight. If an eligible row has zero total weight, the caller can either receive an error (default) or request a uniform allocation over eligible targets.

## Install and run

    python -m pip install -r requirements.txt
    python -m pytest -q

## Scope and limitations

- The package receives an already constructed source-by-target weight matrix. It does not perform polygon overlay or calculate building areas.
- The source totals are treated as correct inputs; the method does not estimate or validate population.
- Ancillary weights are allocation proxies, not truth. Building area, built-up fraction and land-cover suitability can introduce systematic bias.
- The uniform fallback is explicit and should be reported; it is not evidence-based spatial disaggregation.
- This is top-down allocation, not bottom-up microcensus estimation, settlement modelling or a complete gridded-population workflow.

See walkthrough.md and the visual lab at ../../../notebooks/dasymetric-allocation-lab.ipynb.
