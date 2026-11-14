# Intern walkthrough: affine georeferencing

## 1. Build the design matrix

For each source control point (u,v), create one row [1,u,v]. The first column estimates translation; the other two estimate the contribution from each source axis.

## 2. Solve both target coordinates together

The target matrix has one column for x and one for y. NumPy least squares solves the two coefficient vectors against the same design matrix.

## 3. Check rank before trusting the fit

The design matrix must have rank three. Three collinear controls do not span a 2D plane and cannot uniquely determine all six affine parameters. The implementation raises an error instead of returning an unstable result.

## 4. Inspect residuals

Residual vectors are target minus fitted coordinates. Their directions can reveal systematic errors that a single RMSE hides. Plot them at control-point locations and inspect spatial patterns before accepting a georeferencing result.

## 5. Respect raster coordinate conventions

A raster geotransform maps pixel/line coordinates to map coordinates. GDAL defines the upper-left corner of the upper-left pixel at pixel/line (0,0); its centre is (0.5,0.5). Make sure the control points use the same convention as the raster metadata and digitising workflow.

## 6. Choose a more flexible model only with evidence

If residuals show systematic local deformation, an affine model may be insufficient. Polynomial or thin-plate spline models are more flexible but can overfit and extrapolate poorly. Preserve controls and compare models with independent checkpoints, not only fitting residuals.
