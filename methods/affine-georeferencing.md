# Affine georeferencing from ground control points

An affine transformation maps two-dimensional source coordinates to target coordinates using translation, rotation, scale and shear. In raster georeferencing, source coordinates are often pixel/line positions and target coordinates are map coordinates.

It preserves straight lines and parallelism, but not necessarily lengths, angles or area. It cannot represent arbitrary local rubber-sheet distortion.

## The six-parameter model

For source point (u,v) and target point (x,y):

\[
x=a_0+a_1u+a_2v,\qquad
y=b_0+b_1u+b_2v.
\]

The six coefficients are often stored as a 3×2 matrix:

\[
C=
\begin{bmatrix}
a_0&b_0\\
a_1&b_1\\
a_2&b_2
\end{bmatrix}.
\]

For n ground control points, construct the design matrix:

\[
A=
\begin{bmatrix}
1&u_1&v_1\\
1&u_2&v_2\\
\vdots&\vdots&\vdots\\
1&u_n&v_n
\end{bmatrix},
\quad
B=
\begin{bmatrix}
x_1&y_1\\
x_2&y_2\\
\vdots&\vdots\\
x_n&y_n
\end{bmatrix}.
\]

Estimate coefficients by least squares:

\[
\hat C=\arg\min_C\|AC-B\|_F^2.
\]

At least three non-collinear control points are required for a unique affine fit. More points allow an overdetermined least-squares estimate and residual inspection.

## Pixel coordinates are not always pixel centres

GDAL's geotransform maps pixel/line coordinates to georeferenced coordinates. Its origin convention uses the upper-left corner of the upper-left pixel; the centre of that pixel is at (0.5,0.5). Mixing corner and centre conventions can introduce a half-pixel shift.

The implementation in this package is a general 2D affine fit. It does not silently assume pixel coordinates or a particular raster convention; the caller must define the source coordinates consistently.

## Residuals and control-point quality

After fitting, calculate residual vectors:

\[
e_i=\hat p_i-p_i.
\]

Inspect residual direction and magnitude, not only a single RMSE. Large or spatially patterned residuals may indicate an incorrect point match, local distortion, a poor transformation model or an error in the control-point coordinates.

Do not remove a control point only because it worsens RMSE. Investigate the source and document any exclusion.

## When affine is not enough

- Polynomial transformations can represent broader smooth distortions but may behave poorly outside the control-point footprint.
- Thin-plate splines and rubber-sheeting can model local deformation, but may warp regions between sparse controls and can extrapolate badly.
- Image co-registration is a separate problem of finding corresponding features or estimating alignment; the transformation model is only one part of that workflow.

Choose the simplest model that fits the evidence and intended use. Preserve the original image and control-point record.

## Implementation

- [Tested NumPy affine fitting baseline](../implementations/python/affine-georeferencing/README.md)
- [Intern walkthrough](../implementations/python/affine-georeferencing/implementation-walkthrough.md)
- [CRS transformation foundations](../learning-paths/geodesy-foundations.md)

## References

- GDAL documentation. Geotransform Tutorial. https://gdal.org/en/stable/tutorials/geotransforms_tut.html
- GDAL documentation. Raster Data Model: Affine GeoTransform and GCPs. https://gdal.org/en/stable/user/raster_data_model.html
- GDAL C API. GDALGCPsToGeoTransform: first-order fit from ground control points. https://gdal.org/en/stable/api/raster_c_api.html

This implementation is a small least-squares teaching baseline, not a full image-registration or rubber-sheeting system.
