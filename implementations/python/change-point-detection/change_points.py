"""Teaching implementations for univariate mean-shift detection."""
from __future__ import annotations
from math import isfinite
from typing import Iterable

def _series(values: Iterable[float])->list[float]:
    data=[float(x) for x in values]
    if not data or any(not isfinite(x) for x in data):raise ValueError("series must be non-empty and finite")
    return data

def _prefix(data):
    sums=[0.0];squares=[0.0]
    for x in data:sums.append(sums[-1]+x);squares.append(squares[-1]+x*x)
    return sums,squares

def _sse(sums,squares,start,end):
    n=end-start;total=sums[end]-sums[start]
    return max(0.0,squares[end]-squares[start]-total*total/n)

def binary_segmentation(values,penalty=0.0,min_size=2):
    """Greedy recursive SSE splitting; returns zero-based change indices."""
    data=_series(values)
    if not isfinite(penalty) or penalty<0:raise ValueError("penalty must be finite and non-negative")
    if not isinstance(min_size,int) or isinstance(min_size,bool) or min_size<1:raise ValueError("min_size must be a positive integer")
    sums,squares=_prefix(data);changes=[];stack=[(0,len(data))]
    while stack:
        start,end=stack.pop()
        if end-start<2*min_size:continue
        parent=_sse(sums,squares,start,end);gain_best=penalty;split_best=None
        for split in range(start+min_size,end-min_size+1):
            gain=parent-_sse(sums,squares,start,split)-_sse(sums,squares,split,end)
            if gain>gain_best:gain_best,split_best=gain,split
        if split_best is not None:
            changes.append(split_best);stack.extend(((split_best,end),(start,split_best)))
    return sorted(changes)

def pelt_mean(values,penalty,min_size=2):
    """Pruned exact segmentation for additive piecewise-constant mean SSE.

    Minimises sum(segment SSE)+penalty*number_of_changes. For this cost the
    pruning constant K=0 is valid. Worst-case time is quadratic; no universal
    linear-time guarantee is claimed.
    """
    data=_series(values)
    if not isfinite(penalty) or penalty<0:raise ValueError("penalty must be finite and non-negative")
    if not isinstance(min_size,int) or isinstance(min_size,bool) or min_size<1:raise ValueError("min_size must be a positive integer")
    n=len(data)
    if n<2*min_size:return []
    sums,squares=_prefix(data);best=[float("inf")]*(n+1);previous=[-1]*(n+1)
    best[0]=-penalty;candidates=[0]
    for end in range(min_size,n+1):
        eligible=[s for s in candidates if end-s>=min_size and best[s]<float("inf")]
        if not eligible:continue
        options=[(best[s]+_sse(sums,squares,s,end)+penalty,s) for s in eligible]
        best[end],previous[end]=min(options)
        not_yet_eligible=[s for s in candidates if end-s<min_size]
        pruned=[s for s in eligible if best[s]+_sse(sums,squares,s,end)<=best[end]+1e-12]
        candidates=not_yet_eligible+pruned+[end]
    if previous[n]<0:return []
    changes=[];end=n
    while end>0:
        start=previous[end]
        if start<0:raise RuntimeError("failed to reconstruct segmentation")
        if start>0:changes.append(start)
        end=start
    return sorted(changes)

def cusum(values,target_mean,allowance,threshold):
    """Two-sided Page CUSUM; returns (index, direction, statistic) alarms."""
    data=_series(values)
    if not all(isfinite(float(x)) for x in (target_mean,allowance,threshold)):raise ValueError("CUSUM parameters must be finite")
    target_mean=float(target_mean);allowance=float(allowance);threshold=float(threshold)
    if allowance<0 or threshold<=0:raise ValueError("allowance must be non-negative and threshold positive")
    up=down=0.0;alarms=[]
    for i,x in enumerate(data):
        up=max(0.0,up+x-target_mean-allowance);down=max(0.0,down+target_mean-x-allowance)
        if up>threshold:alarms.append((i,"up",up));up=0.0
        if down>threshold:alarms.append((i,"down",down));down=0.0
    return alarms
