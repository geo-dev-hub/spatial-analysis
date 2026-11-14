# Nonseparable space-time covariance

A spatiotemporal field is not always well represented by multiplying one spatial covariance by one temporal covariance. A separable model is convenient, but it locks the two dependence structures together. Nonseparable models allow spatial dependence to change with temporal lag.

For observations \(Z(\mathbf{s}_i,t_i)\), every finite covariance matrix

$$
K_{ij}=\operatorname{Cov}\bigl(Z(\mathbf{s}_i,t_i),Z(\mathbf{s}_j,t_j)\bigr)
$$

must be symmetric positive semidefinite. A smooth, positive-looking formula is not enough.

## One Gneiting-class example

For Euclidean spatial lag \(\mathbf{h}\), temporal lag \(u\), and spatial dimension \(d\), define

$$
q(u)=1+\left(\frac{|u|}{a_t}\right)^{2\alpha}.
$$

One Gaussian-spatial member is

$$
C(\mathbf{h},u)
=
\sigma^2 q(u)^{-\beta d/2}
\exp\left(
-\frac{\|\mathbf{h}\|^2}{a_s^2 q(u)^\beta}
\right).
$$

Here \(\sigma^2\) is the marginal variance, \(a_s>0\) is a spatial scale, and \(a_t>0\) is a temporal scale. Use \(0<\alpha\leq1\) and \(0\leq\beta\leq1\) for this parameterisation. Temporal lag changes both covariance amplitude and effective spatial scale. At \(\beta=0\), this parameterisation has no temporal decay.

The companion implementation is restricted to Euclidean coordinates and linear time. Do not substitute great-circle, ellipsoidal, graph or road-network distance and assume the same theorem applies. Stationarity also assumes covariance depends on lags rather than absolute location and time.

## Reproduce

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

The NumPy package builds a dense matrix from coordinate-time observations. Its eigenvalue diagnostic checks one finite matrix; it does not prove validity for all samples or other geometries.

## References

- Cressie, N. and Huang, H.-C. (1999). Classes of Nonseparable, Spatio-Temporal Stationary Covariance Functions. *Journal of the American Statistical Association*, 94(448), 1330–1339. https://doi.org/10.1080/01621459.1999.10473885
- Gneiting, T. (2002). Nonseparable, Stationary Covariance Functions for Space-Time Data. *Journal of the American Statistical Association*, 97(458), 590–600. https://doi.org/10.1198/016214502760047113
