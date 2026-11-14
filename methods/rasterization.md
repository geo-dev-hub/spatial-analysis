# Rasterization: from continuous geometry to grid cells

Rasterization converts geometric objects into a discrete grid representation. It appears in map rendering, raster GIS, line-of-sight analysis, grid traversal, image processing and collision detection. There is no single universal rasterization algorithm: the correct method depends on what a cell means and which cells should be selected.

A road rendered for display, a river burned into a DEM, and a ray traversing a voxel grid are different tasks. They should not silently share one pixel-selection rule.

## 1. Define the grid

For a north-up raster with upper-left outer-corner origin (x₀,y₀), positive cell width Δx and height Δy, a coordinate maps to column and row as

$$
c=\left\lfloor\frac{x-x_0}{\Delta x}\right\rfloor,\qquad
r=\left\lfloor\frac{y_0-y}{\Delta y}\right\rfloor.
$$

This assumes a north-up grid. Rotated or sheared rasters require the inverse affine transform. Points exactly on the outer maximum edge need an explicit policy; a common convention assigns cells half-open intervals.

Specify cell size, origin, orientation, CRS, centre/corner convention, boundary inclusion, NoData behaviour and whether the output is visual or analytical.

## 2. Line drawing: DDA and Bresenham

### Digital Differential Analyzer (DDA)

For endpoints (x₀,y₀) and (x₁,y₁), let

$$
n=\max(|x_1-x_0|,|y_1-y_0|).
$$

Sample the segment at n increments:

$$
x_k=x_0+k\frac{x_1-x_0}{n},\qquad
y_k=y_0+k\frac{y_1-y_0}{n}.
$$

Map each sample to a pixel using a declared rounding convention. DDA is easy to understand and supports floating-point increments. Its output depends on rounding policy, and repeated addition can accumulate error. Handle n=0 as a point.

### Bresenham's integer line algorithm

For a shallow-slope line, Bresenham tracks an integer decision variable to choose whether the next pixel advances horizontally or diagonally. A symmetric implementation handles all octants by reflecting or swapping axes. Its key idea is to replace repeated floating-point evaluation with incremental integer updates.

The selected pixel stays close to the ideal line, but the exact pixel set depends on pixel-centre and tie-breaking conventions.

| Property | DDA | Bresenham |
|---|---|---|
| Main arithmetic | Incremental floating point | Integer decision updates |
| Teaching value | Direct discretisation of a parametric line | Error accumulator |
| Limitation | Rounding and accumulated floating error | Tie rules and octant handling |
| Use | Simple raster line demonstration | Efficient thin-line rasterisation |

Neither algorithm defines a supercover line. A thin display line selects a connected chain of representative pixels; a supercover selects every cell the continuous segment intersects.

## 3. Anti-aliased lines: Wu's method

A binary line assigns selected pixels foreground or background. This can look jagged because a continuous line rarely passes through pixel centres. Xiaolin Wu's line algorithm distributes intensity between neighbouring pixels according to fractional position, with endpoint handling and axis swapping for steep lines.

The resulting intensity depends on blending and display behaviour. Do not interpret Wu intensity as exact area coverage for every geometry. It is a line-rendering method, not a general polygon-area rasterizer.

## 4. Polygon scan conversion

A scanline polygon filler processes one horizontal sample row at a time:

1. Find polygon edges crossing the scanline under a consistent vertex convention.
2. Compute their x-intersections.
3. Sort intersections from left to right.
4. Fill spans according to the chosen inside rule.
5. Update active-edge intersections incrementally for the next row.

For a simple polygon, the even–odd rule toggles inside/outside state at each crossing. The nonzero winding rule accumulates signed crossings. They differ for self-intersecting rings and nested boundaries, so choose the rule that matches the polygon model.

A half-open edge rule, such as including the lower endpoint but excluding the upper endpoint in crossing tests, avoids counting a shared vertex twice.

~~~mermaid
flowchart TD
    A[Polygon edges] --> B[Build edge table by first active scanline]
    B --> C[Insert edges into active edge list]
    C --> D[Sort intersections by x]
    D --> E[Apply even-odd or winding rule]
    E --> F[Fill spans on this scanline]
    F --> G[Remove expired edges]
    G --> H[Increment intersection x values]
    H --> I{More scanlines?}
    I -->|Yes| C
    I -->|No| J[Raster grid]
~~~

For a non-horizontal edge, the x-intersection can be updated from one scanline to the next by its inverse slope. An edge table avoids recomputing every edge intersection from scratch on every row.

## 5. Supercover lines and grid traversal

A supercover line returns every grid cell touched by the continuous segment, including edge- or corner-only touches if that is the declared rule. This is useful for conservative visibility, occupancy and collision checks: a thin display line may omit a cell that the segment geometrically touches.

Amanatides–Woo-style voxel traversal advances from cell to cell by comparing the next parametric crossing times of grid boundaries. It is a grid traversal algorithm, not the same output contract as Bresenham.

Corner crossings are critical. A traversal may advance both axes at once (diagonal-only visitation) or emit side-adjacent cells too (supercover). Choose based on whether touching counts as intersection.

## 6. Rasterisation is a measurement decision

For a polygon and a cell, common rules include:

- **Centre rule:** select if the cell centre lies inside the polygon.
- **Any-touch rule:** select if the polygon intersects the cell at all.
- **All-touched rule:** software uses this phrase with particular semantics that should be checked.
- **Fractional coverage:** store the proportion of cell area covered by the polygon.

For cell C and polygon P, the ideal coverage fraction is

$$
f_C=\frac{\operatorname{area}(C\cap P)}{\operatorname{area}(C)},\qquad 0\leq f_C\leq1.
$$

A coverage-weighted mean can be formed as

$$
\bar z_P=\frac{\sum_C f_C a_C z_C}{\sum_C f_C a_C},
$$

where aC is cell area. It is constant for equal-area projected cells, but not generally for geographic latitude/longitude cells. This is an area-weighted summary, not a substitute for modelling within-cell variation.

## 7. Common failure modes

- Mixing row/column order with x/y order.
- Treating the upper-left corner as a pixel centre.
- Ignoring affine rotation or shear.
- Assuming longitude/latitude cells have equal ground area.
- Using a thin-line algorithm where every crossed cell must be visited.
- Leaving exact corner and boundary ties undefined.
- Applying even–odd fill where winding semantics are required.
- Treating anti-aliasing intensity as physical area coverage without justification.
- Rasterising adjacent polygons independently and creating seams or double counts.
- Ignoring NoData and masks.

## 8. Choose a method

| Task | Candidate method | Contract to state |
|---|---|---|
| Draw a thin segment | Bresenham or DDA | One connected representative pixel chain |
| Smooth display line | Wu or renderer antialiasing | Pixel intensities and blending |
| Fill a polygon | Scanline conversion | Inside rule and vertex convention |
| Conservative line-cell intersection | Supercover or grid traversal | Whether edge/corner touch counts |
| Burn vector geometry into an analytical raster | Centre, all-touched or fractional rule | Cell inclusion or coverage semantics |
| Area-weighted polygon summary | Fractional cell coverage | Area units and partial-cell treatment |

## 9. Test design

Test horizontal, vertical, steep and shallow lines; all octants and reversed endpoints; zero-length segments; lines through pixel centres, cell boundaries and grid corners; polygons with horizontal edges and scanline-through-vertex cases; concave polygons and holes; self-intersecting rings under both fill rules; features outside the raster extent; rotated affine grids; and NoData masks.

For a supercover implementation, compare returned cells against a slower cell-by-cell segment/rectangle intersection oracle on small grids. For polygon coverage, compare summed intersection areas against the polygon area clipped to the raster footprint within a declared tolerance.

## Further reading

- Marc Levoy, Stanford CS 248, [Rasterization algorithms](https://www.graphics.stanford.edu/courses/cs248-08/scan/scan1.html): line drawing, DDA, Bresenham and polygon scan conversion, including sample positions and edge conventions.
- Xiaolin Wu (1991), “An Efficient Antialiasing Technique,” *Computer Graphics*, 25(4), 143–152. [DOI record](https://doi.org/10.1145/127719.122734).
- Amanatides, J. and Woo, A. (1987), “A Fast Voxel Traversal Algorithm for Ray Tracing,” *Eurographics*. [DOI record](https://doi.org/10.2312/egtp.19871000).

## Scope

**Implemented teaching baseline:** [Python rasterisation package](../implementations/python/rasterization/README.md), [tests](../implementations/python/rasterization/test_rasterization.py), [step-by-step walkthrough](../implementations/python/rasterization/implementation-walkthrough.md) and [executable lab notebook](../notebooks/rasterization-lab.ipynb). The package implements DDA, all-octant integer Bresenham, Wu line intensities, closed-cell supercover traversal and centre-sampled even-odd scanline filling. It does not implement exact fractional-area coverage, holes/multiple rings, an affine geospatial wrapper or Amanatides–Woo voxel traversal. Read the implementation contract before applying it to map data.
