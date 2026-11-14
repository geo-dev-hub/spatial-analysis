from __future__ import annotations
from math import isfinite
from typing import Sequence
Point=tuple[float,float]
Segment=tuple[Point,Point]

def _pt(p:Sequence[float])->Point:
 if len(p)!=2: raise ValueError('point must contain x and y')
 x,y=float(p[0]),float(p[1])
 if not (isfinite(x) and isfinite(y)): raise ValueError('coordinates must be finite')
 return x,y

def _rect(rect):
 if len(rect)!=4: raise ValueError('rectangle is xmin, ymin, xmax, ymax')
 xmin,ymin,xmax,ymax=map(float,rect)
 if not all(map(isfinite,(xmin,ymin,xmax,ymax))) or xmin>xmax or ymin>ymax: raise ValueError('invalid rectangle bounds')
 return xmin,ymin,xmax,ymax

def _outcode(p,r):
 x,y=p; xmin,ymin,xmax,ymax=r; c=0
 if x<xmin:c|=1
 elif x>xmax:c|=2
 if y<ymin:c|=4
 elif y>ymax:c|=8
 return c

def cohen_sutherland(start:Sequence[float],end:Sequence[float],rect:Sequence[float])->Segment|None:
 p0,p1=_pt(start),_pt(end); r=_rect(rect); xmin,ymin,xmax,ymax=r
 while True:
  c0,c1=_outcode(p0,r),_outcode(p1,r)
  if not (c0|c1): return p0,p1
  if c0&c1:return None
  code=c0 or c1; x0,y0=p0; x1,y1=p1
  if code&8:
   if y1==y0:return None
   x=x0+(x1-x0)*(ymax-y0)/(y1-y0); y=ymax
  elif code&4:
   if y1==y0:return None
   x=x0+(x1-x0)*(ymin-y0)/(y1-y0); y=ymin
  elif code&2:
   if x1==x0:return None
   y=y0+(y1-y0)*(xmax-x0)/(x1-x0); x=xmax
  else:
   if x1==x0:return None
   y=y0+(y1-y0)*(xmin-x0)/(x1-x0); x=xmin
  if code==c0:p0=(x,y)
  else:p1=(x,y)

def liang_barsky(start:Sequence[float],end:Sequence[float],rect:Sequence[float])->Segment|None:
 x0,y0=_pt(start); x1,y1=_pt(end); xmin,ymin,xmax,ymax=_rect(rect)
 dx,dy=x1-x0,y1-y0; p=(-dx,dx,-dy,dy); q=(x0-xmin,xmax-x0,y0-ymin,ymax-y0); lo,hi=0.0,1.0
 for pi,qi in zip(p,q):
  if pi==0:
   if qi<0:return None
   continue
  t=qi/pi
  if pi<0:lo=max(lo,t)
  else:hi=min(hi,t)
  if lo>hi:return None
 return ((x0+lo*dx,y0+lo*dy),(x0+hi*dx,y0+hi*dy))

def cyrus_beck(start:Sequence[float],end:Sequence[float],vertices:Sequence[Sequence[float]])->Segment|None:
 p0,p1=_pt(start),_pt(end); ring=[_pt(v) for v in vertices]
 if len(ring)>1 and ring[0]==ring[-1]:ring.pop()
 if len(ring)<3 or len(set(ring))<3:raise ValueError('clip window needs at least three distinct vertices')
 area=sum(ring[i][0]*ring[(i+1)%len(ring)][1]-ring[(i+1)%len(ring)][0]*ring[i][1] for i in range(len(ring)))
 if area==0:raise ValueError('clip window has zero signed area')
 orient=1.0 if area>0 else -1.0
 for i in range(len(ring)):
  a,b,c=ring[i-1],ring[i],ring[(i+1)%len(ring)]
  turn=(b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])
  if orient*turn < 0: raise ValueError('Cyrus-Beck requires a convex clip window')
 dx,dy=p1[0]-p0[0],p1[1]-p0[1]; lo,hi=0.0,1.0
 for i,a in enumerate(ring):
  b=ring[(i+1)%len(ring)]; ex,ey=b[0]-a[0],b[1]-a[1]
  c0=orient*(ex*(p0[1]-a[1])-ey*(p0[0]-a[0])); cd=orient*(ex*dy-ey*dx)
  if cd==0:
   if c0<0:return None
   continue
  t=-c0/cd
  if cd>0:lo=max(lo,t)
  else:hi=min(hi,t)
  if lo>hi:return None
 return ((p0[0]+lo*dx,p0[1]+lo*dy),(p0[0]+hi*dx,p0[1]+hi*dy))


def _rect_area_code(p, r):
    x, y = p
    xmin, ymin, xmax, ymax = r
    code = 0
    if y > ymax: code |= 8
    elif y < ymin: code |= 4
    if x > xmax: code |= 2
    elif x < xmin: code |= 1
    return code


def _nln_transform(code, p0, p1, r):
    """Map the first endpoint into NLN's canonical inside/left/top-left cases."""
    xmin, ymin, xmax, ymax = r
    def transform(p):
        x, y = p
        if code == 8: return (-y, x)
        if code in (2, 10): return (-x, y)
        if code == 4: return (y, x)
        if code == 5: return (x, -y)
        if code == 6: return (-x, -y)
        return (x, y)
    if code == 8: nr = (-ymax, xmin, -ymin, xmax)
    elif code in (2, 10): nr = (-xmax, ymin, -xmin, ymax)
    elif code == 4: nr = (ymin, xmin, ymax, xmax)
    elif code == 5: nr = (xmin, -ymax, xmax, -ymin)
    elif code == 6: nr = (-xmax, -ymax, -xmin, -ymin)
    else: nr = r
    return transform(p0), transform(p1), nr


def _nln_inverse(code, p):
    x, y = p
    if code == 8: return (y, -x)
    if code in (2, 10): return (-x, y)
    if code == 4: return (y, x)
    if code == 5: return (x, -y)
    if code == 6: return (-x, -y)
    return (x, y)


def _nln_sides(p0, p1, r, start_code):
    """Return the exact boundary set selected by the NLN region tests."""
    xmin, ymin, xmax, ymax = r
    x1, y1 = p0
    x2, y2 = p1
    dx, dy = x2 - x1, y2 - y1

    if start_code == 0:
        if dx == 0:
            return ["top"] if dy > 0 else ["bottom"]
        slope = dy / dx
        if x2 > x1:
            tr = (ymax - y1) / (xmax - x1)
            br = (ymin - y1) / (xmax - x1)
            if slope >= tr: return ["top"]
            if slope >= br: return ["right"]
            return ["bottom"]
        tl = (ymax - y1) / (xmin - x1)
        bl = (ymin - y1) / (xmin - x1)
        if slope < tl: return ["top"]
        if slope < bl: return ["left"]
        return ["bottom"]

    if dx == 0:
        return None
    slope = dy / dx
    tr = (ymax - y1) / (xmax - x1)
    br = (ymin - y1) / (xmax - x1)
    bl = (ymin - y1) / (xmin - x1)
    tl = (ymax - y1) / (xmin - x1)

    if start_code == 1:  # left side region
        if tr < slope <= tl:
            return ["left", "top"] if y2 >= ymax else ["left"]
        if br < slope <= tr:
            return ["left", "right"] if x2 >= xmax else ["left"]
        if bl <= slope <= br:
            return ["left", "bottom"] if y2 <= ymin else ["left"]
        return None

    if start_code == 9:  # top-left corner region
        if br < tl:
            if bl <= slope < br:
                return ["left", "bottom"] if y2 <= ymin else ["left"]
            if br <= slope < tl:
                return ["left", "right"] if x2 >= xmax else ["left"]
            if tl <= slope <= tr:
                return ["top", "right"] if x2 >= xmax else ["top"]
        else:
            if bl <= slope < tl:
                return ["left", "bottom"] if y2 <= ymin else ["left"]
            if tl <= slope < br:
                return ["top", "bottom"] if y2 <= ymin else ["top"]
            if br <= slope <= tr:
                return ["top", "right"] if x2 >= xmax else ["top"]
        return None
    return None


def _nln_intersection(p0, p1, r, side):
    xmin, ymin, xmax, ymax = r
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    if side == "left":
        if dx == 0: return None
        t = (xmin - p0[0]) / dx
    elif side == "right":
        if dx == 0: return None
        t = (xmax - p0[0]) / dx
    elif side == "bottom":
        if dy == 0: return None
        t = (ymin - p0[1]) / dy
    else:
        if dy == 0: return None
        t = (ymax - p0[1]) / dy
    return (p0[0] + t * dx, p0[1] + t * dy)


def nicholl_lee_nicholl(start, end, rect):
    """Clip a 2D segment against an axis-aligned rectangle using NLN cases.

    The algorithm reduces the start endpoint to one of three canonical
    regions (inside, left, top-left) by reflections/rotations, then uses
    slope-region comparisons to identify only the boundary or boundary pair
    that can form the visible segment. This is a 2D rectangular-window method.
    """
    p0, p1 = _pt(start), _pt(end)
    r = _rect(rect)
    if r[0] == r[2] or r[1] == r[3]:
        raise ValueError("Nicholl–Lee–Nicholl requires a non-degenerate rectangle")
    c0, c1 = _rect_area_code(p0, r), _rect_area_code(p1, r)
    xmin, ymin, xmax, ymax = r
    # A segment that starts on a boundary and immediately leaves the
    # rectangle has only the start point visible.
    if c0 == 0 and (
        (p0[0] == xmin and p1[0] < xmin) or
        (p0[0] == xmax and p1[0] > xmax) or
        (p0[1] == ymin and p1[1] < ymin) or
        (p0[1] == ymax and p1[1] > ymax)
    ):
        return p0, p0
    if (c0 | c1) == 0:
        return p0, p1
    if (c0 & c1) != 0:
        return None

    q0, q1, qr = _nln_transform(c0, p0, p1, r)
    qcode = _rect_area_code(q0, qr)
    sides = _nln_sides(q0, q1, qr, qcode)
    if not sides:
        return None

    intersections = []
    for side in sides:
        point = _nln_intersection(q0, q1, qr, side)
        if point is not None:
            intersections.append(point)
    if not intersections:
        return None

    dx, dy = q1[0] - q0[0], q1[1] - q0[1]
    length2 = dx * dx + dy * dy
    intersections.sort(key=lambda p: ((p[0]-q0[0])*dx + (p[1]-q0[1])*dy) / length2 if length2 else 0.0)
    start_inside = _rect_area_code(q0, qr) == 0
    end_inside = _rect_area_code(q1, qr) == 0
    if start_inside:
        clipped0 = q0
    else:
        clipped0 = intersections[0]
    if end_inside:
        clipped1 = q1
    else:
        clipped1 = intersections[-1]
    # A tangent may yield the same point twice; preserve it as a zero-length clip.
    out0 = _nln_inverse(c0, clipped0)
    out1 = _nln_inverse(c0, clipped1)
    return out0, out1
