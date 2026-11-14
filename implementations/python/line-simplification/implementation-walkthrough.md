# Intern walkthrough: implement two line simplifiers

## Objective

Build two algorithms that remove vertices from an ordered open polyline while preserving its endpoints. Keep the distance-based and area-based definitions distinct.

## Files

- simplification.py contains coordinate validation, point-to-segment distance, Douglas–Peucker and Visvalingam–Whyatt.
- test_simplification.py checks endpoint preservation, thresholds, duplicates, collinearity and invalid input.
- requirements.txt contains the test dependency only.

## Step 1 — Validate the coordinate model

The functions accept planar x,y pairs and finite numeric coordinates. The tolerance cannot be interpreted as metres unless the input CRS uses metres in the relevant area.

## Step 2 — Implement point-to-segment distance

Project the candidate point onto the segment direction, clamp the projection parameter to [0,1], and measure to the clamped point. If both segment endpoints coincide, use point-to-point distance.

## Step 3 — Implement Douglas–Peucker iteratively

Use a stack of index ranges rather than recursion. Find the largest deviation in each range. Retain that vertex and split the range only when the deviation exceeds tolerance.

The iterative form avoids Python recursion-depth failures on long inputs.

## Step 4 — Implement effective-area elimination

Maintain predecessor and successor arrays. A min-heap selects the smallest effective triangle area. When a point is removed, only its two neighbours need updated candidate areas. Version counters invalidate stale heap entries.

The monotonic floor ensures that later effective areas do not decrease below the last removed value.

## Step 5 — Test the contract

Run the tests. Add fixtures for very long lines, repeated consecutive vertices and coordinates in a projected CRS. Compare outputs with a trusted library on the same input and tolerance semantics before making performance or equivalence claims.

## Step 6 — Know what is deliberately absent

This code does not simplify polygon coverages or preserve topology between neighbouring features. Do not use it as a cadastral boundary generaliser.
