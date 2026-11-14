"""Ensemble forecast CRPS and expected rank histograms."""
from __future__ import annotations
from math import isfinite
from typing import Sequence

def _ensemble_inputs(observations:Sequence[float],ensemble:Sequence[Sequence[float]]):
    obs=[float(x) for x in observations]
    rows=[[float(x) for x in row] for row in ensemble]
    if not obs or len(obs)!=len(rows):raise ValueError("observations and ensemble must have the same non-zero case count")
    if any(not isfinite(x) for x in obs):raise ValueError("observations must be finite")
    if not rows[0] or any(len(row)!=len(rows[0]) for row in rows):raise ValueError("ensemble must be rectangular with at least one member")
    if any(not isfinite(x) for row in rows for x in row):raise ValueError("ensemble values must be finite")
    return obs,rows

def crps_ensemble(observations:Sequence[float],ensemble:Sequence[Sequence[float]])->list[float]:
    """Empirical-distribution CRPS per case using the pairwise ensemble formula."""
    obs,rows=_ensemble_inputs(observations,ensemble);scores=[]
    for y,row in zip(obs,rows):
        m=len(row)
        first=sum(abs(x-y) for x in row)/m
        second=sum(abs(a-b) for a in row for b in row)/(2*m*m)
        scores.append(first-second)
    return scores

def mean_crps_ensemble(observations:Sequence[float],ensemble:Sequence[Sequence[float]])->float:
    """Mean empirical ensemble CRPS across cases."""
    return sum(crps_ensemble(observations,ensemble))/len(observations)

def expected_rank_histogram(observations:Sequence[float],ensemble:Sequence[Sequence[float]])->list[float]:
    """Rank histogram with ties fractionally spread over all admissible ranks.

    For m exchangeable ensemble members, there are m+1 rank bins. When the
    observation ties k members, its one case is distributed equally across
    the k+1 possible insertion ranks. This is the expected randomized-tie
    histogram, deterministic and reproducible.
    """
    obs,rows=_ensemble_inputs(observations,ensemble)
    m=len(rows[0]);hist=[0.0]*(m+1)
    for y,row in zip(obs,rows):
        lower=sum(x<y for x in row);ties=sum(x==y for x in row)
        share=1.0/(ties+1)
        for rank in range(lower,lower+ties+1):hist[rank]+=share
    return hist
