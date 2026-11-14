"""Nearest-neighbour-distance-matching leave-one-out CV (NNDM)."""
from __future__ import annotations
import numpy as np
from scipy.spatial.distance import cdist

def _points(values, name, minimum=2):
    a=np.asarray(values,dtype=float)
    if a.ndim!=2 or len(a)<minimum or a.shape[1]<1 or not np.isfinite(a).all():
        raise ValueError(f"{name} must be a finite 2D coordinate array with at least {minimum} rows")
    return a

def nndm_loo(training_points, prediction_points, *, autocorrelation_range,
             min_train=0.5):
    """Construct NNDM LOO folds using projected Euclidean coordinates.

    Each observation is held out once. Additional observations are greedily
    removed from that fold's analysis set while the modified CV nearest-
    neighbour ECDF remains at least the prediction-to-training ECDF at the
    current minimum CV distance. Distances beyond phi are not matched.

    This is an auditable O(n^3)-style teaching implementation for modest n;
    it does not provide geographic/geodesic distance support.
    """
    train=_points(training_points,"training_points",3)
    pred=_points(prediction_points,"prediction_points",1)
    if train.shape[1]!=pred.shape[1]:
        raise ValueError("training and prediction coordinates must have the same dimension")
    phi=float(autocorrelation_range)
    if not np.isfinite(phi) or phi<0:
        raise ValueError("autocorrelation_range must be finite and non-negative")
    fraction=float(min_train)
    if not np.isfinite(fraction) or not 0<fraction<=1:
        raise ValueError("min_train must be in (0,1]")
    n=len(train)
    distances=cdist(train,train)
    np.fill_diagonal(distances,np.inf)
    pred_nnd=cdist(pred,train).min(axis=1)
    # Each LOO analysis set initially contains all observations except its test point.
    analysis=np.ones((n,n),dtype=bool)
    np.fill_diagonal(analysis,False)
    excluded=[[] for _ in range(n)]
    blocked=np.zeros(n,dtype=bool)
    min_size=max(2,int(np.ceil(fraction*n)))
    removals=0
    # Greedily process the globally shortest current CV nearest-neighbour distance.
    while True:
        current=np.full(n,np.inf)
        nearest=np.full(n,-1,dtype=int)
        for j in range(n):
            candidates=np.flatnonzero(analysis[j])
            if len(candidates):
                k=candidates[np.argmin(distances[j,candidates])]
                current[j]=distances[j,k]; nearest[j]=k
        eligible=np.flatnonzero((~blocked)&(current<=phi)&(nearest>=0)&(analysis.sum(axis=1)>min_size))
        if not len(eligible):
            break
        j=int(eligible[np.argmin(current[eligible])])
        k=int(nearest[j]); r=float(current[j])
        # Trial removal affects only the current LOO analysis set.
        trial=analysis[j].copy(); trial[k]=False
        remaining=np.flatnonzero(trial)
        new_nnd=float(distances[j,remaining].min()) if len(remaining) else np.inf
        trial_cv=current.copy(); trial_cv[j]=new_nnd
        cv_ecdf=float(np.mean(trial_cv<=r))
        prediction_ecdf=float(np.mean(pred_nnd<=r))
        if cv_ecdf+1e-15>=prediction_ecdf:
            analysis[j,k]=False
            excluded[j].append(k)
            removals+=1
        else:
            # This fold cannot remove its current nearest neighbour without
            # violating the ECDF condition at r; later removals only lower G*.
            blocked[j]=True
    folds=[]
    for j in range(n):
        folds.append({"test":np.array([j],dtype=int),
                      "train":np.flatnonzero(analysis[j]),
                      "excluded":np.asarray(excluded[j],dtype=int)})
    cv_nnd=np.array([distances[j,analysis[j]].min() for j in range(n)])
    return {"folds":folds,"prediction_nearest_distances":pred_nnd,
            "cv_nearest_distances":cv_nnd,"training_nearest_distances":distances.min(axis=1),
            "autocorrelation_range":phi,"min_train":fraction,
            "n_removed":removals,"n_excluded_by_fold":np.array([len(x) for x in excluded]),
            "prediction_ecdf_at_cv_distances":np.array([np.mean(pred_nnd<=r) for r in cv_nnd]),
            "cv_ecdf_at_cv_distances":np.array([np.mean(cv_nnd<=r) for r in cv_nnd])}
