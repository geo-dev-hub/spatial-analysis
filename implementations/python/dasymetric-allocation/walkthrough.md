# Weighted dasymetric allocation: intern walkthrough

## 1. Start with source totals

Each source polygon or administrative zone has a known total, such as a census population count. The algorithm does not create this total; it reallocates it to smaller target units.

## 2. Supply ancillary evidence

For each source-target intersection, provide a non-negative proxy weight. Building floor area, residential building area or a built-up fraction are common examples. Also provide an eligibility mask when a target intersects a source zone but has zero proxy weight.

## 3. Normalize within each source

For source zone i, divide each eligible weight by the sum of that row's weights. Multiply the resulting shares by the source total. The shares sum to one, so the allocated total is conserved.

## 4. Handle zero-weight rows deliberately

If a source has positive population and eligible targets but all weights are zero, the default is to stop. A uniform fallback is available only when explicitly requested and is returned in the result metadata.

## 5. What conservation does not prove

Conservation is a numerical accounting property, not evidence that the target-level population is accurate. Accuracy depends on source totals, boundary overlays, ancillary data, the relationship between the proxy and population, and validation against independent small-area data.

## References

- Mennis, J. (2003). Generating surface models of population using dasymetric mapping. The Professional Geographer, 55(1), 31–42. https://doi.org/10.1111/0033-0124.10042
- Eicher, C. L. & Brewer, C. A. (2001). Dasymetric mapping and areal interpolation: implementation and evaluation. Cartography and Geographic Information Science, 28(2), 125–138. https://doi.org/10.1559/152304001782173727
