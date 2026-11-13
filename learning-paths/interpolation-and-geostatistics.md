# From scattered observations to a surface

You have measurements at some locations and need to understand what may be happening between them. This path connects the ways we estimate those missing values, from simple distance-based methods to statistical models that describe spatial dependence and uncertainty.

## The route through the subject

1. **Start with a weighted average.** [Inverse distance weighting](../algorithms/interpolation/inverse-distance-weighting.md) shows how nearby observations can contribute more strongly than distant ones. **Available**
2. **Understand spatial variation.** The [empirical semivariogram](../methods/empirical-semivariogram.md) measures how differences between observations change with separation distance. It includes a tested estimator and an interactive lab. **Available**
3. **Compare deterministic surfaces.** Natural neighbour, splines, radial basis functions and trend surfaces use different geometric or mathematical ideas. These records are planned.
4. **Fit a theoretical variogram.** Learn how a model represents the empirical pattern and how nugget, sill, range and anisotropy are assessed. A dedicated lesson is planned.
5. **Build an ordinary kriging estimate.** [Ordinary kriging](../algorithms/interpolation/ordinary-kriging.md) uses the variogram model and a constrained system of equations to determine its weights. The PyKrige example and interactive prediction/variance lab are available. **Available**
6. **Look at uncertainty.** Distinguish prediction variance, prediction error and validation accuracy.
7. **Move through time.** Explore spatiotemporal models, data assimilation and change analysis after the spatial foundations are clear.

## How to use this path

Begin with the first lesson, then compare the assumptions behind each method. Do not choose an interpolation method because it creates the smoothest-looking map. Check the input data, coordinate system, spatial support and validation results.

The path is being built. Only lessons explicitly linked as available should be treated as completed material.
