"""Connected-component labeling for boolean raster masks."""
from __future__ import annotations
from collections import deque
from typing import Sequence
import numpy as np

def connected_components(foreground: Sequence[Sequence[bool]]|np.ndarray, *, connectivity: int=8, valid: Sequence[Sequence[bool]]|np.ndarray|None=None) -> tuple[np.ndarray,dict[int,int]]:
    """Label foreground components in deterministic row-major discovery order.

    Label zero means background or invalid. A supplied valid mask marks cells
    participating in the analysis; invalid cells are barriers.
    """
    raw=np.asarray(foreground)
    if raw.ndim!=2 or raw.size==0:
        raise ValueError("foreground must be a non-empty 2D array")
    if not (np.issubdtype(raw.dtype,np.bool_) or np.issubdtype(raw.dtype,np.number)):
        raise ValueError("foreground must be boolean or numeric 0/1")
    if not np.isfinite(raw).all() or not np.isin(raw,[0,1]).all():
        raise ValueError("foreground must contain only finite boolean/0/1 values")
    mask=raw.astype(bool)
    if connectivity not in (4,8):
        raise ValueError("connectivity must be 4 or 8")
    if valid is None:
        valid_mask=np.ones(mask.shape,dtype=bool)
    else:
        raw_valid=np.asarray(valid)
        if raw_valid.ndim!=2 or raw_valid.shape!=mask.shape:
            raise ValueError("valid mask must have the same 2D shape as foreground")
        if not (np.issubdtype(raw_valid.dtype,np.bool_) or np.issubdtype(raw_valid.dtype,np.number)) or not np.isfinite(raw_valid).all() or not np.isin(raw_valid,[0,1]).all():
            raise ValueError("valid mask must contain only finite boolean/0/1 values")
        valid_mask=raw_valid.astype(bool)
    rows,cols=mask.shape
    labels=np.zeros(mask.shape,dtype=np.int32)
    if connectivity==4:
        offsets=((-1,0),(1,0),(0,-1),(0,1))
    else:
        offsets=tuple((dr,dc) for dr in (-1,0,1) for dc in (-1,0,1) if (dr,dc)!=(0,0))
    sizes={}
    next_label=0
    for r in range(rows):
        for c in range(cols):
            if not mask[r,c] or not valid_mask[r,c] or labels[r,c]!=0:
                continue
            next_label+=1
            labels[r,c]=next_label
            queue=deque([(r,c)])
            size=0
            while queue:
                cr,cc=queue.popleft()
                size+=1
                for dr,dc in offsets:
                    nr,nc=cr+dr,cc+dc
                    if 0<=nr<rows and 0<=nc<cols and mask[nr,nc] and valid_mask[nr,nc] and labels[nr,nc]==0:
                        labels[nr,nc]=next_label
                        queue.append((nr,nc))
            sizes[next_label]=size
    return labels,sizes
