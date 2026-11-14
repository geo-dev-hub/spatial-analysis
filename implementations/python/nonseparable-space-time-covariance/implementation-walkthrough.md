# Intern walkthrough: nonseparable space-time covariance

## Goal

Build a covariance matrix for observations that each have a location and a time. Unlike a separable product, this model lets temporal lag change spatial dependence.

## Install and test

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Trace the calculation

1. Validate finite non-negative spatial distances and finite temporal lags.
2. Check theorem-scoped parameters: \(0<\alpha\leq1\), \(0\leq\beta\leq1\), positive scales and positive integer spatial dimension.
3. Compute the temporal interaction term

   $$
   q(u)=1+\left(\frac{|u|}{a_t}\right)^{2\alpha}.
   $$

4. Compute the covariance

   $$
   C(\mathbf{h},u)
   =
   \sigma^2 q(u)^{-\beta d/2}
   \exp\left(
   -\frac{\|\mathbf{h}\|^2}{a_s^2q(u)^\beta}
   \right).
   $$

5. The factor \(q(u)^{-\beta d/2}\) changes covariance amplitude.
6. The denominator \(q(u)^\beta\) changes the effective spatial scale.
7. The matrix builder computes pairwise Euclidean distances and absolute time differences.
8. The diagnostic checks symmetry and the minimum eigenvalue.

## Reproduce

~~~python
import numpy as np
from covariance import gneiting_covariance_matrix, covariance_matrix_diagnostics
xy=np.array([[0,0],[1,0],[0,1],[2,1]],float)
times=np.array([0,.5,1,2])
K=gneiting_covariance_matrix(xy,times,spatial_scale=2,temporal_scale=1)
print(K)
print(covariance_matrix_diagnostics(K))
~~~

## Tests and limitations

Tests cover zero-lag variance, lag symmetry, beta-zero behaviour, temporal interaction, duplicate observations, invalid inputs and a finite PSD example. One eigenvalue check is not a theorem. The validity claim comes from the Gneiting construction under its conditions.

Do not treat longitude/latitude degrees as Euclidean coordinates or substitute network/spherical distance without a separate validity result. This package does not fit parameters, estimate measurement error, perform kriging or scale to large datasets.
