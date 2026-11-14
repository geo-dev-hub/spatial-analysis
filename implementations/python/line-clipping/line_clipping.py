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
