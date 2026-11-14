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


## Prediction-oriented validation: NNDM and kNNDM

Spatial blocking and buffering are not universal upgrades over random cross-validation. They answer a particular question: how well does a model transfer when test observations are geographically separated from training observations? If the actual task is to interpolate across a mapped area, forcing every test point to be distant from training data can create a harder prediction problem than the map itself requires.

Milà et al. (2022) proposed **nearest-neighbour distance matching (NNDM) leave-one-out cross-validation** for map validation. Instead of imposing one fixed separation rule, NNDM seeks to match the distribution of nearest-neighbour distances from prediction locations to training locations with the corresponding distribution from held-out test locations to training locations. The prediction area and the observed sampling pattern therefore become part of the validation design.

Linnenbrink et al. (2024) extended this idea to **k-fold NNDM (kNNDM)**. It searches for a k-fold configuration whose empirical distribution of test-to-training nearest-neighbour distances resembles the prediction-to-training distance distribution. The authors report similar accuracy-estimation behaviour to NNDM in their experiments, with substantially lower computation time for their large clustered-data example. That result is evidence for the studied settings, not a universal speed or accuracy guarantee.

These methods are not interchangeable with spatial blocks:

| Design | Main construction | Question it can help answer | Important limitation |
|---|---|---|---|
| Random k-fold / LOO | Randomly partition observations | Performance when test observations resemble the sampled locations and dependence is not causing leakage | Can be optimistic with clustered samples or strong spatial dependence |
| Spatial block k-fold | Hold out whole geographic blocks | Transfer to spatially separated groups or regions | May overstate error for interpolation within the sampled prediction area |
| Buffered LOO | Hold out one observation and remove nearby training observations | Transfer beyond a chosen separation radius | Radius choice is consequential; may discard much training data |
| NNDM LOO | Match test-to-training nearest-neighbour distance distribution to prediction-to-training distances | Map accuracy for a defined prediction area under the method's assumptions | LOO computation can be expensive; distance matching ignores direction and can miss anisotropy or nonstationarity |
| kNNDM | Find k folds that approximate the same distance-distribution match | Prediction-oriented map validation at larger sample sizes | Fold search and match quality require diagnostics; it is not a universal replacement for probability-sample validation |

**Do not choose the method by which gives the highest score.** First define the prediction area, sampling pattern and deployment task. Then inspect the training-to-test distance distributions, covariate-space novelty, residual dependence, fold sizes and geographic coverage. If a probability sample and design-based accuracy assessment are feasible for the map population, cross-validation is not automatically a substitute.

For NNDM, the paper discusses limitations of relying on geographical distance alone: distance distributions do not encode direction, and they do not guarantee that training and prediction covariate distributions are comparable. Anisotropy, nonstationarity and covariate shift therefore still require explicit checks. kNNDM inherits the prediction-oriented distance-matching idea; its folds should be inspected rather than accepted as an opaque score-generating procedure.

A maintained implementation is available in the R package `blockCV` (`cv_nndm`), and the kNNDM method is also documented by its authors and in the package ecosystem. Treat software behaviour as version-specific: cite the package version and record its parameters in any reproducible analysis.

## Practical lab

- [Python spatial block and buffered-fold implementation](../implementations/python/spatial-cross-validation/README.md)
- [NNDM LOO projected-Euclidean teaching implementation](../implementations/python/nndm/README.md)
- [NNDM LOO implementation walkthrough](../implementations/python/nndm/implementation-walkthrough.md)
- [NNDM LOO visual lab](../notebooks/nndm-spatial-validation-lab.ipynb)
- [kNNDM KMeans/Euclidean teaching implementation](../implementations/python/knndm/README.md)
- [kNNDM implementation walkthrough](../implementations/python/knndm/implementation-walkthrough.md)
- [kNNDM visual lab](../notebooks/knndm-spatial-validation-lab.ipynb)
- [Step-by-step spatial block and buffered-fold walkthrough](../implementations/python/spatial-cross-validation/implementation-walkthrough.md)

The implementation provides a deterministic grid-block split for compact planar point datasets. It does not infer a scientifically correct block size, perform temporal grouping, construct polygons, or replace a full validation design review.

## References

- Roberts, D. R. et al. (2017). Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure. *Ecography*, 40, 913–929. https://doi.org/10.1111/ecog.02881
- Valavi, R. et al. (2019). blockCV: An R package for generating spatially or environmentally separated folds for k-fold cross-validation of species distribution models. *Methods in Ecology and Evolution*, 10, 225–232. https://doi.org/10.1111/2041-210X.13107
- Meyer, H. et al. (2018). Improving performance of spatio-temporal machine learning models using forward feature selection and target-oriented validation. *Environmental Modelling & Software*, 101, 1–9. https://doi.org/10.1016/j.envsoft.2017.12.001
- Milà, C., Mateu, J., Pebesma, E. and Meyer, H. (2022). Nearest neighbour distance matching Leave-One-Out Cross-Validation for map validation. *Methods in Ecology and Evolution*, 13(6), 1304–1316. https://doi.org/10.1111/2041-210X.13851\n- Linnenbrink, J., Milà, C., Ludwig, M. and Meyer, H. (2024). kNNDM CV: k-fold nearest-neighbour distance matching cross-validation for map accuracy estimation. *Geoscientific Model Development*, 17, 5897–5912. https://doi.org/10.5194/gmd-17-5897-2024\n- Li, W. et al. (2024). GeoAI for Science and the Science of GeoAI. *Journal of Spatial Information Science*, 29, 1–17. https://doi.org/10.5311/JOSIS.2024.29.349

Passing the code tests proves the splitter contract, not the suitability of a split for a particular study.


## Buffered leave-one-out and cluster-based folds

**Buffered leave-one-out** holds out one observation at a time and excludes every other observation whose Euclidean distance to that test point is below the specified buffer. The implementation is O(n²).

**Spatial k-fold by clustering** applies deterministic farthest-first k-means to projected coordinates and assigns each resulting cluster to one test fold. It does not guarantee equal fold sizes, contiguous geographic regions or alignment with ecological/administrative units. It is not NNDM or kNNDM.

Use these as baselines only after defining the deployment question. Compare fold maps, distances, sample sizes and covariate distributions before interpreting validation scores.


## Strict leave-location-and-time-out (LLTO)

When the deployment task requires transfer to both unseen locations and unseen times, a strict LLTO fold can withhold one observed location/time pair. For held-out location \(s\) and time \(t\):

- **Test:** rows at \(s\) and \(t\).
- **Buffer:** rows at \(s\) at other times, plus rows at other locations at \(t\).
- **Train:** rows at other locations and other times.

The buffer is excluded from both training and testing for that fold. This prevents training examples from sharing either the held-out location or held-out time. Every observed location/time pair generates a fold; every input row appears in exactly one test fold.

This is stricter than leaving out only one location or one time slice and can leave very little training data. It is not rolling-origin forecasting, a spatial-distance buffer, NNDM or kNNDM. Use it only when joint space-and-time transfer is the prediction target.

- [LLTO implementation](../implementations/python/spatiotemporal-validation/README.md)
- [Tests](../implementations/python/spatiotemporal-validation/test_spatiotemporal_validation.py)
- [Intern walkthrough](../implementations/python/spatiotemporal-validation/walkthrough.md)
- [Visual lab](../notebooks/spatiotemporal-llto-lab.ipynb)

