# Raster resampling: nearest neighbour and bilinear interpolation

This teaching implementation resamples a 2D array to a new shape over the same extent and orientation. It implements nearest-neighbour and bilinear methods, not a full geospatial warp.

## Install and test

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Method selection

- Nearest neighbour copies the closest source cell. It preserves categorical labels and class codes, but can create blocky continuous surfaces.
- Bilinear interpolation forms a weighted average of the four surrounding source samples. It is appropriate for many continuous surfaces, but should not be used for nominal categories.

## NoData policy

Bilinear interpolation offers two explicit policies:
- strict: if any neighbour with positive interpolation weight is NoData, the output is NoData;
- renormalize: ignore missing neighbours and renormalize the remaining weights.

Nearest neighbour returns NoData when the selected source cell is non-finite. All non-finite source values are treated as NoData.

## Scope and limitations

- Target and source grids cover the same extent and orientation; only the output shape changes.
- The implementation does not use CRS transformations, affine georeferencing, reprojection, rotated grids or antialiasing.
- Cubic convolution, Lanczos and area-weighted aggregation are not implemented.
- Bilinear interpolation changes values and may smooth extremes. Nearest neighbour is generally preferred for categorical rasters.
- A production workflow must preserve the full transform, CRS, pixel alignment and resampling metadata.

See the [canonical lesson](../../../algorithms/raster/resampling.md) and [intern walkthrough](implementation-walkthrough.md).
