"""Hierarchical spatial generalisation with k-sized location equivalence groups."""
from __future__ import annotations
import numpy as np


def spatial_k_anonymity(x_coordinates, y_coordinates, k, *, max_depth=8):
    """Generalise points into disjoint quadtree cells containing at least k records.

    The root is a padded square covering the supplied points. A cell is split
    only when every non-empty child contains at least k records; otherwise all
    records in that cell are generalised to the parent cell. If the root has
    fewer than k records, all records are suppressed.

    This is location-only k-anonymity. Other released quasi-identifiers,
    attributes, linkage risks and the choice of population are not addressed.
    """
    x = np.asarray(x_coordinates, dtype=float)
    y = np.asarray(y_coordinates, dtype=float)
    if x.ndim != 1 or y.ndim != 1 or x.shape != y.shape or x.size == 0:
        raise ValueError("x and y must be matching non-empty 1D coordinate arrays")
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        raise ValueError("coordinates must be finite")
    if isinstance(k, bool) or not isinstance(k, (int, np.integer)) or k < 1:
        raise ValueError("k must be a positive integer")
    if isinstance(max_depth, bool) or not isinstance(max_depth, (int, np.integer)) or max_depth < 0:
        raise ValueError("max_depth must be a non-negative integer")

    assignments = np.full(x.size, -1, dtype=int)
    if x.size < k:
        return {"group_ids": assignments, "suppressed": assignments < 0, "groups": [],
                "k": int(k), "max_depth": int(max_depth)}

    xmin, xmax = float(x.min()), float(x.max())
    ymin, ymax = float(y.min()), float(y.max())
    width = max(xmax - xmin, ymax - ymin)
    if width == 0:
        width = 1.0
    cx, cy = (xmin + xmax) / 2.0, (ymin + ymax) / 2.0
    half = width / 2.0
    root = (cx - half, cy - half, cx + half, cy + half)
    groups = []

    def emit(indices, bounds, depth):
        group_id = len(groups)
        assignments[indices] = group_id
        groups.append({
            "group_id": group_id,
            "count": int(indices.size),
            "bounds": tuple(float(v) for v in bounds),
            "depth": int(depth),
        })

    def visit(indices, bounds, depth):
        if indices.size < k:
            return False
        if depth >= max_depth:
            emit(indices, bounds, depth)
            return True
        x0, y0, x1, y1 = bounds
        mx, my = (x0 + x1) / 2.0, (y0 + y1) / 2.0
        right, top = x[indices] >= mx, y[indices] >= my
        masks = (~right & ~top, right & ~top, ~right & top, right & top)
        children = [indices[mask] for mask in masks]
        nonempty = [child for child in children if child.size]
        if any(child.size < k for child in nonempty):
            emit(indices, bounds, depth)
            return True
        child_bounds = (
            (x0, y0, mx, my), (mx, y0, x1, my),
            (x0, my, mx, y1), (mx, my, x1, y1),
        )
        for child, child_box in zip(children, child_bounds):
            if child.size:
                visit(child, child_box, depth + 1)
        return True

    visit(np.arange(x.size, dtype=int), root, 0)
    return {"group_ids": assignments, "suppressed": assignments < 0,
            "groups": groups, "k": int(k), "max_depth": int(max_depth)}
