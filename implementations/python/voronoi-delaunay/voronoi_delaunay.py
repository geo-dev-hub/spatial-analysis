"""Library-backed 2D Voronoi and Delaunay construction using SciPy/Qhull."""
from __future__ import annotations
from collections.abc import Sequence
from dataclasses import dataclass
import numpy as np
from scipy.spatial import Delaunay, Voronoi


@dataclass(frozen=True)
class TessellationResult:
    """The validated site coordinates and their SciPy tessellations."""
    points: np.ndarray
    voronoi: Voronoi
    delaunay: Delaunay


def build_tessellations(points: Sequence[Sequence[float]]) -> TessellationResult:
    """Build planar Voronoi and Delaunay structures for unique 2D sites.

    This validates the input contract and delegates construction to Qhull
    through SciPy. QhullError is allowed to propagate for numerical or
    combinatorial degeneracies that Qhull cannot resolve under its defaults.
    """
    coordinates = np.asarray(points, dtype=float)
    if coordinates.ndim != 2 or coordinates.shape[1] != 2:
        raise ValueError("points must be an n-by-2 coordinate array")
    if len(coordinates) < 3:
        raise ValueError("at least three points are required")
    if not np.isfinite(coordinates).all():
        raise ValueError("coordinates must be finite")
    if len(np.unique(coordinates, axis=0)) != len(coordinates):
        raise ValueError("duplicate site coordinates are not allowed")
    if np.linalg.matrix_rank(coordinates - coordinates[0]) < 2:
        raise ValueError("sites must not all be collinear")

    voronoi = Voronoi(coordinates)
    delaunay = Delaunay(coordinates)
    coordinates.setflags(write=False)
    return TessellationResult(coordinates, voronoi, delaunay)
