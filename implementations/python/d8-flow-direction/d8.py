"""Teaching implementation of single-direction D8 flow routing.

This version does not fill depressions or resolve flats. Direction codes use
the ESRI-style powers-of-two convention.
"""
from math import isfinite, hypot
from typing import Sequence

# Row/column offsets, direction codes, ordered clockwise from east.
DIRECTIONS = (
    (0, 1, 1),
    (1, 1, 2),
    (1, 0, 4),
    (1, -1, 8),
    (0, -1, 16),
    (-1, -1, 32),
    (-1, 0, 64),
    (-1, 1, 128),
)


def flow_direction(dem: Sequence[Sequence[float | None]], *,
                   cell_width: float = 1.0,
                   cell_height: float = 1.0) -> list[list[int | None]]:
    """Return D8 direction codes for a rectangular DEM.

    A cell with no strictly lower valid neighbour receives 0. A NoData cell
    (represented by None) remains None. Equal maximum gradients are resolved
    by the fixed order in DIRECTIONS.
    """
    if not dem or not dem[0]:
        raise ValueError("DEM must contain at least one row and column")
    columns = len(dem[0])
    if any(len(row) != columns for row in dem):
        raise ValueError("DEM rows must have equal length")

    width, height = float(cell_width), float(cell_height)
    if not isfinite(width) or width <= 0:
        raise ValueError("cell_width must be finite and positive")
    if not isfinite(height) or height <= 0:
        raise ValueError("cell_height must be finite and positive")

    values: list[list[float | None]] = []
    for row in dem:
        clean_row = []
        for value in row:
            if value is None:
                clean_row.append(None)
            else:
                number = float(value)
                if not isfinite(number):
                    raise ValueError("elevation values must be finite or None")
                clean_row.append(number)
        values.append(clean_row)

    rows = len(values)
    result: list[list[int | None]] = [[None] * columns for _ in range(rows)]
    for r in range(rows):
        for c in range(columns):
            elevation = values[r][c]
            if elevation is None:
                continue
            best_slope = 0.0
            best_code = 0
            for dr, dc, code in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < columns):
                    continue
                neighbour = values[nr][nc]
                if neighbour is None:
                    continue
                distance = hypot(dc * width, dr * height)
                slope = (elevation - neighbour) / distance
                if slope > best_slope:
                    best_slope = slope
                    best_code = code
            result[r][c] = best_code
    return result
