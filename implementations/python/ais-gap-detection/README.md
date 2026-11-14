# AIS gap detection

A transparent track-quality baseline for identifying adjacent vessel reports separated by an unusually long reporting interval or an implausibly high great-circle implied speed.

## Input and output

Inputs are vessel identifiers, numeric timestamps in seconds, longitude and latitude in decimal degrees. Records are grouped by vessel and sorted by timestamp. For each adjacent pair, the implementation calculates elapsed seconds, haversine distance in nautical miles and implied speed in knots. It returns only flagged intervals, with independent reason flags.

    from ais_gap_detection import detect_ais_gaps

    findings = detect_ais_gaps(
        vessel_ids, unix_seconds, longitude, latitude,
        max_gap_seconds=1800,
        max_speed_knots=60,
    )

## Assumptions and limits

- Thresholds are analyst-selected and should vary by vessel class, AIS class, reporting mode, navigation context and study purpose.
- Great-circle distance is a screening approximation between reported positions, not a reconstructed route distance.
- A long interval is not proof that a transponder was switched off. It can reflect coverage, reception, satellite revisit, data ingestion or legitimate reporting behaviour.
- High implied speed may reflect bad coordinates, identity collisions, timestamp errors or a genuine unusual movement; it is not a behaviour classifier.
- This does not infer missing messages, interpolate tracks, detect spoofing, identify illegal fishing or fuse SAR with AIS.
- Duplicate/non-increasing timestamps within a vessel are rejected because a segment's speed would be undefined or ambiguous.

## Install and test

    python -m pip install -r requirements.txt
    python -m pytest -q

See the [walkthrough](walkthrough.md) and [synthetic lab](../../../notebooks/ais-gap-detection-lab.ipynb).
