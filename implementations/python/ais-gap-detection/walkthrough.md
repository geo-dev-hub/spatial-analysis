# AIS gap detection: intern walkthrough

## 1. Sort within vessel

AIS rows arrive from multiple vessels and may not be chronologically ordered. Group by vessel identifier, then sort each group by timestamp. Never connect reports belonging to different vessel identifiers.

## 2. Examine adjacent reports

For consecutive reports i and i+1, calculate elapsed time:

\[
\Delta t=t_{i+1}-t_i.
\]

Calculate great-circle distance with the haversine formula, using a mean Earth radius of 3,440.065 nautical miles:

\[
a=\sin^2(\Delta\phi/2)+\cos\phi_i\cos\phi_{i+1}\sin^2(\Delta\lambda/2),
\quad
d=2R\arcsin(\sqrt{a}).
\]

Then implied speed is:

\[
v=d/(\Delta t/3600)
\]

in knots when d is nautical miles and time is seconds.

## 3. Apply independent screening rules

Flag a long reporting gap when elapsed seconds exceed the configured time threshold. Flag an implausible implied speed when the calculated speed exceeds the configured speed threshold. Both flags may occur on the same segment.

## 4. Complexity

Sorting is \(O(n\log n)\) overall in the worst case. Once sorted, adjacent-pair checks are \(O(n)\). The implementation stores each vessel's row indices and returns only flagged segments.

## 5. Interpretation

This is a quality-control screen. AIS reception gaps, satellite coverage, reporting mode, antenna conditions, ingestion delays, timestamp errors and vessel behaviour can all explain anomalies. Do not infer intentional concealment from a gap alone.

## References

- International Maritime Organization, AIS operational guidance and SOLAS Chapter V, Regulation 19.
- European Maritime Safety Agency, SafeSeaNet / vessel traffic monitoring materials: https://www.emsa.europa.eu/
- Haversine great-circle distance is a spherical approximation; for high-precision navigation use an ellipsoidal geodesic.
