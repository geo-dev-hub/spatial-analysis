# Forecast verification teaching package

The package includes binary-event contingency metrics, Brier score and skill, reliability bins, tied-rank ROC AUC, regular-grid Fractions Skill Score, and a new ensemble-verification module.

The ensemble module implements empirical-distribution CRPS per case and its sample mean, plus an expected rank histogram that fractionally distributes ties across admissible ranks. Inputs are paired cases with a rectangular ensemble and finite values. These metrics do not replace calibration assessment, uncertainty intervals or a spatially valid held-out design.

Run python -m pip install -r requirements.txt and python -m pytest -q from this directory. See the individual module docstrings for contracts and the package walkthrough for derivations.
