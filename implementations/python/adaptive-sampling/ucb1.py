"""UCB1 for independent stationary multi-armed bandits."""
from __future__ import annotations
import numpy as np

def select_ucb1_arm(counts,means,total_pulls):
    """Select the first unpulled arm, otherwise maximise mean+sqrt(2 log(t)/n)."""
    n=np.asarray(counts,dtype=int);m=np.asarray(means,dtype=float)
    if n.ndim!=1 or m.shape!=n.shape or n.size<1 or np.any(n<0) or not np.all(np.isfinite(m)):
        raise ValueError("counts and means must be finite 1D arrays of equal non-zero length")
    if not isinstance(total_pulls,int) or isinstance(total_pulls,bool) or total_pulls<0 or total_pulls!=int(n.sum()):
        raise ValueError("total_pulls must equal the non-negative sum of counts")
    untried=np.flatnonzero(n==0)
    if untried.size:return int(untried[0])
    if total_pulls<1:raise ValueError("at least one pull is required after initialisation")
    scores=m+np.sqrt(2.0*np.log(total_pulls)/n)
    return int(np.argmax(scores))

def run_ucb1(true_means,budget,noise_std=1.0,random_state=0):
    """Simulate UCB1 on Gaussian stationary arms; returns choices and diagnostics."""
    means=np.asarray(true_means,dtype=float)
    if means.ndim!=1 or means.size<1 or not np.all(np.isfinite(means)):
        raise ValueError("true_means must be a finite non-empty vector")
    if not isinstance(budget,int) or isinstance(budget,bool) or budget<1:
        raise ValueError("budget must be a positive integer")
    if not np.isfinite(noise_std) or noise_std<0:raise ValueError("noise_std must be finite and non-negative")
    rng=np.random.default_rng(random_state);counts=np.zeros(len(means),dtype=int)
    estimates=np.zeros(len(means),dtype=float);choices=[];observed=[]
    for t in range(budget):
        arm=select_ucb1_arm(counts,estimates,t)
        reward=float(rng.normal(means[arm],noise_std))
        counts[arm]+=1
        estimates[arm]+=(reward-estimates[arm])/counts[arm]
        choices.append(arm);observed.append(reward)
    return {"choices":choices,"rewards":observed,"counts":counts,"estimated_means":estimates}
