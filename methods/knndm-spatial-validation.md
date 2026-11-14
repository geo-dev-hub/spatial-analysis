# k-fold nearest-neighbour distance matching (kNNDM)

kNNDM is a prediction-oriented spatial cross-validation design. Its objective is to make the distribution of nearest distances from held-out observations to their fold-specific training data resemble the distribution of nearest distances from actual prediction locations to the full training sample.

It addresses a different question from buffered or block cross-validation. Those methods often seek geographic separation or transfer to new regions; kNNDM attempts to reproduce the spatial support conditions of a defined prediction domain.

## Core quantities

- Training NND: for each training point, distance to its closest other training point.
- Prediction NND: for each prediction location, distance to its closest training point.
- CV NND: for each held-out point, distance to its closest point retained in that fold's training complement.

The match is measured by the one-dimensional Wasserstein-1 distance between the CV NND sample and prediction NND sample. Smaller W means a closer distance-distribution match.

The 2024 reference algorithm first uses a one-sided Kolmogorov–Smirnov test to assess whether the training sample is clustered relative to prediction locations. If it does not detect clustering, it returns random k-fold CV. Otherwise, it searches cluster-derived fold configurations and chooses the one with the smallest W.

## Repository implementation

The teaching implementation is in [implementations/python/knndm](../implementations/python/knndm/README.md), with tests and an intern walkthrough. It implements a bounded KMeans/Euclidean version for projected coordinates. It is not an exact port of CAST: hierarchical clustering, spherical distances, exact reference merging details, polygon sampling and several production options are not included.

The original NNDM method is a distinct leave-one-out procedure and is not implemented by this package. Do not cite this package as completion of NNDM LOO.

## Practical workflow

1. Project training and prediction coordinates into a suitable metric CRS.
2. Use prediction points that represent the actual map domain, not merely the training footprint.
3. Generate candidate folds and inspect W and the nearest-distance distributions.
4. Train and predict in each fold without preprocessing leakage.
5. Stack all out-of-fold predictions before calculating map-level accuracy metrics, particularly when folds are unbalanced.
6. Compare against independent probability-sample validation whenever possible.

## References

- Linnenbrink, J., Milà, C., Ludwig, M. & Meyer, H. (2024). *kNNDM CV: k-fold nearest-neighbour distance matching cross-validation for map accuracy estimation*. Geoscientific Model Development, 17, 5897–5912. https://doi.org/10.5194/gmd-17-5897-2024
- Milà, C. et al. (2022). *Nearest neighbour distance matching Leave-One-Out Cross-Validation for map validation*. Methods in Ecology and Evolution. https://doi.org/10.1111/2041-210X.13851
