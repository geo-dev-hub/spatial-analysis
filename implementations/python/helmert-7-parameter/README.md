# Helmert seven-parameter transformation (Position Vector)

A NumPy implementation of the small-angle, geocentric Position Vector convention. It transforms Cartesian XYZ coordinates using three translations, three rotations and a scale correction.

## Install and test

    python -m pip install numpy pytest
    python -m pytest -q

## Example

    import numpy as np
    from helmert import helmert_position_vector

    xyz_wgs72 = np.array([[3657660.66, 255768.55, 5201382.11]])
    xyz_wgs84 = helmert_position_vector(
        xyz_wgs72,
        translations=[0, 0, 4.5],
        rotations_arcsec=[0, 0, 0.554],
        scale_ppm=0.219,
    )
    print(xyz_wgs84)

The result is approximately [3657660.78, 255778.43, 5201387.75] metres.

## Contract and limitations

- Input is a non-empty array of geocentric XYZ coordinates with shape (n, 3).
- Coordinate and translation units must match, normally metres.
- Rotations use arc-seconds; scale correction uses ppm.
- The rotation convention is Position Vector (EPSG method 1033), not Coordinate Frame.
- The rotation matrix uses the small-angle approximation.
- The inverse uses the inverse matrix, not naive parameter sign reversal.
- This is not a full CRS operation: geographic/geocentric conversion, ellipsoid selection, datum grids, area of use and coordinate epochs are outside scope.

See the [method lesson](../../../methods/helmert-7-parameter.md) and [intern walkthrough](implementation-walkthrough.md).
