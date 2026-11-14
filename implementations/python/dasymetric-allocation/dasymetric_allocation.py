"""Top-down population allocation using ancillary and building-level weights."""
from __future__ import annotations
import numpy as np

def dasymetric_allocate(source_totals, ancillary_weights, *, eligible_mask=None, zero_weight="error"):
    """Allocate source-zone totals to eligible targets by ancillary weight."""
    totals = np.asarray(source_totals, dtype=float)
    weights = np.asarray(ancillary_weights, dtype=float)
    if totals.ndim != 1 or totals.size == 0 or not np.all(np.isfinite(totals)) or np.any(totals < 0):
        raise ValueError("source_totals must be finite, non-negative and non-empty")
    if weights.ndim != 2 or weights.shape[0] != totals.size or weights.shape[1] == 0 or not np.all(np.isfinite(weights)) or np.any(weights < 0):
        raise ValueError("ancillary_weights must be a finite non-negative matrix with one row per source")
    if zero_weight not in {"error", "uniform"}:
        raise ValueError("zero_weight must be 'error' or 'uniform'")
    eligible = weights > 0 if eligible_mask is None else np.asarray(eligible_mask, dtype=bool)
    if eligible.shape != weights.shape or np.any((weights > 0) & ~eligible):
        raise ValueError("eligible_mask must match weights and include every positive weight")
    allocations = np.zeros_like(weights, dtype=float)
    fallback = []
    for i, total in enumerate(totals):
        if total == 0: continue
        mask = eligible[i]
        if not np.any(mask): raise ValueError(f"source row {i} has positive total but no eligible targets")
        w = weights[i, mask]
        if w.sum() > 0: shares = w / w.sum()
        elif zero_weight == "uniform":
            shares = np.full(mask.sum(), 1.0 / mask.sum()); fallback.append(i)
        else: raise ValueError(f"source row {i} has eligible targets but zero ancillary weight")
        allocations[i, mask] = total * shares
    return {"allocations": allocations, "target_totals": allocations.sum(axis=0),
            "source_totals_reconstructed": allocations.sum(axis=1),
            "uniform_fallback_rows": tuple(fallback),
            "allocation_method": "within_source_normalized_ancillary_weights"}

def building_based_allocate(source_totals, building_zone, floor_area, *, residential=None,
                            occupancy_factor=None, zero_weight="error"):
    """Allocate zone totals to buildings by eligible residential floor area.

    Weight = floor_area * occupancy_factor. Zone totals are conserved. The
    building-to-zone assignment and proxy variables are supplied by caller;
    this is an allocation, not a building-population observation.
    """
    totals = np.asarray(source_totals, dtype=float)
    zones = np.asarray(building_zone)
    area = np.asarray(floor_area, dtype=float)
    if totals.ndim != 1 or totals.size == 0 or not np.all(np.isfinite(totals)) or np.any(totals < 0):
        raise ValueError("source_totals must be a non-empty finite non-negative 1D array")
    if zones.ndim != 1 or area.ndim != 1 or zones.size == 0 or zones.shape != area.shape:
        raise ValueError("building_zone and floor_area must be matching non-empty 1D arrays")
    if not np.issubdtype(zones.dtype, np.integer) or np.any(zones < 0) or np.any(zones >= totals.size):
        raise ValueError("building_zone must contain valid integer source-zone indices")
    if not np.all(np.isfinite(area)) or np.any(area < 0):
        raise ValueError("floor_area must be finite and non-negative")
    eligible = np.ones(zones.size, dtype=bool) if residential is None else np.asarray(residential, dtype=bool)
    if eligible.shape != zones.shape: raise ValueError("residential must match building arrays")
    occupancy = np.ones(zones.size) if occupancy_factor is None else np.asarray(occupancy_factor, dtype=float)
    if occupancy.shape != zones.shape or not np.all(np.isfinite(occupancy)) or np.any(occupancy < 0):
        raise ValueError("occupancy_factor must be finite, non-negative and match buildings")
    if zero_weight not in {"error", "uniform"}: raise ValueError("zero_weight must be 'error' or 'uniform'")
    weights = area * occupancy
    allocation = np.zeros(zones.size, dtype=float)
    fallback = []
    for zone, total in enumerate(totals):
        if total == 0: continue
        mask = (zones == zone) & eligible
        count = int(mask.sum())
        if count == 0: raise ValueError(f"source zone {zone} has positive total but no eligible buildings")
        w = weights[mask]
        if w.sum() > 0: shares = w / w.sum()
        elif zero_weight == "uniform":
            shares = np.full(count, 1.0 / count); fallback.append(zone)
        else: raise ValueError(f"source zone {zone} has eligible buildings but zero residential floor-area weight")
        allocation[mask] = total * shares
    reconstructed = np.bincount(zones, weights=allocation, minlength=totals.size)
    return {"building_population": allocation, "zone_totals_reconstructed": reconstructed,
            "uniform_fallback_zones": tuple(fallback),
            "allocation_method": "residential_floor_area_times_occupancy_factor"}
