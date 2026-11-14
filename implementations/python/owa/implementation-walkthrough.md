# Intern walkthrough: Ordered Weighted Averaging

## 1. Understand the two weight vectors

Criterion weights follow named criteria. Order weights follow rank positions after sorting values at each cell. The highest value receives the first order weight, the second-highest receives the second, and so on.

## 2. Standard OWA

With no criterion weights supplied, the implementation uses equal importance values. It sorts the criterion values descending per cell and applies the order vector. Equal order weights produce the arithmetic mean; all weight on the first position selects the maximum; all weight on the last position selects the minimum.

## 3. GIS weighted OWA

When criterion weights are supplied, the implementation uses the same per-cell sorting indices to reorder those importance weights. It then calculates the weighted numerator and divides by the sum of the reordered products of criterion and order weights. The denominator is necessary because the products generally do not sum to one.

## 4. ORness

The ORness diagnostic summarises the order vector's position between maximum-like and minimum-like behaviour. It describes the operator, not the accuracy of the suitability map.

## 5. NoData and alignment

The code uses strict common-footprint NoData handling. It validates array shapes but cannot verify geospatial metadata; use a raster library to confirm CRS, transform, resolution and alignment before calling the function.

## 6. Test and extend

Tests cover descending sorting, equal weights, min/max endpoints, a published GIS weighted OWA worked example, ORness and invalid inputs. Extend the lab by comparing three order vectors and mapping the locations whose rank changes most.
