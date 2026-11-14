# Point-pattern foundations: from event locations to spatial intensity

**Status:** Fixed-bandwidth planar KDE, a descriptive Clark–Evans nearest-neighbour index and an uncorrected Ripley's K/L summary now have tested implementations and notebooks; edge correction, formal inference and broader point-process methods remain open.

## Start with the observation process

A point pattern is a set of event locations observed inside a study window. Before calculating a density surface, ask what counts as an event, how the observation window was defined and whether the locations were sampled consistently.

## 1. Visualise intensity with KDE

Read [Kernel density estimation](../algorithms/statistics/point-pattern-kde.md) and run the [point-pattern KDE notebook](../notebooks/point-pattern-kde-lab.ipynb). The notebook compares fixed Gaussian bandwidths on the same synthetic event pattern.

A KDE surface is descriptive. A hotspot is not automatically a statistically significant cluster.

## 2. Understand the bandwidth

Compare a narrow and broad bandwidth. Explain which spatial scales are smoothed away and why bandwidth selection should follow the question rather than map aesthetics.

## 3. Check the observation window

The first implementation does not apply edge correction. Kernels near the study boundary extend beyond the observed window, which can bias the estimated intensity downward. The window and its boundary treatment are part of the model.

## 4. Compare nearest-neighbour spacing

Read [Clark–Evans nearest-neighbour index](../algorithms/statistics/clark-evans.md) and run the [Clark–Evans notebook](../notebooks/clark-evans-lab.ipynb). It compares the observed mean nearest-neighbour distance with a homogeneous Poisson reference. The lesson is deliberately descriptive: edge correction and a significance test remain separate work.

## 5. Compare pair counts across distance scales

Read [Ripley's K and L](../algorithms/statistics/ripley-k.md) and run the [Ripley K/L notebook](../notebooks/ripley-k-lab.ipynb). It compares pair counts across several radii with the homogeneous Poisson reference. The first implementation is uncorrected and descriptive; edge correction and simulation envelopes remain separate work.

## 6. Move from description to inference

The wider point-pattern section includes quadrat analysis, nearest-neighbour statistics, edge-corrected Ripley's K/L, G/F/J functions, pair correlation, stochastic point-process models and scan statistics. These answer different questions and require explicit null models and assumptions.

## Exercises

1. Generate two event clusters and compare three bandwidths.
2. Change the grid resolution while keeping the bandwidth fixed.
3. Move a cluster close to the study-window boundary. Describe the edge effect.
4. Explain why a KDE hotspot does not establish statistically significant clustering.
5. Identify a null model appropriate to a point-pattern research question.

## What remains

Adaptive bandwidths, cross-validated selection, edge correction, network KDE, edge-corrected Ripley's K/L, nearest-neighbour tests and point-process inference require separate lessons and validation.
