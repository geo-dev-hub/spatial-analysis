# Intern walkthrough: adaptive cluster sampling

Adaptive cluster sampling is useful when the variable of interest is rare or clustered. Begin with an initial probability sample of units. If an observed unit meets the prespecified criterion, add its neighbours to the sample. Newly observed qualifying units can trigger further expansion. Continue until no newly recruited unit triggers additional recruitment.

This implementation uses a finite undirected adjacency graph and the rule value >= threshold. It returns the initial sample, the complete realised sample and the recruited units. It deliberately does not estimate population totals: valid estimation requires the sampling design's inclusion probabilities and a suitable adaptive-cluster estimator (for example, network or Hansen–Hurwitz-style formulations under their assumptions).

The threshold and neighbourhood definition must be set before observing outcomes. Report the initial design, network, threshold, expansion rule and estimator separately.


## UCB1 multi-armed bandit

For each arm a with n_a observed rewards and empirical mean μ_a, UCB1 selects the arm maximising

UCB(a)=μ_a+sqrt(2 log(t)/n_a),

where t is the total number of pulls. Untried arms are selected first. The exploration term shrinks as an arm is sampled more often.

The included simulator assumes independent stationary Gaussian reward arms. If arms are candidate spatial locations, spatial autocorrelation violates the independent-arm abstraction unless the reward model explicitly accounts for it. Treat this as a generic bandit baseline, not a spatially aware optimiser.
