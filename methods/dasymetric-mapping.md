# Weighted dasymetric mapping: conservative top-down allocation

Dasymetric mapping disaggregates a known total from coarse source zones to smaller target units using ancillary spatial information. This package implements a deliberately bounded weighted-allocation baseline: within each source zone, distribute its supplied total in proportion to non-negative ancillary weights.

## Allocation rule

Let \(P_i\) be the known total for source zone \(i\), and let \(w_{ij}\geq0\) be an ancillary weight for eligible target unit \(j\) within source \(i\). Then

\[
\hat P_{ij}=P_i\frac{w_{ij}}{\sum_{j\in E_i}w_{ij}},
\]

where \(E_i\) is the set of eligible targets. For every source with a positive weight sum,

\[
\sum_{j\in E_i}\hat P_{ij}=P_i.
\]

Possible weights include residential building floor area, building footprint area, built-up fraction or a justified land-cover suitability measure. The weights must be calculated or supplied by the caller; the algorithm does not determine whether they are valid proxies for population.

## Eligibility and zero-weight handling

Geometric eligibility and ancillary weight are not always the same thing. An optional Boolean eligibility matrix records which target units overlap each source zone, even when their ancillary weight is zero. If a source has positive total but no eligible targets, the function raises an error. If eligible targets exist but all their weights are zero, the default is also to raise an error. A uniform allocation is available only as an explicit fallback and the affected source rows are returned in metadata.

## What this baseline guarantees—and what it does not

- **Guarantee:** every source-zone total is conserved to floating-point precision.
- It does not calculate polygon intersections, resolve overlapping source zones, or derive ancillary weights.
- It does not estimate source totals or validate population counts.
- Conservation does not imply accurate target-level estimates. Ancillary-data quality, source-zone boundaries, population distribution and validation data determine accuracy.
- This is a top-down method. Bottom-up microcensus estimation, settlement-level modelling and full building-based population estimation are separate methods.

## Implementation and learning material

- [Python implementation](../implementations/python/dasymetric-allocation/README.md)
- [Tests](../implementations/python/dasymetric-allocation/test_dasymetric_allocation.py)
- [Intern walkthrough](../implementations/python/dasymetric-allocation/walkthrough.md)
- [Visual lab](../notebooks/dasymetric-allocation-lab.ipynb)

## References

- Mennis, J. (2003). Generating surface models of population using dasymetric mapping. *The Professional Geographer*, 55(1), 31–42. https://doi.org/10.1111/0033-0124.10042
- Eicher, C. L. & Brewer, C. A. (2001). Dasymetric mapping and areal interpolation: implementation and evaluation. *Cartography and Geographic Information Science*, 28(2), 125–138. https://doi.org/10.1559/152304001782173727
