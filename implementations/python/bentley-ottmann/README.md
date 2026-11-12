# Bentley–Ottmann with Python

Two exact-coordinate teaching implementations for a restricted general-position input. Start with the [step-by-step implementation walkthrough](implementation-walkthrough.md) if you want to follow the algorithm as an intern or first-time contributor.

## Run it

Use Python 3.10 or later. From this directory:

```bash
PYTHONPATH=../segment-intersection python bentley_ottmann.py
PYTHONPATH=../segment-intersection python -m pytest -q
```

The list and treap implementations share the same segment representation and pairwise intersection primitive. This keeps geometric pair testing in one canonical example.

## Two status structures

| Version | Status structure | What it teaches |
|---|---|---|
| `bentley_ottmann.py` | Python list | The event logic in its most direct, inspectable form |
| `bentley_ottmann_treap.py` | Implicit randomized treap | Expected logarithmic insertion, deletion, rank and neighbour operations |

The list version makes status updates easy to follow, but insertion, removal and lookup can take linear time. The treap stores the status as an ordered sequence. At a crossing, it explicitly swaps the two adjacent segment nodes instead of relying on a geometric comparator whose order changes as the sweep moves.

Read [how the treap status works](status-structure.md) before modifying its split, merge, rank or swap operations.

## Input contract

Both versions are deliberately restricted to non-vertical segments with distinct integer endpoints, unique IDs, no shared endpoints, no endpoint-on-segment contacts, no collinear overlaps, no multiway intersections and no two distinct event points sharing an x-coordinate.

Some restrictions are checked directly (vertical segments, duplicate IDs, shared endpoints and overlaps encountered during neighbour checks). The remaining general-position conditions are preconditions, not exhaustively validated. Do not pass arbitrary GIS linework and assume unsupported degeneracies will be detected.

## Complexity: abstract algorithm versus these implementations

With a priority queue and a balanced status structure, the classical algorithm runs in:

```
O((n + k) log n)
```

where `n` is the number of segments and `k` is the number of reported intersecting pairs.

The list implementation does **not** achieve that bound. Its status operations can take `O(n)` time; a conservative bound is `O((n+k)n + (n+k) log(n+k))`, excluding arithmetic bit complexity.

The treap implementation has **expected** `O(log n)` status operations because it uses randomized priorities. Its expected running-time bound under the restricted input assumptions is `O((n+k) log n)`. Unlike an AVL or red-black tree, a randomized treap does not give a deterministic worst-case logarithmic-height guarantee.

## Tests

The test suite covers:
- the original list-based sweep and exact rational event coordinates;
- the treap's sequence, parent-pointer, subtree-size, rank, insertion, deletion and swap invariants;
- both sweep implementations against an independent all-pairs oracle;
- seeded randomized general-position cases.

Run all tests from this directory:

```bash
PYTHONPATH=../segment-intersection python -m pytest -q
```

## Benchmark

```bash
PYTHONPATH=../segment-intersection python benchmark.py
```

The benchmark compares both sweeps with the all-pairs oracle on seeded, non-intersecting fixtures. See [the recorded results and interpretation](benchmark-results.md). The fixture is diagnostic, not a representative geospatial workload.

## Limitations

Neither implementation is a production GIS overlay engine. They do not support vertical segments, shared endpoints, endpoint-on-segment contacts, multiway crossings, coincident event points or collinear overlaps. Exact arithmetic does not replace a complete degeneracy policy.
