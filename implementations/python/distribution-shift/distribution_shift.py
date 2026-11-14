"""Kernel MMD and energy-distance two-sample statistics."""
from __future__ import annotations
import numpy as np
from scipy.spatial.distance import cdist

def _samples(x,y):
    a=np.asarray(x,dtype=float);b=np.asarray(y,dtype=float)
    if a.ndim!=2 or b.ndim!=2 or a.shape[1]!=b.shape[1] or min(a.shape[0],b.shape[0])<2:
        raise ValueError("samples must be 2D arrays with matching features and at least two rows each")
    if not np.all(np.isfinite(a)) or not np.all(np.isfinite(b)):raise ValueError("samples must be finite")
    return a,b

def _rbf(a,b,bandwidth):
    d2=cdist(a,b,metric="sqeuclidean")
    return np.exp(-d2/(2*bandwidth*bandwidth))

def mmd_squared(x,y,bandwidth):
    """Unbiased U-statistic estimate of squared MMD with a Gaussian RBF kernel.

    The finite-sample unbiased estimate can be negative; it is not clipped.
    """
    a,b=_samples(x,y);h=float(bandwidth)
    if not np.isfinite(h) or h<=0:raise ValueError("bandwidth must be finite and positive")
    kxx=_rbf(a,a,h);kyy=_rbf(b,b,h);kxy=_rbf(a,b,h)
    m,n=len(a),len(b)
    xx=(kxx.sum()-np.trace(kxx))/(m*(m-1))
    yy=(kyy.sum()-np.trace(kyy))/(n*(n-1))
    return float(xx+yy-2*kxy.mean())

def energy_distance(x,y):
    """Unbiased sample energy-distance statistic for Euclidean feature vectors."""
    a,b=_samples(x,y);m,n=len(a),len(b)
    dxx=cdist(a,a);dyy=cdist(b,b);dxy=cdist(a,b)
    xx=(dxx.sum()-np.trace(dxx))/(m*(m-1))
    yy=(dyy.sum()-np.trace(dyy))/(n*(n-1))
    return float(2*dxy.mean()-xx-yy)

def mmd_permutation_test(x,y,bandwidth,n_permutations=999,random_state=0):
    """Exchangeability-based permutation test for MMD; not spatial-block aware."""
    a,b=_samples(x,y)
    if not isinstance(n_permutations,int) or isinstance(n_permutations,bool) or n_permutations<1:
        raise ValueError("n_permutations must be a positive integer")
    observed=mmd_squared(a,b,bandwidth)
    combined=np.vstack((a,b));m=len(a);rng=np.random.default_rng(random_state)
    null=np.empty(n_permutations)
    for i in range(n_permutations):
        order=rng.permutation(len(combined))
        null[i]=mmd_squared(combined[order[:m]],combined[order[m:]],bandwidth)
    p=(1+np.count_nonzero(null>=observed))/(n_permutations+1)
    return {"statistic":observed,"p_value":float(p),"null_statistics":null}
