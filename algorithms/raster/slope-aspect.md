# Terrain slope and aspect with Horn's 3×3 operator

Stable ID: SA-RASTER-HORN-SLOPE-ASPECT · Draft 0.1 · Source compendium section 4, page 6

## What the derivatives describe

A DEM is a sampled elevation surface. Slope describes steepness; aspect describes the direction of steepest descent. Both are local derivatives, so estimates depend on neighbourhood, cell spacing, elevation units and missing-value policy.

This lesson uses Horn's weighted 3×3 finite-difference operator. It is a transparent baseline, not a claim that every GIS package uses the same estimator.

## The 3×3 neighbourhood

Label elevations:

$$
\begin{matrix}a&b&c\\d&e&f\\g&h&i\end{matrix}
$$

Let Δx and Δy be horizontal cell spacing. The east-positive and north-positive derivatives are:

$$z_x=\frac{(c+2f+i)-(a+2d+g)}{8\Delta x}$$

$$z_y=\frac{(a+2b+c)-(g+2h+i)}{8\Delta y}$$

The sign of zy accounts for raster rows increasing southward. If elevation units differ from horizontal units, multiply both derivatives by a declared vertical conversion factor.

## Slope

$$p=\sqrt{z_x^2+z_y^2}$$

$$\theta=\tan^{-1}(p)\frac{180}{\pi},\qquad S_{\%}=100p$$

A 100% grade is a 45° slope. Degrees and percent rise are different units.

## Downslope aspect

Aspect is measured clockwise from north:

$$\alpha=\operatorname{atan2}(-z_x,-z_y)\pmod{360^\circ}$$

A plane rising eastward faces westward downslope (270°). A plane rising northward faces southward (180°). A perfectly flat cell has no unique aspect.

## Grid, units and NoData

The [Python baseline](../../implementations/python/terrain-derivatives/README.md) requires positive cell spacing and a positive vertical conversion factor. It expects a regular grid in a suitable projected coordinate system. A geographic longitude/latitude grid has spatially varying ground distances and should not be treated as metres.

The implementation uses a strict 3×3 validity rule: borders and any window containing NoData return NaN. Other software may interpolate gaps or use another edge rule; comparisons must align these choices.

## Interpretation cautions

Slope is sensitive to DEM resolution and noise. Aspect becomes unstable on nearly flat terrain. Horizontal and vertical units must be compatible. Resampling changes the sampled surface and therefore its derivatives. Horn slope/aspect does not calculate curvature, visibility, solar radiation or flow direction.

## Exercises

1. Derive slope and aspect for a plane rising one metre per metre eastward.
2. Repeat with a north-rising plane. Explain the aspect sign.
3. Change horizontal spacing while holding elevation differences fixed.
4. Insert one NoData cell. Which output neighbourhoods become invalid?
5. Compare Horn with central-difference or Zevenbergen–Thorne estimators, matching units and edge policy.

## References

- Horn, B. K. P. (1981), *Hill shading and the reflectance map*, Proceedings of the IEEE, 69(1), 14–47.
- Burrough, P. A. and McDonnell, R. A. (1998), *Principles of Geographical Information Systems*, Oxford University Press.

**Scope:** local Horn 3×3 slope and downslope aspect only; no curvature, multiscale derivatives, geographic-grid correction or DEM conditioning.
