# Getis-Ord G: is there an overall concentration of high or low values?

Stable ID: `SA-STAT-GLOBAL-GETIS-ORD-G` · Supplementary method · Added to explain the source-listed Gi* hotspot statistic

## Start with the question

You have a map of positive values: property prices, service requests, population counts or another measurement with a meaningful zero.

Are high values concentrated near one another across the study area? Or are low values concentrated together?

Global Getis-Ord G gives one summary of that concentration.

**Global G asks whether high or low values are more spatially concentrated than we would expect if the same values were assigned randomly to the same locations.**

It does not tell us where the concentrations occur. The local Gi* statistic answers that next question.

## The statistic

For positive values $x_i$ and spatial weights $w_{ij}$, the global statistic is:

$$
G = \frac{\sum_{i=1}^{n}\sum_{j\ne i}w_{ij}x_i x_j}
{\sum_{i=1}^{n}\sum_{j\ne i}x_i x_j}
$$

The diagonal is excluded: a unit is not paired with itself in this global statistic.

Let $S_0$ be the sum of the spatial weights:

$$
S_0 = \sum_{i=1}^{n}\sum_{j=1}^{n}w_{ij}
$$

Under the usual randomisation reference, the expected value is:

$$
E[G] = \frac{S_0}{n(n-1)}
$$

The observed statistic is compared with this expectation and with a reference distribution.

## Why raw positive values matter

Moran's I and Geary's C use deviations or differences. Global G works with raw values and their cross-products.

This makes it useful for positive, ratio-scale measurements such as counts and prices. The zero has meaning: zero requests, zero incidents or zero population is a real state of the measured quantity.

Do not shift a variable by adding an arbitrary constant just to make it positive. That changes the cross-products and can change the interpretation. Variables with zero or negative values need a different method or a carefully justified transformation.

## Read the direction

The standardized statistic compares the observed G with its expected value.

- A positive z-score indicates concentration of high values.
- A negative z-score indicates concentration of low values.

A statistic above its expectation is not automatically significant. Use an analytical reference distribution or a permutation distribution and report which one you used.

PySAL's `esda.G` exposes the observed statistic, expected value, analytical z-score and p-value, and permutation-based quantities. Its API documents `p_norm` and `p_sim` as one-sided; report the z-score direction and do not present those values as generic two-sided p-values.

## Weights are part of the question

The official PySAL guide uses binary weights for global G. A weight of one means the pair contributes; zero means it does not.

Do not row-standardise the matrix by habit. The weights matrix defines which pairs enter the numerator, and the total weight sum defines the expected value.

Record:
- how neighbours were defined;
- whether the matrix is binary;
- whether the diagonal is zero;
- how disconnected units were treated;
- the study-area scale and alternative weights considered.

## Global G and local Gi*

| | Global Getis-Ord G | Local Getis-Ord Gi* |
|---|---|---|
| Output | One statistic for the whole study area | A local statistic and z-score for each unit |
| Main question | Is there overall concentration? | Where are the hotspots and coldspots? |
| Focal unit | Pairwise global sum excludes self-pairs | Gi* includes the focal observation in its neighbourhood |
| What it cannot do | Locate the concentration | Identify High–Low and Low–High outliers like Local Moran |

Global G is the overview. Gi* locates local concentrations. They are related, but they are not interchangeable.

## PySAL example

```python
import numpy as np
from libpysal import graph
from esda import G

# Keep the GeoDataFrame and variable in exactly the same row order.
y = gdf["value"].to_numpy()
w = graph.Graph.build_contiguity(gdf, rook=False)

# Global G uses binary weights in the official example.
w = w.transform("b")

# Global G uses NumPy's random state for its permutation simulation.
np.random.seed(12345)
result = G(y, w, permutations=999)

print("Observed G:", result.G)
print("Expected G:", result.EG)
print("Analytical z-score:", result.z_norm)
print("Analytical p-value:", result.p_norm)
print("Permutation p-value:", result.p_sim)
```

The example uses Queen contiguity and binary weights. The analytical p-value and permutation p-value have their own assumptions and interpretation; consult the API for the installed version.

## Explore the calculation

The accompanying notebook uses a small synthetic ring graph with positive values. It:
- builds binary neighbour weights;
- calculates global G and its expected value;
- inspects the analytical z-score and permutation reference distribution;
- changes the values while keeping the graph fixed;
- compares the global conclusion with the local Gi* lesson.

- [Interactive Global Getis-Ord G notebook](../../notebooks/global-getis-ord-g-lab.ipynb)

The ring graph is not a geographic map. The official PySAL guide demonstrates the workflow on polygon data.

## What to report

Include:
- the positive variable and its meaningful zero;
- the spatial units and study area;
- the weights definition and transformation;
- the observed G and expected value;
- the analytical or permutation inference method;
- the z-score direction and p-value interpretation;
- the number of permutations and random seed;
- the limits of a single global summary.

## References

- Getis, A., and Ord, J. K. (1992). “The Analysis of Spatial Association by Use of Distance Statistics.” *Geographical Analysis*, 24(3), 189–206. [https://doi.org/10.1111/j.1538-4632.1992.tb00261.x](https://doi.org/10.1111/j.1538-4632.1992.tb00261.x)
- PySAL `esda`. [Global Spatial Autocorrelation: Getis-Ord G](https://pysal.org/esda/stable/user-guide/getisord.html).
- PySAL `esda`. [G API reference](https://pysal.org/esda/stable/generated/esda.G.html).

## What this lesson does not claim

- Global G does not locate hotspots or coldspots.
- A difference between observed and expected G is not automatically statistically significant.
- Global G does not measure negative spatial autocorrelation in the same way as Moran's I.
- The method is not a generic substitute for methods designed for variables with zero or negative values.

## Change history

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-11-13 | Initial supplementary lesson with official PySAL workflow and interactive notebook |
