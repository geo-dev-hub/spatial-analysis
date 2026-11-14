# Graph-spectral covariance: a valid construction on an undirected network

A network is not simply a set of points with a distance matrix. Its topology determines which locations are connected, and the validity of a covariance model depends on how that topology enters the construction.

This lesson introduces a graph-spectral covariance baseline. It is intentionally distinct from stationary covariance models built directly from shortest-path or resistance metrics.

## 1. The graph and its Laplacian

Let (A) be a symmetric, non-negative weighted adjacency matrix for a finite undirected graph. Let (D) be the diagonal matrix of weighted vertex degrees. The combinatorial graph Laplacian is

\[
L=D-A.
\]

It is symmetric and positive semidefinite. Its eigendecomposition is

\[
L=Q\Lambda Q^\mathsf T,
\]

where the columns of (Q) are orthonormal graph spectral modes and (Lambda) contains non-negative eigenvalues.

## 2. Constructing a covariance matrix

Choose a non-negative variance for each graph spectral mode:

\[
\gamma_k\geq0.
\]

Then define

\[
K=Q\operatorname{diag}(\gamma_1,\ldots,\gamma_n)Q^\mathsf T.
\]

For any vector (x),

\[
x^\mathsf T Kx
=\sum_{k=1}^{n}\gamma_k(q_k^\mathsf T x)^2\geq0.
\]

So (K) is positive semidefinite by construction. This is a valid finite-dimensional covariance matrix for graph-indexed random variables.

## 3. Heat-kernel spectral variances

One useful choice is

\[
\gamma_k=\sigma^2\exp(-t\lambda_k),\qquad t\geq0.
\]

At (t=0), all spectral variances are equal and the covariance is (sigma^2 I). As (t) increases, modes with larger Laplacian eigenvalues are attenuated more strongly. This creates a graph-smoothing structure.

The diagonal entries of (K) need not be equal on an irregular graph. The construction is positive semidefinite, but it is not automatically stationary or isotropic over vertices.

## 4. What this model is not

Do not confuse graph-spectral covariance with:

- a stationary covariance that is an arbitrary function of shortest-path distance;
- a resistance-distance covariance;
- a flow-aware stream-network model with tail-up or tail-down dependence;
- a covariance model on a generalised network with Euclidean edges;
- a directed road-network model;
- a nonseparable space-time network covariance.

These are different model families with different validity arguments. Recent work on generalised networks constructs stationary nonseparable space-time covariance classes using specific network metrics; it does not imply that any function of any graph distance is valid.

## 5. Implementation contract

The companion NumPy package:

- accepts a symmetric non-negative adjacency matrix with no self-loops;
- constructs the combinatorial Laplacian;
- computes its dense eigendecomposition;
- accepts non-negative spectral variances or uses the heat-kernel choice;
- returns a dense positive-semidefinite covariance matrix;
- provides numerical diagnostics for selected finite examples.

The package is deliberately small and transparent. Large graphs require sparse eigensolvers, low-rank approximations or other computational strategies.

## 6. A modelling workflow

1. Decide whether the domain is an undirected graph, a directed flow network, a linear network or a graph with Euclidean edges.
2. Define the graph topology and edge weights.
3. Choose the Laplacian and state its normalisation.
4. Select and justify a non-negative spectral variance function.
5. Inspect the resulting marginal variances and covariance structure.
6. Validate predictions using graph-aware holdouts and compare against meaningful baselines.
7. Keep the model's stationarity and isotropy claims no stronger than the construction supports.

## 7. References

- Porcu, E., White, P. A., & Genton, M. G. (2023). *Stationary nonseparable space-time covariance functions on networks*. Journal of the Royal Statistical Society: Series B, 85(5), 1417–1440. [DOI: 10.1093/jrsssb/qkad082](https://doi.org/10.1093/jrsssb/qkad082).
- Jeong, J., Jun, M., & Genton, M. G. (2017). *Spherical Process Models for Global Spatial Statistics*. Statistical Science, 32(4), 501–513. [Open access](https://pmc.ncbi.nlm.nih.gov/articles/PMC6457667/).

## 8. Limits and next steps

The graph-spectral construction is a finite graph covariance baseline. Network metric models, directed flow models, resistance metrics, space-time dependence, sparse computation and inference deserve separate lessons and implementations.
