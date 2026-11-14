# Intern walkthrough: adaptive cluster sampling

Adaptive cluster sampling is useful when the variable of interest is rare or clustered. Begin with an initial probability sample of units. If an observed unit meets the prespecified criterion, add its neighbours to the sample. Newly observed qualifying units can trigger further expansion. Continue until no newly recruited unit triggers additional recruitment.

This implementation uses a finite undirected adjacency graph and the rule value >= threshold. It returns the initial sample, the complete realised sample and the recruited units. It deliberately does not estimate population totals: valid estimation requires the sampling design's inclusion probabilities and a suitable adaptive-cluster estimator (for example, network or Hansen–Hurwitz-style formulations under their assumptions).

The threshold and neighbourhood definition must be set before observing outcomes. Report the initial design, network, threshold, expansion rule and estimator separately.
