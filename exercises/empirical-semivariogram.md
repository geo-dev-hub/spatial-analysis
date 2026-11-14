# Empirical semivariogram: from pairs to lag bins

**Related method:** [Empirical semivariogram](../methods/empirical-semivariogram.md)  
**Runnable material:** [Geostatistics implementation](../implementations/python/geostatistics/README.md) · [Interpolation and semivariogram lab](../notebooks/geostatistics-interpolation-lab.ipynb)

## What you will practise

By the end, you should be able to:

- calculate pairwise distances and half-squared value differences;
- group pairs into lag bins and calculate the Matheron estimate;
- explain why pair counts and bin edges matter;
- distinguish an empirical estimate from a fitted theoretical variogram.

You need basic coordinate geometry, subtraction, squaring and arithmetic means.

## 1. Work through a small dataset

Four observations lie on a straight line:

| Location | Coordinate | Value |
|---|---:|---:|
| A | 0 | 1 |
| B | 1 | 2 |
| C | 2 | 4 |
| D | 3 | 7 |

For every unordered pair, calculate the distance (d_{ij}) and half-squared difference ((z_i-z_j)^2/2).

| Pair | Distance | Squared difference | Half-squared difference |
|---|---:|---:|---:|
| A–B | 1 | 1 | 0.5 |
| A–C | 2 | 9 | 4.5 |
| A–D | 3 | 36 | 18 |
| B–C | 1 | 4 | 2 |
| B–D | 2 | 25 | 12.5 |
| C–D | 1 | 9 | 4.5 |

**Task:** group pairs using the edges ([0,1.5,2.5,3]). Remember: bins are left-closed and right-open, except the final bin includes its right edge.

Calculate the mean pair distance, semivariance and pair count for each non-empty bin.

## 2. Check your hand calculation in Python

From the repository root:

~~~bash
cd implementations/python/geostatistics
python -m pip install -r requirements.txt
python -m pytest -q
~~~

Then run:

~~~python
from interpolation import empirical_variogram

samples = [(0, 0, 1), (1, 0, 2), (2, 0, 4), (3, 0, 7)]
print(empirical_variogram(samples, [0, 1.5, 2.5, 3]))
~~~

Expected summaries:

| Mean pair distance | Semivariance | Pair count |
|---:|---:|---:|
| 1 | 7/3 ≈ 2.333 | 3 |
| 2 | 8.5 | 2 |
| 3 | 18 | 1 |

## 3. Investigate bin choices

1. Change the edges to ([0,2,3]). Which pairs move between bins? Does the estimate change?
2. Add an empty distance interval. How does the implementation represent it?
3. Use ([0,1,2]) on points at coordinates 0, 1 and 2. Verify that a pair at distance 1 enters the second bin and a pair at the final edge 2 is included.
4. Add one observation with a very large value. Which bins change most, and why is the classical estimator sensitive to outliers?

## 4. Interpret before fitting

Write a short note answering:

- Do the empirical semivariances rise with distance in this sample?
- Is six pairs enough to infer a stable variogram model?
- What does the pair count tell you that the plotted semivariance alone does not?
- Which coordinate system and distance units would be defensible for a real study?
- What additional checks would you make for a trend or directional anisotropy?

## 5. Check your reasoning

The expected values above are a hand-check for this four-point example, not evidence of a valid fitted model. The empirical semivariogram describes pairwise variation in the supplied sample. It does not estimate a nugget, sill or range, establish stationarity, or validate a kriging model.

For the implementation contract and full discussion of estimator choices, read the [method record](../methods/empirical-semivariogram.md).
