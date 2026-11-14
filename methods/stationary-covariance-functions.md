# Stationary covariance functions: shape, validity and geometry

A covariance model is not just a smooth curve that decreases with distance. It is a rule for constructing covariance matrices that must be mathematically valid for every finite set of locations in the domain where the model is claimed to apply.

This lesson builds the bridge between a distance-based formula and a usable spatial model. It is a Euclidean foundation, not a complete treatment of spherical, network or space–time covariance theory.

## 1. What covariance describes

For a second-order random field \(Z(s)\), the covariance between locations \(s_i\) and \(s_j\) is

\[
C(s_i,s_j)=\operatorname{Cov}\{Z(s_i),Z(s_j)\}.
\]

A stationary isotropic model writes this as a function of separation:

\[
C(s_i,s_j)=C(h_{ij}),\qquad h_{ij}=\lVert s_i-s_j\rVert.
\]

The marginal variance is \(C(0)=\sigma^2\). The corresponding semivariogram is

\[
\gamma(h)=\tfrac12\operatorname{Var}\{Z(s+h)-Z(s)\}
          =C(0)-C(h)
\]

under second-order stationarity. A covariance model and a variogram model are related, but their assumptions should not be silently mixed.

## 2. The validity condition

For any finite set of locations \(s_1,\ldots,s_n\), the matrix

\[
\mathbf C=[C(s_i,s_j)]_{i,j=1}^{n}
\]

must be symmetric positive semidefinite:

\[
\mathbf a^\mathsf T\mathbf C\mathbf a\geq 0
\quad\text{for every }\mathbf a\in\mathbb R^n.
\]

This is the key test. A formula can be positive at every distance and still fail to generate valid covariance matrices. Numerical eigenvalue checks are useful diagnostics for particular point sets; they are not proofs of validity over a whole domain.

## 3. Five Euclidean examples

Let \(r=h/a\), where \(a>0\) is a range or scale parameter.

| Model | Correlation shape | Teaching note |
|---|---|---|
| Exponential | \(e^{-r}\) | Rougher local behaviour than the Gaussian model |
| Gaussian | \(e^{-r^2}\) | Very smooth sample paths |
| Matérn \(\nu=3/2\) | \((1+\sqrt3r)e^{-\sqrt3r}\) | One member of a flexible smoothness family |
| Spherical | \(1-\frac32r+\frac12r^3\) for \(r<1\), else 0 | Compact support; the example is valid in Euclidean dimensions up to 3 |
| Wendland C2 | \((1-r)^4(1+4r)\) for \(r<1\), else 0 | Compact support; dimension is part of the validity contract |

The marginal variance multiplies each correlation shape: \(C(h)=\sigma^2\rho(h)\). The package implements these five models for finite Euclidean coordinates and keeps the dimension restriction explicit for the compact-support examples.

## 4. Why geometry changes the answer

The distance used by the model is part of the mathematical construction. A covariance family known to be valid on the plane does not automatically remain valid when the Euclidean distance is replaced by great-circle distance, network shortest-path distance or graph distance.

A particularly useful warning is the Gaussian-shaped function \(\exp(-\alpha\theta^2)\) with spherical geodesic distance \(\theta\): it is not a generally valid isotropic covariance on the two-sphere for positive \(\alpha\). Spherical covariance models need spherical validity conditions, commonly expressed through nonnegative coefficients in a Legendre-polynomial expansion for isotropic fields on \(S^2\). Network covariance models likewise need constructions designed for the network metric and topology.

Do not confuse these three choices:

1. Euclidean distance in a projected coordinate system;
2. chordal distance between points embedded in three-dimensional space;
3. great-circle distance measured along the sphere.

They encode different geometries and can imply different covariance behaviour.

## 5. Space–time dependence

A separable model has the form

\[
C((s,t),(s',t'))=C_S(s,s')C_T(t,t').
\]

It is convenient, but it forces a particular relationship between spatial and temporal dependence. Nonseparable models allow the spatial covariance structure to change with temporal lag, and vice versa. Gneiting's construction is an influential valid class for stationary space–time covariance models; later work extends this direction to network domains.

A useful modelling question is not simply “which kernel is best?” It is “what dependence structure can the data and scientific process justify?”

## 6. A reproducible matrix check

The companion implementation:

- accepts finite coordinates in a single Euclidean coordinate system;
- constructs pairwise Euclidean distances;
- evaluates one of five explicitly named covariance models;
- builds a dense covariance matrix;
- reports symmetry and the smallest eigenvalue within a caller-selected tolerance.

The code is a teaching baseline. It does not fit covariance parameters, implement anisotropy, estimate a nugget, or claim spherical/network/space–time validity.

## 7. A sensible modelling workflow

1. Define the spatial domain and coordinate geometry.
2. Choose a distance or metric that matches that domain.
3. Select a covariance family whose validity conditions cover that geometry and dimension.
4. State the variance, range, smoothness and nugget conventions.
5. Inspect empirical dependence and fit parameters using a defensible likelihood, restricted likelihood or other justified procedure.
6. Check residual spatial structure and predictive performance using spatially appropriate validation.
7. Report sensitivity to the covariance family and metric.

## 8. References and further reading

- Gneiting, T. (2002). *Nonseparable, stationary covariance functions for space–time data*. Journal of the American Statistical Association, 97(458), 590–600. [DOI: 10.1198/016214502760047113](https://doi.org/10.1198/016214502760047113).
- Gneiting, T. & Schlather, M. (2013). *Space–Time Covariance Models*. Encyclopedia of Environmetrics. [DOI: 10.1002/9780470057339.vas036.pub2](https://doi.org/10.1002/9780470057339.vas036.pub2).
- Gneiting, T. (2013). *Strictly and non-strictly positive definite functions on spheres*. [arXiv:1111.7077](https://arxiv.org/abs/1111.7077).
- *Spherical Process Models for Global Spatial Statistics*. [Open-access review](https://pmc.ncbi.nlm.nih.gov/articles/PMC6457667/).
- *Stationary nonseparable space-time covariance functions on networks*. Journal of the Royal Statistical Society: Series B (2023). [Article](https://academic.oup.com/jrsssb/article/85/5/1417/7263253).

## 9. Limits of this lesson

This is a foundation, not a full covariance catalogue. Spherical harmonics, valid network covariance constructions, cross-covariance for multivariate fields, anisotropy, nonstationarity, low-rank basis expansions, SPDE/GMRF approximations and inference algorithms deserve separate lessons with their own assumptions and tests.
