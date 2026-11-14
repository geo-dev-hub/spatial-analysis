"""Distributional diagnostics for non-negative spatial accessibility values."""
from __future__ import annotations
import math


def _validated(values, weights=None):
    x = [float(v) for v in values]
    if not x or any(not math.isfinite(v) or v < 0 for v in x):
        raise ValueError("values must be a non-empty sequence of finite non-negative numbers")
    w = [1.0] * len(x) if weights is None else [float(v) for v in weights]
    if len(w) != len(x) or any(not math.isfinite(v) or v < 0 for v in w):
        raise ValueError("weights must be finite, non-negative and match values")
    if math.fsum(w) <= 0:
        raise ValueError("weights must have a positive total")
    return x, w


def weighted_lorenz_curve(values, weights=None):
    """Return cumulative population and accessibility shares, including (0, 0)."""
    x, w = _validated(values, weights)
    pairs = sorted((a, b) for a, b in zip(x, w) if b > 0)
    tw, tx = math.fsum(b for _, b in pairs), math.fsum(a*b for a, b in pairs)
    pop, access, cw, cx = [0.0], [0.0], 0.0, 0.0
    for a, b in pairs:
        cw += b
        cx += a*b
        pop.append(cw/tw)
        access.append(cw/tw if tx == 0 else cx/tx)
    return pop, access


def weighted_gini(values, weights=None):
    """Population-weighted Gini from the trapezoid area under the Lorenz curve."""
    pop, access = weighted_lorenz_curve(values, weights)
    area2 = math.fsum((pop[i]-pop[i-1])*(access[i]+access[i-1]) for i in range(1, len(pop)))
    return min(1.0, max(0.0, 1.0-area2))


def weighted_quantile(values, quantile, weights=None):
    """Inverse empirical-CDF weighted quantile."""
    if not math.isfinite(float(quantile)) or not 0 <= quantile <= 1:
        raise ValueError("quantile must be between 0 and 1")
    x, w = _validated(values, weights)
    pairs = sorted((a, b) for a, b in zip(x, w) if b > 0)
    target = quantile * math.fsum(b for _, b in pairs)
    cumulative = 0.0
    for a, b in pairs:
        cumulative += b
        if cumulative >= target:
            return a
    return pairs[-1][0]


def accessibility_summary(values, population_weights=None, minimum_threshold=None):
    """Return weighted mean, Gini, lower-tail quantiles and optional shortfall share."""
    x, w = _validated(values, population_weights)
    total = math.fsum(w)
    result = {
        "weighted_mean": math.fsum(a*b for a, b in zip(x, w))/total,
        "weighted_gini": weighted_gini(x, w),
        "p10": weighted_quantile(x, .10, w),
        "median": weighted_quantile(x, .50, w),
        "p90": weighted_quantile(x, .90, w),
        "minimum": min(a for a, b in zip(x, w) if b > 0),
        "maximum": max(a for a, b in zip(x, w) if b > 0),
    }
    if minimum_threshold is not None:
        t = float(minimum_threshold)
        if not math.isfinite(t) or t < 0:
            raise ValueError("minimum_threshold must be finite and non-negative")
        result["population_share_below_threshold"] = math.fsum(
            b for a, b in zip(x, w) if a < t
        ) / total
    return result


def group_accessibility_summary(values, groups, population_weights=None):
    """Return weighted summaries for caller-supplied group labels."""
    x, w = _validated(values, population_weights)
    if len(groups) != len(x):
        raise ValueError("groups must match values")
    buckets = {}
    for a, group, weight in zip(x, groups, w):
        key = str(group)
        buckets.setdefault(key, ([], []))
        buckets[key][0].append(a)
        buckets[key][1].append(weight)
    return {key: accessibility_summary(a, b)
            for key, (a, b) in sorted(buckets.items()) if math.fsum(b) > 0}


def group_mean_gap(group_summaries):
    """Return the max-minus-min group mean and the min/max ratio."""
    if not group_summaries:
        raise ValueError("group_summaries must not be empty")
    means = {k: float(v["weighted_mean"]) for k, v in group_summaries.items()}
    if any(not math.isfinite(v) or v < 0 for v in means.values()):
        raise ValueError("group means must be finite and non-negative")
    low, high = min(means, key=means.get), max(means, key=means.get)
    lo, hi = means[low], means[high]
    return {"lowest_mean_group": low, "highest_mean_group": high,
            "absolute_gap": hi-lo, "lowest_to_highest_ratio": 1.0 if hi == 0 else lo/hi}
