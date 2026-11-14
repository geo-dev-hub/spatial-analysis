# Exercise: build a valid spherical covariance

**Start with:** [Isotropic covariance on the two-sphere](../methods/isotropic-covariance-on-the-sphere.md), the [implementation](../implementations/python/spherical-covariance/README.md) and its [lab](../notebooks/spherical-covariance-lab.ipynb).

## 1. Convert coordinates

Convert the equator, both poles and two arbitrary locations to unit vectors. Verify that every vector has norm one.

## 2. Work with angular distance

Calculate the central angle between two unit vectors using the dot product. Compare the result for identical, orthogonal and antipodal points.

## 3. Inspect spectral weights

Use three different non-negative coefficient sequences. Plot their covariance functions from zero to (pi). Explain how shifting weight toward higher degrees changes the angular structure.

## 4. Check matrix validity

Build a covariance matrix for at least eight global locations. Inspect symmetry, diagonal variance and the smallest eigenvalue. Explain why the theorem, rather than the numerical test, supplies the general validity guarantee.

## 5. Challenge a tempting shortcut

Compare the valid Legendre-series construction with a Euclidean Gaussian expression evaluated at angular distance. Search for a point set that reveals the difference. Do not claim that one successful finite matrix proves universal validity.

## 6. Extend carefully

Propose a method for estimating a finite set of non-negative coefficients from observations. State the likelihood, constraints, regularisation and validation scheme before implementing it.

**Submission:** a short mathematical explanation, a reproducible notebook, tests and a source note.
