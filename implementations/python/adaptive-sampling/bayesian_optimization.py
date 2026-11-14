"""Gaussian-process upper-confidence-bound selection for candidate survey sites."""
from __future__ import annotations
import numpy as np

def _xy(values,name,allow_empty=False):
    a=np.asarray(values,dtype=float)
    if allow_empty and a.size==0:
        return np.empty((0,2),dtype=float)
    if a.ndim!=2 or a.shape[1]!=2 or (not allow_empty and a.shape[0]<1) or not np.all(np.isfinite(a)):
        raise ValueError(f"{name} must be a finite (n,2) coordinate array")
    return a

def _rbf(a,b,length_scale,signal_variance):
    delta=a[:,None,:]-b[None,:,:]
    d2=np.sum(delta*delta,axis=2)
    return signal_variance*np.exp(-0.5*d2/(length_scale*length_scale))

def gp_ucb_select(observed_coordinates,observed_values,candidate_coordinates,*,
                  length_scale,signal_variance=1.0,noise_variance=1e-6,
                  prior_mean=0.0,beta=2.0,jitter=1e-10):
    """Choose the candidate maximising GP-UCB = posterior mean + sqrt(beta)*std.

    Assumes a zero/constant-mean Gaussian process with isotropic RBF kernel,
    known hyperparameters and independent Gaussian observation noise. This
    is a candidate-set BO baseline, not a spatially nonstationary optimiser.
    """
    x=_xy(observed_coordinates,"observed_coordinates",allow_empty=True)
    c=_xy(candidate_coordinates,"candidate_coordinates")
    y=np.asarray(observed_values,dtype=float)
    if y.ndim!=1 or len(y)!=len(x) or not np.all(np.isfinite(y)):
        raise ValueError("observed_values must be a finite vector matching observed coordinates")
    params=(length_scale,signal_variance,noise_variance,prior_mean,beta,jitter)
    if any(not np.isfinite(float(v)) for v in params):raise ValueError("GP parameters must be finite")
    length_scale,signal_variance,noise_variance,prior_mean,beta,jitter=map(float,params)
    if length_scale<=0 or signal_variance<=0 or noise_variance<0 or beta<0 or jitter<=0:
        raise ValueError("length_scale/signal_variance/jitter must be positive; noise_variance/beta non-negative")
    if len(x)==0:
        mean=np.full(len(c),prior_mean)
        variance=np.full(len(c),signal_variance)
    else:
        K=_rbf(x,x,length_scale,signal_variance)
        K.flat[::len(K)+1]+=noise_variance+jitter
        L=np.linalg.cholesky(K)
        centered=y-prior_mean
        alpha=np.linalg.solve(L.T,np.linalg.solve(L,centered))
        cross=_rbf(x,c,length_scale,signal_variance)
        mean=prior_mean+cross.T@alpha
        v=np.linalg.solve(L,cross)
        variance=np.maximum(signal_variance-np.sum(v*v,axis=0),0.0)
    std=np.sqrt(variance)
    acquisition=mean+np.sqrt(beta)*std
    selected=int(np.argmax(acquisition))
    return {"selected_index":selected,"posterior_mean":mean,"posterior_std":std,
            "ucb":acquisition}
