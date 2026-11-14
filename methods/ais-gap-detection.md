# AIS reporting-gap detection

AIS track quality is a prerequisite for vessel-behaviour analysis and fishing-effort estimation. A gap in received reports is not automatically a gap in vessel movement: terrestrial reception, satellite coverage, message class, reporting mode, antenna conditions and data pipelines all affect observation density.

## Adjacent-report screening

For each vessel identifier, sort reports by timestamp and compare adjacent reports. Let \(\Delta t\) be elapsed seconds and \(d\) the great-circle distance in nautical miles. The implied speed is:

\[
v_{\mathrm{kn}} = \frac{d}{\Delta t/3600}.
\]

Flag the interval if \(\Delta t\) exceeds a configured reporting-gap threshold, or if implied speed exceeds a configured vessel-speed threshold. Both conditions can be reported independently.

The haversine calculation is a spherical screening distance. It does not reconstruct a navigable route or account for currents, manoeuvres or coastlines.

## Interpretation and operational cautions

- Calibrate thresholds by vessel class, AIS class, reporting mode, geography and intended use.
- A long interval may reflect receiver coverage, satellite revisit, data ingestion or legitimate reporting cadence; it is not evidence of intentional AIS disabling.
- High implied speed may be caused by timestamp corruption, coordinate errors, identity collisions or unusual movement. It is not a vessel-behaviour classifier.
- This screen does not interpolate tracks, infer missing messages, detect spoofing, identify illegal fishing or fuse SAR and AIS.
- Preserve raw reports and record the thresholds and data provenance used for each run.

## Implementation

The [Python baseline](../implementations/python/ais-gap-detection/README.md) returns flagged adjacent-report intervals with elapsed time, great-circle distance, implied speed and reason flags. Its [tests](../implementations/python/ais-gap-detection/test_ais_gap_detection.py), [walkthrough](../implementations/python/ais-gap-detection/walkthrough.md) and [synthetic lab](../notebooks/ais-gap-detection-lab.ipynb) exercise the bounded algorithm.

## References

- International Maritime Organization, SOLAS Chapter V, Regulation 19 and AIS carriage/operational guidance.
- European Maritime Safety Agency, vessel traffic monitoring and SafeSeaNet materials: https://www.emsa.europa.eu/
