# Intern walkthrough: GP-UCB for candidate spatial survey sites

Bayesian optimisation maintains a probabilistic surrogate for an expensive spatial response. Given observed sites X and values y, a Gaussian process with an isotropic RBF covariance produces a posterior mean μ(s) and standard deviation σ(s) at candidate sites.

The upper-confidence-bound acquisition is

UCB(s)=μ(s)+sqrt(β) σ(s).

The posterior mean rewards exploitation; posterior uncertainty rewards exploration. β controls the trade-off. The selected site is the candidate with the largest UCB.

This implementation uses fixed hyperparameters, a constant prior mean, independent Gaussian observation noise and an isotropic stationary RBF kernel. It does not fit hyperparameters, enforce survey costs, model barriers or account for spatial nonstationarity. The resulting selection is only as defensible as the kernel, candidate set and reward definition.
