# Hierarchical spatial k-anonymity: walkthrough

## Goal

Replace each precise point with a coarser quadtree cell shared by at least k records. The released location group therefore contains no fewer than k records from the input population.

## Adaptive partition rule

Start with a padded square containing all points. At each node, divide the square into four equal children. Split the node only when every non-empty child has at least k records. If any occupied child would contain fewer than k records, stop splitting and generalise every point in that node to the parent cell. Continue recursively for safe children. At the maximum depth, retain the current cell. If the full input contains fewer than k records, suppress all locations.

This produces disjoint groups: every published record belongs to exactly one cell, and every emitted cell has at least k records.

## Output

The function returns a group ID per input row, a suppression mask, and each group’s record count, cell bounds and hierarchy depth. Group IDs are local to the current call and are not stable identifiers.

## Limitations

- This is location-only k-anonymity over the supplied records, not a guarantee against all re-identification.
- Other released attributes can break equivalence; population definition, auxiliary data, temporal linkage and overlapping releases matter.
- The algorithm uses a quadtree over a square planar coordinate domain. Use an appropriate projected CRS and document its units.
- It does not implement l-diversity, t-closeness, differential privacy, or a global optimal utility/privacy trade-off.
- Generalised cells may be large where sparse points force parent-level aggregation. Suppression may be preferable in some applications.
- The function is a teaching baseline; a production release needs a threat model and review of the complete released dataset.

## Reproduce

Run the spatial privacy package test suite with python -m pytest -q.
