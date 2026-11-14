# Intern walkthrough: Helmert seven-parameter transformation

## 1. Confirm the coordinate domain

The function accepts geocentric Cartesian XYZ coordinates, not longitude, latitude and height. These values are normally measured in metres from the Earth's centre.

## 2. Read the parameter units

Translations use the same linear unit as the coordinates. Rotations arrive in arc-seconds and are converted to radians. Scale correction arrives in ppm and is converted to a dimensionless multiplier using 1 + ppm × 10⁻⁶.

## 3. Build the Position Vector matrix

The implementation uses the small-angle matrix:

    [[ 1, -rz, +ry],
     [+rz,  1, -rx],
     [-ry, +rx,  1]]

This is the Position Vector convention. Coordinate Frame rotations use the opposite signs. Never copy parameters between conventions without converting their signs.

## 4. Apply the transformation

The forward calculation multiplies the source vector by the scaled rotation matrix, then adds translations. The code vectorises this calculation across all input points.

## 5. Reverse the operation

The inverse solves the linear system using the same matrix. Simply negating all seven parameters is not a reliable substitute for inverting the transformation matrix.

## 6. Compare against an authoritative example

The tests use the published WGS 72 to WGS 84 geocentric example from IOGP Guidance Note 7-2. Matching a published example is stronger than only testing that the function is self-consistent.

## 7. What a complete datum operation requires

A full geographic datum transformation commonly converts source longitude/latitude/ellipsoidal height to geocentric XYZ, applies the geocentric operation, then converts XYZ to the target geographic CRS. A real operation may also require grid files, a coordinate epoch, a vertical datum and a defined area of use.

## 8. Extension exercise

Add the Coordinate Frame convention as a separately named option. Test it by reversing the signs of the three rotations while keeping translation and scale fixed, then reproduce the same target coordinates. Do not hide the convention behind an undocumented Boolean.
