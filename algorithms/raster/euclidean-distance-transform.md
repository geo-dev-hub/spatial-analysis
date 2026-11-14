# Euclidean distance transform: distance from every cell to a target

Stable ID: `SA-RASTER-EUCLIDEAN-DISTANCE-TRANSFORM` · Draft 0.1 · Source compendium section 4, page 6

## The question

Given a raster mask of target cells, how far is each other cell from its nearest target? This appears in proximity analysis, buffer-like raster operations, habitat distance, facility access screening and many image-processing workflows.

An exact Euclidean distance transform calculates the straight-line distance between cell centres. It is not a least-cost path and does not account for barriers.

## Definition

Let $T$ be the set of target-cell indices. For cell $p=(r,c)$, with row spacing $s_r$ and column spacing $s_c$, the distance is:

$$
D(p)=\min_{q=(r_q,c_q)\in T}
\sqrt{(s_r(r-r_q))^2+(s_c(c-c_q))^2}.
$$

The spacing terms convert row and column offsets into map units. If cell dimensions differ, the distance is anisotropic in array-index space even though it is Euclidean in map coordinates.

## A small grid

For a target at the centre of a 5 by 5 grid:

~~~text
4  3  2  3  4
3  2  1  2  3
2  1  0  1  2
3  2  1  2  3
4  3  2  3  4
~~~

This illustration assumes square unit cells and shows the centre-to-centre distances. With non-square cells, diagonal and horizontal/vertical distances change according to the supplied spacing.

## Algorithm family

The exact Euclidean distance transform can be computed efficiently using separability of the squared Euclidean distance and one-dimensional lower-envelope computations. Felzenszwalb and Huttenlocher describe a linear-time method for sampled functions and grids. This differs from a chamfer transform, which uses an approximate neighbourhood metric, and from cost-distance, which accumulates costs over a movement model.

The [Python example](../../implementations/python/raster-distance/README.md) wraps SciPy's `distance_transform_edt`; it does not implement the lower-envelope algorithm itself.

## Raster-specific decisions

- **Cell spacing:** pass row and column spacing in map units; do not assume square cells.
- **CRS:** use a suitable projected grid when interpreting distances as ground units.
- **Cell support:** the calculation is between cell centres, not between polygon boundaries.
- **Targets:** True marks target cells; at least one target is required.
- **NoData:** this teaching wrapper does not infer NoData or barrier semantics. Decide how invalid cells should be handled.
- **Movement model:** barriers and travel costs require a different method, such as cost-distance or least-cost path.

## Complexity and implementation

The Felzenszwalb–Huttenlocher family computes the exact transform in time linear in the number of grid cells for a fixed-dimensional grid. The teaching package delegates to SciPy's compiled implementation and exposes only the grid-spacing contract.

## Exercises

1. Change the target from one cell to several. Explain why each cell takes the distance to the nearest target.
2. Change cell spacing from $(1,1)$ to $(2,5)$. Predict the distance to a diagonal neighbour before running the code.
3. Compare the Euclidean result with a Manhattan-distance approximation. Which directions differ most?
4. Add a NoData region. Decide whether distance should be calculated across it, masked there or constrained by it.
5. Explain why a road-network travel-time surface cannot be computed by this Euclidean transform.

## References

- Felzenszwalb, P. F. and Huttenlocher, D. P. (2012), [Distance Transforms of Sampled Functions](https://doi.org/10.4086/cgt.2012.004), Theory of Computing, 8, 415–428.
- [SciPy `distance_transform_edt` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.distance_transform_edt.html).

**Scope:** exact Euclidean distance on a regular 2D raster grid; no cost surface, obstacle-aware path or NoData policy is implemented.
