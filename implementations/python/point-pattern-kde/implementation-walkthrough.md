# Intern walkthrough: planar Gaussian kernel density estimation

## 1. Start with events, not polygons

A point pattern is a set of event locations observed inside a study window. KDE replaces the discrete events with a smooth intensity surface. It is descriptive: it does not, by itself, establish why events are clustered.

## 2. Place a kernel at every event

For event locations $x_i$ and bandwidth $h$, the isotropic two-dimensional Gaussian kernel is:

$$
K_h(x-x_i)=\frac{1}{2\pi h^2}
\exp\left(-\frac{\lVert x-x_i\rVert^2}{2h^2}\right)
$$

The estimated intensity is the sum of the kernels:

$$
\hat{\lambda}_h(x)=\sum_{i=1}^{n}w_iK_h(x-x_i)
$$

With unit weights, the result has units of events per square map unit. With other weights, the interpretation follows the units of those weights per area.

## 3. Evaluate on a regular grid

The implementation creates cell-centre coordinates for the requested bounds and grid shape. It evaluates the kernel sum at each centre.

To limit memory use, grid cells are processed in chunks. The algorithm remains a direct O(nm) evaluation for n events and m grid cells; chunking changes memory use, not the mathematical result.

## 4. Understand bandwidth

A small bandwidth produces a surface with narrow peaks around events. A larger bandwidth spreads each event's contribution over a wider area and produces a smoother surface.

Bandwidth selection is a modelling decision. This baseline accepts a fixed bandwidth and does not perform cross-validation, adaptive selection or sensitivity analysis automatically.

## 5. Understand edge effects

The Gaussian kernel extends beyond the study window. Near the boundary, part of the kernel lies outside the observed window. This implementation applies no edge correction, so intensity estimates near the boundary can be biased downward.

Do not compare edge estimates with interior estimates without considering the observation window and edge treatment.

## 6. Coordinate assumptions

The Euclidean distance in the kernel requires planar coordinates in a suitable projected CRS. A bandwidth of 500 means 500 units in the coordinate system; it is not automatically 500 metres.

## 7. Validate and extend

Tests cover the kernel value at a grid centre, symmetry, weight scaling, chunk-size invariance, bounds and invalid inputs. Useful extensions include edge correction, adaptive bandwidths, cross-validation, network KDE and point-process inference. Each changes the statistical model and should be documented separately.
