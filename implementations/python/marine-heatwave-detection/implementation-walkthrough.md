# Implementation walkthrough: marine heatwave detection

## 1. Keep climatology and event detection separate

The function receives temperature, threshold and climatological mean arrays. In a real study, the threshold and climatology are produced from a selected reference period and day-of-year window. This package deliberately does not hide those upstream choices.

## 2. Validate aligned daily inputs

The three arrays must be one-dimensional and equal length. Index i in every array must describe the same day and location. The function assumes daily, contiguous sampling; it cannot detect a missing calendar date that has been removed before the arrays are passed in.

## 3. Create the exceedance mask

A day is marked hot only when all three inputs are finite and temperature is strictly greater than the supplied threshold. Non-finite values are invalid observations, not cool days.

## 4. Find runs

The Boolean mask is padded with false values at both ends. A difference operation identifies transitions from false to true (run starts) and true to false (run ends). Runs shorter than the minimum duration are discarded.

## 5. Join candidate events

The code walks through qualifying runs in time order. Two runs are joined only when the gap is short enough and every intervening day is observed and below threshold. A missing value therefore prevents joining.

The gap days remain inside the event's calendar interval. The result reports both calendar duration and exceedance-day count so the reader can distinguish them.

## 6. Calculate basic metrics

Intensity is temperature minus climatological mean, not temperature minus the 90th-percentile threshold. The code calculates mean, maximum and cumulative intensity across valid days in the event interval.

## 7. Reproduce the tests

```bash
python -m pytest implementations/python/marine-heatwave-detection/test_marine_heatwave_detection.py
```

The tests cover minimum duration, gap joining, missing values, event metrics and invalid inputs.

## Scope boundary

This is a transparent single-series teaching implementation. It is not the full Hobday reference algorithm, and it does not calculate climatology, seasonal percentiles, uncertainty, gridded spatial connectivity or feature tracks.
