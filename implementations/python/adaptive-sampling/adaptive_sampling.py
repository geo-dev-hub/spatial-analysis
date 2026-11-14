"""Network-based adaptive cluster sampling expansion."""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from math import isfinite
from numbers import Integral
from typing import Sequence

@dataclass(frozen=True)
class AdaptiveSample:
    initial_indices: tuple[int,...]
    sampled_indices: tuple[int,...]
    recruited_indices: tuple[int,...]

def adaptive_cluster_sample(values:Sequence[float],neighbours:Sequence[Sequence[int]],
                            initial_sample:Sequence[int],threshold:float)->AdaptiveSample:
    """Expand a probability sample through neighbours of threshold-positive units.

    Every initially selected unit is observed. Any observed unit with value
    >= threshold recruits all its network neighbours; recruited units are
    observed and may recruit further neighbours. The returned set is the
    realised adaptive sample, not an estimator or inclusion-probability
    calculation.
    """
    y=[float(v) for v in values]
    n=len(y)
    if n==0 or any(not isfinite(v) for v in y):raise ValueError("values must be non-empty and finite")
    if len(neighbours)!=n:raise ValueError("neighbours must have one adjacency list per unit")
    threshold=float(threshold)
    if not isfinite(threshold):raise ValueError("threshold must be finite")
    graph=[]
    for i,row in enumerate(neighbours):
        items=[]
        for j in row:
            if not isinstance(j,Integral) or isinstance(j,bool) or not 0<=j<n:raise ValueError("neighbour indices must be valid integers")
            if j!=i and j not in items:items.append(j)
        graph.append(items)
    for i,row in enumerate(graph):
        for j in row:
            if i not in graph[j]:raise ValueError("neighbour graph must be symmetric")
    initial=[]
    for i in initial_sample:
        if not isinstance(i,Integral) or isinstance(i,bool) or not 0<=i<n:raise ValueError("initial sample indices must be valid integers")
        if i not in initial:initial.append(i)
    if not initial:raise ValueError("initial sample must be non-empty")
    sampled=set(initial);queue=deque(initial)
    while queue:
        i=queue.popleft()
        if y[i]>=threshold:
            for j in graph[i]:
                if j not in sampled:
                    sampled.add(j);queue.append(j)
    ordered=tuple(sorted(sampled))
    return AdaptiveSample(tuple(initial),ordered,tuple(i for i in ordered if i not in initial))
