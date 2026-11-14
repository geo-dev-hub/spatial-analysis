# Adaptive and Bayesian spatial sampling algorithms

This package includes:
- network-based adaptive cluster sampling expansion from an initial sample;
- Gaussian-process upper-confidence-bound (GP-UCB) selection over candidate spatial survey sites.

The GP-UCB baseline assumes an isotropic stationary RBF kernel, known hyperparameters, a constant prior mean and independent Gaussian observation noise. It selects from a supplied finite candidate set. It is not a spatially nonstationary or constrained Bayesian optimiser; hyperparameter fitting, anisotropy, barriers, costs, batch selection and design-based survey inference remain outside scope.

The adaptive cluster sampler returns the realised sample set, not a population estimator. Valid inclusion probabilities and estimators depend on the initial probability-sampling design and adaptive network structure.

Run python -m pip install -r requirements.txt and python -m pytest -q.


The package also includes generic UCB1 for independent stationary reward arms. This is a bandit baseline for comparing survey-site reward strategies; it does not model spatial correlation between candidate locations.
