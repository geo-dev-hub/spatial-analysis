# Discrete biharmonic minimum-curvature gridding: walkthrough

## 1. Objective

For a regular grid z(i,j), approximate curvature with the five-point Laplacian:

\[
L_{ij}(z)=\frac{z_{i,j-1}-2z_{ij}+z_{i,j+1}}{\Delta x^2}
+\frac{z_{i-1,j}-2z_{ij}+z_{i+1,j}}{\Delta y^2}.
\]

The teaching solver minimizes the discrete bending objective

\[
J(z)=\sum_{i=1}^{n_y-2}\sum_{j=1}^{n_x-2} L_{ij}(z)^2
\]

subject to fixed observed grid nodes. The normal equations correspond to a discrete biharmonic system away from the fixed observations.

## 2. Boundary and data contract

- Input is a regular Cartesian grid.
- Finite values are fixed observations; NaN values are unknown.
- Every perimeter node must be supplied as a finite fixed value.
- dx and dy are positive and use the same coordinate units.
- Unknown interior nodes are solved simultaneously by least squares.

The fixed perimeter is a deliberate Dirichlet boundary contract. It differs from the zero-curvature edge conditions and scattered-point handling of the full Briggs algorithm.

## 3. What this is not

This is a small-grid discrete biharmonic teaching solver, not a reproduction of Briggs (1974) or the USGS MINC program. It does not bin scattered observations, interpolate data to grid nodes, build coarse regional grids, use multilevel blocks, or iterate the original scattered-data difference equations. Dense least squares is intended for small teaching grids, not large surveys.

## References

- Briggs, I. C. (1974). Machine contouring using minimum curvature. Geophysics, 39(1), 39–48. https://doi.org/10.1190/1.1440410
- Webring, M. (1981). MINC; a gridding program based on minimum curvature. U.S. Geological Survey Open-File Report 81-1224. https://doi.org/10.3133/ofr811224
