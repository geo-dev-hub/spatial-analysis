"""Raking / iterative proportional fitting for synthetic spatial microdata weights."""
from __future__ import annotations
import numpy as np

def ipf_rake(seed_weights, constraint_matrix, target_margins, *, tolerance=1e-8, max_iter=10000):
    """Calibrate non-negative seed-record weights to supplied categorical margins.

    constraint_matrix[r, c] is 1 when record r belongs to control c. Cyclic
    multiplicative updates fit each target margin. Structural zeros remain
    zero; this adjusts seed weights and does not generate new records.
    """
    weights=np.asarray(seed_weights,dtype=float).copy()
    design=np.asarray(constraint_matrix,dtype=float)
    targets=np.asarray(target_margins,dtype=float)
    tol=float(tolerance)
    if weights.ndim!=1 or weights.size==0 or not np.all(np.isfinite(weights)) or np.any(weights<0):
        raise ValueError("seed_weights must be a non-empty finite non-negative vector")
    if design.ndim!=2 or design.shape[0]!=weights.size or design.shape[1]==0:
        raise ValueError("constraint_matrix must have one row per seed record and at least one column")
    if not np.all(np.isfinite(design)) or np.any((design!=0)&(design!=1)):
        raise ValueError("constraint_matrix must be finite and binary")
    if targets.ndim!=1 or targets.size!=design.shape[1] or not np.all(np.isfinite(targets)) or np.any(targets<0):
        raise ValueError("target_margins must be finite, non-negative and match constraint columns")
    if not np.isfinite(tol) or tol<=0 or not isinstance(max_iter,(int,np.integer)) or max_iter<1:
        raise ValueError("tolerance and max_iter must be positive")
    masks=[design[:,j]==1 for j in range(design.shape[1])]
    for j,mask in enumerate(masks):
        if not np.any(mask) and targets[j]>0: raise ValueError(f"control {j} has positive target but no seed records")
        if targets[j]>0 and not np.any(weights[mask]>0): raise ValueError(f"control {j} has positive target but zero seed support")
    converged=False; error=np.inf
    for iteration in range(1,int(max_iter)+1):
        for j,mask in enumerate(masks):
            current=float(weights[mask].sum()); target=targets[j]
            if target==0: weights[mask]=0.0
            elif current<=0: raise ValueError(f"control {j} lost all positive seed support during raking")
            else: weights[mask]*=target/current
        fitted=design.T@weights
        error=float(np.max(np.abs(fitted-targets)/np.maximum(1.0,targets)))
        if error<=tol: converged=True; break
    return {"weights":weights,"fitted_margins":design.T@weights,"target_margins":targets.copy(),
            "iterations":iteration,"max_relative_error":error,"converged":converged,
            "structural_zero_records":tuple(np.flatnonzero(weights==0).tolist()),
            "method":"iterative_proportional_fitting_raking"}
