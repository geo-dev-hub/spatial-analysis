# kNNDM implementation walkthrough

## Prediction geometry determines validation geometry

Random folds can leave a test point close to training points even when the map must be predicted in sparsely sampled regions. Arbitrary spatial blocks can make test-to-training distances much larger than those encountered during prediction. kNNDM instead compares the nearest-neighbour distances in held-out folds with nearest-neighbour distances from actual prediction locations to the training sample.

## Statistics

For training point x_j, let d_j be its nearest distance to another training point. For prediction point z_i, let d_ij be its nearest distance to any training point. For a fold assignment L, let d*_j(L) be the nearest distance from a test point to a point retained in that fold's training complement.

The empirical distributions of d*_j(L) and d_ij are compared with the one-dimensional Wasserstein-1 distance:

    W = integral |G*_j(r,L) - G_ij(r)| dr

The algorithm first tests whether the training nearest-neighbour distribution is shifted toward shorter distances than the prediction-to-training distribution. If the one-sided KS test does not reject that clustering alternative, it uses random k-fold. Otherwise, it searches spatial cluster configurations and chooses the one with the smallest W.

## Implementation stages

1. Validate finite coordinate arrays in a common projected coordinate system.
2. Compute training-to-training and prediction-to-training nearest-neighbour distances.
3. Run the one-sided KS diagnostic.
4. For clustered samples, generate logarithmically spaced candidate cluster counts, fit KMeans, and order cluster centroids along the first principal component.
5. Merge intermediate clusters into the requested number of folds, subject to the maximum fold fraction.
6. For each candidate, calculate each test point's nearest distance to its fold's training complement and compare that distribution with prediction NNDs.
7. Return the minimum-W configuration, folds and diagnostics.

## Interpretation and limits

kNNDM is a fold-construction strategy, not a model or scoring metric. It does not guarantee unbiased map accuracy. Inspect the distance distributions, confirm prediction points represent the intended domain, and prevent preprocessing leakage within folds. Report metrics from concatenated out-of-fold predictions when fold sizes differ.

This teaching version is a bounded KMeans/Euclidean subset. It does not reproduce every detail of CAST, including hierarchical clustering, spherical distances, exact reference cluster merging, polygon sampling or production-scale nearest-neighbour indexing. It is not the original NNDM leave-one-out algorithm.
