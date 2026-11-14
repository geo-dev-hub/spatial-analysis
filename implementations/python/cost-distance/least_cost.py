"""Multi-source least-cost distance on a regular raster grid."""
from __future__ import annotations
from heapq import heappop, heappush
from typing import Iterable, Sequence
import math
import numpy as np

def least_cost_distance(cost_surface: Sequence[Sequence[float]] | np.ndarray, sources: Iterable[tuple[int,int]], *, cell_size_x: float=1.0, cell_size_y: float=1.0, connectivity: int=8, prevent_corner_cutting: bool=True) -> np.ndarray:
    """Compute accumulated least cost from one or more source cells.

    Cell costs are non-negative cost per horizontal distance unit. Edge cost
    is mean endpoint cost times orthogonal/diagonal step length. NaN cells
    are barriers. Source distance is zero; source-cell cost is not charged.
    """
    cost=np.asarray(cost_surface,dtype=float)
    if cost.ndim!=2 or cost.size==0:
        raise ValueError("cost_surface must be a non-empty 2D array")
    if not np.isfinite([cell_size_x,cell_size_y]).all() or cell_size_x<=0 or cell_size_y<=0:
        raise ValueError("cell sizes must be finite and positive")
    if connectivity not in (4,8):
        raise ValueError("connectivity must be 4 or 8")
    valid=np.isfinite(cost)
    if (cost[valid]<0).any():
        raise ValueError("valid cell costs must be non-negative")
    rows,cols=cost.shape
    source_list=list(sources)
    if not source_list:
        raise ValueError("at least one source cell is required")
    normalized=[]
    for source in source_list:
        if len(source)!=2 or any(not isinstance(v,(int,np.integer)) for v in source):
            raise ValueError("each source must be a (row, column) integer pair")
        r,c=map(int,source)
        if not (0<=r<rows and 0<=c<cols):
            raise ValueError("source is outside the raster")
        if not valid[r,c]:
            raise ValueError("source must be on a valid cost cell")
        normalized.append((r,c))
    steps=[(-1,0,cell_size_y),(1,0,cell_size_y),(0,-1,cell_size_x),(0,1,cell_size_x)]
    if connectivity==8:
        diagonal=math.hypot(cell_size_x,cell_size_y)
        steps += [(-1,-1,diagonal),(-1,1,diagonal),(1,-1,diagonal),(1,1,diagonal)]
    distance=np.full(cost.shape,np.inf,dtype=float)
    queue=[]
    for r,c in sorted(set(normalized)):
        distance[r,c]=0.0
        heappush(queue,(0.0,r,c))
    while queue:
        current,r,c=heappop(queue)
        if current!=distance[r,c]:
            continue
        for dr,dc,length in steps:
            nr,nc=r+dr,c+dc
            if not (0<=nr<rows and 0<=nc<cols) or not valid[nr,nc]:
                continue
            if dr and dc and prevent_corner_cutting:
                if not valid[r+dr,c] or not valid[r,c+dc]:
                    continue
            edge=0.5*(cost[r,c]+cost[nr,nc])*length
            candidate=current+edge
            if candidate<distance[nr,nc]:
                distance[nr,nc]=candidate
                heappush(queue,(candidate,nr,nc))
    distance[~valid]=np.nan
    return distance
