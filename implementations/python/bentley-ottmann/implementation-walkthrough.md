# Follow the sweep: a Bentley–Ottmann implementation walkthrough

This guide follows the Python code in bentley_ottmann.py. It is written so a new contributor can reproduce the run, understand the data structures and trace each event without relying on prior project knowledge.

## 1. What we are trying to do

Given a collection of straight line segments, return every pair that intersects. The straightforward solution checks all pairs. The sweep-line method avoids most of those checks when the number of intersections is small.

We reuse the pairwise operation from the segment-intersection example. That gives us a known geometric primitive and an independent all-pairs test oracle.

## 2. Prepare the environment

Use Python 3.10 or later. From this directory, run:

    PYTHONPATH=../segment-intersection python bentley_ottmann.py
    PYTHONPATH=../segment-intersection python -m pytest -q

The first command runs a small example. The second runs the automated tests. The PYTHONPATH setting makes the sibling pairwise module importable without copying its code.

## 3. Understand the two structures

The algorithm maintains two things.

**The event queue** answers: what is the next thing that can change the sweep?

- Every segment contributes a left endpoint event and a right endpoint event.
- When two active neighbours are found to intersect in the future, their crossing is added as an event.
- Python's heapq removes the smallest event first.

**The status** answers: which segments are active, and in what bottom-to-top order?

- A segment becomes active at its left endpoint.
- It remains active while the sweep passes through it.
- It leaves at its right endpoint.
- When two segments cross, their order swaps.

In this first version, status is a Python list. This is intentionally easy to inspect, but insertion and removal can take linear time. A balanced search tree is needed for the classical asymptotic bound.

## 4. Read the code in this order

### Step A — represent a segment

The Segment dataclass stores an integer ID and two integer-coordinate endpoints. Its constructor rejects zero-length and vertical segments, then normalises the endpoints so a is always the left endpoint.

The y_at(x) method evaluates the segment's height at a given sweep coordinate:

$$
y(x)=y_1+\frac{y_2-y_1}{x_2-x_1}(x-x_1)
$$

The slope is also available. At a crossing, two segments have equal height; comparing their slopes gives their order immediately to the right of the event.

### Step B — calculate a pair intersection

The _intersection(a, b) function delegates to the pairwise implementation. It returns no point when the pair does not meet, an exact pair of rational coordinates when they meet at one point, and an error for collinear overlap, which this sweep does not support.

This keeps pair geometry separate from event scheduling.

### Step C — create the event queue

For each segment, the code inserts two tuples into the heap:

    (x, y, kind, segment_id, other_segment_id)

The event kind sorts left endpoints before crossings and right endpoints at a shared coordinate. Shared-coordinate and grouped-event cases are restricted by the documented input contract; the tuple ordering is not a complete degeneracy policy.

### Step D — insert a segment

When a left endpoint is removed from the queue:

1. Find the segment's position in the status list.
2. Insert it in bottom-to-top order.
3. Identify the segment immediately below and immediately above it.
4. Ask only those two neighbour pairs whether they have a future intersection.

The new segment cannot suddenly cross a segment several positions away without first crossing a segment between them. That is why neighbour checks are enough under the general-position assumptions.

### Step E — remove a segment

At a right endpoint:

1. Remember the ending segment's immediate neighbour below and above.
2. Remove the ending segment.
3. Check the pair that has become neighbours.

The segment that ended cannot take part in any event to the right of its endpoint.

### Step F — process a crossing

At a crossing event:

1. Confirm both segments are still active.
2. Confirm they are still adjacent. If not, the event is stale and is ignored.
3. Record the pair and exact event point.
4. Put the two segments in their order immediately to the right of the crossing.
5. Check the new outside neighbour pairs.

The stale-event check matters because an event can be scheduled while two segments are neighbours, then later become irrelevant after other events change the status.

## 5. Why exact fractions matter

An intersection does not necessarily have integer coordinates. For example, the segments from (0, 0) to (3, 3) and from (0, 2) to (3, 0) meet at:

$$
\left(\frac{6}{5},\frac{6}{5}\right)
$$

The code uses Python's Fraction so the event queue compares exact values rather than rounded decimal approximations. This prevents a display rounding error from changing event order in the supported cases.

Exact arithmetic is not a complete solution to degeneracies. The algorithm still needs a defined policy for coincident events, multiway intersections, vertical segments and overlaps.

## 6. Understand the tests

The test file has two roles:

- **Example tests** check exact coordinates, no-intersection cases and unsupported input.
- **Differential tests** compare the sweep's segment-pair set with the result from checking every pair.

The random test uses a fixed seed so another learner can reproduce the same cases. It excludes inputs that violate the general-position contract. As the implementation grows, every discovered failure should become a permanent regression test.

Run the tests before changing the event logic. After a change, run them again and explain any difference.

## 7. What this implementation does not prove

The abstract Bentley–Ottmann algorithm with a priority queue and balanced status tree has the classical output-sensitive bound:

$$
O((n+k)\log n)
$$

Here, n is the number of segments and k is the number of intersecting pairs.

This Python version uses a list for status. List insertion, deletion and lookup are linear, so this code does not achieve that bound. Its purpose is to make the event logic concrete before introducing a balanced tree with a carefully controlled ordering invariant.

It is also not a production GIS topology engine. Its restricted contract is stated in the implementation README.

## 8. First performance experiment

Run:

    PYTHONPATH=../segment-intersection python benchmark.py

The script compares the sweep against the all-pairs oracle on deterministic, parallel, non-intersecting segments. It counts candidate-pair checks as well as elapsed time. The [benchmark report](benchmark-results.md) records the environment, measurements and limitations.

The important observation is that fewer geometric pair checks do not automatically mean lower runtime. The list status still has linear-time operations. Read the report, then explain why the sweep can perform fewer pair checks and still take as long as—or longer than—the all-pairs method.

## 9. Suggested intern exercises

1. Add a print-only trace that displays each event and the status after processing it.
2. Draw the same trace by hand and compare it with the program output.
3. Add a test in which one segment crosses three others at three distinct event coordinates.
4. Instrument the pairwise routine and count how many candidate pairs the sweep checks.
5. Compare those checks with n(n-1)/2 for the brute-force oracle.
6. Research how a balanced status tree can support neighbour lookup and safe swaps without allowing its comparator to invalidate the tree.
7. Propose an explicit output model for three or more segments meeting at one point before attempting grouped-event support.

Do not add vertical or multiway cases by simply changing a comparison or adding an epsilon. First define the event semantics, then design tests that prove the new contract.
