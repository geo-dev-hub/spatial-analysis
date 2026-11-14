"""Binary-catchment two-step floating catchment area accessibility."""
from __future__ import annotations

from math import isfinite

import numpy as np


def two_step_fca(
    impedance: list[list[float]] | np.ndarray,
    provider_supply: list[float] | np.ndarray,
    population_demand: list[float] | np.ndarray,
    *,
    max_cost: float,
) -> tuple[list[float], list[float]]:
    """Return (provider supply/demand ratios, accessibility by population site).

    Matrix rows are population locations and columns are providers. The
    catchment includes impedance values <= max_cost. Providers with no
    population in their catchment receive a zero ratio.
    """
    costs = np.asarray(impedance, dtype=float)
    supply = np.asarray(provider_supply, dtype=float)
    demand = np.asarray(population_demand, dtype=float)

    if costs.ndim != 2 or costs.shape[0] == 0 or costs.shape[1] == 0:
        raise ValueError("impedance must be a non-empty 2D matrix")
    if np.isnan(costs).any() or np.isneginf(costs).any() or (costs < 0).any():
        raise ValueError("impedance values must be non-negative and cannot be NaN or negative infinity")
    if supply.shape != (costs.shape[1],):
        raise ValueError("provider_supply must have one value per provider column")
    if demand.shape != (costs.shape[0],):
        raise ValueError("population_demand must have one value per population row")
    if not np.isfinite(supply).all() or (supply < 0).any():
        raise ValueError("provider_supply must be finite and non-negative")
    if not np.isfinite(demand).all() or (demand < 0).any():
        raise ValueError("population_demand must be finite and non-negative")
    if not (demand > 0).any():
        raise ValueError("population_demand must contain at least one positive value")
    if not isfinite(max_cost) or max_cost <= 0:
        raise ValueError("max_cost must be finite and greater than zero")

    catchment = costs <= max_cost
    demand_in_catchment = catchment.T @ demand
    ratios = np.divide(
        supply,
        demand_in_catchment,
        out=np.zeros_like(supply, dtype=float),
        where=demand_in_catchment > 0,
    )
    accessibility = catchment @ ratios
    return ratios.tolist(), accessibility.tolist()



def two_step_fca_distance_decay(
    impedance: list[list[float]] | np.ndarray,
    provider_supply: list[float] | np.ndarray,
    population_demand: list[float] | np.ndarray,
    *,
    band_upper_bounds: list[float] | tuple[float, ...],
    band_weights: list[float] | tuple[float, ...],
) -> tuple[list[float], list[float]]:
    """Return E2SFCA-style provider ratios and population accessibility.

    Both steps use the same user-supplied, piecewise-constant distance-decay
    function. Band upper bounds are inclusive, strictly increasing impedance
    limits; the final bound is the maximum catchment. Weights must be finite,
    non-negative and non-increasing. Pairs beyond the final bound receive
    weight zero. Rows are population locations; columns are providers.
    """
    costs = np.asarray(impedance, dtype=float)
    supply = np.asarray(provider_supply, dtype=float)
    demand = np.asarray(population_demand, dtype=float)
    bounds = np.asarray(band_upper_bounds, dtype=float)
    weights = np.asarray(band_weights, dtype=float)

    if costs.ndim != 2 or costs.shape[0] == 0 or costs.shape[1] == 0:
        raise ValueError("impedance must be a non-empty 2D matrix")
    if np.isnan(costs).any() or np.isneginf(costs).any() or (costs < 0).any():
        raise ValueError("impedance values must be non-negative and cannot be NaN or negative infinity")
    if supply.shape != (costs.shape[1],):
        raise ValueError("provider_supply must have one value per provider column")
    if demand.shape != (costs.shape[0],):
        raise ValueError("population_demand must have one value per population row")
    if not np.isfinite(supply).all() or (supply < 0).any():
        raise ValueError("provider_supply must be finite and non-negative")
    if not np.isfinite(demand).all() or (demand < 0).any():
        raise ValueError("population_demand must be finite and non-negative")
    if not (demand > 0).any():
        raise ValueError("population_demand must contain at least one positive value")
    if bounds.ndim != 1 or bounds.size == 0 or not np.isfinite(bounds).all():
        raise ValueError("band_upper_bounds must be a non-empty finite sequence")
    if weights.shape != bounds.shape or not np.isfinite(weights).all():
        raise ValueError("band_weights must be finite and match band_upper_bounds")
    if (bounds <= 0).any() or (np.diff(bounds) <= 0).any():
        raise ValueError("band_upper_bounds must be positive and strictly increasing")
    if (weights < 0).any() or (np.diff(weights) > 0).any():
        raise ValueError("band_weights must be non-negative and non-increasing")

    band_index = np.searchsorted(bounds, costs, side="left")
    in_catchment = band_index < len(bounds)
    weight_matrix = np.zeros_like(costs, dtype=float)
    rows, cols = np.nonzero(in_catchment)
    weight_matrix[rows, cols] = weights[band_index[rows, cols]]

    weighted_demand = weight_matrix.T @ demand
    ratios = np.divide(
        supply,
        weighted_demand,
        out=np.zeros_like(supply, dtype=float),
        where=weighted_demand > 0,
    )
    accessibility = weight_matrix @ ratios
    return ratios.tolist(), accessibility.tolist()
