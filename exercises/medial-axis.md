# Exercise: read a polygon's medial axis

## Goal

Use the definition of maximal inscribed discs to reason about a polygon's internal structure.

## Part 1 — Start with a rectangle

Use a rectangle of width 8 and height 4.

1. Sketch its medial axis.
2. Mark the contact points of a maximal disc centred on the long centreline.
3. What is the largest possible radius?
4. Explain why the medial axis is not the same thing as the rectangle's centroid.

## Part 2 — Add a notch

Modify one long side with a narrow inward notch.

1. Predict where new medial-axis branches appear.
2. Explain which boundary features are closest to points on those branches.
3. Describe how a small notch can create short branches.
4. Propose a pruning rule, and state what geometric information it may discard.

## Part 3 — Connect to Voronoi

Explain why a medial axis can be extracted from a Voronoi diagram of boundary features. Why is a point-site Voronoi diagram of polygon vertices alone insufficient to capture the exact polygon medial axis?

## Part 4 — Compare representations

Compare:
- exact continuous medial axis;
- raster thinning skeleton;
- a manually digitized centreline.

For each, state what it represents, what controls its resolution or precision, and whether it supports exact Euclidean clearance measurements.

## Submission

Provide sketches, contact-point labels, a width interpretation and a short note on sensitivity to boundary noise.
