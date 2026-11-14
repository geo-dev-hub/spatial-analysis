# From scattered observations to a surface

This path connects a simple distance-weighted estimate to spatially modelled interpolation. Work through the assumptions before choosing a method for a real dataset.

## 1. Start with inverse distance weighting

Read [Inverse distance weighting](../algorithms/interpolation/inverse-distance-weighting.md) and run the [IDW visual lab](../notebooks/inverse-distance-weighting-lab.ipynb). Change the power parameter and neighbourhood size. IDW is deterministic and does not provide a model-based prediction variance.

## 2. Understand spatial variation

Continue with [Spatial interpolation: IDW and ordinary kriging](../algorithms/geostatistics/interpolation.md). The lesson includes empirical semivariogram summaries and explains how the assumed spatial dependence model changes the kriging calculation. The teaching baseline does not fit variogram parameters or cover the full kriging family.

## 3. Validate away from sampled locations

Read [Spatial cross-validation](../methods/spatial-cross-validation.md). Compare random splits with spatially separated folds and record how the validation design changes the interpretation of predictive performance.

## 4. Extend carefully

Natural-neighbour interpolation, splines, radial basis functions, anisotropy, co-kriging, large-data Gaussian processes, simulation and spatiotemporal models require separate assumptions and validation.

## Working checklist

- State the coordinate reference system and distance units.
- Inspect duplicate locations, missing values and sampling density.
- Record neighbourhood and parameter choices.
- Distinguish interpolation from extrapolation.
- Validate using a design that reflects where predictions will be made.
- Report prediction uncertainty only when the method actually estimates it.
