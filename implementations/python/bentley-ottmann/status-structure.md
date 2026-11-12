# The sweep-line status: from a list to an implicit treap

This note explains the data structure used by the second Bentley–Ottmann implementation. It focuses on one difficult implementation detail: the order of active segments changes when two segments cross.

## What the status must support

At any sweep event, the status contains the active segments in bottom-to-top order. The algorithm needs to:

1. insert a segment at its correct position;
2. remove a segment when it reaches its right endpoint;
3. find the immediate segment above or below a segment;
4. find a segment's current position;
5. exchange the positions of two adjacent segments at a crossing.

A Python list makes these operations easy to see, but insertion, removal and searching can take linear time.

## Why a normal search-tree comparator is dangerous

A tempting design is to store segments in a balanced binary search tree ordered by their height at the current sweep coordinate:

$$
y_s(x)=y_1+\frac{y_2-y_1}{x_2-x_1}(x-x_1)
$$

But the comparison between two segments changes at their intersection. If the sweep coordinate changes and the comparator begins returning the opposite answer while the nodes remain in the tree, the tree's stored search order may no longer be valid.

We must not silently change the meaning of the tree's ordering.

## The sequence-tree idea

The treap in `status_treap.py` is an *implicit treap*. It stores the status as a sequence, not as a search tree whose keys are geometric heights.

Each node stores:
- a segment ID;
- a random priority used to maintain the treap's heap property;
- left and right child references;
- a parent reference;
- the size of its subtree.

The in-order traversal is the current bottom-to-top status. The node's position is implicit in the shape of the tree.

| Operation | How it works | Expected time |
|---|---|---:|
| Insert at rank | Split the sequence, insert a node, merge | (O(\log n)) |
| Remove at rank | Split around one node, merge the remaining sides | (O(\log n)) |
| Find rank | Climb parent pointers and count left subtrees | (O(\log n)) |
| Find item at rank | Descend using subtree sizes | (O(\log n)) |
| Swap adjacent items | Split around the pair and merge in reverse order | (O(\log n)) |
| Find insertion rank | Search the existing sequence using the geometric order at this event | (O(\log n)) |

These are expected bounds because the treap uses randomized priorities. The implementation seeds its random generator so a learner can reproduce a run.

## Why an adjacent swap is enough

Under the restricted general-position assumptions, the two segments at a crossing are adjacent immediately before they meet. The event handler finds their node ranks and swaps those two positions.

The tree does not need to rebuild its geometric search order. It only changes the sequence at the known crossing event. Node identity remains stable, so the segment-ID-to-node dictionary continues to work after swaps.

At an endpoint insertion, the current event coordinate is used to find the correct insertion rank. Between events, the active segments do not exchange order. At an intersection event, the affected adjacent pair is explicitly swapped before the new outside neighbours are tested.

## What the treap guarantees—and what it does not

A randomized treap gives expected logarithmic height and expected logarithmic operation time. It does not provide the deterministic worst-case guarantee of an AVL or red-black tree. A pathological priority arrangement can produce a tall tree, although randomized priorities make that unlikely.

The current treap implementation also inherits the same geometric input restrictions as the list implementation. It does not solve vertical segments, coincident events, endpoint contacts, multiway intersections or overlaps.

## Read and test the implementation

- [Treap data structure](status_treap.py)
- [Bentley–Ottmann using the treap](bentley_ottmann_treap.py)
- [Data-structure invariant tests](test_status_treap.py)
- [Sweep differential tests](test_bentley_ottmann_treap.py)
- [Benchmark and recorded results](benchmark-results.md)

The most useful learning exercise is to trace one crossing by hand: record the in-order sequence before the event, swap the two segment nodes, then verify that only the two new outside neighbour pairs need to be checked.
