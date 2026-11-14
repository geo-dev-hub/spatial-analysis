# k-fold nearest-neighbour distance matching (kNNDM)

This package implements a bounded, prediction-oriented kNNDM fold selector for projected Euclidean coordinates.

## What it does

1. Computes each training point's nearest-neighbour distance to the other training points.
2. Computes each prediction location's nearest-neighbour distance to the training sample.
3. Uses a one-sided two-sample Kolmogorov–Smirnov diagnostic to check whether training points are more clustered than prediction locations.
4. If clustering is detected, fits candidate KMeans partitions, merges clusters into the requested number of folds using centroid order along the first principal component, and selects the feasible configuration with the smallest 1D Wasserstein distance between cross-validation and prediction nearest-neighbour distances.
5. Otherwise returns seeded random K-fold partitions.

Returned folds contain zero-based indices. The result also exposes the clustering diagnostic, selected intermediate cluster count, candidate scores and both nearest-distance samples.

## Install and run

    python -m pip install -r requirements.txt
    python -m pytest -q

## Coordinate and validation contract

- Supply training and prediction points in the same projected Euclidean coordinate reference system and units. Longitude/latitude degrees are not appropriate.
- Prediction points should represent the actual model domain, such as raster-cell centroids.
- Evaluate metrics on the stacked out-of-fold predictions, not an unweighted average of fold metrics: fold sizes can differ.
- Inspect the two nearest-distance distributions and returned Wasserstein W. A low W indicates a closer match, not proof of unbiased accuracy.
- The KS diagnostic is a simplified implementation of the paper's one-sided clustering check. Spatial dependence, finite prediction-point sampling and model-feature-space differences still matter.

## Explicit exclusions

This is not the original NNDM leave-one-out algorithm. It is a teaching implementation of the k-fold extension with KMeans clustering and Euclidean projected coordinates. It does not implement hierarchical clustering, spherical distances, polygon sampling, target stratification or a full CAST-compatible workflow. Its cluster merging is a transparent reproducible variant and should be compared against CAST before publication or operational map-accuracy claims.

## References

- Linnenbrink, J., Milà, C., Ludwig, M. & Meyer, H. (2024). kNNDM CV: k-fold nearest-neighbour distance matching cross-validation for map accuracy estimation. *Geoscientific Model Development*, 17, 5897–5912. https://doi.org/10.5194/gmd-17-5897-2024
- Milà, C. et al. (2022). Nearest neighbour distance matching Leave-One-Out Cross-Validation for map validation. *Methods in Ecology and Evolution*. https://doi.org/10.1111/2041-210X.13851
