# Adaptive cluster sampling

A transparent network-expansion implementation of adaptive cluster sampling. Start from an initial sample; every observed unit meeting the threshold recruits all of its neighbours. Recruited units are observed and may recruit further neighbours. The result is the realised sample set and the distinction between initial and recruited units.

The function does not calculate a design-unbiased estimator or inclusion probabilities. Those depend on the initial probability-sampling design, network definition, threshold rule and adaptive sampling estimator. Do not treat the expanded sample as a simple random sample.

Run python -m pytest -q.
