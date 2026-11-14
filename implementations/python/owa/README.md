# Ordered Weighted Averaging in Python

This package implements standard OWA and the GIS weighted OWA variant. Values are sorted independently at each cell; order weights attach to sorted positions. In the GIS weighted variant, named criterion importance weights are reordered with the values.

## Install and test

    python -m pip install numpy pytest
    python -m pytest -q

## Example

    import numpy as np
    from owa import ordered_weighted_averaging, orness

    access = np.array([[0.1, 0.8]])
    terrain = np.array([[1.0, 0.4]])
    score = ordered_weighted_averaging([access, terrain], [0.75, 0.25])
    print(score)
    print(orness([0.75, 0.25]))

## Contracts and limitations

- Inputs are non-empty, aligned 2D arrays; matching shapes do not prove matching geotransforms or CRS.
- Finite scores must lie in [0,1] and larger must mean more preferred.
- Order weights are non-negative, match the number of layers and sum to one.
- Optional criterion weights are non-negative, match the layer count and have positive sum; they are normalised internally.
- Any non-finite criterion value makes that output cell NoData.
- If order weights assign all mass to positions whose reordered criterion importance is zero, that cell is undefined and returned as NoData.
- This implementation does not derive weights, standardise criteria, align rasters or validate a real decision.

See the [OWA method lesson](../../../methods/ordered-weighted-averaging.md) and [intern walkthrough](implementation-walkthrough.md).
