# NoData-aware zonal statistics

Zonal statistics summarize raster values grouped by an aligned integer zone raster. Each zone receives count, sum, mean, minimum, maximum, median and population standard deviation.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Contract

- Values and zone labels must be 2D arrays with identical shape and cell alignment.
- Finite zone labels must be integer values in the int64 range.
- Non-finite zone labels are excluded.
- Non-finite raster values are skipped within each zone.
- Zones with no valid values remain in the output with count zero, sum zero and undefined (NaN) descriptive statistics.
- Standard deviation uses population convention (ddof=0).
- This implementation does not align rasters, reproject, resample, calculate polygon zones or produce zonal histograms.

Read the [canonical lesson](../../../algorithms/raster/zonal-statistics.md) and [intern walkthrough](implementation-walkthrough.md).
