"""Bounded MODE-inspired object extraction and one-to-one matching."""
from __future__ import annotations
import numpy as np
from scipy.ndimage import gaussian_filter, label
from scipy.optimize import linear_sum_assignment


def _field(values, name):
    a=np.asarray(values,dtype=float)
    if a.ndim!=2 or min(a.shape)<2 or not np.all(np.isfinite(a)) or np.any(a<0):
        raise ValueError(f"{name} must be a finite non-negative 2D field at least 2x2")
    return a


def identify_objects(field, *, threshold, smooth_sigma=0.0, min_area=1, connectivity=8):
    """Convolve, threshold, label and measure field objects.

    The original unsmoothed field is used for intensity attributes inside
    each resolved object. IDs follow deterministic row-major label order.
    """
    data=_field(field,"field")
    threshold=float(threshold); sigma=float(smooth_sigma)
    if not np.isfinite(threshold) or threshold<=0 or not np.isfinite(sigma) or sigma<0:
        raise ValueError("threshold must be positive and smooth_sigma non-negative")
    if not isinstance(min_area,(int,np.integer)) or min_area<1:
        raise ValueError("min_area must be a positive integer")
    if connectivity not in (4,8): raise ValueError("connectivity must be 4 or 8")
    smoothed=gaussian_filter(data,sigma=sigma,mode="nearest") if sigma>0 else data
    structure=np.array([[0,1,0],[1,1,1],[0,1,0]],dtype=int) if connectivity==4 else np.ones((3,3),dtype=int)
    labels,n=label(smoothed>=threshold,structure=structure)
    objects=[]
    for old_id in range(1,n+1):
        rows,cols=np.where(labels==old_id)
        if rows.size<min_area:
            labels[labels==old_id]=0
            continue
        values=data[rows,cols]
        mass=float(values.sum())
        if mass>0:
            cy=float(np.sum(rows*values)/mass); cx=float(np.sum(cols*values)/mass)
            dr=rows-cy; dc=cols-cx
            covariance=np.array([[np.sum(values*dc*dc),np.sum(values*dc*dr)],
                                 [np.sum(values*dc*dr),np.sum(values*dr*dr)]])/mass
            eigenvalues,eigenvectors=np.linalg.eigh(covariance)
            vector=eigenvectors[:,int(np.argmax(eigenvalues))]
            orientation=float(np.arctan2(vector[1],vector[0]))
        else:
            cy=float(rows.mean()); cx=float(cols.mean()); orientation=0.0
        new_id=len(objects)+1
        labels[labels==old_id]=new_id
        objects.append({"id":new_id,"area":int(rows.size),"centroid_x":cx,
                        "centroid_y":cy,"orientation_radians":orientation,
                        "intensity_sum":mass,"intensity_mean":float(values.mean()),
                        "intensity_max":float(values.max())})
    return {"objects":objects,"labels":labels,"smoothed_field":smoothed}


def match_objects(forecast_objects, observed_objects, field_shape, *,
                  max_centroid_distance=0.25, max_match_cost=1.0,
                  distance_weight=1.0, area_weight=0.25, intensity_weight=0.25):
    """One-to-one minimum-cost object matching with explicit unmatched objects.

    Cost combines domain-diagonal-normalized centroid distance and absolute
    log ratios of area and mean intensity. This transparent assignment is
    MODE-inspired, not the official MET/MODE fuzzy-interest algorithm.
    """
    f=list(forecast_objects); o=list(observed_objects)
    if len(field_shape)!=2 or any(not isinstance(v,(int,np.integer)) or v<2 for v in field_shape):
        raise ValueError("field_shape must contain two integer dimensions >= 2")
    params=np.asarray([max_centroid_distance,max_match_cost,distance_weight,area_weight,intensity_weight],float)
    if not np.all(np.isfinite(params)) or np.any(params<0) or max_centroid_distance<=0 or max_match_cost<=0:
        raise ValueError("distance limits must be positive and weights non-negative")
    for obj in f+o:
        required=("id","area","centroid_x","centroid_y","intensity_mean")
        if any(k not in obj for k in required) or obj["area"]<=0 or obj["intensity_mean"]<0:
            raise ValueError("objects require positive area/intensity and centroid attributes")
        if not np.all(np.isfinite([obj["centroid_x"],obj["centroid_y"],obj["intensity_mean"]])):
            raise ValueError("object attributes must be finite")
    if not f or not o:
        return {"matches":[],"unmatched_forecast":[x["id"] for x in f],
                "unmatched_observed":[x["id"] for x in o],"cost_matrix":np.empty((len(f),len(o)))}
    diagonal=float(np.hypot(*field_shape))
    costs=np.empty((len(f),len(o)),float)
    for i,a in enumerate(f):
        for j,b in enumerate(o):
            distance=np.hypot(a["centroid_x"]-b["centroid_x"],a["centroid_y"]-b["centroid_y"])/diagonal
            area_error=abs(np.log(float(a["area"])/float(b["area"])))
            intensity_error=abs(np.log((float(a["intensity_mean"])+1e-12)/(float(b["intensity_mean"])+1e-12)))
            costs[i,j]=distance_weight*distance+area_weight*area_error+intensity_weight*intensity_error
    # Dummy rows/columns allow either side to remain unmatched. Without
    # them, a forced rectangular assignment can sacrifice a valid low-cost
    # pair merely to pair a distant object elsewhere.
    nf,no=len(f),len(o)
    unmatched_cost=max_match_cost/2.0
    big_cost=max_match_cost*1e6+1.0
    padded=np.full((nf+no,nf+no),big_cost,dtype=float)
    padded[:nf,:no]=costs
    for i in range(nf):
        padded[i,no+i]=unmatched_cost
    for j in range(no):
        padded[nf+j,j]=unmatched_cost
    padded[nf:,no:]=0.0
    rows,cols=linear_sum_assignment(padded)
    matches=[]
    for i,j in zip(rows,cols):
        if i<nf and j<no and costs[i,j]<=max_match_cost:
            distance=np.hypot(f[i]["centroid_x"]-o[j]["centroid_x"],f[i]["centroid_y"]-o[j]["centroid_y"])/diagonal
            if distance<=max_centroid_distance:
                matches.append({"forecast_id":f[i]["id"],"observed_id":o[j]["id"],
                                "cost":float(costs[i,j]),"normalized_centroid_distance":float(distance)})
    matched_f={m["forecast_id"] for m in matches}; matched_o={m["observed_id"] for m in matches}
    return {"matches":matches,"unmatched_forecast":[x["id"] for x in f if x["id"] not in matched_f],
            "unmatched_observed":[x["id"] for x in o if x["id"] not in matched_o],
            "cost_matrix":costs}
