# Spatial distribution-shift statistics

NumPy/SciPy teaching implementations of:
- unbiased squared maximum mean discrepancy (MMD) with a Gaussian RBF kernel;
- unbiased sample energy-distance statistic;
- a reproducible permutation test for MMD.

Inputs are finite feature matrices with matching dimensions. MMD bandwidth is in feature-space units; standardise features deliberately and report the choice. Both unbiased finite-sample U-statistics can be negative and are not clipped; do not interpret an individual estimate as a guaranteed non-negative distance.

The permutation test assumes exchangeable independent rows. It is not valid for spatially autocorrelated samples without a defensible block/cluster permutation or other spatial null design. This package does not implement domain classifiers, area-of-applicability, kernel mean matching or a spatially valid resampling design.

Run python -m pip install -r requirements.txt and python -m pytest -q.
