# Forecast verification teaching package

The package includes binary-event contingency metrics, Brier score and skill, reliability bins, tied-rank ROC AUC, regular-grid Fractions Skill Score, and a new ensemble-verification module.

The ensemble module implements empirical-distribution CRPS per case and its sample mean, plus an expected rank histogram that fractionally distributes ties across admissible ranks. Inputs are paired cases with a rectangular ensemble and finite values. These metrics do not replace calibration assessment, uncertainty intervals or a spatially valid held-out design.

Run python -m pip install -r requirements.txt and python -m pytest -q from this directory. See the individual module docstrings for contracts and the package walkthrough for derivations.


## MODE-inspired object extraction and matching

The object_verification module implements a bounded sequence: optional Gaussian smoothing, thresholding, connected-component labelling, measurement of area/intensity/weighted centroid/orientation, and minimum-cost one-to-one forecast-observation matching with explicit unmatched objects. The matching cost uses normalized centroid distance and log-ratio penalties for area and mean intensity.

This is not a full MODE reproduction. It omits within-field merging and cluster objects, the official fuzzy-interest formulation, multi-threshold hierarchies and temporal tracking. The implementation is a transparent teaching candidate intended for parameter-sensitivity experiments.

Reference: Davis, Brown & Bullock (2006), “Object-Based Verification of Precipitation Forecasts. Part I: Methodology and Application to Mesoscale Rain Areas,” *Monthly Weather Review*, 134, 1772–1784. https://doi.org/10.1175/MWR3145.1
