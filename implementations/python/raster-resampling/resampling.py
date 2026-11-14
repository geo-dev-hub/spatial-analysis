"""Nearest-neighbour and bilinear resampling on a same-extent regular grid."""
from __future__ import annotations
import math
from typing import Sequence
import numpy as np

def resample_to_shape(source: Sequence[Sequence[float]] | np.ndarray, target_shape: tuple[int,int], *, method: str="bilinear", nodata_policy: str="strict") -> np.ndarray:
    """Resample a 2D array to a new shape over the same extent and orientation.

    Target pixel centres map linearly to source pixel-centre coordinates.
    Non-finite source values are NoData. Bilinear NoData policy is either
    'strict' (all positive-weight neighbours must be valid) or 'renormalize'
    (average the valid neighbours after renormalizing their weights).
    """
    data=np.asarray(source,dtype=float)
    if data.ndim!=2 or data.size==0:
        raise ValueError("source must be a non-empty 2D array")
    if len(target_shape)!=2 or any(not isinstance(v,(int,np.integer)) or v<=0 for v in target_shape):
        raise ValueError("target_shape must contain two positive integers")
    if method not in ("nearest","bilinear"):
        raise ValueError("method must be 'nearest' or 'bilinear'")
    if nodata_policy not in ("strict","renormalize"):
        raise ValueError("nodata_policy must be 'strict' or 'renormalize'")
    in_rows,in_cols=data.shape
    out_rows,out_cols=map(int,target_shape)
    output=np.full((out_rows,out_cols),np.nan,dtype=float)
    valid=np.isfinite(data)
    for r in range(out_rows):
        sr=(r+0.5)*in_rows/out_rows-0.5
        for c in range(out_cols):
            sc=(c+0.5)*in_cols/out_cols-0.5
            if method=="nearest":
                rr=min(in_rows-1,max(0,math.floor(sr+0.5)))
                cc=min(in_cols-1,max(0,math.floor(sc+0.5)))
                if valid[rr,cc]:
                    output[r,c]=data[rr,cc]
                continue
            r0=math.floor(sr); c0=math.floor(sc)
            fr=sr-r0; fc=sc-c0
            neighbours=[
                (min(in_rows-1,max(0,r0)),min(in_cols-1,max(0,c0)),(1-fr)*(1-fc)),
                (min(in_rows-1,max(0,r0)),min(in_cols-1,max(0,c0+1)),(1-fr)*fc),
                (min(in_rows-1,max(0,r0+1)),min(in_cols-1,max(0,c0)),fr*(1-fc)),
                (min(in_rows-1,max(0,r0+1)),min(in_cols-1,max(0,c0+1)),fr*fc),
            ]
            weighted=[]; missing_positive_weight=False
            for rr,cc,w in neighbours:
                if w<=0:
                    continue
                if valid[rr,cc]:
                    weighted.append((data[rr,cc],w))
                else:
                    missing_positive_weight=True
            if not weighted or (nodata_policy=="strict" and missing_positive_weight):
                continue
            total_weight=sum(w for _,w in weighted)
            output[r,c]=sum(value*w for value,w in weighted)/total_weight
    return output
