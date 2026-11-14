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

## 7. Add local hillshade

Hillshade is a visualization derived from slope, aspect and a hypothetical light source. With sun altitude h, sun azimuth A and terrain slope θ, the normalized local illumination is:

$$I=\sin(h)\cos(\theta)+\cos(h)\sin(\theta)\cos(A-\alpha)$$

where α is downslope aspect, clockwise from north. The implementation clips the result to [0, 1]. A flat surface has no unique aspect; for zero slope it uses I=sin(h). Missing derivative values remain missing.

This is a local illumination model only. It does not determine whether another ridge blocks the light, and it is not a solar-radiation model.

## 8. Calculate the topographic wetness index

The terrain_indices module applies:

$$\mathrm{TWI}=\ln\left(\frac{a}{\tan\beta}\right)$$

where a is specific catchment area in metres and β is slope in radians. It accepts area and slope as aligned arrays. The input area is not raw cell-count accumulation: it must already be converted to specific catchment area using a declared cell geometry and flow-routing convention.

A zero slope makes the denominator zero. The function therefore uses a positive, caller-declared slope floor (default 0.1°). This parameter affects flat and near-flat cells and must be reported. The index is not a direct soil-moisture measurement.
