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
    if not np.isfinite(costs).all() or (costs < 0).any():
        raise ValueError("impedance values must be finite and non-negative")
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
