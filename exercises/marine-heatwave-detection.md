# Exercise: detect marine heatwave events

## Scenario

You have a daily sea-surface-temperature series and, separately, a seasonal climatological mean and 90th-percentile threshold for each day. Your task is to identify candidate events and explain how data preparation affects the result.

## Part A — Reproduce the baseline

1. Install the package requirements and run its tests.
2. Create a 120-day synthetic series with a seasonal signal and noise.
3. Create a simple threshold and climatology for the simulation (label these as synthetic, not a climatology product).
4. Detect events using a five-day minimum duration and two-day gap rule.
5. Plot temperature, threshold, climatology and the detected event intervals.

## Part B — Sensitivity analysis

Repeat the detection while changing one choice at a time: minimum duration (3, 5 and 7 days), maximum join gap (0, 1 and 2 days), baseline climatology (compare two plausible baseline periods), and missing observations (insert gaps inside and between candidate events).

Report which event starts, ends, counts and intensities change. Do not compare event counts without reporting the detection settings.

## Part C — Move from a point to a grid

Design a gridded workflow: apply quality masks and calculate the seasonal threshold at each valid cell; detect local events independently at each cell; label connected regions on each day; specify how regions are linked across adjacent days; define how splits, merges, coastlines, missing observations and periodic longitude are handled; validate tracks against an independent event catalogue or carefully reviewed case studies.

## Deliverable

Submit a notebook, event table, sensitivity comparison and a one-page spatial-tracking design. Clearly distinguish pointwise event detection from tracking a moving ocean feature.
