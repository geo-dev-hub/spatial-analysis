# Focal raster statistics with integral images

Stable ID: `SA-RASTER-FOCAL-INTEGRAL` · Draft 0.1 · Source compendium section 4, page 6

## What is a focal operation?

A local map-algebra operation calculates an output value at each raster cell using a neighbourhood around that cell. A focal mean is a simple example: replace each cell with the mean of values in a moving window.

This is different from:
- a **local** operation, which combines values from corresponding cells in one or more rasters;
- a **zonal** operation, which summarises cells grouped by a zone identifier;
- a **global** operation, which uses the raster as a whole.

## Integral images

A summed-area table, also called an integral image, stores cumulative sums. For a raster $x$:

$$
I(r,c)=\sum_{i<r,\,j<c}x(i,j)
$$

A rectangular window sum can be computed from four table entries:

$$
S=I(r_1,c_1)-I(r_0,c_1)-I(r_1,c_0)+I(r_0,c_0)
$$

The query takes constant time after the integral image has been built. A second table can store valid-cell counts so NoData values are not silently treated as zeros.

## The focal mean

For a neighbourhood $N(i)$ around cell $i$, let $V$ be the valid cells. The mean is:

$$
\bar{x}_i=\frac{\sum_{j\in N(i)\cap V}x_j}{|N(i)\cap V|}
$$

The [teaching implementation](../../implementations/python/focal-statistics/README.md) returns both the mean and the valid observation count. A result is NaN when fewer than min_count valid observations are present.

## Edge and NoData policy

The implementation uses odd-sized square windows centred on each cell. At raster edges the window is truncated to the in-bounds cells; no padding is introduced. Non-finite values, an optional NoData sentinel and cells excluded by a validity mask are ignored.

This is one possible boundary policy. Some GIS tools pad, mirror, wrap or mark edge results NoData; those choices produce different outputs and must be documented.

## Complexity and limitations

Building the value and count integral images is O(n) for n raster cells. Each cell's rectangular sum and count are then queried in O(1), so the complete operation is O(n) time and O(n) memory.

The example is an unweighted square-window mean. It is not a general convolution engine and does not implement weighted kernels, zonal histograms, resampling or all focal statistics.

## Exercises

1. Calculate the centre-cell mean of a 3×3 raster by hand.
2. Compare edge means under truncated windows and zero padding.
3. Place NoData in the centre and compare the valid-cell count with the total window size.
4. Change min_count. Which outputs become undefined?
5. Explain why an integral image is useful for repeated rectangular queries.
6. Compare a focal mean with a Gaussian-weighted filter.

## References

- Crow, F. C. (1984), *Summed-area tables for texture mapping*, ACM SIGGRAPH Computer Graphics, 18(3), 207–212.

**Scope:** NoData-aware unweighted square-window mean using two integral images; weighted filters, zonal statistics and raster resampling are not included.
