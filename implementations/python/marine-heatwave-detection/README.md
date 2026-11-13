# Marine heatwave detection — Python baseline

Detects threshold-exceedance runs from one daily temperature series and already-computed seasonal threshold and climatology arrays.

## Install and test

```bash
python -m pip install -r implementations/python/marine-heatwave-detection/requirements.txt
python -m pytest implementations/python/marine-heatwave-detection/test_marine_heatwave_detection.py
```

## Input contract

- Three aligned, one-dimensional daily arrays: temperature, threshold and climatological mean.
- Threshold and climatology must already be calculated using a documented baseline and seasonal method.
- The function uses strict exceedance (temperature greater than threshold).
- A candidate run must meet minimum duration before gap joining.
- Qualifying runs may be joined across up to maximum_gap fully observed non-exceedance days.
- Any missing value breaks a run and cannot be bridged.

## Output

Each event reports inclusive start/end array indices, calendar duration, count of threshold-exceedance days, mean and maximum temperature anomaly relative to climatology, and cumulative anomaly in degree-days.

This is a single-location event-detection baseline. It does not calculate seasonal climatologies, read NetCDF/GRIB files, process grids, apply quality masks, or track spatial features. See the method lesson for those boundaries.
