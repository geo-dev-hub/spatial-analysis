from __future__ import annotations
from typing import Iterable
import numpy as np
from statsmodels.tsa.seasonal import STL

def stl_decompose(values: Iterable[float], period: int, *, seasonal: int = 7, trend: int | None = None, low_pass: int | None = None, robust: bool = False):
    """Wrapper around statsmodels STL; not an independent LOESS reimplementation."""
    y = np.asarray(list(values), dtype=float)
    if y.ndim != 1 or y.size < 3 or not np.isfinite(y).all():
        raise ValueError("values must be a finite one-dimensional series")
    if not isinstance(period, int) or period < 2 or y.size < 2 * period:
        raise ValueError("period must be >= 2 and at least two complete cycles are required")
    if not isinstance(seasonal, int) or seasonal < 3 or seasonal % 2 == 0:
        raise ValueError("seasonal must be an odd integer >= 3")
    if trend is not None and (not isinstance(trend, int) or trend < 3 or trend % 2 == 0):
        raise ValueError("trend must be an odd integer >= 3")
    if low_pass is not None and (not isinstance(low_pass, int) or low_pass < 3 or low_pass % 2 == 0):
        raise ValueError("low_pass must be an odd integer >= 3")
    fit = STL(y, period=period, seasonal=seasonal, trend=trend, low_pass=low_pass, robust=robust).fit()
    return {"trend": fit.trend.tolist(), "seasonal": fit.seasonal.tolist(), "resid": fit.resid.tolist(), "period": period, "robust": bool(robust)}
