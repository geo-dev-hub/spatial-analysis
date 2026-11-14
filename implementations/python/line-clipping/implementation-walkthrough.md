# Line clipping implementation walkthrough

1. **Cohen–Sutherland:** classify each endpoint with four outcode bits. A shared outside bit rejects immediately; two inside codes accept; otherwise intersect one outside endpoint with its selected rectangle boundary and repeat.
2. **Liang–Barsky:** parameterise the segment as `P(t)=P0+t(P1-P0)`. Four inequalities tighten the admissible interval `[t_enter,t_leave]`; an empty interval rejects the segment.
3. **Cyrus–Beck:** express a convex window as oriented edge half-planes. Each edge constrains the same parametric interval. Polygon orientation is detected from signed area, so clockwise and counter-clockwise rings share the same implementation.
4. **Validate:** tests cover crossings, rejection, parallel lines, inside/boundary cases, both polygon orientations and malformed windows. These are segment clippers; do not use them as polygon overlay operations.


## Nicholl–Lee–Nicholl

Nicholl–Lee–Nicholl reduces the first endpoint to one of three canonical regions: inside, left, or top-left. Reflections and quarter-turn rotations map the other outside regions into these cases. Rays from the start point to rectangle corners partition the endpoint plane into regions that identify the one or two rectangle boundaries the segment can cross. Slope comparisons select the boundary set, avoiding the repeated boundary clipping loop used by Cohen–Sutherland.

The implementation is restricted to an axis-aligned rectangle. It handles boundary starts and vertical segments explicitly. A randomized differential test compares its output with Liang–Barsky over thousands of segments; this is a correctness oracle, not a proof of equivalence for every floating-point input.
