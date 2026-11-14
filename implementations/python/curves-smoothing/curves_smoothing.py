from __future__ import annotations
from math import isfinite
from typing import Sequence
Point = tuple[float, float]

def _points(values: Sequence[Sequence[float]]) -> list[Point]:
    pts=[]
    for p in values:
        if len(p)!=2: raise ValueError("each point must contain x and y")
        x,y=float(p[0]),float(p[1])
        if not (isfinite(x) and isfinite(y)): raise ValueError("coordinates must be finite")
        pts.append((x,y))
    if len(pts)<2: raise ValueError("at least two points are required")
    return pts

def chaikin(points: Sequence[Sequence[float]], iterations: int=1, *, closed: bool=False) -> list[Point]:
    """Corner-cut a polyline. Open curves retain endpoints; closed rings wrap."""
    pts=_points(points)
    if not isinstance(iterations,int) or iterations<0: raise ValueError("iterations must be a non-negative integer")
    if closed and len(pts)<3: raise ValueError("a closed ring needs at least three vertices")
    for _ in range(iterations):
        out=[]
        if not closed: out.append(pts[0])
        n=len(pts) if closed else len(pts)-1
        for i in range(n):
            p,q=pts[i],pts[(i+1)%len(pts)]
            out.append((0.75*p[0]+0.25*q[0],0.75*p[1]+0.25*q[1]))
            out.append((0.25*p[0]+0.75*q[0],0.25*p[1]+0.75*q[1]))
        if not closed: out.append(pts[-1])
        pts=out
    return pts

def _lerp(a: Point,b: Point,t: float)->Point:
    return (a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t)

def catmull_rom(points: Sequence[Sequence[float]], samples_per_segment: int=16, *, alpha: float=0.5) -> list[Point]:
    """Interpolate an open polyline with a centripetal (alpha=.5) Catmull–Rom spline.

    alpha=0 is uniform, alpha=.5 centripetal, alpha=1 chordal. Endpoints are
    preserved. Consecutive duplicate control points are rejected to avoid
    zero knot intervals and undefined divisions.
    """
    pts=_points(points)
    if not isinstance(samples_per_segment,int) or samples_per_segment<1: raise ValueError("samples_per_segment must be a positive integer")
    if not isfinite(alpha) or alpha<0 or alpha>1: raise ValueError("alpha must be between 0 and 1")
    if any(pts[i]==pts[i+1] for i in range(len(pts)-1)): raise ValueError("consecutive duplicate control points are not supported")
    # Linear endpoint extrapolation avoids inventing repeated endpoint knots.
    ext=[(2*pts[0][0]-pts[1][0],2*pts[0][1]-pts[1][1]),*pts,(2*pts[-1][0]-pts[-2][0],2*pts[-1][1]-pts[-2][1])]
    result=[]
    for seg in range(1,len(ext)-2):
        p0,p1,p2,p3=ext[seg-1:seg+3]
        def advance(a,b):
            return max(((b[0]-a[0])**2+(b[1]-a[1])**2)**(alpha/2),1e-12)
        t0=0.0; t1=t0+advance(p0,p1); t2=t1+advance(p1,p2); t3=t2+advance(p2,p3)
        for k in range(samples_per_segment):
            t=t1+(t2-t1)*k/samples_per_segment
            a1=_lerp(p0,p1,(t-t0)/(t1-t0))
            a2=_lerp(p1,p2,(t-t1)/(t2-t1))
            a3=_lerp(p2,p3,(t-t2)/(t3-t2))
            b1=_lerp(a1,a2,(t-t0)/(t2-t0))
            b2=_lerp(a2,a3,(t-t1)/(t3-t1))
            result.append(_lerp(b1,b2,(t-t1)/(t2-t1)))
    result.append(pts[-1])
    return result

def bezier_curve(control_points: Sequence[Sequence[float]], samples: int=101) -> list[Point]:
    """Evaluate an arbitrary-degree Bezier curve by de Casteljau's algorithm."""
    pts=_points(control_points)
    if not isinstance(samples,int) or samples<2: raise ValueError("samples must be an integer of at least two")
    result=[]
    for step in range(samples):
        t=step/(samples-1); work=pts[:]
        while len(work)>1:
            work=[_lerp(work[i],work[i+1],t) for i in range(len(work)-1)]
        result.append(work[0])
    return result
