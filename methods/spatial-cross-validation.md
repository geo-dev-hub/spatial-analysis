# Spatial cross-validation: test whether a model travels to new places

A model trained on spatial observations is often evaluated on data geographically close to its training data. Nearby observations can share land cover, infrastructure, weather, survey practices, sensor artefacts and even overlapping imagery. A random split may therefore estimate performance on familiar neighbourhoods rather than performance in a new place.

Spatial cross-validation changes the split design to match the intended deployment question. It does not automatically solve spatial dependence, confounding or distribution shift. Block size, buffer, grouping and target geography must be justified.

## Start with the prediction question

- **Interpolation:** predict in gaps surrounded by observed locations. Local validation may be relevant, but dependence still needs inspection.
- **New locations within a region:** hold out spatial blocks or clusters and separate training observations from test observations.
- **New region:** hold out whole regions, catchments, counties, ecological zones or other meaningful geographic units.
- **Future time:** hold out later dates. A spatial split alone does not prevent temporal leakage.
- **New region and future time:** hold out both dimensions to reproduce the deployment setting.

A validation design is useful only insofar as it estimates the deployment task.

## Grid blocks

For point coordinates (xᵢ,yᵢ), a grid block of width b and height h, anchored at origin (x₀,y₀), is:

\[
g_{xi}=\left\lfloor\frac{x_i-x_0}{b}\right\rfloor,\qquad
g_{yi}=\left\lfloor\frac{y_i-y_0}{h}\right\rfloor.
\]

Observations in the same grid cell share a group. Whole groups, not individual rows, are assigned to folds. Grid origin matters: shifting it can change which observations share a block. Repeat the analysis under plausible block sizes and origins.

## Buffered training set

For a test set T and candidate training set R, define the distance from candidate i to its nearest test observation:

\[
d(i,T)=\min_{j\in T}\|s_i-s_j\|_2.
\]

Retain a candidate training observation only when:

\[
d(i,T)\geq r,
\]

where r is the chosen buffer distance. Observations within the buffer are excluded from training for that fold; they are not test observations. Report their number.

The buffer uses the coordinate units of the input. Use an appropriate projected CRS for local Euclidean distances; do not apply a metre buffer directly to longitude/latitude degrees.

## Choosing block size and buffer

Consider:
- the range and anisotropy of spatial autocorrelation in the response and important predictors;
- the size of the deployment region and distance over which predictions must transfer;
- sensor footprint, image overlap, spatial resolution and aggregation unit;
- sampling design and observation density;
- the distance at which dependence becomes negligible for the task.

A variogram or correlogram can inform the choice, but a single estimated range is not a magic threshold. Compare multiple plausible block sizes and buffers. If the design leaves too few independent blocks, report that limitation rather than reverting silently to random CV.

## Keep model development inside training data

All preprocessing that learns from data must be fitted within each training fold: imputation, scaling, feature selection, dimensionality reduction, target encoding, hyperparameter tuning and threshold selection. Use nested spatial CV when tuning and reporting an unbiased outer-fold estimate. Do not use held-out test folds to choose the block size that gives the best score.

## Report the validation design

1. Prediction target and deployment geography/time.
2. Coordinate reference system and distance units.
3. Block dimensions, origin and grouping method.
4. Fold assignment and random seed.
5. Buffer distance and number of excluded training observations per fold.
6. Number of independent blocks and observations per fold.
7. Class balance or response distribution per fold.
8. Preprocessing and tuning procedure.
9. Baselines and metrics, including variation across folds.
10. Geographic performance gaps and areas outside the training data's applicability.

## Practical lab

- [Python spatial block and buffered-fold implementation](../implementations/python/spatial-cross-validation/README.md)
- [Step-by-step intern walkthrough](../implementations/python/spatial-cross-validation/implementation-walkthrough.md)

The implementation provides a deterministic grid-block split for compact planar point datasets. It does not infer a scientifically correct block size, perform temporal grouping, construct polygons, or replace a full validation design review.

## References

- Roberts, D. R. et al. (2017). Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure. *Ecography*, 40, 913–929. https://doi.org/10.1111/ecog.02881
- Valavi, R. et al. (2019). blockCV: An R package for generating spatially or environmentally separated folds for k-fold cross-validation of species distribution models. *Methods in Ecology and Evolution*, 10, 225–232. https://doi.org/10.1111/2041-210X.13107
- Meyer, H. et al. (2018). Improving performance of spatio-temporal machine learning models using forward feature selection and target-oriented validation. *Environmental Modelling & Software*, 101, 1–9. https://doi.org/10.1016/j.envsoft.2017.12.001
- Li, W. et al. (2024). GeoAI for Science and the Science of GeoAI. *Journal of Spatial Information Science*, 29, 1–17. https://doi.org/10.5311/JOSIS.2024.29.349

Passing the code tests proves the splitter contract, not the suitability of a split for a particular study.
