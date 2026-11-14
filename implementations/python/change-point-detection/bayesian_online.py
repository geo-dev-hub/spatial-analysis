"""Bayesian online change-point detection with a Gaussian known-variance model."""
from __future__ import annotations
from math import exp, isfinite, log, log1p, pi

def _logsumexp(values):
    peak=max(values)
    return peak+log(sum(exp(x-peak) for x in values))

def _log_normal_pdf(y,mean,variance):
    return -0.5*(log(2*pi*variance)+(y-mean)**2/variance)

def bayesian_online_changepoint(values,hazard,observation_variance,prior_mean=0.0,prior_variance=1.0):
    """Adams–MacKay run-length recursion for unknown mean, known noise variance.

    Uses a Normal prior for each segment mean, known Gaussian observation
    variance and a constant hazard. Returns run-length posterior, probability
    of a change at each observation, and MAP run length.
    """
    data=[float(x) for x in values]
    params=[hazard,observation_variance,prior_mean,prior_variance]
    if not data or any(not isfinite(x) for x in data):raise ValueError("values must be non-empty and finite")
    if any(not isfinite(float(x)) for x in params):raise ValueError("parameters must be finite")
    hazard,observation_variance,prior_mean,prior_variance=map(float,params)
    if not 0<hazard<1:raise ValueError("hazard must be strictly between 0 and 1")
    if observation_variance<=0 or prior_variance<=0:raise ValueError("variances must be positive")
    run_probs=[1.0];means=[prior_mean];variances=[prior_variance]
    rows=[];change_probs=[];map_runs=[]
    for y in data:
        prior_predictive=_log_normal_pdf(y,prior_mean,observation_variance+prior_variance)
        cp_log=_logsumexp([log(p)+log(hazard)+prior_predictive for p in run_probs if p>0])
        growth_logs=[(log(p) if p>0 else float("-inf"))+log1p(-hazard)+_log_normal_pdf(y,m,observation_variance+v)
                     for p,m,v in zip(run_probs,means,variances)]
        log_masses=[cp_log]+growth_logs
        normalizer=_logsumexp(log_masses)
        run_probs=[exp(x-normalizer) for x in log_masses]
        def update(m,v):
            post_v=1.0/(1.0/v+1.0/observation_variance)
            return post_v*(m/v+y/observation_variance),post_v
        m0,v0=update(prior_mean,prior_variance)
        updated=[update(m,v) for m,v in zip(means,variances)]
        means=[m0]+[m for m,v in updated]
        variances=[v0]+[v for m,v in updated]
        rows.append(run_probs[:]);change_probs.append(run_probs[0])
        map_runs.append(max(range(len(run_probs)),key=run_probs.__getitem__))
    width=max(map(len,rows))
    posterior=[[row[i] if i<len(row) else 0.0 for i in range(width)] for row in rows]
    return {"run_length_posterior":posterior,"change_probability":change_probs,"map_run_length":map_runs}
