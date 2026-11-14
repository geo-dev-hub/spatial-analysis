"""Transparent Theil–Sen robust linear trend estimator."""
from __future__ import annotations
from math import isfinite
from statistics import median
from typing import Iterable

def theil_sen(times: Iterable[float], values: Iterable[float]) -> dict[str, float | int]:
    """Return median pairwise slope and median residual intercept.

    Only pairs with distinct times contribute slopes. Inputs must be finite
    numeric values; time units determine the slope units. This is a point
    estimator, not an autocorrelation-adjusted significance test.
    """
    x=[float(v) for v in times]
    y=[float(v) for v in values]
    if len(x)!=len(y) or len(x)<2:
        raise ValueError("times and values must have equal length of at least two")
    if any(not isfinite(v) for v in x+y):
        raise ValueError("times and values must be finite")
    slopes=[(y[j]-y[i])/(x[j]-x[i])
            for i in range(len(x)) for j in range(i+1,len(x))
            if x[j]!=x[i]]
    if not slopes:
        raise ValueError("at least one pair must have distinct times")
    slope=float(median(slopes))
    intercept=float(median([yi-slope*xi for xi,yi in zip(x,y)]))
    return {"slope":slope,"intercept":intercept,"pair_count":len(slopes)}
