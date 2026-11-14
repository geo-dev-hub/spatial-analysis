# Intern walkthrough: graph-spectral covariance

## 1. Why use a graph construction?

Roads, rail systems, utility networks and other connected systems are not ordinary planar surfaces. A covariance model based only on Euclidean separation may connect places that are not connected in the network. Conversely, shortest-path distance alone does not guarantee that an arbitrary decreasing function of that distance is a valid covariance.

This package demonstrates a different route: use the graph Laplacian and build a positive-semidefinite matrix from its eigenvectors.

## 2. Inspect the input contract

The adjacency matrix must be square, finite, symmetric and non-negative, with a zero diagonal. Symmetry means the graph is undirected. The implementation deliberately rejects directed flow networks.

## 3. Install and test

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## 4. Trace the construction

The combinatorial Laplacian is (L=D-A). Its eigendecomposition is (L=Q\Lambda Q^T). For non-negative spectral variances (gamma_k), the covariance is (K=Q\operatorname{diag}(\gamma)Q^T). Each quadratic form is a sum of non-negative squared projections, so the result is positive semidefinite.

## 5. Explore the heat covariance

The heat example uses (gamma_k=\sigma^2 e^{-t\lambda_k}). At (t=0), every spectral variance is equal and the covariance is the identity. Increasing (t) attenuates higher-frequency modes and creates smoother dependence over the graph.

## 6. Interpret the output

The diagonal values are vertex-specific marginal variances and may differ on irregular graphs. Do not describe the result as stationary or isotropic unless additional conditions justify that claim.

## 7. Extend responsibly

1. Compare a path, cycle, star and irregular graph.
2. Inspect eigenvectors and eigenvalues.
3. Change the spectral variance function while keeping it non-negative.
4. Compare combinatorial and normalised Laplacians as distinct modelling choices.
5. Read network covariance literature before adding shortest-path, resistance, directed-flow or space-time constructions.

## 8. Boundaries

The implementation is a dense, scalar, undirected graph model. It is not a general network geostatistics package and does not provide large sparse inference or flow-aware stream covariance.
