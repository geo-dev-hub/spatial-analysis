"""Target-oriented leave-location-and-time-out cross-validation splits."""
from __future__ import annotations
import math
import numpy as np


def _factorize(values, name):
    """Factorize scalar hashable labels in first-seen order."""
    array = np.asarray(values, dtype=object)
    if array.ndim != 1:
        raise ValueError(f"{name} must be one-dimensional")
    codes = np.empty(array.size, dtype=int)
    labels, lookup = [], {}
    for index, value in enumerate(array):
        if value is None:
            raise ValueError(f"{name} cannot contain missing labels")
        try:
            hash(value)
        except TypeError as exc:
            raise ValueError(f"{name} labels must be hashable scalars") from exc
        try:
            missing = value != value
            if isinstance(missing, (bool, np.bool_)) and missing:
                raise ValueError(f"{name} cannot contain missing labels")
            if isinstance(value, (float, np.floating)) and not math.isfinite(float(value)):
                raise ValueError(f"{name} cannot contain non-finite labels")
            code = lookup.get(value)
        except ValueError:
            raise
        except Exception as exc:
            raise ValueError(f"{name} labels must be comparable scalars") from exc
        if code is None:
            code = len(labels)
            lookup[value] = code
            labels.append(value)
        codes[index] = code
    return codes, labels


def leave_location_and_time_out(location_ids, time_ids):
    """Return strict LLTO folds for categorical location and time groups.

    For each observed (location, time) pair, rows in that pair are test rows.
    Rows sharing either held-out dimension, but not both, form an excluded
    buffer. Training rows share neither held-out location nor held-out time.
    Every input row appears in exactly one test fold. Fold order follows the
    first appearance of each observed pair. Indices are zero-based arrays.

    This is a target-oriented LLTO design, not grouped k-fold, rolling-origin
    forecasting, or a distance-buffer method.
    """
    locations = np.asarray(location_ids, dtype=object)
    times = np.asarray(time_ids, dtype=object)
    if locations.ndim != 1 or times.ndim != 1:
        raise ValueError("location_ids and time_ids must be one-dimensional")
    if locations.size == 0 or locations.size != times.size:
        raise ValueError("location_ids and time_ids must be non-empty and equal length")
    loc_codes, loc_labels = _factorize(locations, "location_ids")
    time_codes, time_labels = _factorize(times, "time_ids")
    pairs = list(dict.fromkeys(zip(loc_codes.tolist(), time_codes.tolist())))
    all_indices = np.arange(locations.size, dtype=int)
    folds = []
    for fold_id, (loc_code, time_code) in enumerate(pairs):
        in_location = loc_codes == loc_code
        in_time = time_codes == time_code
        test_mask = in_location & in_time
        excluded_mask = in_location | in_time
        folds.append({
            "fold_id": fold_id,
            "location": loc_labels[loc_code],
            "time": time_labels[time_code],
            "train": all_indices[~excluded_mask],
            "test": all_indices[test_mask],
            "buffer": all_indices[excluded_mask & ~test_mask],
        })
    return folds
