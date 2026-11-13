"""Teaching baseline for detecting events from daily SST and precomputed thresholds."""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class HeatwaveEvent:
    """One event interval; end_index is inclusive."""
    start_index: int
    end_index: int
    duration_days: int
    exceedance_days: int
    mean_intensity: float
    maximum_intensity: float
    cumulative_intensity: float


def detect_events(temperature, threshold, climatology, *, minimum_duration=5,
                  maximum_gap=2):
    """Detect daily threshold runs, then join qualifying runs over short cool gaps.

    Missing values break events and cannot be bridged. Inputs are daily, aligned
    one-dimensional arrays. Threshold and climatology are assumed precomputed.
    """
    arrays = [np.asarray(v, dtype=float) for v in
              (temperature, threshold, climatology)]
    if any(v.ndim != 1 for v in arrays):
        raise ValueError("Temperature, threshold and climatology must be 1D.")
    if len({v.size for v in arrays}) != 1:
        raise ValueError("All arrays must have the same length.")
    if not isinstance(minimum_duration, (int, np.integer)) or minimum_duration < 1:
        raise ValueError("minimum_duration must be a positive integer.")
    if not isinstance(maximum_gap, (int, np.integer)) or maximum_gap < 0:
        raise ValueError("maximum_gap must be a non-negative integer.")

    temp, thresh, clim = arrays
    valid = np.isfinite(temp) & np.isfinite(thresh) & np.isfinite(clim)
    hot = valid & (temp > thresh)
    padded = np.r_[False, hot, False].astype(np.int8)
    changes = np.diff(padded)
    starts = np.flatnonzero(changes == 1)
    ends = np.flatnonzero(changes == -1) - 1
    runs = [(int(a), int(b)) for a, b in zip(starts, ends)
            if b - a + 1 >= minimum_duration]
    if not runs:
        return []

    merged = [[runs[0][0], runs[0][1]]]
    for start, end in runs[1:]:
        previous_end = merged[-1][1]
        gap_start, gap_end = previous_end + 1, start - 1
        gap_length = start - previous_end - 1
        can_join = (gap_length <= maximum_gap
                    and np.all(valid[gap_start:gap_end + 1])
                    and not np.any(hot[gap_start:gap_end + 1]))
        if can_join:
            merged[-1][1] = end
        else:
            merged.append([start, end])

    events = []
    for start, end in merged:
        interval_valid = valid[start:end + 1]
        intensity = (temp[start:end + 1][interval_valid]
                     - clim[start:end + 1][interval_valid])
        events.append(HeatwaveEvent(
            start_index=start, end_index=end,
            duration_days=end - start + 1,
            exceedance_days=int(np.count_nonzero(hot[start:end + 1])),
            mean_intensity=float(np.mean(intensity)),
            maximum_intensity=float(np.max(intensity)),
            cumulative_intensity=float(np.sum(intensity)),
        ))
    return events
