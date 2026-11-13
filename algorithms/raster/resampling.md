# Raster resampling: nearest neighbour and bilinear interpolation

Stable ID: SA-RASTER-RESAMPLING-NEAREST-BILINEAR · Draft 0.1 · Source compendium section 4, page 6

## Why resampling is a modelling choice

Raster grids often need to be brought onto a common cell size, alignment or shape. Resampling estimates values at new cell centres from the source grid. It changes the sampled surface; it is not merely a file-format conversion.

Two common methods have different semantics:

- **Nearest neighbour** copies the closest source cell. It preserves categorical class codes and is usually appropriate for nominal rasters.
- **Bilinear interpolation** forms a weighted average of four surrounding samples. It is often suitable for continuous variables, but smooths local extremes and is not appropriate for nominal categories.

## Same-extent grid mapping

The [teaching implementation](../../implementations/python/raster-resampling/README.md) changes the array shape while keeping the same extent and orientation. Target pixel centres map to fractional source pixel-centre coordinates:

$$r_s=\left(r_t+\frac12\right)\frac{N_r}{M_r}-\frac12$$

$$c_s=\left(c_t+\frac12\right)\frac{N_c}{M_c}-\frac12$$

where N is the source dimension and M is the target dimension. This is deliberately narrower than a geospatial warp.

## Bilinear weights

For fractional row and column offsets fr and fc, the four interpolation weights are:

$$
(1-f_r)(1-f_c),\quad (1-f_r)f_c,\quad f_r(1-f_c),\quad f_rf_c
$$

The output is the weighted average of the available samples. The implementation offers two NoData policies: strict masking if any positive-weight neighbour is missing, or renormalization over the valid neighbours.

## Choosing a method

| Data meaning | Typical choice | Reason |
|---|---|---|
| Land-cover class, soil type, administrative code | Nearest neighbour | Do not invent fractional category values |
| Elevation, temperature, reflectance | Bilinear may be suitable | Continuous interpolation can be meaningful |
| Aggregating fine cells into coarse cells | Area-weighted aggregation may be better | A point-sample interpolation is not a summary of all source area |

Cubic convolution and Lanczos are also used for continuous imagery, but they can overshoot and need their own support and NoData policies. They are not implemented here.

## Important distinction: resampling versus reprojection

A real geospatial warp maps coordinates through the target CRS, source CRS and source affine transform. It must handle rotation, grid alignment, units, resolution, NoData metadata and sometimes antialiasing. The teaching code only maps same-extent arrays by shape. Do not apply it to georeferenced data and assume the spatial metadata is handled.

## Exercises

1. Resample a categorical grid with nearest neighbour. Are all output values in the original class set?
2. Resample a continuous plane with bilinear interpolation. What should happen at the centre?
3. Insert NoData into one source cell. Compare strict and renormalized interpolation.
4. Explain why bilinear interpolation is not appropriate for land-cover labels.
5. Describe what additional transformations a CRS-aware warp must perform.

## References

- GDAL documentation, *gdalwarp — image reprojection and warping utility*, for production resampling and geospatial warp semantics.
- Burrough, P. A. and McDonnell, R. A. (1998), *Principles of Geographical Information Systems*, Oxford University Press.

**Scope:** same-extent array resampling with nearest and bilinear methods; no CRS-aware warp, cubic/Lanczos interpolation or area-weighted aggregation.
