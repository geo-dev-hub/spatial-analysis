# Clark–Evans nearest-neighbour index

Stable ID: `SA-STAT-CLARK-EVANS` · Draft 0.1 · Source compendium section 2, page 3

## The question

Are event locations, on average, closer together or farther apart than expected under a homogeneous Poisson point process?

The Clark–Evans index compares the observed mean nearest-neighbour distance with its expected value under complete spatial randomness (CSR) in an infinite planar homogeneous Poisson process.

## Observed nearest-neighbour distance

For each event location $x_i$, find the distance to its closest *other* event:

$$
d_i=\min_{j\ne i}\lVert x_i-x_j\rVert
$$

The observed mean is:

$$
\bar d_{obs}=\frac{1}{n}\sum_{i=1}^{n}d_i
$$

## Expected distance and R ratio

For event intensity $\lambda=n/A$, where $A$ is the study-window area, the infinite-plane homogeneous Poisson expectation is:

$$
E(\bar d)=\frac{1}{2\sqrt{\lambda}}
$$

The Clark–Evans ratio is:

$$
R=\frac{\bar d_{obs}}{E(\bar d)}
$$

- $R<1$: events are closer together than the reference expectation (clustering tendency).
- $R\approx1$: mean spacing is near the reference expectation.
- $R>1$: events are farther apart than the reference expectation (regularity tendency).

## What the index does not tell you

The ratio alone is descriptive. It is not a p-value and does not establish statistical significance. A formal test needs an appropriate variance/null procedure and a treatment of the observation window.

The infinite-plane expectation is an approximation for a finite rectangular window. Boundary effects can inflate observed nearest-neighbour distances. The baseline implementation applies no edge correction.

The homogeneous Poisson reference assumes constant event intensity. If the underlying population or observation effort varies across space, apparent clustering may simply reflect that variation.

## Teaching implementation

The [Python implementation](../../implementations/python/clark-evans/README.md) calculates the nearest-neighbour distances with a chunked brute-force pairwise calculation, then reports the observed mean, expected mean and R ratio. It does not calculate significance or apply edge correction.

Coordinates must be planar and expressed in consistent linear units. A projected CRS is required; a geographic longitude/latitude distance is not an appropriate Euclidean input.

## Exercises

1. Calculate R for two points one unit apart in a 2×2 study window.
2. Place events on a regular grid. Is R above or below one?
3. Place events in a tight cluster. How does R change?
4. Move points towards the study-window edge. Explain the boundary effect.
5. Explain why a population gradient can violate the homogeneous Poisson reference.
6. What additional assumptions and procedures would be needed for a significance test?

## References

- Clark, P. J. and Evans, F. C. (1954), *Distance to nearest neighbor as a measure of spatial relationships in populations*, Ecology, 35(4), 445–453.

**Scope:** descriptive Clark–Evans R ratio for a planar rectangular window; no edge correction, z test or p-value is implemented.
