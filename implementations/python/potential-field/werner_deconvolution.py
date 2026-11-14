"""Windowed 2D Werner thin-dike deconvolution for profile anomalies."""
from __future__ import annotations
import numpy as np


def werner_thin_dike_profile(x, *, x0, depth, amplitude_a, amplitude_b):
    """Evaluate the idealized 2D thin-dike profile used by Werner's model."""
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or x.size == 0 or not np.all(np.isfinite(x)):
        raise ValueError("x must be a non-empty finite 1D array")
    params = np.asarray([x0, depth, amplitude_a, amplitude_b], dtype=float)
    if not np.all(np.isfinite(params)) or depth <= 0:
        raise ValueError("parameters must be finite and depth must be positive")
    dx = x - float(x0)
    return (float(amplitude_a) * float(depth) + float(amplitude_b) * dx) / (dx * dx + float(depth) ** 2)


def werner_deconvolution_windows(x, anomaly, *, window_size=7, step=1,
                                  max_condition_number=1e12):
    """Solve overlapping linearized Werner thin-dike systems along a profile.

    The idealized anomaly is
        F(x) = [A h + B (x - x0)] / [(x - x0)^2 + h^2].
    Rearrangement gives
        x^2 F = a0 + a1 x + b0 F + b1 x F,
    where x0=b1/2, h=sqrt(-b0-x0^2), B=a1 and A=(a0+a1*x0)/h.
    Coordinates are centered and scaled within each window before solving to
    improve numerical conditioning; recovered positions/depths are returned
    in the original coordinate units.

    Windows with deficient rank, excessive condition number or non-positive
    recovered depth are reported as rejected. This basic single-thin-dike
    model expects a residual profile with regional background removed. It
    does not implement the thick-interface horizontal-gradient transform,
    polynomial interference model, multi-source clustering or Marquardt
    nonlinear refinement described in later Werner variants.
    """
    x = np.asarray(x, dtype=float)
    f = np.asarray(anomaly, dtype=float)
    if x.ndim != 1 or f.ndim != 1 or x.size != f.size or x.size < 4:
        raise ValueError("x and anomaly must be matching 1D arrays with at least four samples")
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(f)):
        raise ValueError("x and anomaly must be finite")
    if np.any(np.diff(x) <= 0):
        raise ValueError("x coordinates must be strictly increasing")
    if isinstance(window_size, bool) or not isinstance(window_size, (int, np.integer)) or window_size < 4:
        raise ValueError("window_size must be an integer of at least four")
    if isinstance(step, bool) or not isinstance(step, (int, np.integer)) or step < 1:
        raise ValueError("step must be a positive integer")
    limit = float(max_condition_number)
    if not np.isfinite(limit) or limit <= 1:
        raise ValueError("max_condition_number must be finite and greater than one")
    if window_size > x.size:
        raise ValueError("window_size cannot exceed the number of samples")

    solutions, rejected = [], []
    for start in range(0, x.size - window_size + 1, step):
        stop = start + window_size
        xw, fw = x[start:stop], f[start:stop]
        center = float(np.mean(xw))
        scale = float(np.ptp(xw))
        if scale <= 0:
            rejected.append({"start": start, "stop": stop, "reason": "zero_coordinate_span"})
            continue
        u = (xw - center) / scale
        design = np.column_stack((np.ones(window_size), u, fw, u * fw))
        target = u * u * fw
        condition = float(np.linalg.cond(design))
        if not np.isfinite(condition) or condition > limit:
            rejected.append({"start": start, "stop": stop, "reason": "ill_conditioned", "condition_number": condition})
            continue
        coefficients, _, rank, _ = np.linalg.lstsq(design, target, rcond=None)
        if rank < 4:
            rejected.append({"start": start, "stop": stop, "reason": "rank_deficient", "rank": int(rank)})
            continue
        a0, a1, b0, b1 = coefficients
        x0_scaled = b1 / 2.0
        depth_squared_scaled = -b0 - x0_scaled * x0_scaled
        if not np.isfinite(depth_squared_scaled) or depth_squared_scaled <= 0:
            rejected.append({"start": start, "stop": stop, "reason": "non_positive_depth"})
            continue
        depth_scaled = float(np.sqrt(depth_squared_scaled))
        depth = depth_scaled * scale
        x0 = center + float(x0_scaled) * scale
        amplitude_b = float(a1) * scale
        amplitude_a = float((a0 + a1 * x0_scaled) / depth_scaled) * scale
        fitted = (amplitude_a * depth + amplitude_b * (xw - x0)) / ((xw - x0) ** 2 + depth ** 2)
        solutions.append({
            "start": start,
            "stop": stop,
            "x0": float(x0),
            "depth": float(depth),
            "amplitude_a": amplitude_a,
            "amplitude_b": amplitude_b,
            "condition_number": condition,
            "profile_rmse": float(np.sqrt(np.mean((fitted - fw) ** 2))),
        })
    return {"solutions": solutions, "rejected_windows": rejected,
            "window_size": int(window_size), "step": int(step),
            "model": "single_2d_thin_dike_no_background"}
