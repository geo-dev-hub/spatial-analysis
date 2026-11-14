# Local analytical hillshade from slope and aspect

Stable ID: SA-RASTER-LOCAL-HILLSHADE · Draft 0.1 · Source compendium section 4, page 6

## Purpose

Hillshade is a terrain-visualisation method. It estimates how strongly a hypothetical light source illuminates each terrain surface element from its local slope and aspect. It is not a terrain derivative itself: it uses derivatives estimated by a separate method such as [Horn slope and aspect](slope-aspect.md).

## Illumination model

Let θ be slope, α be downslope aspect measured clockwise from north, h be sun altitude above the horizon and A be sun azimuth clockwise from north. The normalized local illumination is:

$$I=\sin(h)\cos(\theta)+\cos(h)\sin(\theta)\cos(A-\alpha)$$

The teaching implementation clips I to [0, 1]. Values below zero represent surfaces facing away from the light and are rendered as zero; values above one are clipped to one.

A flat cell has no unique aspect. Its illumination is assigned as sin(h), the illumination of a horizontal surface under the chosen sun altitude.

## Inputs and conventions

The [Python implementation](../../implementations/python/terrain-derivatives/README.md) accepts slope and aspect arrays, sun azimuth and sun altitude. Angles are in degrees. Azimuth is clockwise from north; aspect is the downslope direction. The output is normalized illumination from zero (dark) to one (bright).

## What this does not model

- Terrain occlusion and cast shadows from ridges or nearby surfaces.
- Diffuse sky illumination, atmospheric scattering or multiple light sources.
- Solar irradiance, seasonal sun paths or energy budgets.
- Multidirectional hillshade or ambient-occlusion rendering.

Hillshade is useful for visual interpretation, but it is not a measurement of elevation, slope, landform or solar energy. A different sun azimuth can make the same landform appear quite different.

## Exercises

1. Illuminate an east-facing slope from the west and then from the east.
2. Change sun altitude while holding azimuth constant.
3. Explain why a flat cell has no aspect but still receives illumination.
4. Compare a single-direction hillshade with a multidirectional composite.
5. Explain why hillshade cannot show whether a distant ridge blocks the light without a terrain-occlusion calculation.

## References

- Horn, B. K. P. (1981), *Hill shading and the reflectance map*, Proceedings of the IEEE, 69(1), 14–47.
- Burrough, P. A. and McDonnell, R. A. (1998), *Principles of Geographical Information Systems*, Oxford University Press.

**Scope:** local illumination from slope/aspect and one sun position; no cast-shadow, atmospheric or physical solar-radiation model.
