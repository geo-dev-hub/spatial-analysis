"""Spatially constrained uncertainty sampling for map-validation labels."""
from __future__ import annotations
import numpy as np

def select_uncertain_spatial_sites(coordinates,uncertainty,batch_size,*,min_distance=0.0,costs=None):
    """Greedy uncertainty-per-cost selection with a minimum spatial separation.

    This is a one-round batch selection heuristic. It does not retrain a model,
    estimate inclusion probabilities or guarantee optimal information gain.
    """
    xy=np.asarray(coordinates,dtype=float);u=np.asarray(uncertainty,dtype=float)
    if xy.ndim!=2 or xy.shape[1]!=2 or xy.shape[0]<1 or not np.all(np.isfinite(xy)):
        raise ValueError("coordinates must be a finite (n,2) array")
    if u.ndim!=1 or len(u)!=len(xy) or not np.all(np.isfinite(u)) or np.any(u<0):
        raise ValueError("uncertainty must be a finite non-negative vector matching candidates")
    if not isinstance(batch_size,int) or isinstance(batch_size,bool) or not 1<=batch_size<=len(xy):
        raise ValueError("batch_size must be an integer between 1 and candidate count")
    if not np.isfinite(min_distance) or min_distance<0:
        raise ValueError("min_distance must be finite and non-negative")
    if costs is None:c=np.ones(len(xy))
    else:
        c=np.asarray(costs,dtype=float)
        if c.ndim!=1 or len(c)!=len(xy) or not np.all(np.isfinite(c)) or np.any(c<=0):
            raise ValueError("costs must be finite, positive and match candidates")
    utility=u/c
    order=np.argsort(-utility,kind="stable")
    selected=[]
    for i in order:
        if all(np.linalg.norm(xy[i]-xy[j])>=min_distance for j in selected):
            selected.append(int(i))
            if len(selected)==batch_size:break
    if len(selected)<batch_size:
        raise ValueError(f"minimum distance permits only {len(selected)} of {batch_size} requested sites")
    return {"selected_indices":selected,"selected_utility":utility[selected]}
