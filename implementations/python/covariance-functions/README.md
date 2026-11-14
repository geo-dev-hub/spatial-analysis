# Euclidean covariance functions

This package is a small, tested reference for turning distances between locations into covariance matrices. It is designed to make the modelling contract visible before introducing variogram fitting, Gaussian-process inference or large spatial datasets.

## Included models

- Exponential: \(C(h)=\sigma^2\exp(-h/a)\)
- Gaussian: \(C(h)=\sigma^2\exp[-(h/a)^2]\)
- Matérn with \(\nu=3/2\): \(C(h)=\sigma^2(1+\sqrt{3}h/a)\exp(-\sqrt{3}h/a)\)
- Spherical: compact support at the supplied range, enabled for Euclidean dimensions up to three
- Wendland C2: compact support at the supplied range, enabled for Euclidean dimensions up to three

The scale parameter \(a\) is a model parameter, not a universal distance at which correlation becomes exactly zero. Only the spherical and Wendland examples have exact compact support.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

~~~python
from covariance import covariance_matrix, covariance_matrix_diagnostics

sites = [(0, 0), (1, 0), (0, 1), (1, 1)]
C = covariance_matrix(sites, model="matern32", variance=4, range_scale=2)
print(C)
print(covariance_matrix_diagnostics(C))
~~~

## Coordinate and interpretation contract

- Coordinates are finite Euclidean coordinates in one consistent system.
- All dimensions use the same linear units; anisotropy and coordinate transformations are not applied automatically.
- The matrix is dense and intended for small learning examples.
- Duplicate locations are allowed and produce repeated rows/columns; they may make the matrix singular.
- Eigenvalue diagnostics are a numerical check on a particular matrix, not a proof that a formula is valid for every possible point set.
- A valid covariance matrix must be symmetric positive semidefinite. A negative eigenvalue beyond numerical tolerance is a warning to inspect the model, geometry, units and numerical precision.
- The spherical and Wendland C2 formulas in this package are restricted to Euclidean dimensions no greater than three.
- This package does not implement covariance fitting, anisotropy, measurement-error/nugget estimation, Gaussian-process prediction, spherical covariance models, network covariance models or space-time covariance models.

Read the [canonical method lesson](../../../methods/stationary-covariance-functions.md) and [intern walkthrough](implementation-walkthrough.md).
