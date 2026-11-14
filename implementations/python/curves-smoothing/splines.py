"""B-spline and NURBS evaluation using the de Boor algorithm."""
from __future__ import annotations
from math import isfinite
from typing import Sequence
Point=tuple[float,float]

def _validate(control_points,degree,knots):
    if not isinstance(degree,int) or isinstance(degree,bool) or degree<0:raise ValueError("degree must be a non-negative integer")
    pts=[]
    for p in control_points:
        if len(p)!=2:raise ValueError("control points must be 2D")
        q=(float(p[0]),float(p[1]))
        if not all(isfinite(x) for x in q):raise ValueError("control points must be finite")
        pts.append(q)
    if len(pts)<degree+1:raise ValueError("need at least degree+1 control points")
    u=[float(x) for x in knots]
    if len(u)!=len(pts)+degree+1:raise ValueError("knot vector length must equal control_count + degree + 1")
    if any(not isfinite(x) for x in u) or any(a>b for a,b in zip(u,u[1:])):raise ValueError("knots must be finite and nondecreasing")
    n=len(pts)-1
    if u[degree]>=u[n+1]:raise ValueError("spline parameter domain must have positive length")
    return pts,u

def _span(n,degree,knots,u):
    if u>=knots[n+1]:return n
    low,high=degree,n+1
    mid=(low+high)//2
    while u<knots[mid] or u>=knots[mid+1]:
        if u<knots[mid]:high=mid
        else:low=mid
        mid=(low+high)//2
    return mid

def _de_boor(coords,degree,knots,u):
    n=len(coords)-1;k=_span(n,degree,knots,u)
    d=[list(coords[j+k-degree]) for j in range(degree+1)]
    for r in range(1,degree+1):
        for j in range(degree,r-1,-1):
            i=k-degree+j
            den=knots[i+degree-r+1]-knots[i]
            alpha=0.0 if den==0 else (u-knots[i])/den
            d[j]=[(1-alpha)*d[j-1][axis]+alpha*d[j][axis] for axis in range(len(d[j]))]
    return tuple(d[degree])

def bspline_point(control_points:Sequence[Sequence[float]],degree:int,knots:Sequence[float],u:float)->Point:
    """Evaluate a non-rational B-spline at u using de Boor."""
    pts,knot=_validate(control_points,degree,knots)
    u=float(u)
    if not isfinite(u) or u<knot[degree] or u>knot[len(pts)]:raise ValueError("u is outside the closed spline domain")
    return _de_boor(pts,degree,knot,u)

def nurbs_point(control_points:Sequence[Sequence[float]],weights:Sequence[float],degree:int,knots:Sequence[float],u:float)->Point:
    """Evaluate a planar NURBS curve via homogeneous de Boor evaluation."""
    pts,knot=_validate(control_points,degree,knots)
    w=[float(x) for x in weights]
    if len(w)!=len(pts) or any(not isfinite(x) or x==0 for x in w):raise ValueError("weights must be finite, non-zero and match control points")
    u=float(u)
    if not isfinite(u) or u<knot[degree] or u>knot[len(pts)]:raise ValueError("u is outside the closed spline domain")
    h=[(p[0]*weight,p[1]*weight,weight) for p,weight in zip(pts,w)]
    x,y,z=_de_boor(h,degree,knot,u)
    if abs(z)<1e-15:raise ValueError("rational denominator is numerically zero")
    return x/z,y/z

def bspline_curve(control_points,degree,knots,samples=101):
    pts,knot=_validate(control_points,degree,knots)
    if not isinstance(samples,int) or isinstance(samples,bool) or samples<2:raise ValueError("samples must be an integer >= 2")
    lo,hi=knot[degree],knot[len(pts)]
    return [bspline_point(pts,degree,knot,lo+(hi-lo)*i/(samples-1)) for i in range(samples)]

def nurbs_curve(control_points,weights,degree,knots,samples=101):
    pts,knot=_validate(control_points,degree,knots)
    if not isinstance(samples,int) or isinstance(samples,bool) or samples<2:raise ValueError("samples must be an integer >= 2")
    lo,hi=knot[degree],knot[len(pts)]
    return [nurbs_point(pts,weights,degree,knot,lo+(hi-lo)*i/(samples-1)) for i in range(samples)]
