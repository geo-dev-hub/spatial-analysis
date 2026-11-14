# Adaptive and Bayesian spatial sampling

Adaptive sampling is a family of designs in which later site selections depend on information collected earlier. The word *adaptive* covers several different statistical problems. A design that expands around rare detections, a Bayesian optimisation policy that searches for a maximum, and an active-learning policy that chooses labels for a classifier do not share the same objective or inferential guarantees.

The first decision is therefore not which acquisition function to use. It is what the survey must estimate or discover.

## 1. Separate the objectives

| Objective | Appropriate family | Primary output | Main inferential caution |
|---|---|---|---|
| Estimate a finite-population total or mean when rare values cluster | Adaptive cluster sampling (ACS) | Design-based estimate and variance | Adaptive inclusion probabilities must be respected |
| Locate a hotspot or maximise an expensive spatial response | Bayesian optimisation / sequential design | Best candidate or high-response region under a model | Optimisation is not automatically unbiased population estimation |
| Improve a predictive model with a limited labelling budget | Active learning | Better learner under a chosen validation target | Query-selected labels are not a probability sample |
| Allocate effort sequentially among spatially varying actions | Contextual or spatial bandits | A sampling/measurement policy | Reward, exploration and policy evaluation must be explicit |

Do not use these names interchangeably. A good policy for finding the maximum may be poor for estimating the domain-wide mean.

## 2. Adaptive cluster sampling

Thompson's classical design starts with a probability sample of spatial units. A condition is fixed in advance. When an initially sampled unit satisfies that condition, neighbouring units are added; if newly observed neighbours also satisfy the condition, expansion continues. The connected qualifying units form a network, and sampled non-qualifying boundary units are often called edge units.

The design is useful when the target is rare and spatially clustered: for example, sparse mineral occurrences, invasive species patches or disease hotspots. The initial probability sample preserves a known design foundation; adaptive expansion concentrates field effort around detections.

A valid ACS plan must specify before fieldwork:

1. the finite population and its sampling units;
2. the initial probability design and inclusion probabilities;
3. the neighbourhood relation (contiguity, distance, graph edges, or another rule);
4. the expansion condition and whether it is based on a measured value or a predeclared class;
5. the rule for handling networks encountered more than once;
6. the estimator and variance estimator that correspond to the actual design.

A naive average of all visited units is generally not design-unbiased. The adaptive rule changes which units are observed and how networks enter the final sample. Thompson (1990) derives design-unbiased estimators for the stated adaptive cluster designs; later work develops improved estimators and variants. The estimator must match the implemented sampling design, including without-replacement and network-selection details.

## 3. Bayesian optimisation for spatial fields

Bayesian optimisation is appropriate when evaluating a candidate site is expensive and the goal is to optimise a response, not necessarily to estimate a population mean. A surrogate model (often a Gaussian process) represents uncertainty over the response surface. At each iteration, an acquisition function balances exploration of uncertain areas with exploitation of areas predicted to have high value.

Common acquisition families include:

- **Expected improvement:** expected gain over the best observed response.
- **Probability of improvement:** probability that a candidate exceeds the current best by a chosen margin.
- **Upper confidence bound:** a tunable combination of predictive mean and uncertainty.
- **Knowledge gradient:** expected improvement in the value of the best decision after observing a candidate.

For spatial problems, the covariance model encodes assumptions about distance, anisotropy, barriers, nonstationarity and possibly multiple scales. A Euclidean isotropic Gaussian process is not automatically appropriate for coastlines, river networks, road systems or disconnected regions.

The acquisition function must reflect the objective. If the objective is integrated prediction accuracy or uncertainty reduction, use an integrated criterion rather than a maximum-seeking criterion. If sites are selected in batches, account for redundancy among proposed locations; selecting the top-k marginal acquisition values independently can cluster the batch.

## 4. Active learning for map validation

Active learning chooses which unlabelled examples should receive expensive reference labels. Uncertainty sampling, query-by-committee and diversity-aware selection can improve a classifier efficiently. In map validation, however, the purpose of the labels matters:

- For **model development**, adaptive labels can be useful if the training procedure and validation design are kept separate.
- For **accuracy estimation**, a probability sample with known inclusion probabilities is generally needed for design-based estimates of area-adjusted accuracy and class area.
- For **error discovery**, targeted review of uncertain or high-impact regions can be useful, but the resulting sample should not be reported as if it were a representative probability sample.

A map can be confidently wrong. Uncertainty-only selection may miss systematic errors in familiar-looking regions or under-represent rare classes. Use stratification, minimum class coverage, spatial diversity and independent probability-sample audits where the goal requires population-level accuracy estimates.

## 5. Adaptive cluster sampling versus model-based sequential design

These approaches answer different questions.

- ACS obtains additional observations by a predeclared neighbourhood-expansion rule and can support design-based inference when paired with its matching estimators.
- Bayesian optimisation uses a probabilistic response model and an objective-specific acquisition rule; its guarantees depend on modelling assumptions and the optimisation setup.
- Active learning selects labels to improve a learner; it does not by itself produce an unbiased estimate of map accuracy or population totals.
- Bandit methods allocate sequential effort to maximise cumulative or terminal reward; they require explicit treatment of exploration, spatial context, costs and policy evaluation.

A hybrid is possible, but the components should remain explicit. For example, a probability sample can provide a design-based audit while an active-learning stream improves the classifier between audits.

## 6. A defensible spatial sampling workflow

1. State the estimand or optimisation target before selecting a design.
2. Define the population, spatial support, time window and candidate locations.
3. Separate probability-sample observations from adaptively selected observations in the data model.
4. Record every selection decision, candidate set, acquisition score, stopping decision and observation cost.
5. Predefine neighbourhoods, thresholds, batch rules and stopping criteria.
6. Model spatial dependence at a scale justified by the process and data; test sensitivity to covariance and neighbourhood assumptions.
7. Reserve independent probability-sample or deployment-relevant evaluation data when unbiased population inference or generalisation is required.
8. Report effort, inclusion probabilities where defined, uncertainty, coverage gaps and the limitations of the selection mechanism.

## 7. What to implement next

The next executable package should not try to combine all these families. A sound first target is a small, auditable ACS teaching implementation with a finite lattice, a probability-selected initial sample, explicit adjacency and threshold rules, network bookkeeping, and an estimator/variance derivation tied to one precisely stated design. Bayesian optimisation should be a separate package with a declared surrogate and acquisition function. Active-learning selection should likewise remain separate from design-based accuracy estimation.

## References

- Thompson, S. K. (1990). “Adaptive Cluster Sampling.” *Journal of the American Statistical Association*, 85(412), 1050–1059. [https://doi.org/10.1080/01621459.1990.10474975](https://doi.org/10.1080/01621459.1990.10474975)
- Salehi, M. M., & Seber, G. A. F. (1997). “Adaptive cluster sampling with networks selected without replacement.” *Biometrika*, 84(1), 209–219. [https://doi.org/10.1093/biomet/84.1.209](https://doi.org/10.1093/biomet/84.1.209)
- Thompson, S. K. (2006). “Adaptive Web Sampling.” *Biometrics*, 62(4), 1224–1234. [https://doi.org/10.1111/j.1541-0420.2006.00576.x](https://doi.org/10.1111/j.1541-0420.2006.00576.x)
- Andrade-Pacheco, R., et al. (2020). “Finding hotspots: development of an adaptive spatial sampling approach.” *Scientific Reports*, 10, 10939. [https://doi.org/10.1038/s41598-020-67666-3](https://doi.org/10.1038/s41598-020-67666-3)
- Di Fiore, F., Nardelli, M., & Mainini, L. (2024). “Active Learning and Bayesian Optimization: A Unified Perspective to Learn with a Goal.” *Archives of Computational Methods in Engineering*, 31, 2985–3013. [https://doi.org/10.1007/s11831-024-10064-z](https://doi.org/10.1007/s11831-024-10064-z)
- Moradi, M., & Brown, J. (2024). “Mapping using an adaptive sampling design.” *Spatial Statistics*, 60, 100820. [https://doi.org/10.1016/j.spasta.2024.100820](https://doi.org/10.1016/j.spasta.2024.100820)

This is a method-selection and design guide, not an implementation. The ACS estimators, spatial Bayesian optimisation, acquisition-function diagnostics, active-learning strategies and survey-weighted map-accuracy estimators remain separate implementation tasks.


## Executable adaptive cluster sampling

The package now implements network expansion from an initial sample: a unit meeting the prespecified threshold recruits all of its neighbours, and recruited qualifying units can continue expansion. It returns the realised sample and separates initial from recruited units. It does not calculate an estimator or inclusion probabilities; those depend on the initial probability-sampling design and the adaptive estimator.

- [Implementation and tests](../implementations/python/adaptive-sampling/README.md)
- [Intern walkthrough](../implementations/python/adaptive-sampling/implementation-walkthrough.md)
- [Lab](../notebooks/adaptive-cluster-sampling-lab.ipynb)


## Executable Gaussian-process UCB baseline

The companion package now includes candidate-site selection with a Gaussian-process upper-confidence-bound acquisition, using a stationary isotropic RBF kernel, fixed hyperparameters and Gaussian observation noise. It is a transparent baseline rather than a full constrained Bayesian optimiser. The notebook visualises posterior mean, uncertainty-driven UCB and the selected candidate.

- [Implementation and tests](../implementations/python/adaptive-sampling/README.md)
- [GP-UCB walkthrough](../implementations/python/adaptive-sampling/bayesian-optimization-walkthrough.md)
- [Lab](../notebooks/gp-ucb-spatial-survey-lab.ipynb)


## UCB1 baseline for survey-arm selection

A generic UCB1 implementation now accompanies the GP-UCB spatial candidate selector. It simulates independent stationary reward arms and uses the classical empirical-mean plus exploration-bound rule. It is useful as a baseline for survey allocation, but it does not model spatial correlation between sites; a spatial bandit requires a contextual or correlated reward model.

- [UCB1 implementation and tests](../implementations/python/adaptive-sampling/ucb1.py)
