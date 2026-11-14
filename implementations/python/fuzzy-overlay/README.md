# Boolean and fuzzy overlay in Python

This package demonstrates logical overlay of Boolean masks and common fuzzy combination operators on aligned two-dimensional arrays.

## Install and test

    python -m pip install numpy pytest
    python -m pytest -q

## Example

    import numpy as np
    from fuzzy_overlay import boolean_overlay, fuzzy_overlay

    protected_area = np.array([[True, False], [False, False]])
    outside_flood_zone = np.array([[True, True], [False, True]])
    eligible = boolean_overlay([~protected_area, outside_flood_zone], "and")

    access = np.array([[0.2, 0.8], [0.7, 0.4]])
    terrain = np.array([[0.7, 0.5], [0.8, 0.9]])
    graded = fuzzy_overlay([access, terrain], "gamma", gamma=0.8)

## Contract and limitations

- Layers must be non-empty, aligned, non-empty 2D arrays. This code cannot verify geotransforms or coordinate reference systems; matching array shapes alone do not prove spatial alignment.
- Boolean layers must have Boolean dtype.
- Fuzzy values must be finite or non-finite NoData, with finite values in [0,1].
- Fuzzy NoData uses a strict common-footprint rule.
- Gamma is bounded to [0,1]; gamma=0 returns fuzzy product and gamma=1 returns probabilistic sum.
- This is a numerical teaching baseline, not a complete GIS raster processing package. It does not derive membership curves, resample rasters or validate the conceptual model.

See the [method lesson](../../../methods/boolean-and-fuzzy-overlay.md) and [intern walkthrough](implementation-walkthrough.md).
