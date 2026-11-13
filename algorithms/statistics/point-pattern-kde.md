# Kernel density estimation for planar point patterns

Stable ID: `SA-STAT-POINT-KDE` · Draft 0.1 · Source compendium section 2, page 3

## From event locations to an intensity surface

A point pattern records the locations of events inside a study window: service requests, observed incidents, tree locations or another point-referenced phenomenon.

Kernel density estimation (KDE) replaces the discrete events with a smooth surface. It is useful for visualising where events are concentrated, but a high estimated intensity does not explain the process that generated the pattern.

## The Gaussian kernel

For an event at location $x_i$, a two-dimensional isotropic Gaussian kernel with bandwidth $h$ is:

$$
K_h(x-x_i)=\frac{1}{2\pi h^2}
\exp\left(-\frac{\lVert x-x_i\rVert^2}{2h^2}\right)
$$

The estimated intensity is the sum of the event kernels:

$$
\hat{\lambda}_h(x)=\sum_{i=1}^{n}w_iK_h(x-x_i)
$$

Here $w_i$ is an optional event weight. With unit weights, the intensity is measured in events per square map unit. If weights represent another quantity, the output units change accordingly.

## Bandwidth controls the scale

- A small bandwidth preserves local peaks and can make random variation look like structure.
- A large bandwidth smooths local variation and can merge nearby concentrations.
- Bandwidth should be selected and tested in relation to the spatial scale of the question, not chosen only because the resulting map looks attractive.

This lesson uses one fixed bandwidth. Adaptive bandwidths and cross-validated selection are separate methods.

## Grid evaluation and edge effects

The [teaching implementation](../../implementations/python/point-pattern-kde/README.md) evaluates the kernel sum at regular grid-cell centres. It uses a chunked direct calculation to limit memory use, but its computational cost is O(nm) for n events and m grid cells.

No edge correction is applied. Kernels near the study-window boundary extend outside the observed window, which can bias estimates downward near the edge. The output is intensity per unit area, not a count per raster cell.

## Coordinate system

The method uses Euclidean distances. Coordinates should therefore be in a suitable projected CRS with consistent linear units. A bandwidth of 500 is 500 coordinate units, not automatically 500 metres.

## Limitations

- The example uses an isotropic Gaussian kernel and one fixed bandwidth.
- No edge correction is applied.
- It does not account for barriers, road networks or anisotropic movement.
- It is a descriptive intensity estimator, not a test of clustering or a point-process model.
- It does not implement Ripley's K/L, nearest-neighbour tests, adaptive bandwidths or bandwidth cross-validation.

## Exercises

1. Plot the same point pattern with three bandwidths. Which spatial scales remain visible?
2. Add weights to selected events. How does the intensity surface change?
3. Move a cluster towards the study-window edge. Why can its estimated intensity appear lower?
4. Change the grid resolution while keeping the bandwidth fixed. Does the underlying estimate change, or only the sampling of the surface?
5. Explain why a KDE hotspot is not, by itself, evidence of statistically significant clustering.

## References

- Silverman, B. W. (1986), *Density Estimation for Statistics and Data Analysis*, Chapman & Hall.
- Diggle, P. J. (1985), *A kernel method for smoothing point process data*, Journal of the Royal Statistical Society: Series C (Applied Statistics), 34(2), 138–147.

**Scope:** fixed-bandwidth isotropic Gaussian KDE on a planar observation window, without edge correction or inferential point-process testing.
