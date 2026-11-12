# Bentley–Ottmann with Python

A small, exact-arithmetic teaching implementation for a restricted general-position input.

## Run it

Use Python 3.10 or later. From this directory:

```bash
PYTHONPATH=../segment-intersection python bentley_ottmann.py
PYTHONPATH=../segment-intersection python -m pytest -q
```

The implementation reuses the pairwise intersection routine in the sibling `segment-intersection` directory so that geometric pair testing remains a single canonical example.

## What it demonstrates

- A heap-based event queue containing endpoints and discovered crossing events.
- A bottom-to-top status list containing the currently active segments.
- Neighbour-only scheduling after insertions, removals and crossings.
- Stale-event checks when a scheduled pair is no longer adjacent.
- Exact rational intersection coordinates using `fractions.Fraction`.
- Differential tests against an independent all-pairs oracle.

## Input contract

The first version is deliberately restricted to non-vertical segments with distinct integer endpoints, unique IDs, no shared endpoints, no endpoint-on-segment contacts, no collinear overlaps, no multiway intersections and no two distinct event points sharing an x-coordinate.

Some restrictions are checked directly (vertical segments, duplicate IDs, shared endpoints and overlaps encountered during neighbour checks). The remaining general-position conditions are preconditions, not exhaustively validated. Do not pass arbitrary GIS linework and assume unsupported degeneracies will be detected.

## Complexity: abstract algorithm versus this code

With a priority queue and balanced status tree, the classical algorithm runs in `O((n+k) log n)` under its assumptions, where `n` is the number of segments and `k` is the number of reported intersecting pairs.

This teaching implementation uses a Python list for the status so insertion, removal and neighbour changes are easy to inspect. Those operations can take `O(n)` time. A conservative bound for this version is `O((n+k)n + (n+k) log(n+k))`, excluding arithmetic bit complexity. It does **not** achieve the classical balanced-tree bound.

## Limitations

This is not a production GIS overlay engine. It does not support vertical segments, shared endpoints, endpoint-on-segment contacts, multiway crossings, coincident event points or collinear overlaps. Exact arithmetic does not replace a complete degeneracy policy.
