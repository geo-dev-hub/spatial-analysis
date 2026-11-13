"""NoData-aware zonal summaries for aligned value and zone rasters."""
from __future__ import annotations
from typing import Sequence
import numpy as np

def zonal_statistics(values: Sequence[Sequence[float]]|np.ndarray, zones: Sequence[Sequence[float]]|np.ndarray) -> dict[int,dict[str,float|int]]:
    """Summarize finite values by integer zone label.

    Non-finite zone labels are excluded. Non-finite values are skipped.
    Every zone label is returned, including zones with no valid values.
    Standard deviation is population standard deviation (ddof=0).
    """
    data=np.asarray(values,dtype=float)
    labels=np.asarray(zones,dtype=float)
    if data.ndim!=2 or data.size==0:
        raise ValueError("values must be a non-empty 2D array")
    if labels.ndim!=2 or labels.shape!=data.shape:
        raise ValueError("zones must be a 2D array with the same shape as values")
    finite_labels=labels[np.isfinite(labels)]
    if ((finite_labels!=np.floor(finite_labels)).any()
        or (finite_labels>=float(2**63)).any()
        or (finite_labels<np.iinfo(np.int64).min).any()):
        raise ValueError("finite zone labels must be integers in int64 range")
    result={}
    for zone in np.unique(finite_labels.astype(np.int64)):
        selected=data[(labels==zone)&np.isfinite(data)]
        count=int(selected.size)
        if count==0:
            result[int(zone)]={"count":0,"sum":0.0,"mean":float("nan"),"min":float("nan"),"max":float("nan"),"median":float("nan"),"std":float("nan")}
        else:
            result[int(zone)]={"count":count,"sum":float(selected.sum()),"mean":float(selected.mean()),"min":float(selected.min()),"max":float(selected.max()),"median":float(np.median(selected)),"std":float(selected.std(ddof=0))}
    return result
