# Spatial interpolation: estimating what we have not measured

**Status:** Introductory interpolation and empirical-semivariogram lessons are published; the wider geostatistics path is still being developed.

## The question

You have measurements at some locations, but need an estimate at another location. This path starts with a deterministic distance-weighted estimate, then introduces a model-based estimator and the uncertainty that comes with its assumptions.

## Before you begin

It helps to understand:
- coordinates and distance in a projected coordinate system;
- weighted averages;
- a mean, variance and a matrix;
- the idea that nearby observations may be spatially related.

The path introduces the empirical semivariogram as a separate method before using a theoretical variogram in the kriging system.

## Follow the path

### 1. Understand inverse distance weighting

Read [Spatial interpolation](../algorithms/geostatistics/interpolation.md), then run the [interactive lab](../notebooks/geostatistics-interpolation-lab.ipynb).

Change the power, search radius and number of neighbours. Notice that IDW is a weighted average, not a probability model.

### 2. Calculate an empirical semivariogram

Read [Empirical semivariogram](../methods/empirical-semivariogram.md) and run the [interactive binning lab](../notebooks/empirical-semivariogram-lab.ipynb). Work through pairwise distances, squared differences, lag bins and pair counts. The empirical estimate describes the sample; it is not yet a fitted covariance model.

### 3. Understand the variogram assumption

Return to [Spatial interpolation](../algorithms/geostatistics/interpolation.md). The kriging example uses an isotropic exponential semivariogram. Follow the distance scale and partial sill through the kriging matrix. They are supplied model parameters, not values that the implementation estimates automatically.

### 4. Solve the ordinary-kriging system

Work through the augmented matrix and its sum-of-weights constraint. Inspect the prediction and model-based variance separately in the [ordinary-kriging sensitivity lab](../notebooks/ordinary-kriging-lab.ipynb).

### 5. Validate in space

Use a spatially separated holdout rather than relying only on random splits. Explain what kind of geographic generalisation the split tests.

## Exercises

1. Compare IDW powers 1, 2 and 4.
2. Change the variogram range scale while holding observations fixed.
3. Move a target point from the edge of the sample network toward its centre.
4. Compare the kriging variance with held-out prediction errors. Why are they different quantities?
5. Design a spatial block cross-validation scheme for a study area you know.

## What comes next

The next lessons should cover variogram model fitting, anisotropy, universal and regression kriging, block prediction, co-kriging and scalable Gaussian-process approximations. The full source section also includes spatial simulation, space-time models, data assimilation, uncertainty propagation and small-area estimation. Those topics are not yet covered by this first lesson.
