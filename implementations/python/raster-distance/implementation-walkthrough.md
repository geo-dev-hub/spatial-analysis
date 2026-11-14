# Intern walkthrough: Euclidean distance on a raster grid

## 1. Define what a cell represents

A raster is an array, but its indices are not map coordinates. Each cell represents an area; this method measures between cell centres. The spacing must be supplied in row and column order, with both values expressed in the same map unit.

## 2. Mark the target cells

The Boolean mask uses True for target cells. The distance transform expects zero-valued cells to be the sources from which distance is measured. We therefore invert the mask before calling SciPy.

## 3. Supply physical cell spacing

For square cells of 10 metres, use `(10, 10)`. For a grid with 10-metre rows and 20-metre columns, use `(10, 20)`. The resulting diagonal distance is:

$$
d=\sqrt{(10)^2+(20)^2}=22.36\text{ m (approximately)}
$$

Passing only array indices would silently assume square unit cells.

## 4. Understand the output

Each output cell stores its Euclidean distance to the nearest target cell. Target cells have distance zero. This is not a path distance: the calculation does not route around barriers, follow terrain or accumulate travel cost.

## 5. Validate the grid assumptions

Tests cover target cells, multiple targets, rectangular cell spacing, diagonal distances and invalid masks. The wrapper does not infer NoData semantics. Decide whether NoData cells should be included, excluded or masked in the downstream analysis before interpreting the raster.

## 6. Know which algorithm is being used

SciPy's `distance_transform_edt` supplies the computational implementation. The canonical lesson links the exact Euclidean distance transform to the Felzenszwalb–Huttenlocher linear-time family. This package is a reproducible API wrapper, not a reimplementation of that algorithm.
