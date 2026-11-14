"""Threshold-integrated Brier decomposition of ensemble CRPS.

This is a finite-threshold quadrature of the CRPS-as-integrated-Brier-score
identity, with a Murphy reliability/resolution/uncertainty decomposition at
each threshold. It is not the exact bin-width Hersbach (2000) estimator.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import trapezoid
from ensemble_verification import _ensemble_inputs


def _brier_decomposition(observed_event, probabilities):
    obs=np.asarray(observed_event,dtype=float)
    probs=np.asarray(probabilities,dtype=float)
    climatology=float(obs.mean())
    reliability=0.0
    resolution=0.0
    for p in np.unique(probs):
        mask=probs==p
        weight=float(mask.mean())
        observed_frequency=float(obs[mask].mean())
        reliability+=weight*(float(p)-observed_frequency)**2
        resolution+=weight*(observed_frequency-climatology)**2
    uncertainty=climatology*(1.0-climatology)
    score=float(np.mean((probs-obs)**2))
    return {"brier_score":score,"reliability":reliability,
            "resolution":resolution,"uncertainty":uncertainty,
            "decomposition_residual":score-(reliability-resolution+uncertainty)}


def crps_brier_decomposition(observations, ensemble, *, thresholds=None,
                             n_thresholds=501):
    """Approximate mean ensemble CRPS and decompose it by threshold.

    At each threshold z, forecast event probability is the ensemble fraction
    exceeding z and the verifying event is 1[y > z]. The Brier decomposition
    is integrated over z with trapezoidal quadrature. Returns REL - RES + UNC,
    plus the direct integrated Brier score and the threshold grid.
    """
    obs,rows=_ensemble_inputs(observations,ensemble)
    y=np.asarray(obs,dtype=float)
    x=np.asarray(rows,dtype=float)
    if thresholds is None:
        if not isinstance(n_thresholds,(int,np.integer)) or n_thresholds<2:
            raise ValueError("n_thresholds must be an integer >= 2")
        lo=float(min(y.min(),x.min())); hi=float(max(y.max(),x.max()))
        if lo==hi:
            grid=np.array([lo,hi+1.0],dtype=float)
            # A degenerate common constant forecast has zero score and no
            # threshold interval with non-zero contribution.
            return {"crps":0.0,"direct_integrated_brier":0.0,
                    "reliability":0.0,"resolution":0.0,"uncertainty":0.0,
                    "decomposition_residual":0.0,"thresholds":grid,
                    "quadrature":"trapezoid"}
        grid=np.linspace(lo,hi,int(n_thresholds))
    else:
        grid=np.asarray(thresholds,dtype=float)
        if grid.ndim!=1 or grid.size<2 or not np.all(np.isfinite(grid)) or np.any(np.diff(grid)<=0):
            raise ValueError("thresholds must be a finite strictly increasing 1D array with >=2 values")
    components={k:[] for k in ("brier_score","reliability","resolution","uncertainty","decomposition_residual")}
    for z in grid:
        event=(y>z).astype(float)
        probability=np.mean(x>z,axis=1)
        part=_brier_decomposition(event,probability)
        for key in components: components[key].append(part[key])
    integrated={key:float(trapezoid(values,grid)) for key,values in components.items()}
    return {"crps":integrated["reliability"]-integrated["resolution"]+integrated["uncertainty"],
            "direct_integrated_brier":integrated["brier_score"],
            "reliability":integrated["reliability"],
            "resolution":integrated["resolution"],
            "uncertainty":integrated["uncertainty"],
            "decomposition_residual":integrated["decomposition_residual"],
            "thresholds":grid,"quadrature":"trapezoid"}
