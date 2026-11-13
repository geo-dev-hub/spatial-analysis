# Geodesy foundations: coordinates, projections and transformations

**Status:** First coordinate-transformation lesson published. This path begins with CRS semantics and explicit axis order; advanced geodetic operations remain open.

## 1. Understand what a coordinate means

A coordinate pair is not meaningful without a coordinate reference system (CRS). Geographic coordinates are angular; projected coordinates are generally linear. A CRS label cannot be changed without transforming the coordinates.

Read [Coordinate transformation and CRS axis order](../algorithms/geodesy/crs-transformation.md) and run the [CRS transformation notebook](../notebooks/crs-transformation-lab.ipynb). It demonstrates longitude/latitude input order, Web Mercator, UTM and round-trip conversion through PROJ.

## 2. Learn the limits of a projection

A projection maps the curved Earth to a plane. It cannot preserve every geometric property everywhere. Choose a projection based on the task:
- area measurement needs an equal-area projection or geodesic method;
- local distance and engineering tasks need an appropriate local projected CRS;
- web-map display often uses Web Mercator, but its distortion makes it unsuitable for many measurements.

## 3. Learn a geocentric datum transformation

Read [Helmert seven-parameter transformation](../methods/helmert-7-parameter.md) and run its [tested Position Vector implementation](../implementations/python/helmert-7-parameter/README.md). The example uses geocentric XYZ coordinates and explicitly names the rotation convention. It is one step in a datum operation, not a replacement for source/target ellipsoid conversions, grid shifts or epoch-aware operations.

## 4. Georeference an image with control points

Read [Affine georeferencing](../methods/affine-georeferencing.md) and run its [least-squares fitting example](../implementations/python/affine-georeferencing/README.md). The lesson covers the six-parameter 2D model, non-collinear control requirements, residual diagnostics and pixel coordinate conventions. It is not a rubber-sheeting or image-matching system.

## 5. Separate projection from datum transformation

A CRS operation may include a map projection and a datum/reference-frame transformation. High-accuracy work may require grid-shift files, a coordinate epoch, vertical datum and a specific operation. Record the operation and its resources so results can be reproduced.

## 6. What comes next

The source section also includes Helmert and Molodensky transformations, Bursa-Wolf parameters, NTv2 grids, ECEF/ENU conversions, geoid models, spherical geometry, GNSS, satellite orbits and network adjustment. These need dedicated methods, assumptions, reference data and validation.

## Exercises

1. Explain why relabelling longitude/latitude as Web Mercator is not a transformation.
2. Compare the scale and area distortion of Web Mercator and an equal-area projection.
3. Explain the meaning of always_xy.
4. List the information needed to reproduce a datum transformation with grid shifts.
5. Explain why a projected CRS appropriate for one region may be unsuitable elsewhere.
