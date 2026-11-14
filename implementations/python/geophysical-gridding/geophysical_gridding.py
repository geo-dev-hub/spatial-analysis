"""Scattered point gridding: nearest neighbour and Delaunay linear interpolation."""
from __future__ import annotations
import numpy as np
from scipy.spatial import cKDTree,Delaunay,QhullError

def _samples(points,values):
    p=np.asarray(points,dtype=float);v=np.asarray(values,dtype=float)
    if p.ndim!=2 or p.shape[1]!=2 or len(p)<1:raise ValueError("points must have shape (n,2)")
    if v.ndim!=1 or len(v)!=len(p):raise ValueError("values must have one scalar per point")
    if not np.all(np.isfinite(p)) or not np.all(np.isfinite(v)):raise ValueError("sample coordinates and values must be finite")
    if len(np.unique(p,axis=0))!=len(p):raise ValueError("duplicate sample coordinates are not supported")
    return p,v

def _grid(x_coordinates,y_coordinates):
    x=np.asarray(x_coordinates,dtype=float);y=np.asarray(y_coordinates,dtype=float)
    if x.ndim!=1 or y.ndim!=1 or len(x)<1 or len(y)<1:raise ValueError("grid coordinates must be non-empty 1D arrays")
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):raise ValueError("grid coordinates must be finite")
    xx,yy=np.meshgrid(x,y)
    return np.column_stack((xx.ravel(),yy.ravel())),xx.shape

def nearest_neighbor_grid(points,values,x_coordinates,y_coordinates,max_distance=None):
    """Assign each grid node the value at its nearest sample point."""
    p,v=_samples(points,values);q,shape=_grid(x_coordinates,y_coordinates)
    if max_distance is not None and (not np.isfinite(max_distance) or max_distance<0):raise ValueError("max_distance must be finite and non-negative")
    distance,index=cKDTree(p).query(q,k=1)
    out=v[index].astype(float)
    if max_distance is not None:out[distance>max_distance]=np.nan
    return out.reshape(shape)

def triangulation_grid(points,values,x_coordinates,y_coordinates,fill_value=np.nan):
    """Piecewise-linear interpolation over a Delaunay triangulation.

    Grid nodes outside the convex hull receive fill_value. Interpolation is
    barycentric within each simplex and exactly reproduces affine planes.
    """
    p,v=_samples(points,values)
    if len(p)<3:raise ValueError("triangulation needs at least three non-collinear samples")
    q,shape=_grid(x_coordinates,y_coordinates)
    try:tri=Delaunay(p)
    except QhullError as exc:raise ValueError("sample points must span a non-degenerate 2D triangulation") from exc
    simplex=tri.find_simplex(q);out=np.full(len(q),float(fill_value),dtype=float)
    inside=simplex>=0
    if np.any(inside):
        s=simplex[inside];delta=q[inside]-tri.transform[s,2]
        first=np.einsum("nij,nj->ni",tri.transform[s,:2],delta)
        weights=np.column_stack((first,1-first.sum(axis=1)))
        out[inside]=np.einsum("ni,ni->n",v[tri.simplices[s]],weights)
    return out.reshape(shape)


def thin_plate_spline_grid(points, values, x_coordinates, y_coordinates, smoothing=0.0):
    """Grid scattered data with a 2D thin-plate-spline radial basis function.

    The kernel r**2 * log(r) with an affine polynomial tail gives the
    minimum-bending-energy thin-plate spline interpolant when smoothing=0.
    Positive smoothing trades exact sample fit for a smoother least-squares
    surface. This is a thin-plate-spline minimum-curvature-style method; it
    should not be confused with the classic Briggs iterative gridding scheme.
    """
    from scipy.interpolate import RBFInterpolator

    p, v = _samples(points, values)
    if len(p) < 3:
        raise ValueError("thin-plate spline needs at least three non-collinear samples")
    design = np.column_stack((np.ones(len(p)), p))
    if np.linalg.matrix_rank(design) < 3:
        raise ValueError("thin-plate spline samples must span a non-degenerate 2D domain")
    smoothing = float(smoothing)
    if not np.isfinite(smoothing) or smoothing < 0:
        raise ValueError("smoothing must be finite and non-negative")
    q, shape = _grid(x_coordinates, y_coordinates)
    try:
        interpolator = RBFInterpolator(
            p, v, kernel="thin_plate_spline", degree=1, smoothing=smoothing
        )
        result = interpolator(q)
    except (ValueError, np.linalg.LinAlgError) as exc:
        raise ValueError("thin-plate spline system could not be solved for these samples") from exc
    return np.asarray(result, dtype=float).reshape(shape)
