from __future__ import annotations
from math import ceil, floor, isfinite
from typing import Iterable, Sequence

Point = tuple[float, float]
Cell = tuple[int, int]

def _point(p: Sequence[float]) -> Point:
    if len(p) != 2: raise ValueError('point must contain x and y')
    x, y = float(p[0]), float(p[1])
    if not (isfinite(x) and isfinite(y)): raise ValueError('coordinates must be finite')
    return x, y

def _round_cell(v: float) -> int:
    return floor(v + 0.5) if v >= 0 else -floor(-v + 0.5)

def dda_line(start: Sequence[float], end: Sequence[float]) -> list[Cell]:
    x0,y0=_point(start); x1,y1=_point(end); dx,dy=x1-x0,y1-y0
    steps=ceil(max(abs(dx),abs(dy)))
    if steps == 0: return [(_round_cell(x0),_round_cell(y0))]
    sx,sy=dx/steps,dy/steps; x,y=x0,y0; out=[]
    for _ in range(steps+1):
        c=(_round_cell(x),_round_cell(y))
        if not out or out[-1] != c: out.append(c)
        x+=sx; y+=sy
    return out

def bresenham_line(start: Sequence[int], end: Sequence[int]) -> list[Cell]:
    vals=(*_point(start),*_point(end))
    if any(v != int(v) for v in vals): raise ValueError('Bresenham requires integer endpoints')
    x0,y0,x1,y1=map(int,vals); dx,dy=abs(x1-x0),abs(y1-y0)
    sx=1 if x0<x1 else -1; sy=1 if y0<y1 else -1; err=dx-dy; out=[]
    while True:
        out.append((x0,y0))
        if (x0,y0)==(x1,y1): return out
        e2=2*err
        if e2 > -dy: err-=dy; x0+=sx
        if e2 < dx: err+=dx; y0+=sy

def supercover_line(start: Sequence[int], end: Sequence[int]) -> list[Cell]:
    vals=(*_point(start),*_point(end))
    if any(v != int(v) for v in vals): raise ValueError('supercover requires integer endpoints')
    x0,y0,x1,y1=map(int,vals); dx,dy=x1-x0,y1-y0
    nx,ny=abs(dx),abs(dy); sx=(dx>0)-(dx<0); sy=(dy>0)-(dy<0)
    x,y,ix,iy=x0,y0,0,0; out=[(x,y)]; seen={(x,y)}
    def add(c):
        if c not in seen: seen.add(c); out.append(c)
    while ix<nx or iy<ny:
        lhs=(1+2*ix)*ny; rhs=(1+2*iy)*nx
        if lhs==rhs:
            if sx and sy: add((x+sx,y)); add((x,y+sy))
            x+=sx; y+=sy; ix+=1; iy+=1; add((x,y))
        elif lhs<rhs: x+=sx; ix+=1; add((x,y))
        else: y+=sy; iy+=1; add((x,y))
    return out

def wu_line(start: Sequence[float], end: Sequence[float]) -> dict[Cell,float]:
    x0,y0=_point(start); x1,y1=_point(end); steep=abs(y1-y0)>abs(x1-x0)
    if steep: x0,y0=y0,x0; x1,y1=y1,x1
    if x0>x1: x0,x1,y0,y1=x1,x0,y1,y0
    dx,dy=x1-x0,y1-y0
    if dx==0: return {(_round_cell(x0),_round_cell(y0)):1.0}
    gradient=dy/dx; out={}
    def ip(v): return floor(v)
    def fp(v): return v-floor(v)
    def put(x,y,w):
        c=(y,x) if steep else (x,y); out[c]=min(1.0,out.get(c,0.0)+max(0.0,w))
    xe=_round_cell(x0); ye=y0+gradient*(xe-x0); gap=1-fp(x0+0.5)
    xp1,yp1=xe,ip(ye); put(xp1,yp1,(1-fp(ye))*gap); put(xp1,yp1+1,fp(ye)*gap)
    inter=ye+gradient; xe=_round_cell(x1); ye=y1+gradient*(xe-x1); gap=fp(x1+0.5)
    xp2,yp2=xe,ip(ye); put(xp2,yp2,(1-fp(ye))*gap); put(xp2,yp2+1,fp(ye)*gap)
    for x in range(xp1+1,xp2):
        y=ip(inter); put(x,y,1-fp(inter)); put(x,y+1,fp(inter)); inter+=gradient
    return {c:w for c,w in out.items() if w>0}

def scanline_polygon_fill(vertices: Iterable[Sequence[float]]) -> set[Cell]:
    ring=[_point(p) for p in vertices]
    if len(ring)>1 and ring[0]==ring[-1]: ring.pop()
    if len(set(ring))<3: raise ValueError('ring requires at least three distinct vertices')
    edges=list(zip(ring,ring[1:]+ring[:1])); miny=floor(min(y for x,y in ring)-0.5); maxy=floor(max(y for x,y in ring)-0.5)
    minx=floor(min(x for x,y in ring)-0.5); maxx=floor(max(x for x,y in ring)-0.5); filled=set()
    for row in range(miny,maxy+1):
        sy=row+0.5; xs=[]
        for (x0,y0),(x1,y1) in edges:
            if (y0<=sy<y1) or (y1<=sy<y0): xs.append(x0+(sy-y0)*(x1-x0)/(y1-y0))
        xs.sort()
        if len(xs)%2: raise ValueError('odd scanline intersection count; ring may be invalid')
        for left,right in zip(xs[::2],xs[1::2]):
            for col in range(max(minx,floor(left-0.5)+1),min(maxx,floor(right-0.5))+1):
                cx=col+0.5
                if left<cx<right: filled.add((col,row))
    return filled
