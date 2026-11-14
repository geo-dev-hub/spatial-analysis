# Exercise: follow a straight-skeleton wavefront

## Goal

Understand how a straight skeleton is created by polygon edges moving inward in parallel.

## Part 1 — Rectangle

Start with a rectangle 10 units wide and 6 units high.

1. Draw the wavefront after 1 unit of propagation time.
2. Identify which edges disappear first.
3. Trace the four moving wavefront vertices.
4. Sketch the straight skeleton.
5. Compare it with the rectangle's medial axis.

## Part 2 — Concave polygon

Draw an L-shaped polygon and trace its inward wavefront.

1. Identify a likely edge event.
2. Identify where a reflex vertex may trigger a split event.
3. Explain how one event changes the set of active wavefront cycles.
4. Why is it unsafe to process all initially computed events without checking whether they remain valid?

## Part 3 — Compare the definitions

Explain why a straight skeleton and medial axis coincide for a convex polygon but can differ for a non-convex polygon. Your answer must distinguish Euclidean distance to boundary features from parallel supporting-line motion.

## Part 4 — Implementation design

Design the data structures for an event-driven implementation:
- active wavefront vertices and edges;
- candidate event queue;
- links from events to the topology they depend on;
- invalidation of stale events;
- exact or robust event-time comparisons;
- face reconstruction and validation.

Do not claim a complete implementation from a drawing or a wavefront animation.

## Submission

Provide event sketches, event classifications, a comparison table and your proposed event-queue design.
