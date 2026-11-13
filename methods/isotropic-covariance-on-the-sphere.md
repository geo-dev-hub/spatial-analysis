# Isotropic covariance on the two-sphere

A spherical covariance model must respect the geometry of the sphere. A covariance function that is valid in Euclidean space may become invalid when its distance argument is replaced by great-circle distance. This lesson builds a valid model directly from the spherical spectral representation.

## 1. The domain and distance

Represent a location on the unit sphere by a unit vector (uinmathbb R^3). For two locations (u) and (v), the central angle is

\[
\theta(u,v)=\arccos(u^\mathsf T v),\qquad 0\leq\theta\leq\pi.
\]

This angle is dimensionless and measured in radians. Multiplying by a chosen sphere radius gives spherical surface distance; it does not turn the model into an ellipsoidal geodesic.

## 2. The validity construction

For an isotropic scalar covariance on (S^2), Schoenberg's characterization gives a Legendre expansion with non-negative coefficients:

\[
C(\theta)=\sum_{\ell=0}^{\infty} b_\ell P_\ell(\cos\theta),
\qquad b_\ell\geq0,\quad \sum_{\ell=0}^{\infty}b_\ell<\infty.
\]

(P_\ell) is the Legendre polynomial of degree (ell). The summability condition gives a finite variance, and (C(0)=\sum b_\ell). The companion package uses a finite truncation, which preserves the non-negative coefficient construction.

A normalised correlation is obtained by dividing all coefficients by their sum, giving unit variance.

## 3. Why this is not a generic distance kernel

A common mistake is to take a planar Gaussian covariance and substitute the great-circle angle:

\[
C(\theta)=\exp(-\alpha\theta^2).
\]

This is not a generally valid isotropic covariance on (S^2) for positive (alpha). The issue is not whether the curve is positive or decreases smoothly; it is whether every finite covariance matrix generated on the sphere is positive semidefinite.

## 4. From geographic coordinates to a matrix

Latitude (phi) and longitude (lambda), in radians, map to a unit vector:

\[
u=(\cos\phi\cos\lambda,\;\cos\phi\sin\lambda,\;\sin\phi).
\]

For a set of locations, form the dot-product matrix (U U^\mathsf T), clip numerical values to [-1, 1], and apply arccos elementwise. The covariance evaluator then applies the Legendre series to each angular separation.

The package implements this workflow with NumPy and includes an explicit unit-vector input route. It does not perform ellipsoidal geodesy.

## 5. The finite series implementation

The Legendre polynomials are evaluated with the three-term recurrence:

\[
P_0(x)=1,\qquad P_1(x)=x,
\]

\[
P_\ell(x)=\frac{(2\ell-1)xP_{\ell-1}(x)-(\ell-1)P_{\ell-2}(x)}{\ell}.
\]

This avoids a dependency on a special-functions library. The dense matrix is suitable for small teaching examples, not global-scale inference.

## 6. What the tests can and cannot establish

The tests check coordinate conversion, domain validation, diagonal variance, symmetry and eigenvalue behaviour for selected site sets. These are software checks. They do not prove the theorem. The validity claim follows from the non-negative Legendre coefficients and the spherical representation.

## 7. Where to go next

- Add coefficient estimation under a stated likelihood and a defensible regularisation scheme.
- Explore spherical harmonics and spectral truncation choices.
- Compare scalar and vector-valued spherical random fields.
- Study nonstationary and space-time spherical models.
- Keep ellipsoidal geodesics separate from perfect-sphere covariance theory.

## References

- *Spherical Process Models for Global Spatial Statistics*. Open-access review, including Schoenberg's Legendre characterization and examples of invalid Euclidean kernels under geodesic distance: [PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC6457667/).
- Schoenberg, I. J. (1942). Positive definite functions on spheres. *Duke Mathematical Journal*, 9, 96–108.
- Gneiting, T. (2013). Strictly and non-strictly positive definite functions on spheres. [arXiv:1111.7077](https://arxiv.org/abs/1111.7077).
