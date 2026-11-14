"""Small-grid discrete biharmonic interpolation with fixed boundary values."""
from __future__ import annotations
import numpy as np


def discrete_biharmonic_grid(values, *, dx=1.0, dy=1.0):
    """Fill NaN interior grid nodes by minimizing squared discrete curvature.

    Finite input values are fixed observations. Every perimeter node must be
    finite and is treated as a Dirichlet boundary condition. The objective is
    the sum of squared five-point Laplacians over all interior grid nodes:

        sum_ij (d2z/dx2 + d2z/dy2)**2

    Unknown nodes are solved simultaneously by least squares. This is a
    transparent small-grid discrete minimum-curvature baseline; it is not the
    full Briggs scattered-data algorithm, which includes scattered-point
    constraints, initialization, regional grids and iterative block solving.
    """
    grid = np.asarray(values, dtype=float)
    if grid.ndim != 2 or min(grid.shape) < 3:
        raise ValueError("values must be a 2D grid at least 3 by 3")
    if np.any(np.isinf(grid)):
        raise ValueError("values may contain finite observations or NaN unknowns, not infinity")
    spacing = np.asarray([dx, dy], dtype=float)
    if not np.all(np.isfinite(spacing)) or np.any(spacing <= 0):
        raise ValueError("dx and dy must be finite and positive")
    known = np.isfinite(grid)
    if not (np.all(known[0, :]) and np.all(known[-1, :]) and
            np.all(known[:, 0]) and np.all(known[:, -1])):
        raise ValueError("all perimeter nodes must be finite fixed boundary values")

    free_indices = np.flatnonzero(~known)
    if free_indices.size == 0:
        return grid.copy()
    known_indices = np.flatnonzero(known)
    nrows, ncols = grid.shape
    n_equations = (nrows - 2) * (ncols - 2)
    laplacian = np.zeros((n_equations, nrows * ncols), dtype=float)
    wx, wy = 1.0 / float(dx) ** 2, 1.0 / float(dy) ** 2
    row = 0
    for i in range(1, nrows - 1):
        for j in range(1, ncols - 1):
            center = i * ncols + j
            laplacian[row, center] = -2.0 * wx - 2.0 * wy
            laplacian[row, center - 1] = wx
            laplacian[row, center + 1] = wx
            laplacian[row, center - ncols] = wy
            laplacian[row, center + ncols] = wy
            row += 1

    flat = grid.ravel()
    system = laplacian[:, free_indices]
    rhs = -(laplacian[:, known_indices] @ flat[known_indices])
    solution, _, rank, _ = np.linalg.lstsq(system, rhs, rcond=None)
    if rank < free_indices.size:
        raise ValueError("fixed observations do not uniquely constrain all unknown grid nodes")
    result = grid.copy().ravel()
    result[free_indices] = solution
    return result.reshape(grid.shape)
