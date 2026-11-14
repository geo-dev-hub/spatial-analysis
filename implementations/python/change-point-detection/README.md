# Change-point detection: executable mean-shift baselines

This package implements three transparent univariate teaching algorithms:
- CUSUM: two-sided Page-style sequential monitoring against a known reference mean.
- Binary segmentation: greedy retrospective recursive splitting.
- PELT mean: pruned dynamic programming for a penalised piecewise-constant mean objective using segment SSE.

Run python -m pip install -r requirements.txt and python -m pytest -q.

Inputs are finite numeric observations in temporal order. The segmentation methods assume equally weighted observations and a piecewise-constant mean. Change points are zero-based indices of the first observation in the new segment. Minimum segment length is in observations.

CUSUM needs a known reference mean, allowance and threshold. It is not automatically calibrated for a target false-alarm rate. PELT is exact for the stated objective subject to numerical arithmetic; its worst-case runtime is quadratic. The package does not implement variance/distribution shifts, BOCPD, BEAST, irregular-time likelihoods or a general plug-in cost framework.
