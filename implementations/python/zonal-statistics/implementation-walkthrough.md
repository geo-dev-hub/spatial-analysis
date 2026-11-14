# Intern walkthrough: zonal raster statistics

## 1. Align the two rasters first

The value raster and zone-label raster must refer to the same cells. Equal array shape alone does not prove geospatial alignment: a production workflow must also compare CRS, affine transform, resolution, origin and pixel alignment.

This teaching function accepts already-aligned arrays and deliberately does not reproject or resample.

## 2. Define valid zones and values

A finite integer zone label identifies a group. Non-finite zone labels are excluded. Within each zone, non-finite raster values are skipped.

A zone can exist even when every corresponding value is NoData. The implementation preserves that zone with count zero and undefined summary statistics rather than silently dropping it.

## 3. Calculate summaries

For zone z with valid values x₁,…,xₙ:

$$\bar x_z=\frac{1}{n}\sum_{i=1}^{n}x_i$$

The population standard deviation is:

$$\sigma_z=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i-\bar x_z)^2}$$

The implementation also reports count, sum, minimum, maximum and median. The ddof=0 convention is explicit; a sample standard deviation would use n−1 in the denominator.

## 4. Complexity and limitations

The function scans the arrays to identify zone labels, then selects values for each zone. Its straightforward implementation is intended for clarity and small-to-medium teaching arrays, not optimal large-raster performance. A production implementation can sort or group cell indices once to avoid rescanning for each zone.

Zonal statistics are not focal statistics: focal operations use neighbourhoods around each cell, while zonal operations aggregate cells sharing a zone identifier.

## 5. Validation

Tests cover multiple zones, descriptive statistics, NoData values, empty zones, missing zone labels, shape mismatch and non-integer labels. They do not validate the geospatial alignment of source rasters.

## 6. Build a zonal histogram

The zonal_histogram function uses explicit, strictly increasing bin edges. It returns one count array per zone, including all-zero arrays for zones with no valid values. Non-finite values are skipped and values outside the supplied edge range are not counted. Histogram bins are a modelling choice: use meaningful class boundaries for categorical data or defensible intervals for continuous data.
