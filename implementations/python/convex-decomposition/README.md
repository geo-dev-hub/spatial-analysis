# Convex decomposition by triangulation and greedy merging

This package triangulates one simple polygon ring with the repository's exact-predicate ear-clipping implementation, then greedily merges adjacent pieces whenever the merged boundary remains convex.

## Run the tests

```bash
python -m pip install -r requirements.txt
PYTHONPATH=../ear-clipping python -m pytest -q
```

## Scope

- One simple, non-degenerate polygon ring; no holes or self-intersections.
- Exact rational predicates through `fractions.Fraction`.
- The output is a set of convex pieces whose areas sum exactly to the input area.
- Greedy merge order affects the partition. The result is not guaranteed to use the fewest possible pieces.
- This is a teaching baseline, not a complexity-optimized or certified Hertel–Mehlhorn implementation.

The initial triangulation uses the current ear-clipping package, whose transparent implementation has an (O(n^3)) worst-case bound. The merge pass also uses straightforward repeated pair scans. Do not attribute the linear-time bound of a specialized Hertel–Mehlhorn post-processing algorithm to this package.
