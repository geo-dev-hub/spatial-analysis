# TOPSIS in Python

A transparent small-matrix implementation of classical TOPSIS using vector normalisation, weighted Euclidean distances and relative closeness to positive and negative ideal solutions.

## Install and test

    python -m pip install numpy pytest
    python -m pytest -q

## Example

    import numpy as np
    from topsis import topsis

    # Rows are candidate sites; columns are access (benefit) and cost (cost).
    result = topsis(
        np.array([[80, 20], [60, 10], [90, 40]], dtype=float),
        weights=[0.5, 0.5],
        benefit=[True, False],
    )
    print(result.scores)
    print(result.ranking)

Ranking contains row indices, ordered from highest relative closeness to lowest.

## Contract and limitations

- Rows are alternatives; columns are criteria.
- All measurements must be finite and non-negative. Vector normalisation is not appropriate for every data type; transform signed or otherwise unsuitable measurements using a justified alternative before use.
- Weights are finite, non-negative and normalised internally.
- Benefit direction must be a Boolean vector.
- A zero-norm criterion is rejected.
- Identical alternatives produce zero distance to both ideals; the implementation returns 0.5 for this undefined closeness case.
- The method is compensatory and relative to the supplied alternative set. It is not a spatial raster overlay or probability model.

See the [TOPSIS method lesson](../../../methods/topsis.md) and [intern walkthrough](implementation-walkthrough.md).
