# Notebooks and interactive labs

Notebooks are used when changing values, inspecting intermediate calculations or plotting a result makes a method easier to understand. They supplement the canonical Markdown lesson and tested implementation; they do not replace either.

## Available labs

- [Global Moran's I](global-morans-i-lab.ipynb): build a four-area neighbourhood graph, compare binary and row-standardised weights, inspect the spatial lag and enumerate a small permutation distribution.
- [Global Geary's C](gearys-c-lab.ipynb): compare squared differences between neighbours, contrast similar and alternating values, and inspect all 24 permutations of a four-unit example.
- [Local Moran's I](local-morans-i-lab.ipynb): build a synthetic neighbour graph, inspect High–High and Low–Low clusters and spatial outliers, and apply an FDR cutoff to conditional permutation results.
- [Local Geary](local-geary-lab.ipynb): compare each unit with its neighbours, inspect local squared-difference values and compare raw labels with an FDR-filtered classification.
- [Global Getis-Ord G](global-getis-ord-g-lab.ipynb): test overall concentration of positive values and inspect the permutation reference distribution.
- [Getis-Ord Gi*](getis-ord-gi-star-lab.ipynb): calculate local hotspot and coldspot z-scores, inspect permutation p-values and apply FDR control.
- [STR-packed R-tree](str-packed-rtree-lab.ipynb): compare bounding-box candidates with exact geometry intersections and inspect how the node capacity affects grouping.

## Run a notebook

Install the dependencies from the repository root:

```bash
python -m pip install -r notebooks/requirements.txt
python -m pip install jupyterlab
jupyter lab
```

Open the notebook from JupyterLab and run the cells in order. You can also open [Moran's I in Google Colab](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/global-morans-i-lab.ipynb) or [Geary's C in Google Colab](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/gearys-c-lab.ipynb), or [Local Moran's I in Google Colab](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/local-morans-i-lab.ipynb), or [Local Geary in Google Colab](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/local-geary-lab.ipynb), or [Getis-Ord Gi* in Google Colab](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/getis-ord-gi-star-lab.ipynb), or [Global Getis-Ord G in Google Colab](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/global-getis-ord-g-lab.ipynb), or [STR-packed R-tree in Google Colab](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/str-packed-rtree-lab.ipynb).

The repository workflow also executes all seven notebooks on relevant pushes and pull requests. A successful run checks that the cells execute in the configured environment; it does not replace review of the statistical assumptions.

These notebooks are learning materials. For production analysis, check the input assumptions, use maintained geospatial libraries and record the environment used to produce results.
