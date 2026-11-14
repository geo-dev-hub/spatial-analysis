"""Bounded Gaussian column-plume inversion with fixed source and wind geometry."""
from __future__ import annotations
import numpy as np
from scipy.optimize import lsq_linear


def gaussian_column_kernel(x_coordinates, y_coordinates, source_x, source_y,
                           wind_speed_m_s, sigma_y0_m, dispersion_growth):
    """Return column enhancement per unit emission rate (s/m²).

    Coordinates are projected into downwind/crosswind axes. For downwind x>0,
    sigma_y=sqrt(sigma_y0²+(growth*x)²). The vertically integrated Gaussian
    kernel is exp(-y²/(2 sigma_y²))/(sqrt(2*pi)*U*sigma_y); upwind is zero.
    """
    x, y = np.asarray(x_coordinates, dtype=float), np.asarray(y_coordinates, dtype=float)
    if x.ndim != 2 or x.shape != y.shape or not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        raise ValueError("coordinate grids must be matching finite 2D arrays")
    sx, sy = float(source_x), float(source_y)
    wind, sigma0, growth = map(float, (wind_speed_m_s, sigma_y0_m, dispersion_growth))
    if not all(np.isfinite(v) for v in (sx, sy, wind, sigma0, growth)):
        raise ValueError("source, wind and dispersion parameters must be finite")
    if wind <= 0 or sigma0 <= 0 or growth < 0:
        raise ValueError("wind speed and initial dispersion must be positive; growth must be non-negative")
    downwind, crosswind = x - sx, y - sy
    sigma = np.sqrt(sigma0 * sigma0 + (growth * np.maximum(downwind, 0.0)) ** 2)
    kernel = np.exp(-0.5 * (crosswind / sigma) ** 2) / (np.sqrt(2.0 * np.pi) * wind * sigma)
    return np.where(downwind > 0, kernel, 0.0)


def invert_gaussian_plume(column_enhancement_kg_m2, x_coordinates, y_coordinates, *,
                          source_x, source_y, wind_speed_m_s, sigma_y0_m, dispersion_growth):
    """Fit non-negative Q (kg/s) and unconstrained constant background (kg/m²).

    Uses linear least squares with Q>=0. This fixed-geometry model does not
    estimate source location, wind direction, wind speed or dispersion.
    """
    observed = np.asarray(column_enhancement_kg_m2, dtype=float)
    if observed.ndim != 2 or not np.all(np.isfinite(observed)):
        raise ValueError("column enhancement must be a finite 2D array")
    kernel = gaussian_column_kernel(x_coordinates, y_coordinates, source_x, source_y,
                                    wind_speed_m_s, sigma_y0_m, dispersion_growth)
    if observed.shape != kernel.shape:
        raise ValueError("column and coordinate grids must have matching shapes")
    design = np.column_stack((kernel.ravel(), np.ones(kernel.size)))
    if np.linalg.matrix_rank(design) < 2:
        raise ValueError("inversion is not identifiable: plume kernel and background are collinear")
    fit = lsq_linear(design, observed.ravel(),
                     bounds=([0.0, -np.inf], [np.inf, np.inf]), method="trf")
    if not fit.success:
        raise RuntimeError(f"least-squares inversion failed: {fit.message}")
    q, background = map(float, fit.x)
    plume = q * kernel
    prediction = plume + background
    residual = observed - prediction
    return {
        "emission_rate_kg_s": q,
        "background_kg_m2": background,
        "plume_column_kg_m2": plume,
        "fitted_column_kg_m2": prediction,
        "residual_kg_m2": residual,
        "rms_residual_kg_m2": float(np.sqrt(np.mean(residual * residual))),
        "sample_count": int(observed.size),
        "solver_status": int(fit.status),
    }
