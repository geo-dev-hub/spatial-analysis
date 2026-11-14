# Intern walkthrough: interpolation and ordinary kriging

## Objective

Build two estimators that answer the same practical question—what value might be found at an unsampled location?—while making their assumptions visibly different.

## 1. Begin with observations, not a surface

Each input sample is an `(x, y, value)` triple. Coordinates must share one projected CRS and unit. A degree of longitude is not a constant ground distance, so this example does not accept geographic coordinates as if they were metres.

We reject duplicate sample coordinates because they need a declared policy: aggregate them, model measurement error, or retain them in a model that explicitly supports replicates. Silently keeping one value would hide a data decision.

## 2. Build inverse-distance weights

For target location $s_0$, sample locations $s_i$ and power $p>0$:

$$
\hat z(s_0)=\frac{\sum_i d(s_0,s_i)^{-p}z(s_i)}
{\sum_i d(s_0,s_i)^{-p}}
$$

The implementation calculates Euclidean distance, optionally filters by a search radius, sorts candidates deterministically and can keep only the nearest $k$. If the target is exactly at an observation, it returns that observation rather than dividing by zero. If no sample remains inside a requested radius, it returns `None`.

IDW is a local weighted average. It has no stochastic spatial model and does not produce a kriging variance.

## 3. Estimate an empirical semivariogram\n\nFor every unique sample pair, calculate separation distance $h_{ij}$ and half the squared value difference. Group pairs into caller-defined lag bins:\n\n$\n\\hat\\gamma(h)=\\frac{1}{2N(h)}\\sum_{(i,j)\\in B(h)}(z_i-z_j)^2\n$\n\nThe implementation reports the mean pair distance, semivariance and number of pairs in each bin. Empty bins are retained rather than silently disappearing. Sparse bins are uncertain, and this isotropic summary can hide directional structure. It is a diagnostic, not a model fit.\n\n## 4. State the variogram before solving kriging

Ordinary kriging assumes an unknown constant mean and a specified covariance or semivariogram model. This teaching implementation uses an isotropic exponential semivariogram with zero nugget:

$$
\gamma(h)=c(1-e^{-h/a}), \quad \gamma(0)=0
$$

The partial sill $c$ controls the asymptotic semivariance and $a$ is the distance scale. They are inputs, not estimated from these observations. Fitting a variogram is a separate statistical task and must be justified by the empirical variogram, sampling geometry and domain knowledge.

## 5. Assemble the ordinary-kriging system

For $n$ observations, the augmented semivariogram system is:

$$
\begin{bmatrix}
\Gamma & \mathbf 1 \\
\mathbf 1^T & 0
\end{bmatrix}
\begin{bmatrix}
\boldsymbol\lambda \\
\mu
\end{bmatrix}
=
\begin{bmatrix}
\boldsymbol\gamma_0 \\
1
\end{bmatrix}
$$

Here $\Gamma_{ij}=\gamma(\lVert s_i-s_j\rVert)$ and $\gamma_{0,i}=\gamma(\lVert s_i-s_0\rVert)$. The final row enforces $\sum_i\lambda_i=1$, which makes the estimator unbiased for an unknown constant mean.

The estimate is $\hat z(s_0)=\sum_i\lambda_i z(s_i)$. Under this semivariogram convention, the kriging variance is $\sigma_K^2=\boldsymbol\lambda^T\boldsymbol\gamma_0+\mu$. The code solves the dense linear system directly and raises a clear error if it is singular.

## 6. Read the variance carefully

The variance describes uncertainty implied by the chosen model and sample geometry. It is not an empirical accuracy score, and it does not include uncertainty from selecting or fitting the variogram parameters. Evaluate predictions with spatially appropriate holdouts; random point splits can be over-optimistic when nearby observations leak information across train and test sets.

## 7. Verify with tests

The tests cover exact sample reproduction, symmetric IDW weights, power effects, search-radius behaviour, duplicate coordinates, empirical variogram pair counts and empty bins, semivariogram shape, non-negative kriging variance, a sample-location query and invalid model parameters. They are small numerical fixtures, not a substitute for cross-validation against real data.
