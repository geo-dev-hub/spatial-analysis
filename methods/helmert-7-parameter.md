# Helmert seven-parameter transformation in geocentric coordinates

A seven-parameter Helmert transformation relates Cartesian coordinates in one geocentric reference frame to Cartesian coordinates in another using three translations, three small rotations and one scale correction. It is commonly called a Bursa–Wolf transformation.

This lesson implements the **Position Vector** convention for geocentric Cartesian coordinates. The rotation convention is part of the method: parameters from the Coordinate Frame convention have opposite rotation signs and must not be passed into this implementation unchanged.

## Coordinate domain and parameters

The input and output are geocentric Cartesian coordinates (X,Y,Z), normally expressed in metres. Parameters are:

- translations tX, tY, tZ in the same linear unit as the coordinates;
- rotations rX, rY, rZ in arc-seconds;
- scale correction dS in parts per million (ppm).

Convert rotations to radians and scale to a dimensionless multiplier:

\[
r_{\mathrm{rad}}=r_{\mathrm{arcsec}}\frac{\pi}{180\cdot3600},
\qquad M=1+dS\cdot10^{-6}.
\]

Under the small-angle Position Vector convention, the rotation matrix is approximated by:

\[
R\approx
\begin{bmatrix}
1&-r_Z&r_Y\\
r_Z&1&-r_X\\
-r_Y&r_X&1
\end{bmatrix}.
\]

The forward operation is:

\[
\begin{bmatrix}X_T\\Y_T\\Z_T\end{bmatrix}
=
M R
\begin{bmatrix}X_S\\Y_S\\Z_S\end{bmatrix}
+
\begin{bmatrix}t_X\\t_Y\\t_Z\end{bmatrix}.
\]

The implementation uses the inverse of the same linear matrix for reverse transformation. It does not simply negate every parameter, which is not generally an exact inverse when scale and rotations interact.

## Worked EPSG/IOGP example

The IOGP Guidance Note 7-2 gives a WGS 72 to WGS 84 geocentric example using:

- translations (0, 0, +4.5) m;
- rotations (0, 0, +0.554) arc-seconds;
- scale correction +0.219 ppm.

Input:

\[
(X_S,Y_S,Z_S)=(3657660.66,\ 255768.55,\ 5201382.11)\ \mathrm{m}.
\]

The Position Vector transformation gives approximately:

\[
(X_T,Y_T,Z_T)=(3657660.78,\ 255778.43,\ 5201387.75)\ \mathrm{m}.
\]

The test suite reproduces this published example within a stated numerical tolerance.

## The rotation-convention trap

The Coordinate Frame convention uses the opposite signs for the rotation parameters. The translation and scale definitions are the same, but the rotation matrix differs. Always record the convention alongside the seven values.

The code also does not convert geographic longitude/latitude/ellipsoidal height to geocentric XYZ. A complete datum operation commonly requires:

1. geographic-to-geocentric conversion using the source ellipsoid;
2. a geocentric Helmert transformation;
3. geocentric-to-geographic conversion using the target ellipsoid.

It does not choose a transformation from an EPSG database, apply grid shifts, model a coordinate epoch or handle time-dependent 14-parameter transformations.

## Implementation

- [Tested Position Vector Python implementation](../implementations/python/helmert-7-parameter/README.md)
- [Intern walkthrough](../implementations/python/helmert-7-parameter/implementation-walkthrough.md)
- [CRS transformation foundations](../learning-paths/geodesy-foundations.md)

## References

- IOGP (2019). *Geomatics Guidance Note 7, Part 2: Coordinate Conversions and Transformations including Formulas*. Publication 373-7-2, Section 4.2.3. https://www.iogp.org/wp-content/uploads/2019/09/373-07-02.pdf
- EPSG. Position Vector transformation (geocentric domain), method 1033. https://epsg.io/1033-method
- PROJ documentation. Helmert transform. https://proj.org/en/stable/operations/transformations/helmert.html

This is a small-angle, geocentric Position Vector implementation. For production datum transformations, use an authoritative coordinate operation with the correct area of use, epoch, grids and convention.
