# Zonal statistics for raster values

Stable ID: SA-RASTER-ZONAL-STATISTICS · Draft 0.1 · Source compendium section 4, page 6

## The question

What is the distribution of raster values within each zone?

A zone raster assigns an integer label to each cell. Cells with the same label form a group. Zonal statistics aggregate the values of a second, aligned raster by those groups.

This differs from focal statistics: focal operations summarize a neighbourhood around each cell; zonal operations summarize all cells sharing a zone identifier.

## Descriptive summaries

For zone z with n valid cell values x₁,…,xₙ, the arithmetic mean is:

$$\bar x_z=\frac{1}{n}\sum_{i=1}^{n}x_i$$

Population standard deviation:

$$\sigma_z=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i-\bar x_z)^2}$$

The teaching implementation also returns count, sum, minimum, maximum and median. It uses population standard deviation (ddof=0), not sample standard deviation.

## Alignment and NoData

The [Python implementation](../../implementations/python/zonal-statistics/README.md) assumes the value and zone arrays are already aligned cell by cell. Matching array dimensions is not sufficient in a real GIS: CRS, affine transform, pixel origin, resolution and alignment must also match.

Non-finite zone labels are excluded. Non-finite values are skipped inside each zone. A zone with no valid values remains represented with count zero and undefined statistics. This keeps the distinction between an absent zone and a zone whose values are all missing.

## Focal versus zonal

| Operation | Grouping rule | Typical question |
|---|---|---|
| Focal | Neighbourhood around each output cell | What is the local mean around this cell? |
| Zonal | All cells sharing a zone identifier | What is the mean elevation in this catchment or administrative area? |

## Limitations

- This baseline does not align, reproject or resample input rasters.
- It does not construct zones from vector polygons.
- It does not implement zonal histograms or categorical frequency tables.
- It is a clear teaching implementation, not an optimized large-raster grouping engine.

## Exercises

1. Calculate the mean and population standard deviation for a zone by hand.
2. Insert NoData values. Which statistics change?
3. Create a zone whose values are all NoData. Why retain it in the result?
4. Explain why matching array shapes does not guarantee geospatial alignment.
5. Compare focal and zonal statistics on the same raster.

## References

- Tomlin, C. D. (1990), *Geographic Information Systems and Cartographic Modeling*, Prentice Hall.
- Burrough, P. A. and McDonnell, R. A. (1998), *Principles of Geographical Information Systems*, Oxford University Press.

**Scope:** descriptive statistics grouped by an existing aligned integer zone raster; no raster alignment, polygonization or zonal histograms.
