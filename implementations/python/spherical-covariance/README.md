# Isotropic covariance on the two-sphere

This package constructs valid isotropic covariance functions on the unit two-sphere (S^2) using a finite Schoenberg/Legendre series. It is a spherical counterpart to the Euclidean examples, not a planar kernel with a new distance pasted in.

## The construction

For angular separation (	hetain[0,pi]),

\[
C(\theta)=\sum_{\ell=0}^{L} b_\ell P_\ell(\cos\theta),
\qquad b_\ell\geq 0.
\]

Here (P_\ell) is the Legendre polynomial of degree (ell). Non-negative coefficients make this a valid isotropic covariance on (S^2); the marginal variance is (C(0)=\sum_\ell b_\ell). The finite series is a truncated spectral construction, not a fit to observations.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

~~~python
from spherical_covariance import (
    latlon_to_unit_vectors,
    spherical_covariance_matrix,
)

sites = latlon_to_unit_vectors([0, 20, -35], [0, 90, 140])
C = spherical_covariance_matrix(sites, [1.0, 0.5, 0.2, 0.1])
print(C)
~~~

## Coordinate contract

- Input geographic coordinates are latitude and longitude in degrees, converted to unit XYZ vectors on a perfect sphere.
- Alternatively, supply unit XYZ vectors directly. The function checks their norms.
- Angular distance is the central angle on the unit sphere, in radians, derived from the dot product.
- This is not an ellipsoidal geodesic calculation. It does not model a reference ellipsoid, geoid, datum epoch or physical distance in metres.
- Longitude is restricted to [-180, 180] degrees; latitude to [-90, 90].
- The dense matrix is intended for small teaching examples.
- The coefficients are non-negative and finite; no coefficient-fitting or Bayesian inference is included.
- This package does not implement vector-valued fields, non-isotropic spherical fields, space-time covariance, or spherical Gaussian-process prediction.

The implementation uses the Legendre three-term recurrence and NumPy only. Its finite-dimensional eigenvalue checks are useful tests, but the validity claim comes from the non-negative Legendre-series construction, not from numerical checks on a handful of site sets.

See the [method lesson](../../../methods/isotropic-covariance-on-the-sphere.md) and [intern walkthrough](implementation-walkthrough.md).
