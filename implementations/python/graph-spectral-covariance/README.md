# Graph-spectral covariance

This package constructs covariance matrices on a finite **undirected weighted graph** using the graph Laplacian. It provides a valid positive-semidefinite covariance construction, not a universal stationary covariance model based on shortest-path distance.

## Construction

For symmetric non-negative adjacency matrix (A), define the combinatorial Laplacian

\[
L=D-A=Q\Lambda Q^\mathsf T.
\]

Given non-negative spectral variances (gamma_k), define

\[
K=Q\operatorname{diag}(\gamma_k)Q^\mathsf T.
\]

For every vector (x), (x^\mathsf T Kx=\sum_k\gamma_k(q_k^\mathsf T x)^2\geq0). Thus the matrix is positive semidefinite by construction.

The heat-kernel example chooses (gamma_k=\sigma^2\exp(-t\lambda_k)), where (t\geq0) and (lambda_k) are Laplacian eigenvalues.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

~~~python
import numpy as np
from graph_covariance import graph_heat_covariance

A = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=float)
K = graph_heat_covariance(A, diffusion_time=0.8)
print(K)
~~~

## Interpretation and limits

- The graph must be finite, undirected, with symmetric non-negative edge weights.
- This package uses the combinatorial Laplacian and rejects self-loops.
- The heat covariance is positive semidefinite, but its diagonal can vary across vertices on an irregular graph.
- The model is generally not isotropic or stationary over graph vertices.
- Spectral modes are tied to the graph topology and its Laplacian eigenvectors.
- This is not a directed flow-network model, a tail-up/tail-down stream covariance, or a generalised-network construction based on geodesic or resistance metrics.
- The dense eigendecomposition is intended for small teaching examples, not large sparse graphs.
- Numerical eigenvalue checks are diagnostics; the non-negative spectral variances provide the construction guarantee.

Read the [method lesson](../../../methods/graph-spectral-covariance.md) and [intern walkthrough](implementation-walkthrough.md).
