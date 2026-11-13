# Notebooks and interactive labs

Notebooks are used when changing values, inspecting intermediate calculations or plotting a result makes a method easier to understand. They supplement the canonical Markdown lesson and tested implementation; they do not replace either.

## Available labs

- [Empirical semivariogram](empirical-semivariogram-lab.ipynb): inspect pairwise differences, change lag bins and maximum distance, and see how pair counts affect the empirical curve.

- [Inverse distance weighting](inverse-distance-weighting-lab.ipynb): change the target location, distance power and neighbourhood size to see how each choice changes an estimated surface.

### Geometry foundations

- [Geometry foundations lab](geometry-foundations-lab.ipynb): move a point, adjust a segment and change two rectangles to inspect point location, segment intersection and polygon overlay.

- [Global Moran's I](global-morans-i-lab.ipynb): build a four-area neighbourhood graph, compare binary and row-standardised weights, inspect the spatial lag, enumerate a small permutation distribution, and use sliders to compare Moran's I with Geary's C as the values change.
- [Global Geary's C](gearys-c-lab.ipynb): compare squared differences between neighbours, contrast similar and alternating values, and inspect all 24 permutations of a four-unit example.
- [Local Moran's I](local-morans-i-lab.ipynb): build a synthetic neighbour graph, inspect High–High and Low–Low clusters and spatial outliers, and apply an FDR cutoff to conditional permutation results.
- [Local Geary](local-geary-lab.ipynb): compare each unit with its neighbours, inspect local squared-difference values and compare raw labels with an FDR-filtered classification.
- [Global Getis-Ord G](global-getis-ord-g-lab.ipynb): test overall concentration of positive values and inspect the permutation reference distribution.
- [Getis-Ord Gi*](getis-ord-gi-star-lab.ipynb): calculate local hotspot and coldspot z-scores, inspect permutation p-values and apply FDR control.
- [STR-packed R-tree](str-packed-rtree-lab.ipynb): compare bounding-box candidates with exact geometry intersections and inspect how the node capacity affects grouping.
- [Filter-and-refine spatial join](filter-refine-spatial-join-lab.ipynb): join points to polygons, inspect candidate pairs and compare exact predicates with a brute-force result.
- [Spatial weights](spatial-weights-lab.ipynb): compare Rook and Queen contiguity, distance bands, kNN, row standardisation and isolates.

## Run a notebook

Install the dependencies from the repository root. The spatial-weights lab uses GeoPandas GeoSeries as input to the libpysal Graph builders:

```bash
python -m pip install -r notebooks/requirements.txt
python -m pip install jupyterlab
jupyter lab
```

Open the notebook from JupyterLab and run the cells in order. The Global Moran's I lab includes live controls built with ipywidgets; change the four area values or the weights style to update the statistics and scatterplot. The other notebooks are editable labs: change an input in a code cell and rerun it to inspect the result.

### Open a lab in Google Colab

- [Geometry foundations](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/geometry-foundations-lab.ipynb)
- [Empirical semivariogram](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/empirical-semivariogram-lab.ipynb)
- [Inverse distance weighting](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/inverse-distance-weighting-lab.ipynb)
- [Global Moran's I](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/global-morans-i-lab.ipynb)
- [Global Geary's C](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/gearys-c-lab.ipynb)
- [Local Moran's I](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/local-morans-i-lab.ipynb)
- [Local Geary](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/local-geary-lab.ipynb)
- [Global Getis-Ord G](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/global-getis-ord-g-lab.ipynb)
- [Getis-Ord Gi*](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/getis-ord-gi-star-lab.ipynb)
- [STR-packed R-tree](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/str-packed-rtree-lab.ipynb)
- [Filter-and-refine spatial join](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/filter-refine-spatial-join-lab.ipynb)
- [Spatial weights](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/spatial-weights-lab.ipynb)

The repository workflow also executes all twelve notebooks on relevant pushes and pull requests. A successful run checks that the cells execute in the configured environment; it does not replace review of the statistical assumptions.

These notebooks are learning materials. For production analysis, check the input assumptions, use maintained geospatial libraries and record the environment used to produce results.
