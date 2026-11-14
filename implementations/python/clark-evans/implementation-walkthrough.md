# Intern walkthrough: Clark–Evans nearest-neighbour index

## 1. Calculate each event's nearest neighbour

For each point $x_i$, calculate its distance to every other point and retain the smallest:

$$
d_i=\min_{j\ne i}\lVert x_i-x_j\rVert
$$

The implementation uses a chunked pairwise Euclidean-distance calculation and excludes each point's distance to itself.

## 2. Calculate the observed mean distance

The observed statistic is:

$$
\bar d_{obs}=\frac{1}{n}\sum_{i=1}^{n}d_i
$$

## 3. Compare with a homogeneous Poisson reference

For intensity $\lambda=n/A$ in a planar study window of area $A$, the infinite-plane homogeneous Poisson expectation is:

$$
E(\bar d)=\frac{1}{2\sqrt{\lambda}}
$$

The Clark–Evans ratio is:

$$
R=\frac{\bar d_{obs}}{E(\bar d)}
$$

A value below one indicates closer spacing than the reference expectation; a value above one indicates wider spacing.

## 4. Do not over-interpret R

This baseline reports the descriptive ratio only. It does not calculate a z statistic or p-value, and it applies no edge correction. Points near the boundary have neighbours outside the observation window that are not observed, which can increase measured nearest-neighbour distances.

The homogeneous Poisson reference also assumes constant intensity over the window. Strong variation in population density or observation effort can invalidate that reference.

## 5. Complexity

The direct pairwise calculation is O(n²) in time. Chunking limits temporary memory to O(chunk_size × n), but does not change the time complexity.

## 6. Validate

Tests cover a two-point example with a known distance, duplicate events, chunk-size invariance and invalid inputs. For larger patterns, a spatial index such as a k-d tree can reduce nearest-neighbour search cost; it is intentionally not hidden inside this first-principles baseline.
