# Nearest-neighbour distance matching (NNDM) LOO CV

This package implements the original prediction-oriented NNDM leave-one-out fold construction for projected Euclidean coordinates.

## Method

For each observation j, initialise its analysis set with every training observation except j. Compute the nearest distance from each held-out observation to its current analysis set. At each step, select the globally smallest current CV nearest-neighbour distance r and its closest analysis observation k. Trial-remove k from that fold. Accept the removal only when the modified CV nearest-neighbour ECDF at r remains at least as large as the prediction-to-training nearest-neighbour ECDF at r. Continue while the smallest eligible CV distance is within the supplied autocorrelation range phi and the minimum analysis-set size is respected.

The returned folds include one test observation each, retained training indices and additionally excluded indices. The package also returns prediction and CV nearest-distance samples and ECDF diagnostics.

## Usage

    python -m pip install -r requirements.txt
    python -m pytest -q

    from nndm import nndm_loo
    result = nndm_loo(training_xy, prediction_xy,
                      autocorrelation_range=250.0, min_train=0.5)
    for fold in result["folds"]:
        # fit on training_xy[fold["train"]], predict at training_xy[fold["test"]]
        pass

## Assumptions and limitations

- Coordinates must be in a common projected Euclidean CRS with meaningful linear units. Geographic/geodesic distance support is not implemented.
- prediction_points should represent the actual target map domain (e.g. valid raster-cell centroids), not just the training footprint.
- autocorrelation_range phi must be chosen from a defensible variogram/residual or outcome autocorrelation analysis. It is not inferred by this package.
- min_train prevents folds from becoming too small. If the cap binds, matching may remain incomplete; inspect diagnostics.
- This is a transparent O(n^3)-style teaching implementation, not a production-scale CAST replacement. It recomputes nearest neighbours across folds and is intended for modest datasets.
- The algorithm matches geographical nearest-distance conditions; it does not solve covariate shift, temporal dependence, sampling bias or model leakage.
- Tests use synthetic geometry and do not establish unbiased map-accuracy estimation.

## References

- Milà, C., Mateu, J., Pebesma, E. & Meyer, H. (2022). Nearest neighbour distance matching Leave-One-Out Cross-Validation for map validation. Methods in Ecology and Evolution, 13, 1304–1316. https://doi.org/10.1111/2041-210X.13851
- CAST NNDM reference documentation: https://hannameyer.github.io/CAST/reference/nndm.html
