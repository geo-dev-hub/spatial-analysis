"""Schneider's recursive cubic Bezier fitting algorithm (Graphics Gems, 1990)."""
from __future__ import annotations
from math import hypot, isfinite
from typing import Sequence
Point=tuple[float,float]
Curve=tuple[Point,Point,Point,Point]

def _points(values):
    pts=[(float(p[0]),float(p[1])) for p in values]
    if len(pts)<2 or any(len(p)!=2 for p in values):raise ValueError("at least two 2D points are required")
    if any(not isfinite(x) or not isfinite(y) for x,y in pts):raise ValueError("points must be finite")
    return pts

def _add(a,b):return (a[0]+b[0],a[1]+b[1])
def _sub(a,b):return (a[0]-b[0],a[1]-b[1])
def _scale(a,s):return (a[0]*s,a[1]*s)
def _dot(a,b):return a[0]*b[0]+a[1]*b[1]
def _norm(a):return hypot(a[0],a[1])
def _unit(a,fallback=(1.0,0.0)):
    length=_norm(a)
    return _scale(a,1/length) if length>1e-15 else fallback

def _bezier(c,u):
    v=1-u
    return _add(_add(_scale(c[0],v**3),_scale(c[1],3*v*v*u)),
                _add(_scale(c[2],3*v*u*u),_scale(c[3],u**3)))

def _derivatives(c,u):
    d1=[_scale(_sub(c[i+1],c[i]),3.0) for i in range(3)]
    d2=[_scale(_sub(d1[i+1],d1[i]),2.0) for i in range(2)]
    v=1-u
    q1=_add(_add(_scale(d1[0],v*v),_scale(d1[1],2*v*u)),_scale(d1[2],u*u))
    q2=_add(_scale(d2[0],v),_scale(d2[1],u))
    return q1,q2

def _chord_parameters(points):
    distances=[0.0]
    for a,b in zip(points,points[1:]):distances.append(distances[-1]+_norm(_sub(b,a)))
    total=distances[-1]
    if total<=1e-15:return [i/(len(points)-1) for i in range(len(points))]
    return [d/total for d in distances]

def _generate(points,u,left,right):
    p0,p3=points[0],points[-1]
    c00=c01=c11=x0=x1=0.0
    for p,t in zip(points,u):
        v=1-t
        b0=v*v*v;b1=3*t*v*v;b2=3*t*t*v;b3=t*t*t
        a1=_scale(left,b1);a2=_scale(right,b2)
        tmp=_sub(p,_add(_scale(p0,b0+b1),_scale(p3,b2+b3)))
        c00+=_dot(a1,a1);c01+=_dot(a1,a2);c11+=_dot(a2,a2)
        x0+=_dot(a1,tmp);x1+=_dot(a2,tmp)
    det=c00*c11-c01*c01
    seg=_norm(_sub(p3,p0))
    if abs(det)<=1e-12*max(c00*c11,1.0):
        alpha_l=alpha_r=seg/3.0
    else:
        alpha_l=(x0*c11-x1*c01)/det
        alpha_r=(c00*x1-c01*x0)/det
        eps=1e-6*seg
        if not isfinite(alpha_l) or not isfinite(alpha_r) or alpha_l<eps or alpha_r<eps:
            alpha_l=alpha_r=seg/3.0
    return (p0,_add(p0,_scale(left,alpha_l)),_add(p3,_scale(right,alpha_r)),p3)

def _max_error(points,curve,u):
    best=-1.0;split=1
    for i in range(1,len(points)-1):
        q=_bezier(curve,u[i]);d=_sub(points[i],q);err=_dot(d,d)
        if err>best:best,split=err,i
    return best,split

def _reparameterize(points,curve,u):
    out=[0.0]
    for p,t in zip(points[1:-1],u[1:-1]):
        q=_bezier(curve,t);q1,q2=_derivatives(curve,t);delta=_sub(q,p)
        denominator=_dot(q1,q1)+_dot(delta,q2)
        candidate=t if abs(denominator)<1e-15 else t-_dot(delta,q1)/denominator
        if not isfinite(candidate):return None
        out.append(min(1.0,max(out[-1],candidate)))
    out.append(1.0)
    return out

def _fit(points,left,right,tolerance,max_iterations,depth=0):
    n=len(points)
    if n==2:
        distance=_norm(_sub(points[-1],points[0]))/3.0
        return [(points[0],_add(points[0],_scale(left,distance)),
                 _add(points[-1],_scale(right,distance)),points[-1])]
    if _norm(_sub(points[-1],points[0]))<=1e-15 and max(_norm(_sub(p,points[0])) for p in points)<=1e-15:
        return [(points[0],points[0],points[-1],points[-1])]
    u=_chord_parameters(points)
    curve=_generate(points,u,left,right)
    max_error,split=_max_error(points,curve,u)
    if max_error<=tolerance:return [curve]
    iteration_error=4.0*tolerance
    if max_error<iteration_error:
        for _ in range(max_iterations):
            improved=_reparameterize(points,curve,u)
            if improved is None or any(b<a for a,b in zip(improved,improved[1:])):break
            candidate=_generate(points,improved,left,right)
            new_error,new_split=_max_error(points,candidate,improved)
            if new_error>=max_error-1e-14:break
            u,curve,max_error,split=improved,candidate,new_error,new_split
            if max_error<=tolerance:return [curve]
    split=max(1,min(n-2,split))
    center=_unit(_add(_sub(points[split-1],points[split]),_sub(points[split],points[split+1])),
                   _unit(_sub(points[split-1],points[split+1]),left))
    left_curves=_fit(points[:split+1],left,center,tolerance,max_iterations,depth+1)
    right_curves=_fit(points[split:],_scale(center,-1.0),right,tolerance,max_iterations,depth+1)
    return left_curves+right_curves

def fit_bezier_curves(points:Sequence[Sequence[float]],error_tolerance:float,max_iterations:int=4)->list[Curve]:
    """Fit a piecewise cubic Bezier chain; tolerance is maximum squared error.

    Uses chord-length parameterisation, least-squares tangent handle lengths,
    Newton–Raphson reparameterisation for close fits, and recursive splitting
    at the maximum-error sample. The result is a sequence of 4-control-point
    cubic curves whose adjacent endpoints coincide.
    """
    pts=_points(points)
    if not isfinite(error_tolerance) or error_tolerance<0:raise ValueError("error_tolerance must be finite and non-negative")
    if not isinstance(max_iterations,int) or isinstance(max_iterations,bool) or max_iterations<0:raise ValueError("max_iterations must be a non-negative integer")
    left=next((_unit(_sub(p,pts[0])) for p in pts[1:] if _norm(_sub(p,pts[0]))>1e-15),(1.0,0.0))
    right=next((_unit(_sub(p,pts[-1])) for p in reversed(pts[:-1]) if _norm(_sub(p,pts[-1]))>1e-15),(-left[0],-left[1]))
    return _fit(pts,left,right,float(error_tolerance),max_iterations)
