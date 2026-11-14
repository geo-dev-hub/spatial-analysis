"""Detect long reporting gaps and implausible jumps in vessel AIS tracks."""
from __future__ import annotations
import math
from collections import defaultdict
import numpy as np

EARTH_RADIUS_NM = 3440.065


def haversine_distance_nm(lon1, lat1, lon2, lat2):
    """Great-circle distance between longitude/latitude pairs in nautical miles."""
    values = np.asarray([lon1, lat1, lon2, lat2], dtype=float)
    if not np.all(np.isfinite(values)):
        raise ValueError("coordinates must be finite")
    if not (-180 <= lon1 <= 180 and -180 <= lon2 <= 180):
        raise ValueError("longitude must be in [-180, 180]")
    if not (-90 <= lat1 <= 90 and -90 <= lat2 <= 90):
        raise ValueError("latitude must be in [-90, 90]")
    lon1, lat1, lon2, lat2 = np.deg2rad(values)
    dlon, dlat = lon2 - lon1, lat2 - lat1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    return float(2 * EARTH_RADIUS_NM * np.arcsin(np.sqrt(np.clip(a, 0.0, 1.0))))


def detect_ais_gaps(vessel_ids, timestamps_seconds, longitudes, latitudes, *,
                    max_gap_seconds=1800.0, max_speed_knots=60.0):
    """Return adjacent-report segments violating temporal or speed thresholds.

    Input timestamps are numeric Unix seconds (or another common seconds
    scale); longitude/latitude are decimal degrees. Rows are grouped by vessel
    and stably sorted by timestamp. A segment is flagged when its elapsed time
    is strictly greater than max_gap_seconds and/or its great-circle implied
    speed is strictly greater than max_speed_knots. Flags are independent.

    The function identifies suspicious reporting intervals, not proof of AIS
    malfunction, deliberate disabling, illegal activity or vessel identity
    fraud. Thresholds must reflect vessel class, reporting mode and study area.
    """
    ids = np.asarray(vessel_ids, dtype=object)
    times = np.asarray(timestamps_seconds, dtype=float)
    lon = np.asarray(longitudes, dtype=float)
    lat = np.asarray(latitudes, dtype=float)
    arrays = (ids, times, lon, lat)
    if any(a.ndim != 1 for a in arrays) or len({a.size for a in arrays}) != 1 or ids.size < 2:
        raise ValueError("all inputs must be matching one-dimensional arrays with at least two rows")
    if not np.all(np.isfinite(times)) or not np.all(np.isfinite(lon)) or not np.all(np.isfinite(lat)):
        raise ValueError("timestamps and coordinates must be finite")
    if np.any((lon < -180) | (lon > 180)) or np.any((lat < -90) | (lat > 90)):
        raise ValueError("longitude/latitude outside geographic bounds")
    gap_limit = float(max_gap_seconds)
    speed_limit = float(max_speed_knots)
    if not np.isfinite(gap_limit) or gap_limit <= 0:
        raise ValueError("max_gap_seconds must be finite and positive")
    if not np.isfinite(speed_limit) or speed_limit <= 0:
        raise ValueError("max_speed_knots must be finite and positive")

    grouped = defaultdict(list)
    for index, vessel in enumerate(ids):
        if vessel is None:
            raise ValueError("vessel identifiers cannot be missing")
        try:
            hash(vessel)
        except TypeError as exc:
            raise ValueError("vessel identifiers must be hashable") from exc
        grouped[vessel].append(index)

    findings = []
    for vessel, indices in grouped.items():
        ordered = sorted(indices, key=lambda i: (times[i], i))
        for previous, current in zip(ordered[:-1], ordered[1:]):
            elapsed = float(times[current] - times[previous])
            if elapsed <= 0:
                raise ValueError(f"vessel {vessel!r} has duplicate or non-increasing timestamps")
            distance = haversine_distance_nm(lon[previous], lat[previous], lon[current], lat[current])
            speed = distance / (elapsed / 3600.0)
            flags = []
            if elapsed > gap_limit:
                flags.append("long_reporting_gap")
            if speed > speed_limit:
                flags.append("implausible_implied_speed")
            if flags:
                findings.append({
                    "vessel_id": vessel,
                    "from_index": int(previous),
                    "to_index": int(current),
                    "elapsed_seconds": elapsed,
                    "distance_nm": distance,
                    "implied_speed_knots": speed,
                    "flags": tuple(flags),
                })
    return findings
