"""Fractions Skill Score for thresholded, regular 2D grids."""
from __future__ import annotations
from math import isfinite
from numbers import Real
from typing import Sequence


def _grid(values: Sequence[Sequence[Real]], name: str) -> list[list[float]]:
    try:
        rows = [list(row) for row in values]
    except TypeError as exc:
        raise ValueError(f"{name} must be a non-empty 2D grid") from exc
    if not rows or not rows[0]:
        raise ValueError(f"{name} must be a non-empty 2D grid")
    width = len(rows[0])
    result = []
    for row in rows:
        if len(row) != width:
            raise ValueError(f"{name} must be rectangular")
        converted = []
        for value in row:
            if isinstance(value, bool) or not isinstance(value, Real) or not isfinite(float(value)):
                raise ValueError(f"{name} values must be finite real numbers")
            converted.append(float(value))
        result.append(converted)
    return result


def _prefix_sum(binary: list[list[int]]) -> list[list[int]]:
    height, width = len(binary), len(binary[0])
    prefix = [[0] * (width + 1) for _ in range(height + 1)]
    for r in range(height):
        row_total = 0
        for c in range(width):
            row_total += binary[r][c]
            prefix[r + 1][c + 1] = prefix[r][c + 1] + row_total
    return prefix


def _rectangle_sum(prefix: list[list[int]], r0: int, c0: int, r1: int, c1: int) -> int:
    return prefix[r1][c1] - prefix[r0][c1] - prefix[r1][c0] + prefix[r0][c0]


def fractions_skill_score(
    observed: Sequence[Sequence[Real]],
    forecast: Sequence[Sequence[Real]],
    threshold: Real,
    window_size: int = 1,
    edge_policy: str = "truncate",
) -> float | None:
    """Calculate FSS for paired 2D fields thresholded at threshold.

    Windows are odd square widths in grid cells. truncate clips windows at
    edges; valid evaluates only centres with complete windows. Returns None
    when the score denominator is zero. Grid spacing, projection and masks
    must be handled by the caller.
    """
    obs, fcst = _grid(observed, "observed"), _grid(forecast, "forecast")
    if len(obs) != len(fcst) or len(obs[0]) != len(fcst[0]):
        raise ValueError("observed and forecast grids must have identical shapes")
    if isinstance(threshold, bool) or not isinstance(threshold, Real) or not isfinite(float(threshold)):
        raise ValueError("threshold must be a finite real number")
    if isinstance(window_size, bool) or not isinstance(window_size, int) or window_size < 1 or window_size % 2 == 0:
        raise ValueError("window_size must be a positive odd integer")
    if edge_policy not in {"truncate", "valid"}:
        raise ValueError("edge_policy must be 'truncate' or 'valid'")
    height, width, radius = len(obs), len(obs[0]), window_size // 2
    if edge_policy == "valid" and (height < window_size or width < window_size):
        raise ValueError("grid is smaller than a complete valid neighbourhood")
    obs_binary = [[int(v >= threshold) for v in row] for row in obs]
    fcst_binary = [[int(v >= threshold) for v in row] for row in fcst]
    op, fp = _prefix_sum(obs_binary), _prefix_sum(fcst_binary)
    rows = range(radius, height - radius) if edge_policy == "valid" else range(height)
    cols = range(radius, width - radius) if edge_policy == "valid" else range(width)
    numerator = denominator = 0.0
    for r in rows:
        r0, r1 = max(0, r-radius), min(height, r+radius+1)
        for c in cols:
            c0, c1 = max(0, c-radius), min(width, c+radius+1)
            area = (r1-r0) * (c1-c0)
            of = _rectangle_sum(op, r0, c0, r1, c1) / area
            pf = _rectangle_sum(fp, r0, c0, r1, c1) / area
            numerator += (pf-of) ** 2
            denominator += pf ** 2 + of ** 2
    return None if denominator == 0 else 1.0 - numerator / denominator
