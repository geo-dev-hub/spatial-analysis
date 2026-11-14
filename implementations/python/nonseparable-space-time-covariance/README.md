# Nonseparable space-time covariance

A NumPy implementation of one valid Gneiting-class covariance on Euclidean space crossed with linear time.

For spatial lag h, temporal lag u and spatial dimension d, define q = 1 + (u / temporal_scale)^(2 alpha). The covariance is variance times q^(-beta*d/2) times exp(-((h/spatial_scale)^2)/q^beta). The parameter restrictions are 0 < alpha <= 1 and 0 <= beta <= 1, with positive spatial and temporal scales.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Contract

- Validity is for this parameterised construction on Euclidean space and linear time.
- Coordinates must share one Euclidean coordinate system and linear units.
- Do not replace Euclidean distance with great-circle, ellipsoidal, graph or road-network distance.
- Beta controls space-time interaction; beta=0 removes temporal decay.
- Eigenvalue diagnostics inspect one finite matrix and are not a universal proof.
- Parameter fitting, kriging, nugget estimation and large-scale approximations are out of scope.

Read the method lesson and intern walkthrough before adapting the code.
