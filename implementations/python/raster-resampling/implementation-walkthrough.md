# Intern walkthrough: nearest-neighbour and bilinear resampling

## 1. Separate the grid mapping from the interpolation

This example keeps the same extent and orientation and changes only the raster shape. Each target pixel centre is mapped to a fractional source pixel-centre coordinate:

$$r_s=\left(r_t+\frac12\right)\frac{N_r}{M_r}-\frac12$$

$$c_s=\left(c_t+\frac12\right)\frac{N_c}{M_c}-\frac12$$

where N is the source dimension and M is the target dimension. This is a same-extent grid mapping, not a coordinate-reference-system transformation.

## 2. Nearest neighbour

Round the fractional source coordinate to the nearest source cell, clamping at the source boundary. The selected source value is copied without averaging. This preserves class codes, but the output may look blocky.

## 3. Bilinear interpolation

Find the four surrounding source cells. Let fr and fc be the fractional row and column offsets. The four weights are:

$$
(1-f_r)(1-f_c),\quad (1-f_r)f_c,\quad f_r(1-f_c),\quad f_rf_c
$$

The output is the weighted average:

$$z_t=\frac{\sum_i w_i z_i}{\sum_i w_i}$$

When all four samples are valid, the weights sum to one. At the grid edge, source indices are clamped to the boundary.

## 4. NoData policy

Strict mode returns NoData if any positive-weight neighbour is missing. Renormalize mode averages the valid neighbours and divides by their remaining total weight. This can preserve more output cells but changes the interpolation support near gaps.

A zero-weight neighbour does not affect the output and is not required to be valid.

## 5. What is outside the example

A true geospatial warp must map target coordinates through target CRS, source CRS and source affine transform. It must account for pixel alignment, rotation, resolution, nodata metadata and often antialiasing. This implementation does not do that. It also does not implement cubic, Lanczos or area aggregation.

## 6. Validate the method choice

Use nearest neighbour for categorical labels when preserving class membership is essential. Use bilinear interpolation for many continuous surfaces when smoothing is acceptable. Resampling is not a neutral operation: it changes the sampled values and may alter extremes and derived statistics.
