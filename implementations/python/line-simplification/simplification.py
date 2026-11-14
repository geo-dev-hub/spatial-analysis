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


def opheim(points, strip_half_width, min_distance, max_distance):
    """Constrained moving-strip Opheim variant for an open polyline.

    At each retained anchor, orient a strip toward the first subsequent point
    at least min_distance away. Advance while vertices remain inside the
    strip and within max_distance of the anchor; retain the last eligible
    vertex and restart there. Endpoints are always retained.

    strip_half_width is the perpendicular half-width of the corridor. The
    min/max radii are Euclidean distances in the same coordinate units.
    """
    pts = _points(points)
    params = (strip_half_width, min_distance, max_distance)
    if any(not isfinite(float(x)) for x in params):
        raise ValueError("Opheim distances must be finite")
    width, minimum, maximum = map(float, params)
    if width < 0 or minimum <= 0 or maximum < minimum:
        raise ValueError("require width >= 0 and 0 < min_distance <= max_distance")
    n = len(pts)
    if n <= 2:
        return pts[:]
    out = [pts[0]]
    anchor = 0
    while anchor < n - 1:
        direction = anchor + 1
        while direction < n - 1 and hypot(
            pts[direction][0] - pts[anchor][0],
            pts[direction][1] - pts[anchor][1]
        ) < minimum:
            direction += 1
        if direction == n - 1:
            out.append(pts[-1])
            break
        a, b = pts[anchor], pts[direction]
        chosen = direction
        i = direction + 1
        while i < n:
            distance = hypot(pts[i][0] - a[0], pts[i][1] - a[1])
            if distance > maximum or _distance_to_line(pts[i], a, b) > width:
                break
            chosen = i
            i += 1
        if chosen <= anchor:
            chosen = min(anchor + 1, n - 1)
        out.append(pts[chosen])
        anchor = chosen
        if anchor == n - 1:
            break
    if out[-1] != pts[-1]:
        out.append(pts[-1])
    return out


def zhao_saalfeld_narrow_sleeve(points, tolerance):
    """Zhao–Saalfeld narrow-sleeve (epsilon-width) variant.

    Maintains the intersection of angular sector bounds for all vertices in
    the active sleeve. A candidate endpoint is accepted only when its
    direction lies in the current intersection; otherwise the previous
    original vertex is committed and becomes the next sleeve's start.

    The guarantee is perpendicular distance to the supporting line of each
    simplified segment, not necessarily distance to the finite segment.
    """
    from math import asin, atan2, pi
    pts = _points(points)
    if not isfinite(tolerance) or tolerance < 0:
        raise ValueError("tolerance must be finite and non-negative")
    n = len(pts)
    if n <= 2:
        return pts[:]
    out = [pts[0]]
    anchor = 0
    while anchor < n - 1:
        lower = None
        upper = None
        i = anchor + 1
        while i < n:
            dx = pts[i][0] - pts[anchor][0]
            dy = pts[i][1] - pts[anchor][1]
            distance = hypot(dx, dy)
            if distance == 0:
                i += 1
                continue
            angle = atan2(dy, dx)
            if lower is not None:
                middle = (lower + upper) / 2.0
                angle += 2.0 * pi * round((middle - angle) / (2.0 * pi))
                if angle < lower - 1e-12 or angle > upper + 1e-12:
                    break
            if distance > tolerance:
                half_angle = asin(min(1.0, tolerance / distance))
                lo, hi = angle - half_angle, angle + half_angle
                if lower is None:
                    lower, upper = lo, hi
                else:
                    lower, upper = max(lower, lo), min(upper, hi)
            i += 1
        if i == n:
            out.append(pts[-1])
            break
        # i is the first point that cannot join this sleeve. Commit the last
        # accepted original vertex and restart from it; no accepted point is
        # revisited, giving the narrow-sleeve variant its linear scan.
        new_anchor = i - 1
        if new_anchor <= anchor:
            new_anchor = anchor + 1
        out.append(pts[new_anchor])
        anchor = new_anchor
    if out[-1] != pts[-1]:
        out.append(pts[-1])
    return out
