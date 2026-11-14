# Forecast verification teaching package

The package includes binary-event contingency metrics, Brier score and skill, reliability bins, tied-rank ROC AUC, regular-grid Fractions Skill Score, and a new ensemble-verification module.

The ensemble module implements empirical-distribution CRPS per case and its sample mean, plus an expected rank histogram that fractionally distributes ties across admissible ranks. Inputs are paired cases with a rectangular ensemble and finite values. These metrics do not replace calibration assessment, uncertainty intervals or a spatially valid held-out design.

Run python -m pip install -r requirements.txt and python -m pytest -q from this directory. See the individual module docstrings for contracts and the package walkthrough for derivations.


## MODE-inspired object extraction and matching

The object_verification module implements a bounded sequence: optional Gaussian smoothing, thresholding, connected-component labelling, measurement of area/intensity/weighted centroid/orientation, and minimum-cost one-to-one forecast-observation matching with explicit unmatched objects. The matching cost uses normalized centroid distance and log-ratio penalties for area and mean intensity.

This is not a full MODE reproduction. It omits within-field merging and cluster objects, the official fuzzy-interest formulation, multi-threshold hierarchies and temporal tracking. The implementation is a transparent teaching candidate intended for parameter-sensitivity experiments.

Reference: Davis, Brown & Bullock (2006), “Object-Based Verification of Precipitation Forecasts. Part I: Methodology and Application to Mesoscale Rain Areas,” *Monthly Weather Review*, 134, 1772–1784. https://doi.org/10.1175/MWR3145.1


## SAL structure-amplitude-location verification

The sal_verification module computes the amplitude component from domain means, the structure component from precipitation-mass-weighted scaled object volumes, and location as L1 centroid displacement plus L2 difference in object scatter. Forecast and observation objects are identified independently using a fraction of each field's own maximum. The implementation does not match objects between fields, consistent with the SAL method.

The connected-component object finder is a bounded teaching choice, not a claim of exact parity with the original coherent-object identification. Dry-field edge cases are explicit. See [implementation](sal_verification.py), [tests](test_sal_verification.py) and [lab](../../../notebooks/sal-precipitation-verification-lab.ipynb).

Reference: Wernli, Paulat, Hagen & Frei (2008), “SAL—A Novel Quality Measure for the Verification of Quantitative Precipitation Forecasts,” *Monthly Weather Review*, 136, 4470–4487. https://doi.org/10.1175/2008MWR2415.1
