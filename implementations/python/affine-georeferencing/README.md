# Affine georeferencing from control points

A NumPy-only least-squares implementation of the six-parameter 2D affine model. It fits source control coordinates to target coordinates and returns coefficients, residual vectors, RMSE and design-matrix rank.

## Install and test

    python -m pip install numpy pytest
    python -m pytest -q

## Example

    import numpy as np
    from affine_georeferencing import apply_affine, fit_affine

    pixel_line = np.array([[0, 0], [100, 0], [0, 100], [100, 100]])
    map_xy = np.array([[500000, 9800000], [500100, 9800010],
                       [499990, 9799900], [500090, 9799910]])
    fit = fit_affine(pixel_line, map_xy)
    transformed = apply_affine(pixel_line, fit.coefficients)

    print(fit.coefficients)
    print(fit.rmse)
    print(fit.residual_vectors)

## Contract and limitations

- Source and target arrays must have matching shape (n, 2), with at least three controls.
- Three non-collinear controls determine an exact affine transform; additional controls produce a least-squares fit.
- Residual vectors are target minus fitted target coordinates; RMSE is the root mean squared Euclidean residual.
- Coordinates must be finite. The fit rejects rank-deficient source control geometry.
- The caller defines coordinate meaning and units. For raster georeferencing, document whether pixel coordinates refer to pixel corners or centres.
- No outlier rejection, robust estimation, polynomial transform, thin-plate spline, image matching or CRS conversion is performed.

See the [method lesson](../../../methods/affine-georeferencing.md) and [intern walkthrough](implementation-walkthrough.md).
