# AHP priority weights in Python

This package demonstrates one computational step in the Analytic Hierarchy Process: deriving a normalised priority vector from a positive reciprocal pairwise-comparison matrix using its principal right eigenvector.

It does not elicit judgements, build a hierarchy, validate stakeholder evidence, standardise GIS layers or combine spatial criteria.

## Install and test

    python -m pip install numpy pytest
    python -m pytest -q

## Example

    import numpy as np
    from ahp_weights import ahp_weights

    matrix = np.array([
        [1,   3,   5],
        [1/3, 1,   2],
        [1/5, 1/2, 1],
    ], dtype=float)

    result = ahp_weights(matrix, ["road_access", "terrain", "low_flood_exposure"])
    print(result.weights)
    print(result.consistency_ratio)

The weights sum to one. CR is None for matrices of order one or two because the conventional random-index reference is zero at those orders.

## Input contract and limitations

- Matrix must be non-empty, square, finite and strictly positive.
- Diagonal entries must equal one; reciprocal entries must satisfy a_ij * a_ji = 1 within numerical tolerance.
- Optional criterion names must be unique and match matrix order.
- The implementation uses NumPy's eigensolver: a small dense teaching baseline, not a specialised large-scale solver.
- The conventional random-index table is included only for orders 1–10; no extrapolation is silently invented.
- CR is a diagnostic, not proof of validity or a universal pass/fail test.

See the [AHP method lesson](../../../methods/analytic-hierarchy-process.md) and [intern walkthrough](implementation-walkthrough.md).
