"""Shannon, Simpson, multigroup entropy segregation and exposure statistics."""
from __future__ import annotations
import numpy as np

def _counts(values):
    x=np.asarray(values,dtype=float)
    if x.ndim!=2 or min(x.shape)<1 or not np.all(np.isfinite(x)) or np.any(x<0):
        raise ValueError("counts must be a finite non-negative 2D array")
    return x

def shannon_entropy(counts,axis=-1):
    """Shannon entropy of non-negative counts; zero-count categories contribute zero."""
    x=np.asarray(counts,dtype=float)
    if x.ndim<1 or not np.all(np.isfinite(x)) or np.any(x<0):raise ValueError("counts must be finite and non-negative")
    total=x.sum(axis=axis,keepdims=True)
    p=np.divide(x,total,out=np.zeros_like(x),where=total>0)
    terms=np.zeros_like(p);mask=p>0;terms[mask]=-p[mask]*np.log(p[mask])
    return terms.sum(axis=axis)

def simpson_concentration(counts,axis=-1):
    """Simpson concentration D=sum(p_i^2); larger means less diversity."""
    x=np.asarray(counts,dtype=float)
    if x.ndim<1 or not np.all(np.isfinite(x)) or np.any(x<0):raise ValueError("counts must be finite and non-negative")
    total=x.sum(axis=axis,keepdims=True)
    p=np.divide(x,total,out=np.zeros_like(x),where=total>0)
    return np.sum(p*p,axis=axis)

def reardon_firebaugh_entropy_index(counts):
    """Multigroup entropy index H=(E-E_bar)/E for areal group counts."""
    x=_counts(counts);unit=x.sum(axis=1);group=x.sum(axis=0);total=unit.sum()
    if np.any(unit<=0) or total<=0 or np.any(group<=0):raise ValueError("each unit and group must have positive total count")
    p=group/total
    entropy=-np.sum(p*np.log(p))
    if entropy<=0:return 0.0
    local=shannon_entropy(x,axis=1)
    average=np.sum((unit/total)*local)
    return float((entropy-average)/entropy)

def exposure_matrix(counts):
    """Return P*ij = sum_k (x_ik/X_i)*(x_jk/t_k).

    Rows index focal groups i; columns index exposed groups j. Units are
    unweighted areal units; no distance or adjacency weighting is applied.
    """
    x=_counts(counts);unit=x.sum(axis=1);group=x.sum(axis=0)
    if np.any(unit<=0) or np.any(group<=0):raise ValueError("each unit and group must have positive total count")
    within=x/unit[:,None]
    composition=x/group[None,:]
    return within.T@composition

def isolation_indices(counts):
    """Return the diagonal group isolation probabilities from exposure_matrix."""
    return np.diag(exposure_matrix(counts))
