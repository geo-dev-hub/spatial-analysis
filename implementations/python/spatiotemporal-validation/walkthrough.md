# Leave-location-and-time-out: intern walkthrough

## Why random folds can mislead

Repeated observations from the same place and time period are dependent. A random split can put similar location/time contexts in both training and test sets, making transfer performance look better than it is. Target-oriented validation withholds the dimensions to which a model is expected to generalise.

## Construct one fold

Choose a location group s and time group t. Partition rows into four conceptual cells:

- Test: location s and time t.
- Buffer: location s at other times, or other locations at time t.
- Train: other locations at other times.

The buffer is deliberately unused for that fold so neither the held-out location nor held-out time leaks into training.

## Repeat over observed pairs

Enumerate distinct observed (location, time) pairs in first-seen order. Each pair produces one fold. Test sets partition the input rows, while train and buffer are recomputed for each pair.

## Complexity

For n rows and f observed location/time pairs, the direct implementation performs Boolean mask construction per fold: O(nf) time and O(n) temporary storage per fold. It is a transparent teaching implementation; large panels can use grouped indexing to reduce repeated scans.

## Interpretation

The score estimates joint transfer to unseen location/time combinations under the chosen grouping. It does not estimate interpolation to nearby places, future-only forecasting, or performance under a spatial-distance buffer.

## References

- Meyer, H., Reudenbach, C., Hengl, T., Katurji, M. & Nauss, T. (2018). Improving performance of spatio-temporal machine learning models using forward feature selection and target-oriented validation. Environmental Modelling & Software, 101, 1–9. https://doi.org/10.1016/j.envsoft.2017.12.001
- Cerqueira, V., et al. (2021). Evaluation procedures for forecasting with spatiotemporal data. Mathematics, 9(6), 691. https://doi.org/10.3390/math9060691
- Clark, L. P., et al. (2024). A review of geospatial exposure models and approaches for health data integration. Journal of Exposure Science & Environmental Epidemiology. https://doi.org/10.1038/s41370-024-00712-8
