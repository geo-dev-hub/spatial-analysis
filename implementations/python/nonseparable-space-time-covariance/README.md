# Nonseparable space-time covariance

A NumPy implementation of one Gneiting-class covariance on Euclidean space crossed with linear time.

For spatial lag \(\mathbf{h}\), temporal lag \(u\), and spatial dimension \(d\), define

$$
q(u)=1+\left(\frac{|u|}{a_t}\right)^{2\alpha},
$$

and

$$
C(\mathbf{h},u)
=
\sigma^2 q(u)^{-\beta d/2}
\exp\left(
-\frac{\|\mathbf{h}\|^2}{a_s^2q(u)^\beta}
\right).
$$

The parameter restrictions are \(0<\alpha\leq1\), \(0\leq\beta\leq1\), and positive spatial and temporal scales. Here \(\sigma^2\) is the marginal variance. The absolute temporal lag ensures symmetry in time.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Contract

- Validity is for this parameterised construction on Euclidean space and linear time.
- Coordinates must share one Euclidean coordinate system and linear units.
- Do not replace Euclidean distance with great-circle, ellipsoidal, graph or road-network distance.
- \(\beta\) controls space-time interaction; \(\beta=0\) removes temporal decay.
- Eigenvalue diagnostics inspect one finite matrix and are not a universal proof.
- Parameter fitting, kriging, nugget estimation and large-scale approximations are out of scope.

Read the method lesson and intern walkthrough before adapting the code.
