# Notebooks and interactive labs

Notebooks are used when changing values, inspecting intermediate calculations or plotting a result makes a method easier to understand. They supplement the canonical Markdown lesson and tested implementation; they do not replace either.

## Available labs

- [Global Moran's I](global-morans-i-lab.ipynb): build a four-area neighbourhood graph, compare binary and row-standardised weights, inspect the spatial lag and enumerate a small permutation distribution.
- [Global Geary's C](gearys-c-lab.ipynb): compare squared differences between neighbours, contrast similar and alternating values, and inspect all 24 permutations of a four-unit example.
- [Local Moran's I](local-morans-i-lab.ipynb): build a synthetic neighbour graph, inspect High–High and Low–Low clusters and spatial outliers, and apply an FDR cutoff to conditional permutation results.

## Run a notebook

Install the dependencies from the repository root:

```bash
python -m pip install -r notebooks/requirements.txt
python -m pip install jupyterlab
jupyter lab
```

Open the notebook from JupyterLab and run the cells in order. You can also open [Moran's I in Google Colab](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/global-morans-i-lab.ipynb) or [Geary's C in Google Colab](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/gearys-c-lab.ipynb), or [Local Moran's I in Google Colab](https://colab.research.google.com/github/geo-dev-hub/spatial-analysis/blob/main/notebooks/local-morans-i-lab.ipynb).

The repository workflow also executes all three notebooks on relevant pushes and pull requests. A successful run checks that the cells execute in the configured environment; it does not replace review of the statistical assumptions.

These notebooks are learning materials. For production analysis, check the input assumptions, use maintained geospatial libraries and record the environment used to produce results.
