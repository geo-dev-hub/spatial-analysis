# Precision models, fixed grids and snap rounding

Spatial algorithms operate on finite-precision coordinates. The way a system represents, rounds and compares those coordinates can change topology: two edges that should meet may miss by a tiny amount, or an overlay can create slivers and inconsistent intersections.

Precision handling is therefore part of the geometry model, not a cosmetic cleanup step.

## Three related but different operations

| Operation | Main purpose | Typical effect |
|---|---|---|
| Coordinate quantisation / precision reduction | Map coordinates to a declared grid | Coordinates move; short segments or components may collapse |
| Robust fixed-precision overlay | Compute Boolean operations under a consistent precision model | Noding and overlay use the selected precision model |
| Snap rounding | Node a planar arrangement consistently on a grid | Segments are routed through grid hot pixels under a defined algorithm |

These terms should not be used interchangeably. Rounding each input coordinate independently does not, by itself, implement a complete snap-rounding noder.

## Grid size and scale

For grid size g, a coordinate is represented at a grid spacing of g in the input coordinate units. If the data are in a projected CRS measured in metres, g=0.01 represents a centimetre grid. If the data are longitude and latitude, the same number is in degrees and is not a uniform ground-distance precision.

A grid is a modelling decision. Choose it from source accuracy, measurement purpose and downstream tolerance—not because a smaller number sounds more precise.

## Why topology changes

- A short line may collapse to a point or disappear.
- A narrow polygon may collapse.
- Distinct vertices may become coincident.
- Rings can change shape or orientation.
- A fixed precision overlay may produce a different result from floating precision overlay.

A precision reduction operation should state how collapsed components are handled. The output must be validated and compared with the input.

## GEOS and Shapely route

Shapely exposes precision reduction through `set_precision` and fixed-grid overlay through the `grid_size` argument on supported overlay operations. GEOS also has robust noding and snap-rounding machinery. Calling `set_precision` is not a reason to claim that an application has implemented the full snap-rounding algorithm.

## Runnable investigation

Use a geometry pair whose boundaries nearly meet. Compare:
1. floating-precision intersection;
2. precision-reduced inputs followed by intersection;
3. fixed-grid intersection with an explicit grid size.

Record validity, area, component count, coordinate movement and whether the result matches the intended model. Do not assume one result is universally correct.

## Runnable fixed-grid example

The [precision-grid package](../../implementations/python/precision-grid/README.md) wraps Shapely/GEOS coordinate precision reduction and fixed-grid intersection. Its tests cover coordinate quantisation, fixed-grid intersection at a crossing and collapse of a narrow polygon. The [intern walkthrough](../../implementations/python/precision-grid/implementation-walkthrough.md) explains the precision contract.

## Status

This dossier distinguishes the concepts and gives a reproducible research plan. Fixed-grid precision operations now have a tested teaching wrapper. A dedicated implementation of a snap-rounding noder, including its hot-pixel construction and arrangement-level correctness tests, remains open. The current wrapper is not a from-scratch snap-rounding implementation.

## References

- Hobby, J. D. (1999), [Practical segment intersection with finite precision output](https://doi.org/10.1007/PL00009321), Computational Geometry.
- [GEOS precision model](https://libgeos.org/doxygen/classgeos_1_1geom_1_1PrecisionModel.html).
- [GEOS OverlayNG](https://libgeos.org/doxygen/classgeos_1_1operation_1_1overlayng_1_1OverlayNG.html).
- [Shapely set_precision](https://shapely.readthedocs.io/en/stable/reference/shapely.set_precision.html).
- [Shapely intersection](https://shapely.readthedocs.io/en/stable/reference/shapely.intersection.html).

**Scope:** conceptual and API-level precision treatment; no independent snap-rounding implementation is claimed.
