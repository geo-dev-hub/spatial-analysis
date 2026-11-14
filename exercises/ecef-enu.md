# Exercise: move from global coordinates to a local ENU frame

## Part A — Name the frames

1. Explain the difference between geodetic longitude/latitude/height and ECEF XYZ.
2. Why is geodetic latitude not the same as geocentric latitude?
3. Why must the local ENU origin be stated?
4. What is the difference between ellipsoidal and orthometric height?

## Part B — Predict before running

Use a local origin at longitude 5°, latitude 55°, ellipsoidal height 200 m.

1. What ENU coordinates should the origin itself have?
2. If a point is directly above the origin by 100 m in ellipsoidal height, what should its local Up coordinate be approximately?
3. Which direction should East increase when the origin is on the equator at longitude 0°?
4. Why does the local frame rotate when the origin moves?

## Part C — Reproduce the published example

Run the package tests and notebook. The EPSG:9836 example uses the origin above and an ECEF target of (3771793.968, 140253.342, 5124304.349) metres.

1. Record the computed East, North and Up values.
2. Compare them with the published result.
3. Explain why the test is valuable for catching sign and axis-order errors.

## Part D — Test the transformation

1. Convert several geodetic points to ECEF and then to ENU.
2. Convert the ENU coordinates back to ECEF.
3. Calculate the maximum absolute round-trip error.
4. Repeat with a spherical ellipsoid. Which coordinates change?
5. Move the local origin and explain how the ENU coordinates change.

## Part E — Apply it to a spatial problem

Imagine a survey team measuring assets around a facility. Explain when a local ENU frame is useful and when a projected coordinate reference system or full geodetic workflow is more appropriate.

Do not treat local ENU as a global map projection. State the ellipsoid, horizontal reference frame, height type and local origin in every reproducible result.
