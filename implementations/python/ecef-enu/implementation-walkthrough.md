# Intern walkthrough: geodetic coordinates to local ENU

## Goal

Move between a global Earth-fixed frame and a local Cartesian frame. This is useful when local distances and directions matter: GNSS, surveying, sensor placement, robotics, local transport models and engineering analysis.

## 1. Name the coordinate frame before calculating

A triple of numbers is not enough. Record:

- the horizontal reference frame / datum;
- whether coordinates are geodetic longitude and latitude or geocentric XYZ;
- the ellipsoid;
- angular units and axis order;
- height type and vertical datum;
- the local ENU origin.

The package uses WGS 84 by default, longitude then latitude in degrees, metres for XYZ and ellipsoidal height.

## 2. Convert geodetic coordinates to ECEF

The function `geodetic_to_ecef` computes the prime-vertical radius and then X, Y and Z. Study the equator and pole tests. At longitude 0°, latitude 0° and zero height, X equals the semi-major axis and Y and Z are zero.

## 3. Define the local origin

The origin is supplied as longitude, latitude and ellipsoidal height. It is converted to ECEF. The difference between a target and this origin is the vector that will be rotated.

A target equal to the origin must become (0, 0, 0) in ENU.

## 4. Rotate ECEF differences into ENU

The rotation matrix uses the origin's geodetic latitude and longitude. Its rows are the local East, North and Up unit vectors expressed in ECEF coordinates.

The output order is always (East, North, Up). Do not swap North and East or silently treat latitude as longitude.

## 5. Reverse the operation

The inverse is the transpose of the orthonormal rotation matrix, followed by adding the ECEF origin. The round-trip test verifies that an ECEF point survives ECEF → ENU → ECEF.

## 6. Reproduce an external reference example

The tests reproduce the EPSG:9836 example with a topocentric origin at longitude 5°, latitude 55°, ellipsoidal height 200 m. The published ECEF target is transformed to approximately:

- East: −189,013.869 m
- North: −128,642.040 m
- Up: −4,220.171 m

This is a useful independent check of signs and axis order.

## 7. Interpret height correctly

Ellipsoidal height is measured along the ellipsoid normal. Orthometric height is related to the geoid and is commonly used for elevations. They are not interchangeable. A local ENU conversion does not perform a vertical-datum transformation.

## 8. Suggested investigations

1. Move the origin east while holding latitude fixed. How does the local frame rotate?
2. Compare the same point using a spherical ellipsoid and WGS 84.
3. Convert a point 100 m directly above the origin. What ENU values do you expect?
4. Why is ENU a local frame rather than a global projection?
5. What happens to local directions when the origin moves across the antimeridian?
