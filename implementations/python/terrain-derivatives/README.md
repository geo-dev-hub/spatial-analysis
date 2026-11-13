# Horn 3×3 slope and aspect

This package estimates local terrain slope and downslope aspect from a regular elevation grid using Horn's 3×3 finite-difference operator.

## Install and test

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Contract

- Input is a 2D elevation array; finite values are valid and NaN marks NoData.
- Horizontal cell spacings are positive and in the same linear unit.
- z_factor converts elevation units into the horizontal unit; default 1 assumes matching units.
- Slope is returned in degrees and percent rise.
- Aspect is clockwise from north, points downslope, and lies in [0, 360). Flat cells have NaN aspect.
- The outer border is NaN because a complete 3×3 neighbourhood is required. Any window containing NoData is also NaN.
- The method assumes a regular grid in a suitable projected coordinate system. It does not reproject, resample, smooth or condition the DEM.

See the [canonical lesson](../../../algorithms/raster/slope-aspect.md) and [intern walkthrough](implementation-walkthrough.md).
