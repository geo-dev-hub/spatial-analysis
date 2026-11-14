# Exercise: covariance on a graph

**Start with:** [Graph-spectral covariance](../methods/graph-spectral-covariance.md), the [implementation](../implementations/python/graph-spectral-covariance/README.md) and the [visual lab](../notebooks/graph-spectral-covariance-lab.ipynb).

## 1. Build small graphs

Create a path, cycle, star and irregular weighted graph. Compare their adjacency matrices and combinatorial Laplacians.

## 2. Inspect graph modes

Compute the Laplacian eigenvalues and eigenvectors. Explain why the constant vector is a zero-eigenvalue mode for each connected graph.

## 3. Construct covariance matrices

Use non-negative spectral variances to build covariance matrices. Verify symmetry, inspect marginal variances and check the smallest eigenvalue.

## 4. Explore heat smoothing

Compare diffusion times 0, 0.2, 1 and 3. Describe how the covariance changes and why the marginal variances can differ on an irregular graph.

## 5. Challenge the assumptions

Explain why this model is not a directed stream-flow covariance, and why a generic decreasing function of shortest-path distance is not automatically a valid covariance.

## 6. Extend

Compare the combinatorial and normalised Laplacian. State the spectral construction and how its interpretation changes before writing code.

**Submission:** graph definitions, a notebook or script, tests and a short modelling note.
