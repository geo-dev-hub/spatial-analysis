# Intern walkthrough: Horn slope and aspect

## 1. Start with the elevation surface

The input is a regular raster grid. Horizontal cell spacing and elevation units matter: a vertical change of one metre over one metre is not the same gradient as one metre over one degree of longitude. This baseline expects projected horizontal distances and a declared vertical conversion factor.

## 2. Estimate the derivatives

For each 3×3 neighbourhood:

$$
\begin{matrix}a&b&c\\d&e&f\\g&h&i\end{matrix}
$$

The east-positive derivative is:

$$z_x=\frac{(c+2f+i)-(a+2d+g)}{8\Delta x}$$

Rows increase southward, so the north-positive derivative is:

$$z_y=\frac{(a+2b+c)-(g+2h+i)}{8\Delta y}$$

Multiply both by the vertical-unit conversion factor.

## 3. Convert gradient to slope

$$p=\sqrt{z_x^2+z_y^2}$$

$$\theta=\tan^{-1}(p)\frac{180}{\pi},\qquad S_{\%}=100p$$

A 100% grade corresponds to 45 degrees.

## 4. Convert gradient to downslope aspect

Aspect is clockwise from north and points downhill:

$$\alpha=\operatorname{atan2}(-z_x,-z_y)\pmod{360^\circ}$$

A flat cell has no unique downslope direction, so its aspect is NaN.

## 5. NoData and edge policy

A complete 3×3 neighbourhood is required. The outermost raster row and column remain NaN. Any neighbourhood containing a non-finite value is also masked. This conservative policy avoids estimating gradients across missing terrain.

## 6. Limitations and tests

Horn's operator is one estimator, not a universal terrain truth. Results depend on DEM resolution, noise, projection, vertical datum and preprocessing. This package does not calculate curvature, sky-view factor or hydrological flow direction.

Tests use planes with known gradients, rectangular cell spacing, unit conversion, flats, NoData and small arrays. Compare with other GIS software only after matching the derivative algorithm, units, aspect convention and edge handling.
