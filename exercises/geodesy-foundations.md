# Geodesy and georeferencing exercises

Use the [Geodesy foundations path](../learning-paths/geodesy-foundations.md), [Helmert transformation lesson](../methods/helmert-7-parameter.md) and [affine georeferencing lesson](../methods/affine-georeferencing.md).

## 1. Coordinate meaning

- Explain why a pair of numbers is not a complete coordinate without a CRS.
- Distinguish geographic longitude/latitude from projected easting/northing and geocentric XYZ.
- Explain why changing a CRS label without transforming coordinate values is not a coordinate operation.
- Identify when pixel coordinates should refer to pixel corners versus pixel centres.

## 2. Reproduce the Helmert example

Run the [Helmert implementation](../implementations/python/helmert-7-parameter/README.md).

- Reproduce the published WGS 72 to WGS 84 geocentric example.
- Convert 0.554 arc-seconds to radians by hand.
- Convert +0.219 ppm into a dimensionless scale multiplier.
- Change the Z rotation sign and compare the output.
- Explain why Position Vector and Coordinate Frame conventions cannot share rotation values without sign conversion.

## 3. Understand the complete datum operation

Draw a three-stage diagram:

1. source geographic coordinates to source geocentric XYZ;
2. geocentric Helmert operation;
3. target geocentric XYZ to target geographic coordinates.

Annotate the source and target ellipsoids. Identify where grid shifts, coordinate epoch and vertical datum may be required. Explain why the seven-parameter function in this repository is only the middle stage.

## 4. Fit an affine transformation

Run the [affine georeferencing implementation](../implementations/python/affine-georeferencing/README.md).

- Create four non-collinear source control points and transform them with known coefficients.
- Fit the coefficients from the controls and compare them with the known values.
- Add a small error to one target control point. Inspect residual vectors and RMSE.
- Make all source controls collinear and explain why the affine fit is rank deficient.
- Compare a three-control exact fit with a least-squares fit using more controls.

## 5. Inspect pixel conventions

Use the GDAL geotransform convention in the lesson.

- Calculate the map coordinate for pixel/line (0,0).
- Calculate the coordinate for the centre of the upper-left pixel at (0.5,0.5).
- Quantify the half-pixel offset for a 10 m square pixel.
- Explain why the same control points interpreted with different pixel conventions create a systematic shift.

## 6. Design a quality report

Write a short georeferencing report that records the source and target CRS, transformation method, parameter convention, units, control-point source, residual vectors, independent checkpoints, pixel convention, area of use and limitations.

Do not report fitting RMSE as independent positional accuracy. Use independent checkpoints for that claim.
