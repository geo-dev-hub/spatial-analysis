"""Additional teaching implementations for open-polyline simplification."""
from __future__ import annotations
from heapq import heappop, heappush
from math import hypot, isfinite
from typing import Sequence
Point = tuple[float, float]
def _points(values):
    if any(len(p)!=2 for p in values): raise ValueError("Each point must contain two coordinates")
    result=[(float(p[0]),float(p[1])) for p in values]
    if any(not isfinite(x) or not isfinite(y) for x,y in result): raise ValueError("Coordinates must be finite")
    return result
def _distance_to_segment(p,a,b):
    dx,dy=b[0]-a[0],b[1]-a[1]; q=dx*dx+dy*dy
    if q==0:return hypot(p[0]-a[0],p[1]-a[1])
    t=min(1.0,max(0.0,((p[0]-a[0])*dx+(p[1]-a[1])*dy)/q))
    return hypot(p[0]-a[0]-t*dx,p[1]-a[1]-t*dy)
def _distance_to_line(p,a,b):
    dx,dy=b[0]-a[0],b[1]-a[1]; length=hypot(dx,dy)
    if length==0:return hypot(p[0]-a[0],p[1]-a[1])
    return abs(dx*(a[1]-p[1])-(a[0]-p[0])*dy)/length
def douglas_peucker(points,tolerance):
    pts=_points(points)
    if not isfinite(tolerance) or tolerance<0:raise ValueError("tolerance must be finite and non-negative")
    if len(pts)<=2:return pts[:]
    keep={0,len(pts)-1}; stack=[(0,len(pts)-1)]
    while stack:
        a,b=stack.pop(); best=-1.0; index=None
        for i in range(a+1,b):
            d=_distance_to_segment(pts[i],pts[a],pts[b])
            if d>best:best,index=d,i
        if index is not None and best>tolerance:keep.add(index);stack.extend(((a,index),(index,b)))
    return [pts[i] for i in sorted(keep)]
def _area(a,b,c):
    return abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))/2
def visvalingam_whyatt(points,area_threshold):
    pts=_points(points)
    if not isfinite(area_threshold) or area_threshold<0:raise ValueError("area_threshold must be finite and non-negative")
    n=len(pts)
    if n<=2:return pts[:]
    prev=[i-1 for i in range(n)];nxt=[i+1 for i in range(n)];nxt[-1]=-1
    alive=[True]*n;version=[0]*n;heap=[]
    def push(i,floor):
        if i<=0 or i>=n-1 or not alive[i]:return
        version[i]+=1;heappush(heap,(max(floor,_area(pts[prev[i]],pts[i],pts[nxt[i]])),i,version[i]))
    for i in range(1,n-1):push(i,0.0)
    floor=0.0
    while heap:
        area,i,v=heappop(heap)
        if not alive[i] or version[i]!=v:continue
        if area>area_threshold:break
        floor=max(floor,area);alive[i]=False;left,right=prev[i],nxt[i];nxt[left]=right;prev[right]=left
        push(left,floor);push(right,floor)
    return [p for i,p in enumerate(pts) if alive[i]]
def reumann_witkam(points,tolerance):
    """Moving infinite-strip variant; retains the last in-strip vertex at each exit."""
    pts=_points(points)
    if not isfinite(tolerance) or tolerance<0:raise ValueError("tolerance must be finite and non-negative")
    n=len(pts)
    if n<=2:return pts[:]
    out=[pts[0]];anchor=0;direction=1;i=2
    while i<n:
        if _distance_to_line(pts[i],pts[anchor],pts[direction])<=tolerance:i+=1;continue
        retained=i-1
        if retained>anchor:out.append(pts[retained])
        anchor=retained;direction=min(anchor+1,n-1);i=max(direction+1,anchor+2)
    if out[-1]!=pts[-1]:out.append(pts[-1])
    return out
def lang(points,tolerance,lookahead):
    """Bounded look-ahead variant using finite-segment deviation."""
    pts=_points(points)
    if not isfinite(tolerance) or tolerance<0:raise ValueError("tolerance must be finite and non-negative")
    if not isinstance(lookahead,int) or isinstance(lookahead,bool) or lookahead<1:raise ValueError("lookahead must be a positive integer")
    n=len(pts)
    if n<=2:return pts[:]
    out=[pts[0]];anchor=0
    while anchor<n-1:
        limit=min(n-1,anchor+lookahead);chosen=anchor+1
        for candidate in range(anchor+2,limit+1):
            if all(_distance_to_segment(pts[k],pts[anchor],pts[candidate])<=tolerance for k in range(anchor+1,candidate)):chosen=candidate
            else:break
        out.append(pts[chosen]);anchor=chosen
    return out
