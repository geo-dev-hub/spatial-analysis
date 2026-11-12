# Follow the sweep: a Bentley–Ottmann implementation walkthrough

This guide follows two Python implementations of the same event-driven sweep. It is written so a new contributor can reproduce the run, understand the data structures and trace each event without relying on prior project knowledge.

## 1. What we are trying to do

Given a collection of straight line segments, return every pair that intersects. The straightforward solution checks all pairs. The sweep-line method avoids most of those checks when the number of intersections is small.

We reuse the pairwise operation from the segment-intersection example. That gives us a known geometric primitive and an independent all-pairs test oracle.

## 2. Prepare the environment

Use Python 3.10 or later. From this directory, run:

    PYTHONPATH=../segment-intersection python bentley_ottmann.py
    PYTHONPATH=../segment-intersection python -m pytest -q

The first command runs the list-based example. The second runs the complete test suite, including the treap implementation and its data-structure tests. The PYTHONPATH setting makes the sibling pairwise module importable without copying its code.

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

The event queue is a heap in both versions. The status structure is different: the first version uses a Python list, while the second uses an implicit treap.

## 4. Read the list implementation first

Open `bentley_ottmann.py`.

The list version makes the event logic visible without introducing tree rotations or split/merge operations. It is the reference implementation for understanding the sequence of events.

### Step A — represent a segment

The Segment dataclass stores an integer ID and two integer-coordinate endpoints. Its constructor rejects zero-length and vertical segments, then normalises the endpoints so a is always the left endpoint.

The `y_at(x)` method evaluates the segment's height at a given sweep coordinate:

$$
y(x)=y_1+\frac{y_2-y_1}{x_2-x_1}(x-x_1)
$$

The slope is also available. At a crossing, two segments have equal height; comparing their slopes gives their order immediately to the right of the event.

### Step B — calculate a pair intersection

The shared `_intersection(a, b)` function delegates to the pairwise implementation. It returns no point when the pair does not meet, an exact pair of rational coordinates when they meet at one point, and an error for collinear overlap, which these sweeps do not support.

This keeps pair geometry separate from event scheduling.

### Step C — create the event queue

For each segment, the code inserts two tuples into the heap:

    (x, y, kind, segment_id, other_segment_id)

The event kind sorts left endpoints before crossings and right endpoints at a shared coordinate. Shared-coordinate and grouped-event cases are restricted by the documented input contract; the tuple ordering is not a complete degeneracy policy.

### Step D — insert a segment

When a left endpoint is removed from the queue:

1. Find the segment's position in the status.
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

## 6. Why the list version is not enough

The list is easy to inspect, but insertion, deletion, search and position lookup can take linear time. The algorithm may avoid most geometric pair tests and still spend substantial time maintaining the active status.

That is why we built a second implementation rather than simply repeating the textbook complexity beside the list code.

## 7. Understand the treap status

Open `status_treap.py`, then `bentley_ottmann_treap.py`. The companion [status-structure note](status-structure.md) explains the design in detail.

The treap is an *implicit sequence tree*. Its in-order traversal is the bottom-to-top status. Each node stores its subtree size and parent pointer, allowing the implementation to find a node's rank and retrieve its neighbours.

The important design decision is that the treap does not keep a search-tree ordering based on a geometric comparator that changes continuously with the sweep coordinate.

- At a left endpoint, the current event coordinate is used to find the segment's insertion rank in the already-correct status sequence.
- At a right endpoint, the segment's node identity is used to find its rank and remove it.
- At a crossing, the two segment nodes are already adjacent. The treap swaps their sequence positions explicitly.
- The same node objects remain associated with their segment IDs after the swap.

The split and merge operations maintain the implicit sequence. Randomized priorities give expected logarithmic height and expected logarithmic operation costs. They do not give the deterministic worst-case guarantee of an AVL or red-black tree.

## 8. Understand the tests

The test suite has three roles:

- **Sweep examples** check exact coordinates, no-intersection cases and supported input.
- **Data-structure tests** check the treap's sequence order, parent pointers, subtree sizes, ranks, insertions, removals and adjacent swaps.
- **Differential tests** compare both sweep implementations with the result from checking every pair.

The randomized tests use fixed seeds so another learner can reproduce the same cases. They exclude inputs that violate the general-position contract. As the implementation grows, every discovered failure should become a permanent regression test.

Run the tests before changing the event logic or the tree. After a change, run them again and explain any difference.

## 9. First performance experiment

Run:

    PYTHONPATH=../segment-intersection python benchmark.py

The script compares the list sweep, treap sweep and all-pairs oracle on deterministic, parallel, non-intersecting segments. It counts candidate-pair checks as well as elapsed time. The [benchmark report](benchmark-results.md) records the environment, measurements and limitations.

The important observation is that the two sweeps make the same small number of candidate-pair checks, but their runtimes differ because their status structures have different operation costs. The report is a controlled first experiment, not proof of performance on real GIS data.

## 10. Suggested intern exercises

1. Add a print-only trace that displays each event and the status after processing it.
2. Draw the same trace by hand and compare it with the program output.
3. Construct a case where one segment crosses three others at three distinct event coordinates.
4. Trace the treap's in-order sequence before and after one crossing.
5. Explain why the segment-ID-to-node dictionary remains valid after an adjacent swap.
6. Instrument the pairwise routine and compare candidate-pair checks with n(n-1)/2.
7. Propose an explicit output model for three or more segments meeting at one point before attempting grouped-event support.

Do not add vertical or multiway cases by simply changing a comparison or adding an epsilon. First define the event semantics, then design tests that prove the new contract.
